# Hermes Agent Research — April 23, 2026

## 1. Version and Release Date

| Version | Release Date | Tag |
|---------|-------------|-----|
| **v0.10.0** (current) | April 16, 2026 | v2026.4.16 |
| v0.9.0 | April 13, 2026 | v2026.4.13 |
| v0.8.0 | April 8, 2026 | v2026.4.8 |
| v0.7.0 | April 3, 2026 | v2026.4.3 |
| v0.6.0 | March 30, 2026 | v2026.3.30 |

**No v0.11 found** — v0.10.0 (Apr 16, 2026) is the latest tagged release as of this research.

Jason is running a development build 1197 commits ahead of v2026.4.16.

---

## 2. Key New Features by Version

### v0.10.0 — Tool Gateway (Apr 16, 2026)
- **Nous Tool Gateway** — Paid Nous Portal subscribers access web search, image generation, TTS, browser automation with zero extra API keys
- Runtime prefers gateway even when direct API keys exist
- Replaces old `HERMES_ENABLE_NOUS_MANAGED_TOOLS` env var
- Full integration with `hermes tools` and `hermes status`

### v0.9.0 — Everywhere Release (Apr 13, 2026)
- **Local Web Dashboard** — browser-based management UI
- **Fast Mode (`/fast`)** — priority processing for OpenAI and Anthropic
- **iMessage via BlueBubbles** and **WeChat/WeCom** native support
- **Termux / Android** native support
- **Background Process Monitoring** — `watch_patterns` for real-time output alerts
- **Native xAI Grok and Xiaomi MiMo** providers
- **16 Supported Platforms** including DingTalk, Feishu, Mattermost
- Security hardening: path traversal protection, shell injection neutralization, SSRF guards, Twilio RCE fix

### v0.8.0 — Intelligence (Apr 8, 2026)
- **Background Process Auto-Notifications** (`notify_on_complete`)
- **Live Model Switching** across all platforms (`/model` command)
- **Google AI Studio (Gemini)** native provider
- **Inactivity-Based Agent Timeouts**
- **Approval Buttons** on Slack & Telegram
- **MCP OAuth 2.1 PKCE**

---

## 3. Breaking Changes / Migration Notes

- `HERMES_ENABLE_NOUS_MANAGED_TOOLS` env var replaced by per-tool `use_gateway` config
- Nous Portal subscribers: runtime prefers gateway tools even when direct API keys exist
- Firecrawl may require separate API key if not using Nous Portal

---

## 4. Current System Status (Jason's VPS)

- Running: Hermes Agent v0.10.0 (2026.4.16) + 1197 dev commits ahead
- Gateway: PID 167495, active
- Web backend: Tavily (configured)
- EXA_API_KEY: present in .env but not yet activated
- No v0.11 detected in any release channel
