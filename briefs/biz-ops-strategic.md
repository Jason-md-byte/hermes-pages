# Business Operations — Strategic Brief
**For:** Nova (Hermes Agent) · **From:** Jason · **Date:** April 2026
**Classification:** Strategic context — projections, risks, competitive positioning, timeline
**File:** `biz-ops-strategic.md`

---

## 1. Financial Summary

| Metric | Conservative | Realistic (12-month) |
|--------|------------:|---------------------:|
| Monthly Revenue | $16,800 | $47,100 |
| Monthly Profit | $15,647 | $39,000 |
| Weighted Avg Margin | 93% | 93% |
| Year 1 Profit | ~$169K | ~$390K |
| LLM API Cost (all 7) | ~$12/mo | ~$30/mo |
| Tool Stack Cost (all 7) | $291/mo | $291/mo |
| **True All-In Cost** | **~$303/mo** | **~$321/mo** |

**LLM:** deepseek-v4-flash via OpenRouter · $0.14/M input · $0.28/M output

---

## 2. SWOT Analysis

### Strengths
- **Near-zero LLM cost** ($0.14/M input) — ~$12/mo for all 7 businesses combined. Structural cost advantage that compounds.
- **Full stack control** on own VPS. No platform dependency, no per-credit billing, no black box.
- **8 tools replaced at $0** by Hermes natively: prospecting, CRM, trend research, alerts, trading execution, scheduling, content distribution, SEO research.
- **Already operational** — 59 skills loaded, GitHub + Filesystem MCP active, morning briefing running, Telegram + Discord live.
- **Dog-fooding at scale** — n8n self-hosted on same VPS means the product (sold workflows) and infrastructure (Hermes) are the same stack.

### Weaknesses
- **Single operator** — no redundancy if Jason is unavailable.
- **No existing customer base** — all acquisition starts from zero.
- **YouTube requires 6 months** before first revenue. Tests patience.
- **Airbnb Operator requires property capital** — not asset-light.
- **Browser automation via Browserbase** is inherently fragile against platforms that actively fight it.

### Opportunities
- **SMB automation gap** is enormous. Fewer than 5% of local businesses have meaningful AI tooling. First-mover advantage is real and fleeting.
- **n8n now supports MCP** — Nova can trigger n8n workflows directly via MCP. Differentiated product feature competitors don't have.
- **Cross-sell naturally** — n8n clients need appointment setting. Local biz clients need AI reception. Build one, pitch both.
- **Airbnb Co-Hosting scales linearly** — 20 properties = $5,380/mo with same $62/mo stack. Zero additional capital.
- **YouTube faceless content demand** is accelerating. AI tooling makes production cost near-zero.

### Threats
| Threat | Severity | Mitigation |
|--------|:--------:|------------|
| Crypto capital loss | 🔴 **HIGH** | Paper trade 30d minimum. Hard cap 5% NW. Kill switch -15%. |
| Airbnb ToS drift | 🔴 **HIGH** | Monitor Hospitable announcements. Document Browserbase fallback. |
| Agency client churn | 🟡 MED | Monthly ROI reporting. Demonstrate value. Month-to-month contracts. |
| Email deliverability drift | 🟡 MED | Rotate Instantly domains. Weekly bounce monitoring cron. |
| YouTube AI content demonetization | 🟡 MED | Diversify niches. Affiliate revenue as backup. |
| Local biz client turnover | 🟡 MED | 3-month auto-renew contracts. Focus on call capture + rank movement. |
| OpenRouter pricing change | 🟢 LOW | deepseek-v4-flash MIT licensed/open-weight. Self-hostable on this VPS. |
| Hermes breaking update | 🟢 LOW | Pinned to v0.10.0. Test staging. Never auto-update production. |

---

## 3. Risk Register

| # | Risk | Severity | Businesses Affected | Mitigation |
|---|------|:--------:|---------------------|------------|
| 1 | Crypto capital loss | 🔴 **HIGH** | Crypto Bot | Paper trade 30d minimum. -15% hard stop-loss. Never >5% liquid net worth. |
| 2 | Airbnb ToS / Hospitable policy change | 🔴 **HIGH** | Airbnb Op, Co-Host | Monitor Hospitable announcements. Document Browserbase fallback plan. |
| 3 | Agency client churn (no results) | 🟡 MED | n8n, Appt, Local Biz | Monthly ROI reporting. Auto-renew contracts with 30-day notice. |
| 4 | Email deliverability collapse | 🟡 MED | Appt Setting, n8n outreach | Rotate Instantly domains weekly. Warm new inboxes. Monitor bounce rates. |
| 5 | YouTube AI content demonetization | 🟡 MED | YouTube Empire | Diversify across 3+ niches. Affiliate as AdSense fallback. |
| 6 | FAL/ElevenLabs API outage | 🟡 MED | YouTube, Local Biz | Local TTS fallback. Static stock footage fallback scripted. |
| 7 | Local biz client turnover | 🟡 MED | Local Biz Pkg | 3-month auto-renew contracts. Focus on measurable call capture + SEO rank. |
| 8 | OpenRouter API outage | 🟢 LOW | All | Fallback model stack (minimax) already configured. |
| 9 | Hospitable.com API change | 🟢 LOW | Airbnb Op, Co-Host | Monitor status page. Browser-based fallback pre-documented. |
| 10 | Hermes breaking version change | 🟢 LOW | All | Pinned to v0.10.0. Never upgrade production without testing. |
| 11 | n8n self-hosted instance down | 🟢 LOW | n8n Agency | Add n8n healthcheck to existing service monitor cron. |

---

## 4. Competitive Context: Naive AI

A YC-backed startup (usenaive.ai, Spring 2025 batch) builds "AI employees" to run businesses. They charge $49-149/mo platform fees on top of tool costs.

**The key difference:**

| | Naïve AI | Nova (You) |
|---|---|---|
| Tool costs (all 7 ops) | ~$460/mo | ~$291/mo |
| Platform fee | $49-149/mo | $0 |
| LLM API | bundled/unknown | ~$12/mo (deepseek-v4-flash) |
| **All-in total** | **$509-609/mo** | **~$303/mo** |
| Prompt access | none | full |
| Data sovereignty | their servers | Jason's VPS |
| Customizability | template-only | unlimited |

**Key insight:** Naive AI's existence validates demand. Their SaaS model means they can't compete on price or customization.

---

## 5. 12-Month Timeline

| Month | Active Businesses | Conservative Profit | Cumulative |
|:-----:|------------------|-------------------:|:----------:|
| 1 | n8n, Appointment, Crypto, Airbnb Op (partial) | ~$8,000 | $8,000 |
| 2 | Above + Airbnb Co-Host starting | ~$10,270 | $18,270 |
| 3 | + Local Business starting | ~$12,000 | $30,270 |
| 4 | All except YouTube at full run rate | ~$14,750 | $45,020 |
| 5 | Steady | ~$14,750 | $59,770 |
| 6 | + YouTube monetizes | ~$15,647 | $75,417 |
| 7-12 | All 7 fully operational | ~$15,647/mo | — |
| | **Year 1 total** | | **~$169,299** |

---

## 6. Realistic Scaling Path (12-month target)

| Business | Conservative | Realistic | Scaling Lever |
|----------|------------:|----------:|:--------------|
| n8n Automation Agency | $3,950 | $9,950 | Raise rates to $2.5K/project · 4 projects/mo |
| Appointment Setting | $4,440 | $11,940 | 6 clients @ $2K vs 3 @ $1.5K |
| Local Business AI Package | $3,942 | $9,942 | 10 clients @ $1K vs 5 @ $800 |
| Crypto Trading Bot | $120 | $570-720 | $15K capital vs $5K (paper validated) |
| Airbnb Co-Hosting | $538 | $2,338 | 8 properties vs 2 (same stack cost) |
| Airbnb Operator | $1,760 | $5,700 | 3 properties vs 1 (if property situation allows) |
| Faceless YouTube Empire | $897 | $3,447 | 5 channels @ 400K views vs 3 @ 150K |
| **Total** | **$15,647** | **$39,000+** | — |

---

## 7. Tool Acquisition Priority

Based on what unlocks the most value simultaneously:

| Order | Tool | Cost | Unlocks |
|:-----:|------|:----:|---------|
| 1 | **ElevenLabs** | $22/mo | Local Biz receptionist + YouTube voice |
| 2 | **Instantly** | $37/mo | Appointment Setting + n8n outreach |
| 3 | **FAL_KEY** | ~$20/mo | YouTube visual pipeline |
| 4 | **Twilio** | ~$20/mo | Live AI receptionist (Local Biz) |
| 5 | **Hospitable.com** | $40/mo | Both Airbnb operations |
| 6 | **PriceLabs** | $20/mo | Airbnb pricing automation |
| 7 | **Exchange API keys** | $0 | Live crypto trading (paper first) |

**If budget is tight, buy in this order:** ElevenLabs → Instantly → FAL → Twilio → Hospitable → PriceLabs → Exchange keys

---

## 8. Key Facts (for Nova's Memory)

- All 7 businesses run on same stack · ~$303/mo total tool+LLM cost
- deepseek-v4-flash at $0.14/M input — lowest cost capable model Apr 2026
- 8 software tools replaced at $0 by Hermes natively
- n8n MCP support enables meta-automation (Nova triggers workflows directly)
- Year 1 conservative: ~$169K · Realistic 12-month: ~$39K/mo profit
- Maximum downside risk: crypto capital loss (mitigated by paper trade + kill switch)

---

**Conservative values = stabilized floor projections assuming minimal execution.**
**Realistic values = achievable with focused execution at 12-month mark.**
**Not financial advice. Crypto capital at risk. Airbnb Operator excludes property cost/mortgage.**
**Generated April 2026.**
