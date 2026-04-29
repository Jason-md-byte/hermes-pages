# Hermes — Full Gap Analysis
> Generated: Apr 29, 2026

---

## Overview

**Disk:** 19G/116G (17%) ✅ healthy
**Memory:** 3.8GB RAM, **no swap** ⚠️
**Services:** Dashboard (200), n8n Docker (200), Postgres (accepting)

---

## 🔴 Critical Gaps (fix now)

| # | Gap | Category | Fix |
|---|-----|----------|-----|
| 1 | **No swap file** — 3.8GB RAM, gateway peaks at 2.8GB. OOM risk | infra | `fallocate -l 4G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile` |
| 2 | **fail2ban not installed** — SSH brute-force protection missing on internet-facing VPS | security | `sudo apt install fail2ban` + configure SSH jail |
| 3 | **Root SSH login enabled** — `PermitRootLogin yes` is a best-practice violation | security | Set to `PermitRootLogin prohibit-password` |
| 4 | **n8n on `*:5678`** — bound to all interfaces, not just localhost/Tailscale | security | Change to `127.0.0.1:5678` in Docker compose |
| 5 | **n8n restart storm** — 3,358 restarts in ~24h. Systemd service races with `@reboot` cron's `start-n8n-stack.sh` | infra | Remove the `@reboot` cron, let systemd manage n8n solo |
| 6 | **Dashboard restart storm** — 541 restarts. Currently running but flaky | infra | Investigate crash cause in journalctl |
| 7 | **Hindsight MCP broken** — `HINDSIGHT_API_LLM_API_KEY=***` is a literal placeholder | config | Set a real API key or disable the broken MCP config |
| 8 | **Secrets in plaintext script** — n8n encryption key + DB password in `start-n8n-stack.sh` (world-readable) | security | Move to `.env` file, `chmod 600` the script, or use systemd env vars |

## 🟡 Medium Gaps (fix this week)

| # | Gap | Category | Fix |
|---|-----|----------|-----|
| 9 | **No fallback providers** — if OpenRouter goes down, agent has zero failover | config | Enable Copilot and/or OpenAI Codex credentials from auth.json |
| 10 | **OpenAI Codex / Copilot credentials never health-checked** — `last_status: null`, `request_count: 0` since Apr 24/27 | config | Run a health check on both credential pool entries |
| 11 | **Timezone not set** — `timezone: ''` in config. Session reset at `at_hour: 4` uses UTC, not ET | config | Set `timezone: America/New_York` |
| 12 | **Newsletter schedule mismatch** — draft runs Mon 00:00 UTC, send runs Tue 13:00 UTC. First send (Apr 28) ran before first draft (May 5) | cron | Reschedule send to start May 5+ |
| 13 | **No failed-job alerting** — Apr 27 HTTP 402 (daily note) had zero notification. Gateway monitor was removed with no replacement | cron | Add a daily cron that checks last-run status of all jobs |
| 14 | **No backup automation** — `~/.hermes/` config, env vars, cron config itself have no offsite backup | cron | Weekly backup cron (tar + SCP or GPG + Telegram) |
| 15 | **~29 duplicate skills** — skills exist in two categories (n8n/ vs n8n-automation/, fal/ vs video/, marketing/ vs marketing-growth/, etc.) | skills | Deduplicate — pick canonical category per skill |
| 16 | **4 macOS-only skills installed** — `apple-notes`, `imessage`, `findmy`, `apple-reminders` on Ubuntu VPS | skills | Remove them |
| 17 | **7 empty/placeholder dirs** — `diagramming/`, `domain/`, `feeds/`, `gifs/`, `gsap/`, `inference-sh/`, `mlops/vector-databases/` | skills | Clean up or implement |
| 18 | **`test.txt` in skills root** — leftover junk | skills | Remove |
| 19 | **34 evey-* plugin symlinks are unloadable** — no `plugin.py`, only `__init__.py`. Only 2/40 plugins actually enabled | plugins | Either implement proper Hermes plugin wrappers or remove symlinks |

## 🔵 Low Gaps (fix when convenient)

| # | Gap | Category | Fix |
|---|-----|----------|-----|
| 20 | **`~/.hermes/keys/` empty** — no keys stored despite many skills needing them (Spotify, Airtable, Notion, Linear, Replicate, etc.) | config | Populate if/when those skills are needed |
| 21 | **Tailscale not in PATH** — health check cron uses bare `tailscale` command which will fail if serve needs re-applying | infra | Add `export PATH=$PATH:/home/hermes/bin` or use full path in cron prompt |
| 22 | **Two crons stacked at 06:00 UTC** — Disk Monitor + GitHub Sync run simultaneously | cron | Offset one by 15-30 min |
| 23 | **Missing critical skills** — Docker management, Ansible, Postgres/SQL, backup, firewall, SSH troubleshooting | skills | Add when needed |
| 24 | **Google Voice/TTS/STT not configured** — `VOICE_TOOLS_OPENAI_KEY` not set, no ElevenLabs key | config | Add when voice features wanted |
| 25 | **Stale cron output dirs** — 10+ files from removed gateway monitor jobs (512KB) | cron | Clean up `~/.hermes/cron/output/` |
| 26 | **Hermes 256 commits behind** — `hermes update` recommended | config | Run `hermes update` |

## 💼 Biz-Ops Stream Gaps

| # | Stream | Target | Progress | Next Action |
|---|--------|--------|----------|-------------|
| 1 | **n8n Agency** | $3,950/mo | 🟢 ~60% | Find first client, build portfolio page |
| 2 | **Appt Setting** | $4,440/mo | 🟡 ~30% | Create Instantly ($37/mo), config sending domain SPF/DKIM, set up Cal.com, build reply-qualification cron |
| 3 | **Personal Brand** | $1,200/mo | 🟢 ~50% | Cross-post to YouTube, engage organically in AI communities |
| 4 | **Templates** | $2,000/mo | 🟡 ~40% | Create Gumroad account, publish 3 packaged n8n templates |
| 5 | **Faceless YouTube** | $2,500/mo | 🔴 0% | Sign up ElevenLabs ($22), FAL ($20), Shotstack ($5), VidIQ ($10). Build pipeline |
| 6 | **Crypto Bot** | $120/mo | 🔴 0% | Install CCXT + web3.py, create Alchemy account ($25/mo), build paper trading harness |
| 7 | **Airbnb Co-Host** | $538/mo | ⏸️ Shelved | No action until Month 6 |

---

## Quick Wins (< 15 min each)

1. Remove `@reboot` n8n cron → systemd manages it solo
2. Add swap file
3. Install fail2ban
4. Set timezone in config
5. Remove 4 macOS skills + `test.txt` + 7 empty dirs
6. Remove 512KB of stale cron output
7. `hermes update`
