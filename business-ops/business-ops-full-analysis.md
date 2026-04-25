# Business Operations — Full Operational Analysis
**Classification:** Exploratory/ideation research (Claude Chat, Apr 24 2026) — not verified market data
**Prepared for:** Nova (Hermes Agent, execution layer)
**Living document:** Update as businesses launch and evolve

---

## Table of Contents
1. [Current Status & Tool Tracker](#1-current-status--tool-tracker)
2. [Stack & Cost Summary](#2-stack--cost-summary)
3. [Executive Projections](#3-executive-projections)
4. [Per-Business Deep Dives](#4-per-business-deep-dives)
5. [Build Timeline](#5-build-timeline)
6. [SWOT Analysis](#6-swot-analysis)
7. [Risk Register](#7-risk-register)
8. [Tool Acquisition Priority](#8-tool-acquisition-priority)

---

## 1. Current Status & Tool Tracker

*Last updated: Apr 24 2026 — Pre-launch (all in planning)*

### Tool Acquisition Status

| Tool | Status | Cost | Unlocks |
|------|--------|:----:|---------|
| ✅ n8n (self-hosted) | 🔲 Not installed yet | $0 | n8n Agency |
| ✅ Hermes + Codex | ✅ Active | ~$0.50/mo | n8n Agency |
| ✅ Browserbase | ✅ Configured | Included | Appointment Setting |
| ✅ Tavily | ✅ Active | Included | All |
| ✅ Telegram | ✅ Active | $0 | All alerts |
| ✅ Discord | ✅ Active | $0 | All alerts |
| ❌ Instantly | Needs account + setup | $37/mo | n8n Agency, Appt Setting |
| ❌ Cal.com | Needs setup | Free | Appt Setting |
| ❌ ElevenLabs API Key | Needs acquisition | $22/mo | Local Biz, YouTube |
| ❌ Twilio Account | Needs setup | ~$20/mo | Local Biz |
| ❌ DataForSEO API | Needs account | ~$15/mo | Local Biz |
| ❌ FAL_KEY | Needs acquisition | ~$20/mo | YouTube Empire |
| ❌ Shotstack API | Needs account | ~$5/mo | YouTube Empire |
| ❌ Hospitable.com | Needs account | $40/mo | Airbnb Op + Co-Host |
| ❌ PriceLabs | Needs account | $20/listing | Airbnb Op + Co-Host |
| ❌ VidIQ | Needs account | $10/mo | YouTube Empire |
| ❌ Exchange API Keys (CEX) | Needs setup | Free | Crypto Bot |
| ❌ Alchemy/Infura | Needs account | $25/mo | Crypto Bot |

### Key Gaps Blocking Launch

| Missing Key | Blocks |
|---|---|
| ElevenLabs + Twilio | Local Business Package, YouTube voice |
| FAL_KEY | YouTube visuals |
| Hospitable.com | Both Airbnb ops |

---

## 2. Stack & Cost Summary

**Baseline stack cost (all 7 running): ~$303/mo**
**Compare: Naïve AI equivalent = $509-609/mo (incl. platform fees)**

| Category | Monthly |
|:---------|:-------:|
| LLM (deepseek-v4-flash via OpenRouter) | ~$12 |
| Instantly | $37 |
| ElevenLabs | $22 |
| Twilio | ~$20 |
| FAL.ai | ~$20 |
| Shotstack | ~$5 |
| Hospitable.com | $40-120 |
| PriceLabs | $20-60 |
| DataForSEO | ~$15 |
| VidIQ | $10 |
| Misc (domains, etc.) | ~$30 |
| **Total tools** | **~$291/mo** |
| **Total with LLM** | **~$303/mo** |

---

## 3. Executive Projections

### Conservative (Months 1-6, stabilized)

| Business | Revenue | Profit | Margin |
|----------|-------:|------:|:-----:|
| Appointment Setting Agency | $4,500 | $4,440 | 98.7% |
| n8n Automation Agency | $4,000 | $3,950 | 98.8% |
| Local Business AI Package | $4,000 | $3,942 | 98.6% |
| Airbnb Operator (operational) | $2,600 | $1,760 | 67.7% |
| Faceless YouTube Empire | $950 | $897 | 94.4% |
| Airbnb Co-Hosting | $600 | $538 | 89.7% |
| Crypto Trading Bot ($5K cap) | $150* | $120* | 80.0% |
| **Total** | **$16,800** | **$15,647** | **93.1%** |

*Crypto: 3% monthly return on $5K. Capital at risk. Not guaranteed.

**Year 1 projected profit (accounting for ramp-up): ~$169,000**

### Realistic (Months 7-12+, scaled)

| Business | Revenue | Profit |
|----------|-------:|------:|
| n8n Automation Agency | $15,000 | $14,920 |
| Appointment Setting Agency | $20,000 | $19,880 |
| Local Business AI Package | $18,000 | $17,880 |
| Faceless YouTube Empire | $8,000 | $7,900 |
| Airbnb Co-Hosting | $4,500 | $4,270 |
| Airbnb Operator (3 properties) | $10,560 | $8,340 |
| Crypto Trading Bot ($25K cap) | $750 | $720 |
| **Total** | **~$76,810** | **~$73,910** |

**Year 1 realistic range: ~$250K-$320K**

---

## 4. Per-Business Deep Dives

---

### 4.1 n8n Automation Agency

**Model:** Build and sell custom n8n workflow automations to businesses. Charge per project ($2K-3K avg).

**Priority:** #1 — best fit for stack, zero marginal cost, fastest to revenue

**Why it works:** Hermes + Codex generates workflow JSON natively. Delivery time is hours, not weeks.

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | 99% margin, zero new tools needed, Codex does the building |
| **Weaknesses** | Need client pipeline; no portfolio yet |
| **Opportunities** | n8n now has MCP support — Nova can trigger workflows via MCP meta-automation |
| **Threats** | Competition from fiverr/upwork operators; clients may build in-house later |

**Action items:**
1. 🔲 Install n8n: `docker run -d -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n`
2. 🔲 Build 3 demo workflows (lead capture→CRM, invoice→notify, form→Slack)
3. 🔲 Set up Instantly with sending domain
4. 🔲 Codex-generate an n8n workflow template for "local business lead capture"
5. 🔲 Create outreach campaign targeting SMB in legal/medical/real estate

**Key risks:** Client churn, deliverability issues in outreach

**Timeline:** Month 1 launch, 2 clients by month 2, scaling by month 4-6

**Costs:** ~$0.50/mo LLM + $37/mo Instantly + $20 misc = ~$58/mo

---

### 4.2 Appointment Setting Agency

**Model:** Prospect, personalize, send outbound email sequences for B2B clients. Monthly retainer ($1.5K-2.5K/client).

**Priority:** #2 — second fastest cash, enables sales motion for all other businesses

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | Hermes runs the full loop end-to-end; 99% margin |
| **Weaknesses** | Needs Instantly + sending domain; deliverability is fragile |
| **Opportunities** | Combine with n8n lead capture for pipeline synergy |
| **Threats** | Email deliverability getting harder industry-wide |

**Action items:**
1. 🔲 Create Instantly account + SPF/DKIM/DMARC for sending domain
2. 🔲 Build LinkedIn scraper skill (Browserbase → extract ICP leads)
3. 🔲 Write first 5-touch email sequence (target: roofing, HVAC, dental)
4. 🔲 Configure Cal.com booking page
5. 🔲 Create daily Hermes cron: check replies → qualify → book → log to Notion

**Key risks:** Deliverability collapse (mitigation: rotate domains, warm inboxes)

**Timeline:** Month 1-2 launch, 3 clients by month 2

**Costs:** ~$60/mo

---

### 4.3 Local Business AI Package

**Model:** AI phone receptionist + local SEO + ad monitoring. $800-1,200/mo retainer.

**Priority:** #3 — highest local demand, obvious value pitch

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | Immediate obvious value; easy demo ("missed calls → lost revenue") |
| **Weaknesses** | Blocked until ElevenLabs + Twilio acquired; local biz clients are price-sensitive |
| **Opportunities** | Massive underserved market; can white-label to digital agencies |
| **Threats** | Client turnover; competing on price |

**Action items:**
1. 🔲 Get ElevenLabs API key + Twilio account (~$42/mo)
2. 🔲 Build "AI receptionist" demo (Twilio → ElevenLabs → Hermes intent handling → booking)
3. 🔲 Run DataForSEO keyword audit for demo business (e.g., "plumber Toronto")
4. 🔲 Generate SEO content brief + first article
5. 🔲 Build outreach (Facebook Groups, Google Maps scrape, LinkedIn)

**Key risks:** Client churn (mitigation: 3-month auto-renewal contracts)

**Timeline:** Month 2 launch, 5 clients by month 4-6

**Costs:** ~$58/mo

---

### 4.4 Faceless YouTube Empire

**Model:** 3-5 channels in high-CPM niches. AdSense + affiliates. Slow build, compound growth.

**Priority:** #7 — start as background build, monetizes at month 6

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | Compound indefinitely; once built, runs mostly autonomously |
| **Weaknesses** | 6-month monetization delay; blocked until FAL + ElevenLabs acquired |
| **Opportunities** | Finance/investing/real estate niches have $12-30 CPM |
| **Threats** | Algorithm changes; niche selection risk |

**Action items:**
1. 🔲 Acquire FAL_KEY + ElevenLabs key
2. 🔲 Sign up for Shotstack (or test ffmpeg as fallback)
3. 🔲 Set up YouTube Data API OAuth
4. 🔲 Pick 3 high-CPM niches (finance, AI tools explainers, stoicism)
5. 🔲 Create daily cron: 09:00 ET → Tavily topics → script → ElevenLabs → FAL → Shotstack → YouTube

**Key risks:** Algorithm shift (mitigation: diversify across 3-5 niches)

**Timeline:** Month 3 launch, month 6 monetize, month 12 scaled

**Costs:** ~$53/mo per 3 channels

---

### 4.5 Crypto Trading Bot

**Model:** Momentum/mean-reversion strategies via CCXT + DeFiLlama. $5K starting capital.

**Priority:** #4 — paper trade now, go live after 30-day validation

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | CCXT + Tavily sentiment + DeFiLlama data — full pipeline available |
| **Weaknesses** | Investment capital at risk; no backtesting done yet |
| **Opportunities** | Compounding returns on larger capital; DeFi yield strategies |
| **Threats** | 🔴 Capital loss risk; market volatility |

**Action items:**
1. 🔲 Set up Alchemy free tier (Ethereum RPC)
2. 🔲 Configure CCXT with read-only exchange API keys
3. 🔲 Build paper trading script: market data → simulate → log P&L → Telegram alert
4. 🔲 **RUN PAPER TRADING 30 DAYS MINIMUM**
5. 🔲 After validation: add live execution, -10% hard stop-loss

**Key risks:** 🔴 Capital loss (mitigation: 30-day paper trade, -10% hard stop, never >5% liquid net worth)

**Timeline:** Month 1 paper trade start, month 2-3 live if validated

**Costs:** ~$30/mo (Alchemy $25 + LLM $5)

---

### 4.6 Airbnb Operator

**Model:** Operate own short-term rental. AI guest communications + dynamic pricing.

**Priority:** #6 — needs property situation evaluated first

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | Proven model; AI makes it nearly hands-off |
| **Weaknesses** | Property cost/rent not modelled; blocked until Hospitable acquired |
| **Opportunities** | Combine with Co-Hosting for portfolio scaling |
| **Threats** | Airbnb ToS changes; local STR regulations |

**Action items:**
1. 🔲 Evaluate property situation (own vs rent vs arbitrage)
2. 🔲 Sign up for Hospitable.com + request API access
3. 🔲 Connect Hermes to Hospitable API → guest message automation
4. 🔲 Connect PriceLabs → seasonal pricing
5. 🔲 Daily cron: new bookings → pre-arrival → post-stay review request

**Key risk:** ❗ Property cost not modelled. Need to confirm numbers before pursuing.

**Timeline:** Month 1 if property ready, otherwise contingent

**Costs:** ~$840/mo operational (excl. property cost)

---

### 4.7 Airbnb Co-Hosting

**Model:** Manage other owners' listings for 15-18% revenue cut. Zero capital at risk.

**Priority:** #5 — lower risk than Operator, builds same muscle

#### Structured Extract

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | Zero capital required; scales linearly with properties |
| **Weaknesses** | Finding property owners is the barrier; needs Hospitable |
| **Opportunities** | Can start as Co-Host then transition to Operator |
| **Threats** | Same as Operator (Airbnb ToS) |

**Action items:**
1. 🔲 Same Hospitable + PriceLabs setup as Operator
2. 🔲 Build co-hosting pitch: "85% revenue to you, hands-off management"
3. 🔲 Find property owners via: Facebook (Airbnb Hosts), Nextdoor, local investor meetups
4. 🔲 Draft co-hosting agreement (consult local STR laws)
5. 🔲 Build outreach: Hermes researches host profiles → emails them

**Key risk:** Slow to find property owners willing to outsource

**Timeline:** Month 2-3 launch, 10 properties by month 9

**Costs:** ~$62/mo for 2 properties

---

## 5. Build Timeline

```
MONTH 1
├── Week 1: Install n8n on VPS. Build 3 demo workflows.
├── Week 2: Set up Instantly. Write first outreach sequence.
├── Week 3: Launch n8n Agency outreach. Target 2 first clients.
├── Week 4: Start crypto paper trading (CCXT + Alchemy).
└── Goal: First n8n client signed = $2,000 first revenue.

MONTH 2
├── Appointment Setting fully live.
├── n8n Agency: 2 active, 1 in pipeline.
├── Paper trading: continue logging.
├── Acquire ElevenLabs + Twilio → build AI receptionist demo.
└── Goal: $6,390/mo run rate (n8n + appointment).

MONTH 3
├── Local Business Package: first 2 clients.
├── Start Airbnb co-hosting outreach.
├── YouTube: launch first channel (needs FAL + ElevenLabs).
├── Paper trading: 30-day mark. Evaluate live deployment.
└── Goal: $14,330/mo run rate (n8n + appointment + local biz).

MONTH 4-5
├── Airbnb Co-Hosting: 2 properties onboarded.
├── Airbnb Operator: evaluate property.
├── Local Business: scale to 5 clients.
├── Crypto: live on $5K if paper validated.
├── YouTube: 3 channels posting.
└── Goal: $15,200/mo run rate (all except YouTube monetized).

MONTH 6
├── YouTube monetization threshold hit.
├── All 7 operations active.
├── Conservative combined: $15,647/mo profit.
├── Begin scaling: raise agency rates, add properties.
└── Goal: All ops stabilized.

MONTH 7-12
├── Scale what's working, double down on highest-margin ops.
├── Realistic by month 12: $40K-$66K/mo profit.
├── Year 1 total conservative: ~$169,000.
├── Year 1 total realistic: ~$250K-$320K.
└── Goal: $50K/mo profit milestone.
```

---

## 6. SWOT Analysis

### Strengths
- **DeepSeek V4 Flash at $0.14/M input** — cheapest capable model as of Apr 2026
- **1M context window** enables complex multi-document work
- **Self-hosted n8n** replaces $20-50/mo SaaS tools
- **Full terminal access** (Python, bash, CCXT, ffmpeg)
- **MCP servers** (GitHub + Filesystem) for structured data
- **Codex CLI** for AI code generation
- **Near-100% margins** on agency businesses
- **No customer acquisition cost** modelled (organic/outbound)
- **Infrastructure doesn't multiply** — all 7 ops on same stack
- **No headcount** — Nova executes, Jason strategizes
- **Self-hosted Naïve AI competitor** — transparent, customizable, cheaper

### Weaknesses
- ❌ No FAL_KEY → YouTube blocked
- ❌ No ElevenLabs key → voice businesses blocked
- ❌ No exchange API keys → Crypto paper-trade only
- ❌ Hospitable.com dependency (no official Airbnb API)
- ❌ YouTube requires 6 months before any revenue
- ⚠️ Single operator (Jason) — all businesses depend on one person
- ⚠️ No proper CRM yet
- ⚠️ No sales page / landing page infrastructure
- ⚠️ No accounting/invoicing setup
- ⚠️ Crypto strategy not backtested
- ⚠️ No STR operating experience
- ⚠️ YouTube niche selection not validated

### Opportunities
- AI automation agency market growing rapidly
- Local businesses massively underserved
- Naïve AI proves demand but can't match on price/customization
- n8n MCP support → Nova can trigger workflows via MCP meta-automation
- agent-swarm-development skill for complex builds
- Skills compound over time
- Agencies fund tool acquisition for YouTube/Crypto
- YouTube channels compound indefinitely
- Co-hosting scales linearly with no capital ceiling
- White-label Local Biz Package to digital agencies

### Threats
| Threat | Severity | Mitigation |
|--------|:--------:|------------|
| Crypto capital loss | 🔴 High | Paper trade 30d, -10% stop, never >5% NW |
| Email deliverability collapse | 🟡 Med | Rotate domains, warm inboxes |
| Airbnb ToS change / account ban | 🟡 Med | Hospitable API (legitimate); Browserbase fallback |
| Agency client churn | 🟡 Med | Monthly ROI reports; 30-day auto-renewal |
| YouTube algorithm shift | 🟡 Med | Diversify across 3-5 niches |
| FAL/ElevenLabs API downtime | 🟡 Med | Build fallback (local TTS, static footage) |
| OpenRouter outage | 🟡 Med | Fallback model already configured |
| Local biz client dissatisfaction | 🟡 Med | Monthly metrics; 30-day trial for first 2 |
| Hermes breaking update | 🟢 Low | Pin v0.10.0, test staging |
| n8n instance down | 🟢 Low | Add n8n healthcheck to cron |

---

## 7. Risk Register (Full)

| # | Risk | Severity | Businesses Affected | Mitigation |
|---|------|:--------:|---------------------|------------|
| 1 | Crypto capital loss | 🔴 High | Crypto Bot | 30-day paper trade min; -10% hard stop-loss; never >5% liquid net worth |
| 2 | Email deliverability collapse | 🟡 Medium | Appt Setting, n8n Agency | Rotate Instantly domains; warm new inboxes; monitor spam rates weekly |
| 3 | Airbnb ToS change / account ban | 🟡 Medium | Airbnb Op, Co-Host | Hospitable API (legitimate); have Browserbase fallback |
| 4 | Agency client churn | 🟡 Medium | n8n, Appt, Local Biz | Monthly ROI reports; auto-renewal contracts; 30-day notice |
| 5 | YouTube algorithm shift | 🟡 Medium | YouTube Empire | Diversify across 3-5 niches/platforms |
| 6 | FAL/ElevenLabs API downtime | 🟡 Medium | YouTube, Local Biz | Local TTS fallback; static stock footage fallback |
| 7 | OpenRouter API outage | 🟡 Medium | All | Fallback model stack (minimax) already configured |
| 8 | Local biz dissatisfaction | 🟡 Medium | Local Biz Pkg | Monthly reporting; 30-day trial period first 2 clients |
| 9 | Hospitable.com API changes | 🟡 Medium | Airbnb Op, Co-Host | Monitor ToS; have browser scrap fallback |
| 10 | Hermes breaking change | 🟢 Low | All | Pin version; never upgrade production without testing |
| 11 | n8n instance downtime | 🟢 Low | n8n Agency | Add n8n healthcheck to existing service monitor cron |
| 12 | Missing key blocks business launch | 🟡 Medium | YouTube, Local Biz | Prioritize acquisition order: ElevenLabs → FAL → Twilio |

---

## 8. Tool Acquisition Priority

Based on what unlocks the most value simultaneously:

| Order | Tool | Monthly Cost | Unlocks |
|:-----:|------|:-----------:|---------|
| 1 | **ElevenLabs API key** | $22 | Local Biz receptionist + YouTube voice |
| 2 | **FAL_KEY** | ~$20 | YouTube visual pipeline |
| 3 | **Twilio** | ~$20 | AI receptionist (live calls) |
| 4 | **Hospitable.com** | $40 | Both Airbnb operations |
| 5 | **Exchange API keys** | $0 | Live Crypto trading |

---

*Based on research by Claude Chat (Apr 24, 2026). Market data is exploratory/unverified — take projections as directional ideas, not commitments. Update as real data comes in.*
