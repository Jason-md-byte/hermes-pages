# Business Operations — Operational Brief
**For:** Nova (Hermes Agent) · **From:** Jason · **Date:** April 2026
**Classification:** Action document — what to build, in what order, with what tools
**File:** `biz-ops-operational.md`

---

## Priority: Build Order

| Rank | Business | Profit | Key Cost | Start |
|:----:|----------|-------:|:--------:|:-----:|
| **1** | n8n Automation Agency | $3,950/mo | $0 new | Week 1 |
| **2** | Appointment Setting | $4,440/mo | $37/mo (Instantly) | Week 2 |
| **3** | Local Business AI Package | $3,942/mo | $42/mo (ElevenLabs + Twilio) | Week 3-4 |
| **4** | Crypto Trading Bot | $120/mo | $25/mo (Alchemy) | Month 1 (paper) |
| **5** | Airbnb Co-Hosting | $538/mo | $62/mo (Hospitable + PriceLabs) | Month 2-3 |
| **6** | Airbnb Operator | $1,760/mo | $840/mo operational excl. property | If property ready |
| **7** | Faceless YouTube Empire | $897/mo | $53/mo (ElevenLabs + FAL + Shotstack) | Month 6 |

**Combined conservative at stabilization:** $15,647/mo profit · **Year 1:** ~$169K
**Combined realistic 12-month target:** ~$39,000/mo profit

---

## Per-Business Action Items

### 1. n8n Automation Agency — $3,950/mo profit · 98.8% margin
**Model:** Sell custom n8n workflow automations per project ($2K-2.5K). Hermes + Codex generates the workflow JSON.

**Status:** ✅ Zero new tools needed · Best fit for this stack

- [ ] **Install n8n** — `docker run -d -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n`
- [ ] **Build Hermes skill:** `n8n-workflow-generator` — takes business problem description, outputs deployable workflow JSON via Codex
- [ ] **Build 3 demo workflows**: lead capture→CRM, invoice→notify, form→Slack
- [ ] **Draft outreach sequence** — 3-touch cold email targeting ops-heavy SMBs (agencies, e-commerce ops, RevOps teams)
- [ ] **Instantly account** ($37/mo) — needed for outreach; skip if using manual outreach first

**Costs:** $0.50/mo LLM + ~$30 misc = ~$50/mo total

---

### 2. Appointment Setting Agency — $4,440/mo profit · 98.7% margin
**Model:** B2B outbound email sequences. Monthly retainer ($1,500-2K/client). Hermes handles the full loop.

**Status:** 🔲 Needs Instantly + sending domain

- [ ] **Create Instantly account** ($37/mo) + configure sending domain with SPF/DKIM/DMARC
- [ ] **Build LinkedIn scraper** — Browserbase workflow for ICP-matched lead extraction
- [ ] **Set up Cal.com** (free) — webhook → Notion MCP pipeline for auto-logging booked meetings
- [ ] **Write first 5-touch sequence** — target niche: HVAC, roofing, dental, or real estate
- [ ] **Create daily Hermes cron** — check Instantly replies → qualify → book via Cal.com → log to Notion

**Costs:** $37/mo Instantly + $0 Cal.com + $0 Hunter.io (free tier) ≈ ~$60/mo

---

### 3. Local Business AI Package — $3,942/mo profit · 98.6% margin
**Model:** AI phone receptionist + local SEO + ad management. $800-1K/mo retainer. Client pays own ad spend.

**Status:** 🔲 Needs ElevenLabs + Twilio accounts

- [ ] Sign up **ElevenLabs** ($22/mo) + **Twilio** (~$20/mo)
- [ ] **Build AI receptionist demo** — Twilio phone number → ElevenLabs TTS → Hermes intent handling → booking/logging
- [ ] **Set up DataForSEO API** ($15/mo) + Google Search Console API for keyword data
- [ ] **Target outreach** — dentists, HVAC, plumbers, realtors in Toronto + GTA area
- [ ] **Create SEO content cron** — Tavily research → Hermes writes → schedule via blog/social

**Costs:** $22 ElevenLabs + $20 Twilio + $15 DataForSEO + $1 LLM ≈ ~$58/mo

---

### 4. Crypto Trading Bot — $120/mo profit · 80% margin
**Model:** Systematic momentum/mean-reversion strategies via CCXT + DeFiLlama data.

**Status:** 🔲 Needs exchange API keys + Alchemy RPC

- [ ] **Install CCXT** — `pip install ccxt web3.py`
- [ ] **Set up Alchemy free tier** ($25/mo for paid RPC) — Ethereum node access
- [ ] **Configure exchange API keys** (Binance/Coinbase) — read-only first
- [ ] **Build paper trading harness** — Tavily news cron (30-min) → signal scoring → CCXT paper positions → Telegram P&L
- [ ] **Implement stop-loss** — auto-close if drawdown > 15% on any position
- [ ] **Paper trade minimum 30 days** before any live capital

**⚠️ Risk:** Capital at risk. Never deploy >5% of liquid net worth. Hard kill switch required.

**Costs:** $25/mo Alchemy + $5/mo LLM ≈ ~$30/mo

---

### 5. Airbnb Co-Hosting — $538/mo profit · 89.7% margin
**Model:** Manage other owners' listings for 15% revenue cut. Zero capital at risk.

**Status:** 🔲 Needs Hospitable.com + PriceLabs accounts

- [ ] **Sign up Hospitable.com** ($40/mo) + **PriceLabs** ($20/listing)
- [ ] **Build co-hosting pitch:** "You collect 85% of revenue, we handle everything"
- [ ] **Find property owners** — Facebook (Airbnb Hosts groups), Nextdoor, local investor meetups
- [ ] **Draft co-hosting agreement** — Hermes generates, Jason reviews once
- [ ] **Outreach campaign** — Browserbase scrapes host profiles with low review response rates → email sequence

**Costs:** $40 Hospitable + $20 PriceLabs + $2 LLM ≈ ~$62/mo (for 2 properties)

---

### 6. Airbnb Operator — $1,760/mo profit (operational) · 67.7% margin
**Model:** Operate own short-term rental with full AI management.

**Status:** 🔲 Needs property evaluation + Hospitable + PriceLabs

- [ ] **Evaluate property situation** — own vs rent vs arbitrage. Mortgage/rent cost not modelled.
- [ ] **Sign up Hospitable.com + PriceLabs** (same accounts as Co-Hosting)
- [ ] **Build guest message automation** — pre-arrival → mid-stay → post-checkout review request
- [ ] **Set up daily cron** — check new bookings → trigger auto-sequence

**Costs:** $840/mo operational (cleaning, supplies, fees, tools) — **excludes property cost**

---

### 7. Faceless YouTube Empire — $897/mo profit · 94.4% margin
**Model:** 3 high-CPM channels. AdSense + affiliates. Slow-build compound asset.

**Status:** 🔲 Needs ElevenLabs + FAL_KEY + VidIQ + Shotstack

- [ ] **Sign up ElevenLabs ($22) + FAL.ai (~$20) + VidIQ ($10) + Shotstack ($5)**
- [ ] **Pick 3 high-CPM niches** — personal finance, AI tools explainers, stoicism
- [ ] **Create daily cron** — 7am ET: Tavily trending topics → script → ElevenLabs voice → FAL visuals → Shotstack assembly → YouTube upload
- [ ] **Start immediately as background build** — 6 months to monetization threshold (1K subs + 4K watch hours)

**Costs:** $22 ElevenLabs + $20 FAL + $5 Shotstack + $10 VidIQ + $0.50 LLM ≈ ~$53/mo

---

## Stack Requirements Summary

| Tool | Monthly Cost | Status | Business |
|------|:-----------:|:------:|----------|
| n8n (self-hosted) | $0 | ✅ Ready | n8n Agency |
| Hermes + Codex | ~$0.50/mo | ✅ Active | All |
| Browserbase | Included | ✅ Active | Appointment, Co-Host |
| Telegram/Discord | $0 | ✅ Active | All alerts |
| **Instantly** | **$37** | ❌ Need | Appt Setting, n8n outreach |
| **ElevenLabs** | **$22** | ❌ Need | Local Biz, YouTube |
| **Twilio** | **$20** | ❌ Need | Local Biz |
| **FAL.ai** | **$20** | ❌ Need | YouTube |
| **Hospitable.com** | **$40** | ❌ Need | Airbnb Op + Co-Host |
| **PriceLabs** | **$20** | ❌ Need | Airbnb Op + Co-Host |
| **DataForSEO** | **$15** | ❌ Need | Local Biz |
| **Shotstack** | **$5** | ❌ Need | YouTube |
| **VidIQ** | **$10** | ❌ Need | YouTube |
| **Alchemy/Infura** | **$25** | ❌ Need | Crypto Bot |
| **Exchange API keys** | **$0** | ❌ Need | Crypto Bot |

**Total needed tools:** ~$144/mo to fully unlock all 7 businesses

---

**See companion document:** `biz-ops-strategic.md` for SWOT, risk register, 12-month timeline, and competitive context.
