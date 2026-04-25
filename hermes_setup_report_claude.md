# Hermes Agent Setup — Handoff Report for Claude Chat
**Date:** 2026-04-23 | **Prepared by:** Hermes Session | **For:** Claude Chat (Jason's complementary agent)

---

## System Overview

| Item | Value |
|---|---|
| Host | IONOS VPS, Ubuntu 22.04 x86_64 |
| User | `hermes` (non-root) |
| Hermes version | v0.10.0 (2026.4.16) |
| Primary model | `minimax/minimax-m2.7` via OpenRouter |
| Claw Code default | `google/gemini-2.5-flash` (large context, $0.30/$2.50/1M) |
| Config | `~/.hermes/config.yaml` |
| API keys | `~/.hermes/.env` |

---

## Active Cron Jobs

| Job ID | Name | Schedule | Delivery |
|---|---|---|---|
| `f42fd7648421` | Service Monitor | Every 5 min | Telegram (alert only) |
| `ce2d980c21b2` | Disk Monitor | Daily 06:00 UTC | Telegram (alert only) |
| `36ffb50207ef` | Morning Briefing | Daily 07:30 Toronto (ET) | Telegram |
| `9caa193e259c` | Daily Wiki Note | Daily 12:00 UTC | Local + Discord |

---

## Active Monitoring (watch_pattern)

Two watch patterns are active on the gateway process:
- **Service state** — triggers when `hermes-gateway` enters stopped/failed/inactive → Telegram alert
- **Disk usage** — triggers when any disk hits 90%+ → Telegram alert

These are registered via cron jobs (the cron script polls and fires alerts, not a true inotify watch_pattern since Hermes cron doesn't support that natively).

---

## Setup Phases — Status

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Infrastructure Monitoring | ✅ Complete |
| Phase 2 | Daily Briefing Cron | ✅ Complete |
| Phase 3 | Web Search Unlock | ✅ Complete |
| Phase 4 | Image Generation (FAL_KEY) | ⏸ Paused — operator skipped |
| Phase 5 | Skills Hub (GITHUB_TOKEN) | ⏸ Blocked by Phase 4 |

---

## Web Search — Backend Chain

All three tested and working:

1. **Tavily** (primary) — `tvly-*` key in `.env`, working now
2. **Exa** (fallback) — `ba1de09b*` key in `.env`, excellent results
3. **DuckDuckGo Lite** (ultimate fallback) — no key needed

The `~/bin/web-search.sh` script already implements this fallback chain. Hermes `web.backend = tavily` in config.

---

## Tools Status

| Tool | Status | Key |
|---|---|---|
| Vision | ✅ Active | Own |
| Browser | ✅ Active | Own |
| TTS | ✅ Active | Own |
| Terminal | ✅ Active | Own |
| Skills | ✅ Active | Own |
| Web Search | ✅ Active | Tavily (primary) |
| Image Generation | ❌ Not enabled | Needs `FAL_KEY` |
| Skills Hub | ❌ Not enabled | Needs `GITHUB_TOKEN` |
| RL Training | ❌ Not available | Nous requires paid portal |

---

## Key Files & Paths

| Path | Purpose |
|---|---|
| `~/.hermes/config.yaml` | Main Hermes config |
| `~/.hermes/.env` | API keys |
| `~/hermes/scratch/` | Scratch workspace |
| `~/.hermes/cron/output/` | Cron job output files |
| `~/bin/web-search.sh` | Web search fallback script |
| `~/bin/todo` | Todo skill script |
| `~/bin/flashcards_generate.py` | Flashcards generator |

---

## Safety Gates (Jason's Rules)

- ❌ Do NOT run `hermes update` without operator approval
- ❌ Do NOT modify UFW firewall rules
- ❌ Do NOT open any ports beyond 22 (SSH)
- ❌ Do NOT install system packages without operator instruction
- ❌ Do NOT spawn sub-agents for infrastructure tasks (Phase 1/2)
- ❌ Do NOT attempt self-evolution, Jeepa pipeline, or RL training

---

## Known Quirks

- Memory is at ~80% usage — keep entries compact
- Memory storage: `/home/hermes/.hermes/memory.json`
- `deepseek-chat` and `deepseek-r1` have 64K context — too small for Claw Code's ~68K system prompt; do not use them with Claw Code
- Tavily key: `tvly-d...5M3z` — Exa key: `ba1de09b...` in `.env`

---

## What Jason Wants from Claude Chat

Jason runs **two-agent setup**:
- **Claude Chat** = brainstorming, web research, planning
- **Hermes** = persistent execution, cron jobs, monitoring

Claude Chat should focus on research and planning tasks, hand off execution to Hermes. Communicate findings concisely. Jason is in Toronto (ET timezone).

---

*End of report.*
