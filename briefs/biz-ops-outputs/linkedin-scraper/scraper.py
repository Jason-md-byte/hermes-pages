#!/usr/bin/env python3
"""
LinkedIn ICP-Matched Lead Scraper
==================================
Browser-based extraction using Playwright (Playwright + Browserbase compatible).
Extracts prospect leads matching defined ICP criteria from LinkedIn Sales Navigator
or LinkedIn People Search.

Usage:
    python scraper.py --config config.yaml [--headless] [--browserbase]
"""

import asyncio
import csv
import json
import logging
import os
import random
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field, HttpUrl

# ---------------------------------------------------------------------------
# Pydantic Models
# ---------------------------------------------------------------------------

class LeadRecord(BaseModel):
    """A single extracted prospect record matching the output schema."""
    name: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    profile_url: str = Field(..., pattern=r"^https://(www\.)?linkedin\.com/in/.+")
    company_size: Optional[str] = None


class SearchConfig(BaseModel):
    """Search parameters derived from config."""
    titles: list[str]
    locations: list[str]
    industries: list[str]
    company_sizes: list[str]
    keyword_groups: list[list[str]]
    max_pages: int = 5
    results_per_page: int = 25
    sort: str = "relevance"


# ---------------------------------------------------------------------------
# Logger
# ---------------------------------------------------------------------------

logger = logging.getLogger("linkedin_scraper")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(
    "%(asctime)s  %(levelname)-8s  %(name)s  %(message)s"
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# ---------------------------------------------------------------------------
# Config Loader
# ---------------------------------------------------------------------------

def load_config(path: str) -> dict:
    """Load YAML configuration file."""
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    logger.info("Configuration loaded from %s", path)
    return cfg


# ===========================================================================
# PLAYWRIGHT-BASED SCRAPER (Browserbase Compatible)
# ===========================================================================
#
# This module uses Playwright for browser automation. It supports two modes:
#   1. Local mode — runs Chromium on the local machine.
#   2. Browserbase mode — connects to a remote Browserbase session via CDP.
#
# The pseudo-code below illustrates the full scraping pipeline. Each function
// demonstrates the pattern but requires a live browser context to execute.
# ===========================================================================

class LinkedInScraper:
    """
    Main scraper class. Manages Playwright browser context, login/session,
    search navigation, lead extraction, deduplication, and export.
    """

    def __init__(self, config: dict):
        self.cfg = config
        self.target = config["target"]
        self.search_cfg = config["search"]
        self.timing = config["timing"]
        self.output_cfg = config["output"]
        self.browser_cfg = config["browser"]
        self.session_cfg = config["session"]

        self.browser = None
        self.context = None
        self.page = None
        self.leads: dict[str, LeadRecord] = {}  # dedup keyed by profile_url

    # ------------------------------------------------------------------
    # Browser Setup
    # ------------------------------------------------------------------

    async def _setup_local_browser(self):
        """Launch a local Chromium instance with Playwright."""
        from playwright.async_api import async_playwright

        p = await async_playwright().start()
        local = self.browser_cfg["local"]
        self.browser = await p.chromium.launch(
            headless=local["headless"],
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        self.context = await self.browser.new_context(
            viewport={"width": local["viewport"]["width"],
                       "height": local["viewport"]["height"]},
            user_agent=local["user_agent"],
            locale=local.get("locale", "en-CA"),
            timezone_id=local.get("timezone", "America/Toronto"),
        )
        self.page = await self.context.new_page()
        logger.info("Local browser session started")

    async def _setup_browserbase_session(self):
        """
        Connect to a Browserbase cloud browser via CDP.
        Requires BROWSERBASE_API_KEY env var.
        """
        import httpx
        from playwright.async_api import async_playwright

        api_key = os.environ.get(
            self.browser_cfg["browserbase"]["api_key_env"]
        )
        if not api_key:
            raise RuntimeError(
                f"Missing {self.browser_cfg['browserbase']['api_key_env']}"
            )

        # -- Create a Browserbase session --------------------------------
        project_id = os.environ.get(
            self.browser_cfg["browserbase"].get("project_id_env", ""),
            ""
        )
        bb_config = self.browser_cfg["browserbase"]

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://api.browserbase.com/v1/sessions",
                headers={
                    "X-BB-API-Key": api_key,
                    "Content-Type": "application/json",
                },
                json={
                    "projectId": project_id,
                    "region": bb_config.get("region", "us-east-1"),
                    "proxy": bb_config.get("proxy", "fingerprint-resistant"),
                    "ttl": bb_config.get("session_ttl_seconds", 300),
                    "activityTtl": bb_config.get("activity_ttl_seconds", 60),
                },
            )
            session_data = resp.json()
            session_id = session_data["id"]
            cdp_url = session_data["connectUrl"]

        # -- Connect Playwright to the remote browser via CDP ------------
        p = await async_playwright().start()
        self.browser = await p.chromium.connect_over_cdp(cdp_url)
        self.context = self.browser.contexts[0]
        self.page = self.context.pages[0] if self.context.pages \
                     else await self.context.new_page()
        logger.info("Browserbase cloud session started: %s", session_id)

    async def setup(self):
        """Initialize browser — local or Browserbase."""
        mode = self.browser_cfg.get("mode", "local")
        if mode == "browserbase":
            await self._setup_browserbase_session()
        else:
            await self._setup_local_browser()

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    async def _load_cached_session(self) -> bool:
        """Load previously saved cookies to skip login."""
        cookie_path = Path(self.session_cfg["cookie_cache"])
        if cookie_path.exists():
            cookies = json.loads(cookie_path.read_text())
            await self.context.add_cookies(cookies)
            logger.info("Loaded cached session cookies (%d cookies)", len(cookies))
            return True
        return False

    async def _save_session(self):
        """Persist current browser cookies to disk."""
        cookie_path = Path(self.session_cfg["cookie_cache"])
        cookie_path.parent.mkdir(parents=True, exist_ok=True)
        cookies = await self.context.cookies()
        cookie_path.write_text(json.dumps(cookies, indent=2))
        logger.info("Session cookies saved (%d cookies)", len(cookies))

    async def login(self):
        """
        Log in to LinkedIn. Tries cached session first; falls back to
        interactive login.
        """
        await self.page.goto("https://www.linkedin.com/login",
                             wait_until="domcontentloaded")

        if await self._load_cached_session():
            await self.page.goto("https://www.linkedin.com/feed",
                                 wait_until="domcontentloaded")
            if "feed" in self.page.url:
                logger.info("Session valid — logged in via cached cookies")
                return
            logger.info("Cached session expired — re-authenticating")

        # -- Interactive / env-var login ----------------------------------
        email = os.environ.get(
            self.session_cfg["credentials"]["email_env"]
        )
        password = os.environ.get(
            self.session_cfg["credentials"]["password_env"]
        )

        if not email or not password:
            print("\n=== LinkedIn Login ===")
            email = input("Email: ").strip()
            password = input("Password: ").strip()

        await self.page.fill('input[id="username"]', email)
        await self.page.fill('input[id="password"]', password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)

        # -- Handle 2FA / verification challenge --------------------------
        if "checkpoint" in self.page.url:
            print("\n⚠️  LinkedIn verification required.")
            print("Complete the challenge in the browser, then press Enter...")
            input("Press Enter after completing verification...")
            await self.page.wait_for_timeout(3000)

        # -- Save session for future runs ---------------------------------
        await self._save_session()
        logger.info("Login successful")

    # ------------------------------------------------------------------
    # Search & Navigation
    # ------------------------------------------------------------------

    def _build_search_url(self, title: str, location: str,
                          industry: str) -> str:
        """
        Build a Sales Navigator or LinkedIn search URL from ICP parameters.
        Supports both free LinkedIn search and Sales Navigator.
        """
        # URL-encode parameters
        import urllib.parse

        base = self.search_cfg.get("sales_navigator_base",
                   "https://www.linkedin.com/sales/search/people")

        # Sales Navigator URL format (example)
        params = {
            "query": f"(spellCorrectionEnabled:true,keywords:{urllib.parse.quote(title)})",
            "location": urllib.parse.quote(location),
            "industry": urllib.parse.quote(industry),
        }
        # In practice, Sales Navigator uses a more complex JSON-based filter.
        # The simplified version below constructs a basic search URL.
        query_str = f"{title} {location} {industry}"
        encoded = urllib.parse.quote(query_str)
        return f"{base}?keywords={encoded}"

    async def execute_search(self, search_url: str) -> list[LeadRecord]:
        """
        Navigate to the search URL, scroll through results, and extract leads
        from result cards.
        """
        page = self.page
        found_leads = []
        max_pages = self.search_cfg.get("max_pages", 5)

        logger.info("Navigating to: %s", search_url)
        await page.goto(search_url, wait_until="domcontentloaded",
                        timeout=self.timing.get("page_load_timeout", 30) * 1000)

        for page_num in range(1, max_pages + 1):
            logger.info("Scraping page %d/%d", page_num, max_pages)

            # -- Wait for result cards to render --------------------------
            try:
                await page.wait_for_selector(
                    'div[class*="search-result"]',
                    timeout=10000
                )
            except Exception:
                logger.warning("No result cards found on page %d", page_num)
                break

            # -- Scroll to trigger lazy loading ---------------------------
            await self._slow_scroll()

            # -- Extract leads from current page --------------------------
            page_leads = await self._extract_results_from_page()
            found_leads.extend(page_leads)
            logger.info("  Extracted %d leads from page %d",
                        len(page_leads), page_num)

            # -- Navigate to next page ------------------------------------
            next_btn = page.locator('button[aria-label="Next"]')
            if await next_btn.is_disabled() or not await next_btn.is_visible():
                logger.info("No more pages available")
                break

            # -- Throttle before clicking next ----------------------------
            await self._human_delay()
            await next_btn.click()
            await page.wait_for_timeout(3000)

        return found_leads

    # ------------------------------------------------------------------
    # Extraction
    # ------------------------------------------------------------------

    async def _extract_results_from_page(self) -> list[LeadRecord]:
        """
        Parse LinkedIn search result cards and extract lead data.
        Selectors vary between Sales Navigator and free LinkedIn search;

        Sales Navigator result-card selectors:
          - Name:     a[class*="profile-name"]
          - Title:    div[class*="title"]
          - Company:  div[class*="company-name"]
          - Location: div[class*="location"]

        Free LinkedIn search selectors:
          - Name:     span[class*="entity-result__title-text"]
          - Title:    div[class*="entity-result__primary-subtitle"]
          - Company:  div[class*="entity-result__secondary-subtitle"]
          - Location: div[class*="entity-result__tertiary-subtitle"]
        """
        leads = []

        # -- Try Sales Navigator card selectors first --------------------
        cards = await self.page.query_selector_all(
            'div[class*="search-result"]'
        )
        if not cards:
            # -- Fallback to free LinkedIn search selectors --------------
            cards = await self.page.query_selector_all(
                'li[class*="search-result"]'
            )

        for card in cards:
            try:
                lead = await self._parse_card(card)
                if lead and self._matches_icp(lead):
                    leads.append(lead)
            except Exception as e:
                logger.debug("Skipping malformed card: %s", e)
                continue

        return leads

    async def _parse_card(self, card) -> Optional[LeadRecord]:
        """Parse a single result card into a LeadRecord."""
        # -- Name --------------------------------------------------------
        name_el = await card.query_selector(
            'a[class*="profile-name"], span[class*="entity-result__title-text"] a'
        )
        name = await name_el.inner_text() if name_el else None

        # -- Profile URL -------------------------------------------------
        profile_url = await name_el.get_attribute("href") if name_el else None
        if profile_url and not profile_url.startswith("http"):
            profile_url = f"https://www.linkedin.com{profile_url}"
        # Clean up tracking params
        if profile_url:
            profile_url = profile_url.split("?")[0]

        # -- Title -------------------------------------------------------
        title_el = await card.query_selector(
            'div[class*="title"], div[class*="entity-result__primary-subtitle"]'
        )
        title = await title_el.inner_text() if title_el else None

        # -- Company -----------------------------------------------------
        company_el = await card.query_selector(
            'div[class*="company-name"], div[class*="entity-result__secondary-subtitle"]'
        )
        company = await company_el.inner_text() if company_el else None

        # -- Location ----------------------------------------------------
        location_el = await card.query_selector(
            'div[class*="location"], div[class*="entity-result__tertiary-subtitle"]'
        )
        location = await location_el.inner_text() if location_el else None

        if not all([name, title, company, location, profile_url]):
            return None

        # Clean up whitespace
        name = name.strip()
        title = title.strip()
        company = company.strip()
        location = location.strip()

        return LeadRecord(
            name=name,
            title=title,
            company=company,
            location=location,
            profile_url=profile_url,
            company_size=None,  # populated during enrichment
        )

    async def _parse_company_size(self) -> Optional[str]:
        """
        When viewing a company page or profile, attempt to extract the
        company size from the "About" section or company page header.
        Example: "51-200 employees"
        """
        try:
            # Attempt selector variations
            size_el = await self.page.query_selector(
                'dd:has-text("employees"), '
                'span:has-text("employees"), '
                'div[class*="company-size"]'
            )
            if size_el:
                text = await size_el.inner_text()
                return text.strip()
        except Exception:
            pass
        return None

    # ------------------------------------------------------------------
    # Enrichment — Visit Each Profile for Company Size
    # ------------------------------------------------------------------

    async def enrich_leads(self, leads: list[LeadRecord]) -> list[LeadRecord]:
        """
        Visit each profile page to extract additional data not available
        on the search results card (e.g., company_size).
        """
        enriched = []
        total = len(leads)
        for idx, lead in enumerate(leads):
            logger.info("Enriching %d/%d: %s", idx + 1, total, lead.name)
            try:
                await self.page.goto(
                    lead.profile_url,
                    wait_until="domcontentloaded",
                    timeout=self.timing.get("page_load_timeout", 30) * 1000,
                )
                await self.page.wait_for_timeout(2000)

                # -- Extract company size from profile or company section
                company_size = await self._parse_company_size()
                if company_size:
                    lead.company_size = company_size

                enriched.append(lead)

                # -- Throttle between profile visits --------------------
                await self._human_delay(
                    min_sec=self.timing.get("profile_delay_min", 5),
                    max_sec=self.timing.get("profile_delay_max", 10),
                )
            except Exception as e:
                logger.warning("Failed to enrich %s: %s", lead.profile_url, e)
                enriched.append(lead)  # keep the record anyway

        return enriched

    # ------------------------------------------------------------------
    # ICP Matching
    # ------------------------------------------------------------------

    def _matches_icp(self, lead: LeadRecord) -> bool:
        """
        Apply post-extraction ICP filters defined in config.yaml.
        Checks title regex match and location inclusion.
        """
        filters = self.cfg.get("filters", {})

        # -- Title regex check -------------------------------------------
        title_regexes = filters.get("title_regex", [])
        if title_regexes:
            title_lower = lead.title.lower()
            match = any(
                re.search(pattern, title_lower, re.IGNORECASE)
                for pattern in title_regexes
            )
            if not match:
                return False

        # -- Location inclusion check ------------------------------------
        location_contains = filters.get("location_contains", [])
        if location_contains:
            match = any(
                loc.lower() in lead.location.lower()
                for loc in location_contains
            )
            if not match:
                return False

        # -- Title exclusion check ---------------------------------------
        title_exclude = filters.get("title_exclude", [])
        if title_exclude:
            title_lower = lead.title.lower()
            match = any(
                ex.lower() in title_lower
                for ex in title_exclude
            )
            if match:
                return False

        return True

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    async def _human_delay(self, min_sec: float = None, max_sec: float = None):
        """Wait a random interval to simulate human behavior."""
        min_sec = min_sec or self.timing.get("delay_min", 3)
        max_sec = max_sec or self.timing.get("delay_max", 7)
        delay = random.uniform(min_sec, max_sec)
        logger.debug("Delay %.1f seconds", delay)
        await asyncio.sleep(delay)

    async def _slow_scroll(self):
        """
        Slowly scroll the page to trigger lazy-loaded results.
        LinkedIn loads content incrementally as the user scrolls.
        """
        for _ in range(8):
            await self.page.evaluate(
                "window.scrollBy(0, window.innerHeight / 2)"
            )
            await asyncio.sleep(random.uniform(0.5, 1.2))

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def export(self, leads: list[LeadRecord]):
        """Write extracted leads to JSONL and/or CSV files."""
        output_dir = Path(self.output_cfg.get("directory", "output"))
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        prefix = self.output_cfg.get("filename_prefix", "leads")
        formats = self.output_cfg.get("formats", ["jsonl"])

        records = [lead.model_dump() for lead in leads]

        # -- JSONL -------------------------------------------------------
        if "jsonl" in formats:
            path = output_dir / f"{prefix}_{timestamp}.jsonl"
            with open(path, "w") as f:
                for rec in records:
                    f.write(json.dumps(rec) + "\n")
            logger.info("Exported %d leads to %s", len(records), path)

        # -- CSV ---------------------------------------------------------
        if "csv" in formats:
            path = output_dir / f"{prefix}_{timestamp}.csv"
            if records:
                with open(path, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=records[0].keys())
                    writer.writeheader()
                    writer.writerows(records)
            logger.info("Exported %d leads to %s", len(records), path)

    # ------------------------------------------------------------------
    # Orchestration
    # ------------------------------------------------------------------

    async def run(self):
        """Full pipeline: setup → login → search → enrich → export."""
        await self.setup()
        await self.login()

        all_leads = []

        # Build queries from ICP combinations
        for title in self.target["titles"][:3]:   # limit to 3 for demo
            for location in self.target["locations"][:2]:
                for industry in self.target["industries"][:3]:
                    url = self._build_search_url(title, location, industry)
                    logger.info("=== Search: title=%s | location=%s | industry=%s",
                                title, location, industry)
                    leads = await self.execute_search(url)

                    # Deduplicate
                    for lead in leads:
                        if lead.profile_url not in self.leads:
                            self.leads[lead.profile_url] = lead

                    await self._human_delay()

        all_leads = list(self.leads.values())
        logger.info("Total unique leads extracted: %d", len(all_leads))

        # -- Enrich with company_size if configured ----------------------
        if self.output_cfg.get("enrich_profiles", True) and all_leads:
            logger.info("Enriching %d leads with profile data...", len(all_leads))
            all_leads = await self.enrich_leads(all_leads)

        # -- Export ------------------------------------------------------
        self.export(all_leads)
        logger.info("Pipeline complete — %d leads exported", len(all_leads))

        # -- Cleanup -----------------------------------------------------
        if self.browser:
            await self.browser.close()

        return all_leads


# ===========================================================================
# Entry Point
# ===========================================================================

async def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="LinkedIn ICP-Matched Lead Scraper"
    )
    parser.add_argument(
        "--config", default="config.yaml",
        help="Path to configuration YAML file"
    )
    parser.add_argument(
        "--headless", action="store_true",
        help="Run browser in headless mode"
    )
    parser.add_argument(
        "--browserbase", action="store_true",
        help="Use Browserbase cloud browser instead of local"
    )
    args = parser.parse_args()

    # -- Load config -------------------------------------------------------
    config = load_config(args.config)

    # -- Override browser mode from CLI args -------------------------------
    if args.browserbase:
        config["browser"]["mode"] = "browserbase"
    if args.headless:
        config["browser"]["local"]["headless"] = True

    # -- Run scraper -------------------------------------------------------
    scraper = LinkedInScraper(config)
    try:
        leads = await scraper.run()
        print(f"\n✅ Done! {len(leads)} leads extracted.")
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user — exporting partial results...")
        if scraper.leads:
            scraper.export(list(scraper.leads.values()))
        sys.exit(1)
    except Exception as e:
        logger.exception("Fatal error: %s", e)
        if scraper.leads:
            scraper.export(list(scraper.leads.values()))
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
