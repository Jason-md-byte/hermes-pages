# Business Operations Executive Brief
**Source:** Claude Chat (research/brainstorming, Apr 24 2026)
**Classification:** Exploratory/ideation — not verified market data. Take specifics with a grain of salt; the ideas and reasoning are the value.
**Prepared for:** Nova (Hermes Agent, execution layer)
**Status:** Pre-launch — all businesses in planning phase

---

## At a Glance: The 7 Operations

| # | Business | Conservative Profit | Realistic Profit | Ramp | Key Missing Thing |
|---|----------|-------------------:|-----------------:|:----:|-------------------|
| 1 | n8n Automation Agency | $3,950/mo | $14,920/mo | 1-2mo | Outreach (Instantly) |
| 2 | Appointment Setting Agency | $4,440/mo | $19,880/mo | 1-2mo | Email sending infra |
| 3 | Local Business AI Package | $3,942/mo | $17,880/mo | 1-2mo | ElevenLabs + Twilio keys |
| 4 | Crypto Trading Bot | $120/mo | $720/mo | 1mo (paper) | Exchange API keys |
| 5 | Airbnb Co-Hosting | $538/mo | $4,270/mo | 2-3mo | Hospitable.com account |
| 6 | Airbnb Operator | $1,860/mo | $8,340/mo | 1mo | Property + Hospitable |
| 7 | Faceless YouTube Empire | $897/mo | $7,900/mo | 6mo | FAL_KEY + ElevenLabs key |

**Combined realistic target (month 7-12+): ~$66K/mo profit**
**Year 1 conservative estimate: ~$169K | Realistic: $250K-$320K**

---

## Priority Order

### Launch immediately (Month 1 — $0 upfront cost)
1. **n8n Automation Agency** — Best fit for your stack. Codex writes workflows, n8n runs them, you sell output. 99% margin. No keys needed to start building demos.
2. **Appointment Setting Agency** — Outbound email for B2B clients. Hermes handles the whole loop. Needs Instantly ($37/mo) to launch.

### Launch Month 2 (after tool acquisition)
3. **Local Business AI Package** — AI receptionist + local SEO. Unlocks when ElevenLabs + Twilio are configured.
4. **Crypto Trading Bot** — Paper trade now while Agency revenue funds the capital. 30-day validation required.

### Launch Month 2-3 (build relationships)
5. **Airbnb Co-Hosting** — Manage other owners' properties for 15-18% revenue share. No capital at risk.

### Needs property first
6. **Airbnb Operator** — Directly operate your own rental. Property cost not modelled.

### Slow burn — start early
7. **Faceless YouTube Empire** — 6-month monetization ramp. Start now, let it compound. Needs FAL_KEY + ElevenLabs.

---

## Single Most Important Action Per Business

| Business | Do this TODAY |
|----------|---------------|
| n8n Agency | Install n8n on VPS & build 3 demo workflows |
| Appointment Setting | Create Instantly account + set up sending domain |
| Local Biz Package | Get ElevenLabs API key → build receptionist demo |
| Crypto Bot | Set up CCXT + paper trading script, start logging |
| Co-Hosting | Sign up for Hospitable.com |
| YouTube | Get FAL_KEY + ElevenLabs → pick 3 high-CPM niches |
| Airbnb Operator | Evaluate property situation first |

---

## Key Costs Summary

| Category | Monthly (all 7 running) |
|----------|:-----------------------:|
| LLM (deepseek-v4-flash) | ~$12 |
| Instantly | $37 |
| ElevenLabs | $22 |
| Twilio | ~$20 |
| FAL.ai | ~$20 |
| Shotstack/assembly | ~$5 |
| Hospitable.com | $40-120 |
| PriceLabs | $20-60 |
| DataForSEO | ~$15 |
| VidIQ | $10 |
| **Total tools** | **~$291/mo** |

Compare: Naïve AI for the same 7 operations = $509-609/mo + platform fee. Nova mode = $0 platform fee, full transparency.

---

## Key Risk Quick Reference

| Risk | Severity | Fix |
|------|:--------:|-----|
| Crypto capital loss | 🔴 High | 30-day paper trade, -10% hard stop |
| Email deliverability failing | 🟡 Medium | Rotate domains, warm inboxes |
| Airbnb ToS change | 🟡 Medium | Use Hospitable API (legitimate) |
| YouTube monetization change | 🟡 Medium | Diversify across 3-5 niches |
| Missing API key blocks business | 🟡 Medium | Prioritize: ElevenLabs → FAL → Twilio |
| Hermes breaking update | 🟢 Low | Pin version, test before upgrade |

---

## Recommended First Week

```
Day 1: Install n8n (docker), build 3 demo workflow templates
Day 2: Create Instantly account + configure sending domain + SPF/DKIM
Day 3: Order ElevenLabs and FAL.ai API keys
Day 4: Start crypto paper trading script
Day 5: Set up business-ops daily cron to check progress
```

Full analysis document: `~/hermes/scratch/business-ops/business-ops-full-analysis.md`
