# LinkedIn ICP-Matched Lead Scraper

> Browser-based LinkedIn lead extraction for Ideal Customer Profile (ICP) targeting.

## Overview

This scraper automates LinkedIn Sales Navigator and search results to extract prospect leads matching a defined ICP. It uses a browser-automation pattern compatible with **Playwright** (via `selenium-wire` bridge or direct Playwright) and works locally or on **Browserbase** cloud browsers.

## Target ICP Criteria

| Dimension    | Values                                                                 |
|-------------|------------------------------------------------------------------------|
| **Titles**   | Operations Manager, CEO, Founder, COO, General Manager                 |
| **Location** | Toronto, Greater Toronto Area (GTA), Mississauga, Brampton, Scarborough|
| **Industries** | Construction, Real Estate, Dental, HVAC, Property Management          |
| **Company Size** | 11–200 employees (SME focus), 201–1000 (mid-market)                 |

## Prerequisites

- Python 3.10+
- [Playwright](https://playwright.dev/python/) (`pip install playwright`)
- A LinkedIn account (Sales Navigator recommended for advanced filters)
- (Optional) [Browserbase](https://browserbase.com/) API key for cloud execution

## Installation

```bash
cd linkedin-scraper
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### requirements.txt

```
playwright>=1.40.0
pyyaml>=6.0
pydantic>=2.0
httpx>=0.25.0
rich>=13.0
```

## Configuration

Edit `config.yaml` to set:

- **`search.queries`** — LinkedIn search URLs or keyword combinations
- **`target.titles`** — Job titles to match
- **`target.locations`** — Geographic areas
- **`target.industries`** — Industry verticals
- **`browser`** — Local vs Browserbase mode
- **`output`** — File format and path for extracted leads

## Usage

### Local Execution

```bash
python scraper.py --config config.yaml --headless
```

Login credentials are prompted on first run; session cookies are cached to `data/session.json` for reuse.

### Browserbase Cloud

```bash
export BROWSERBASE_API_KEY="your-key"
python scraper.py --config config.yaml --browserbase
```

The script creates a remote Browserbase session and routes all Playwright calls through it.

## Output Schema

Extracted leads are saved as JSON Lines (`.jsonl`) and optionally as CSV. Each record follows `output-schema.json`:

| Field          | Type   | Description                              |
|---------------|--------|------------------------------------------|
| `name`        | string | Prospect full name                       |
| `title`       | string | Current job title                        |
| `company`     | string | Current company name                     |
| `location`    | string | Geographic location from profile         |
| `profile_url` | string | LinkedIn public profile URL              |
| `company_size`| string | Employee count range (e.g. "51-200")     |

## Workflow

1. **Login & Session** — Authenticate via headless browser, persist cookies
2. **Search & Navigate** — Execute ICP search queries via Sales Navigator / LinkedIn Search
3. **Extract Results** — Parse profile cards from search result pages
4. **Deduplicate** — Remove duplicates by `profile_url`
5. **Enrich** — Optionally open each profile for additional details (company size, industry)
6. **Export** — Write to `output/leads-{timestamp}.jsonl`

## Notes

- LinkedIn actively rate-limits; use humane delays (`delay_min: 3`, `delay_max: 7` seconds)
- A single session should stay under 200 profile views to avoid soft blocks
- Use **Browserbase's fingerprinting-resist** proxy for large-scale extraction
- Respect LinkedIn's ToS; this tool is intended for internal lead management
