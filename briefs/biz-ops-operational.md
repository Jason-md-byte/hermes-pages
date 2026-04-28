# Business Operations — Operational Brief (v2)
**For:** Nova (Hermes Agent) · **From:** Jason · **Date:** April 2026
**Classification:** Action document — what to build, in what order, with what tools
**File:** `biz-ops-operational.md`

---

## Priority: Build Order (v2 — Post-Council Revision)

| Rank | Business | Profit | Key Cost | Start | Kill Criterion |
|:----:|----------|-------:|:--------:|:-----:|----------------|
| **1** | n8n Automation Agency | $3,950/mo | $0 new | Week 1 | No client by Month 2 → templates-only |
| **2** | Appointment Setting | $4,440/mo | $37/mo (Instantly) | Week 2+ | No client by Month 3 → pause |
| **3** | Personal Brand (Newsletter + Social) | $1,200/mo | $0 | Week 1 | No audience growth by Month 3 |
| **4** | AI Workflow Templates | $2,000/mo | $0 (Gumroad) | Week 2 | <$200/mo by Month 3 |
| **5** | Faceless YouTube Empire (5 channels) | $2,500/mo | $53/mo (ElevenLabs + FAL + Shotstack) | Month 3 | No channel monetized by Month 9 |
| **6** | Crypto Trading Bot | $120/mo | $25/mo (Alchemy) | Month 1 (paper) | Paper loses >20% in 30d → abandon |
| **7** | Airbnb Co-Hosting | $538/mo | $62/mo (Hospitable + PriceLabs) | Month 6 eval | No property by Month 6 → shelve |

**Combined conservative at stabilization:** ~$12,947/mo profit · **Year 1:** ~$142K
**Combined realistic 12-month target:** ~$28,900/mo profit
**Pre-revenue burn:** ~$600 total (2-3 months)
**Month 1 focus:** 3 streams max — n8n, Personal Brand, Crypto (background paper)

---

## Per-Business Action Items

### 1. n8n Automation Agency — $3,950/mo profit · 98.8% margin
**Model:** Sell custom n8n workflow automations per project ($2K-2.5K). Hermes + Codex generates the workflow JSON.
**Retainer add-on:** Every n8n client is also a support/update client. Attach $200-500/mo recurring maintenance retainer for workflow updates, bug fixes, monitoring, and webhook maintenance. Pitch as separate SLA tier or bundle into the project fee for the first 3 months as a trial.
**Status:** ✅ Zero new tools needed · Best fit for this stack · **Priority #1**
**Kill criterion:** No paying client by end of Month 2 → pivot to templates-only model.

- [x] **Install n8n** — `n8n start --port=5678` via npm
- [x] **Build Hermes skill:** `n8n-workflow-generator` — takes business problem description, outputs deployable workflow JSON via Codex
- [x] **Build 3 demo workflows**: lead capture→CRM, invoice→notify, form→Slack
- [x] **Draft outreach sequence** — 3-touch cold email targeting ops-heavy SMBs
- [x] **Bundle with Appointment Setting:** same pitch → "Sales Pipeline Automation"
- [ ] **Find first n8n client** — Upwork / referrals / cold outreach
- [ ] **Build portfolio page** with 3 demo workflows and descriptions
- [ ] **Install n8n systemd service** — paste sudo cp + systemctl enable one-liner

**Costs:** $0.50/mo LLM + ~$30 misc = ~$50/mo total

---

### 2. Appointment Setting Agency — $4,440/mo profit · 98.7% margin
**Model:** B2B outbound email sequences. Monthly retainer ($1,500-2K/client). Hermes handles the full loop.
**Status:** 🔲 Needs Instantly + sending domain
**Kill criterion:** No client by Month 3 → pause, reallocate effort to n8n/templates.

- [x] **Bundle with n8n Agency** — one pitch: "Sales Pipeline Automation"
- [x] **Build LinkedIn scraper** — Browserbase workflow for ICP-matched lead extraction
- [x] **Write first 5-touch sequence** — target niche: HVAC, roofing, dental, or real estate
- [x] **Document Cal.com + Notion pipeline** — webhook → Notion MCP for auto-logging
- [ ] **Create Instantly account** ($37/mo) + configure sending domain with SPF/DKIM/DMARC
- [ ] **Set up Cal.com** (free) — webhook → Notion MCP pipeline for auto-logging booked meetings
- [ ] **Create daily Hermes cron** — check Instantly replies → qualify → book via Cal.com → log to Notion

**Costs:** $37/mo Instantly + $0 Cal.com + $0 Hunter.io ≈ ~$60/mo

---

### 3. Personal Brand (Newsletter + Social) — $1,200/mo profit · 95% margin
**Model:** Newsletter (Beehiiv/Substack) + Twitter/X + LinkedIn. Digital products, sponsorships, consulting leads.
**Status:** ✅ Zero new tools needed
**Kill criterion:** <500 subscribers/followers by Month 3 → pivot content strategy.

- [x] **Pick platform** — Beehiiv (newsletter) + Twitter/X (short-form) + LinkedIn (professional)
- [x] **Define niche:** "Building AI automation businesses with Hermes — real stack, real numbers, no fluff"
- [x] **Write first 3 posts** — build process posts, revenue transparency, tool comparisons
- [x] **Create lead magnet** — "7 AI Automation Workflows Under $200/mo" (free PDF → email list)
- [x] **Set up weekly cron** — Sunday 8pm ET draft → Tuesday 9am ET send (newsletter cron live)
- [ ] **Cross-post to YouTube Channel 1** — repurpose newsletter content as short-form video
- [ ] **Grow organically** — engage in AI communities, reply to threads

**Costs:** $0 (Beehiiv free tier, Twitter/LinkedIn free)

---

### 4. AI Workflow Templates Store — $2,000/mo profit · 97% margin
**Model:** Sell pre-built n8n/Hermes workflow templates on Gumroad. Build once, sell forever.
**Status:** ✅ Zero new tools needed · Leverages n8n Agency work
**Kill criterion:** <$200/mo revenue by Month 3 → drop price or bundle as giveaway for lead gen.

- [ ] **Create Gumroad account** (free)
- [ ] **Package first 3 templates** from n8n Agency demo workflows:
  - Lead Capture → CRM
  - Invoice → Email Notification
  - Form → Slack Alert
- [ ] **Price at $29-49 each** or bundle of 3 for $79
- [ ] **Promote via Personal Brand** — newsletter, Twitter, LinkedIn
- [ ] **Build 3 more templates per month** — new products drive repeat sales
- [ ] **Create "Template Club"** — $49/mo for all templates + new ones each month

**Costs:** $0 (Gumroad takes 3.5% + $0.30 per sale)

---

### 5. Faceless YouTube Empire (5 channels) — $2,500/mo profit · 94% margin
**Model:** 5 automated channels. AdSense + affiliates. Slow-build compound asset.
**Status:** 🔲 Needs ElevenLabs + FAL_KEY + VidIQ + Shotstack
**Kill criterion:** No channel monetized by Month 9 → drop niche, double down on strongest performer.

- [ ] **Sign up ElevenLabs ($22) + FAL.ai (~$20) + VidIQ ($10) + Shotstack ($5)**
- [ ] **Pick 5 high-CPM niches** (starting with 3, scale to 5):
  - **Channel 1:** AI Tools & Automation Tutorials (personal brand crossover)
  - **Channel 2:** Business Systems & No-Code (n8n tutorials, automation demos)
  - **Channel 3:** Stoicism / Mindset (evergreen high-CPM, lower competition)
  - **Channel 4:** Personal Finance / Wealth Building (high RPM, proven format)
  - **Channel 5:** Tech Reviews / AI News (trending, taps current events)
- [ ] **Build full pipeline cron** — daily 7am ET:
  1. Tavily research trending topics per niche
  2. Hermes writes script (5-8 min)
  3. ElevenLabs generates voiceover
  4. FAL.ai generates visuals/storyboard
  5. Shotstack assembles final video
  6. YouTube upload via API (scheduled)
- [ ] **Channels 1-2 double as personal brand** — repurpose to Twitter/LinkedIn

**Costs:** $22 ElevenLabs + $20 FAL + $5 Shotstack + $10 VidIQ + $0.50 LLM ≈ ~$53/mo
**v2 change:** Scaled from 3 to 5 channels. Channels 1-2 now feed personal brand flywheel.

---

### 6. Crypto Trading Bot — $120/mo profit · 80% margin
**Model:** Systematic momentum/mean-reversion strategies via CCXT + DeFiLlama data.
**Status:** 🔲 Needs exchange API keys + Alchemy RPC
**Kill criterion:** Paper trade strategy loses >20% in any 30-day window → abandon.

- [ ] **Install CCXT** — `pip install ccxt web3.py`
- [ ] **Set up Alchemy free tier** ($25/mo for paid RPC)
- [ ] **Configure exchange API keys** (Binance/Coinbase) — read-only first
- [ ] **Build paper trading harness** — Tavily news cron → signal scoring → CCXT paper positions → Telegram P&L
- [ ] **Implement stop-loss** — auto-close if drawdown > 15% on any position
- [ ] **Paper trade minimum 30 days** before any live capital

**⚠️ Risk:** Capital at risk. Never deploy >5% of liquid net worth. Hard kill switch required.
**Costs:** $25/mo Alchemy + $5/mo LLM ≈ ~$30/mo

---

### 7. Airbnb Co-Hosting — $538/mo profit · 89.7% margin
**Model:** Manage other owners' listings for 15% revenue cut. Zero capital at risk.
**Status:** 🔲 **SHELVED until Month 6 eval** 🔲 Needs Hospitable.com + PriceLabs accounts
**Kill criterion:** No property owner signed by Month 9 → drop permanently.

- [ ] **Re-evaluate at Month 6** — is there time? Is there demand?
- [ ] **If greenlit:** Sign up Hospitable.com ($40/mo) + PriceLabs ($20/listing)
- [ ] **Build co-hosting pitch:** "You collect 85% of revenue, we handle everything"
- [ ] **Find property owners** — Facebook groups, Nextdoor, local investor meetups

**Costs:** $40 Hospitable + $20 PriceLabs + $2 LLM ≈ ~$62/mo

---

## Stack Requirements Summary (v2)

| Tool | Monthly Cost | Status | Business |
|------|:-----------:|:------:|----------|
| n8n (self-hosted) | $0 | ✅ Ready | n8n Agency, Templates |
| Hermes + Codex | ~$0.50/mo | ✅ Active | All |
| Browserbase | Included | ✅ Active | Appt Setting |
| Gumroad | $0 (3.5% fee) | ✅ Ready | Templates |
| Telegram/Discord | $0 | ✅ Active | All alerts |
| Beehiiv/Substack | $0 (free tier) | ✅ Ready | Personal Brand |
| **Instantly** | **$37** | ❌ Need | Appt Setting, n8n outreach |
| **ElevenLabs** | **$22** | ❌ Need | YouTube (all channels) |
| **FAL.ai** | **$20** | ❌ Need | YouTube visual pipeline |
| **Shotstack** | **$5** | ❌ Need | YouTube assembly |
| **VidIQ** | **$10** | ❌ Need | YouTube keyword research |
| **Alchemy/Infura** | **$25** | ❌ Need | Crypto Bot |
| **Exchange API keys** | **$0** | ❌ Need | Crypto Bot |
| **Hospitable.com** | **$40** | ❌ Shelved | Airbnb Co-Host |
| **PriceLabs** | **$20** | ❌ Shelved | Airbnb Co-Host |

**Total needed to activate first 5 streams:** ~$94/mo (+ the $91/mo optional = $185/mo all-in)

---

## Month 1 Execution Plan

**Week 1:**
- Install n8n (`docker run -d -p 5678:5678 n8nio/n8n`)
- Create Gumroad account
- Start newsletter (Beehiiv) + Twitter/X account
- Install CCXT for crypto paper trading

**Week 2:**
- Build 3 n8n demo workflows
- Package first 3 templates for Gumroad
- Write first 3 brand posts
- Set up crypto paper trading harness

**Week 3-4:**
- Draft n8n outreach sequence
- Write first newsletter issue
- Begin Instantly setup (if committed to Appt Setting path)
- **Assessment check:** Do you have an n8n client lead? If yes, full steam. If no, prep templates launch.

**Kill criteria check (End of Month 1):**
- n8n: Any leads? → Yes/No
- Templates: Built? → Yes/No  
- Brand: First content published? → Yes/No
- Crypto: Paper trading running? → Yes/No
- **If any is No, that stream is delayed — don't advance until basics are done.**

---

**v2 Changes from v1:**
- **Dropped:** Local AI Package ($3,942/mo), Airbnb Operator ($1,760/mo)
- **Added:** Personal Brand ($1,200/mo), AI Workflow Templates ($2,000/mo)
- **Scaled:** YouTube from 3 to 5 channels ($897→$2,500/mo)
- **Added:** Kill criteria for every stream
- **Added:** Month 1 execution plan with weekly breakdown
- **Added:** Flywheel model (n8n → templates → brand → YouTube → clients)
- **Budget reduced:** $303/mo → ~$200/mo
- **Council confidence:** v1=68% → v2=~82%

**See companion document:** `biz-ops-strategic.md` for SWOT, risk register, 12-month timeline, and competitive context.
