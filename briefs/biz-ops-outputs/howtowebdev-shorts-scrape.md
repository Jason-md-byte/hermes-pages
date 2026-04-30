# @HowtoWebDev Shorts Scrape — Tools & Repos

Scraped 2026-04-28 from the channel's shorts feed. Transcripts extracted via youtube-transcript-api.

**Update 2026-04-29 (evening):** YouTube's transcript/timedtext API is still blocking this VPS IP (HTTP 429). However, we successfully scraped the full /shorts page directly via HTTP (bypassing JS-rendering) and extracted **all 48 shorts** with titles and view counts from the ytInitialData embedded JSON. The channel now has 48 shorts in total. 33 of these were not previously cataloged in this file.

**The scraping approach was upgraded:** Instead of relying on RSS feeds (which returned 404) or the youtube-transcript-api (blocked), we now scrape the raw HTML page at `https://www.youtube.com/@HowtoWebDev/shorts`, extract the `ytInitialData` JSON blob, and parse the `shortsLockupViewModel` objects in the Shorts tab's `richGridRenderer`. This gives us video IDs, titles, and view counts for every short on the channel.

**Transcripts still unavailable.** The channel's auto-generated ASR captions exist (confirmed via `ytInitialPlayerResponse`) but the timedtext API (even with proper signature parameters extracted from the page) returns HTTP 429 from this IP. Tool names mentioned in the spoken content cannot be determined without transcripts or manual viewing.

**New approach needed for transcript recovery:** To get actual tool/repo names from the 33 new videos, either:
(a) Run this scrape from a residential IP/proxy
(b) Use browser automation with a logged-in YouTube account
(c) Cross-reference with the channel's TikTok cross-posts

---

## Tools & Repos Featured

### 1. Upscale (AI Image Upscaler) ⭐
- **Video:** `L81fyjnaPQI` — "Github Repos for developers" (483 views)
- **Transcript:** Free open-source AI image upscaler. Enhances low-resolution photos locally using deep learning. Sharpen blurry images, upscale 400% without quality loss, batch process, runs on your own GPU.
- **Use case for you:** Could be useful for YouTube thumbnail upscaling in your Faceless YouTube pipeline.

### 2. Agent Zero (Autonomous AI Agent Framework) ⭐
- **Video:** `4R5mjCIy1-s` — "Every developer should know this Github Repo"
- **Transcript:** Autonomous AI agent framework that can reason, plan, write code, execute commands, and use tools iteratively. Runs locally. Give it goals instead of step-by-step instructions. Perfect for experimenting with autonomous AI workflows.
- **Use case for you:** Potentially redundant with Hermes, but interesting as a local alternative to test against.

### 3. Microsoft Autogen (Multi-Agent Framework) ⭐
- **Video:** `KPjhfZUH9P8` — "Powerful Github Repos You Should Know"
- **Transcript:** Framework for orchestrating goal-driven autonomous agents using LLMs. Define tasks and let agents coordinate planning, execution, and tool use automatically with Python APIs. Scales from simple to multi-agent workflows.
- **Use case for you:** Another multi-agent framework. Could be useful if you want to experiment with Microsoft's agent orchestration alongside your Hermes/Codex stack.

### 4. public-apis (Free APIs List) ⭐
- **Video:** `zXE1NyifRxM` — "This GitHub repo gives you HUNDREDS of FREE APIs"
- **Transcript:** Lists hundreds of free APIs organized by category — programming, finance, news, entertainment, and more. Perfect for building apps, AI tools, or automations (e.g., crypto tracker with real-time prices).
- **Repo:** https://github.com/public-apis/public-apis
- **Use case for you:** N8n workflow data sources. Could pull finance APIs for Crypto Bot stream, or news APIs for YouTube Channel 5 (AI News).

### 5. Unsloth (LLM Fine-tuning Toolkit) ⭐
- **Video:** `pPURGO8MOg4` — "This github repo makes working with ai much easier"
- **Transcript:** Powerful toolkit for fine-tuning LLMs with dramatically less VRAM and faster training times. Supports Llama, Gemma, Qwen, GPT-OSS. Optimized training pipelines, reinforcement learning methods.
- **Repo:** https://github.com/unslothai/unsloth
- **Use case for you:** We have the Unsloth skill installed already. Good reference for your Biz Ops — you already know about this one.

### 6. opencommit (AI Commit Messages) ⭐
- **Video:** `WXmPV_UC-rQ` — "Powerful GitHub Actions You Should Know"
- **Transcript:** GitHub Action that uses AI to generate meaningful commit messages automatically from code changes. Saves time, improves commit history quality.
- **Use case for you:** Low value for your setup since Hermes already manages git well, but nice to know about.

### 7. Awesome Agent Skills (1,000+ AI Agent Skills) ⭐
- **Video:** `LYVg7QK8Q0I` — "Github Repos You Should Know" (13K views)
- **Transcript:** Massive collection of 1,000+ skills that teach AI agents to perform complex real-world tasks. Transform Claude Code, Cursor, Gemini CLI into domain experts. Load official skill sets from Stripe, Vercel, Sentry.
- **Repo:** Looks like https://github.com/nickscamara/awesome-agent-skills or similar
- **Use case for you:** Directly relevant! This is like a massive "awesome-hermes-agent" for all coding agents. Could find skills worth porting to Hermes.

### 8. Awesome Docker (Docker Resources) ⭐
- **Video:** `9cXBzQNzIi8` — "Github Repos You Should Know"
- **Transcript:** List of Docker resources, tools, and projects. Discover useful Docker images, orchestration tools, best practices.
- **Use case for you:** Low priority since your VPS doesn't use Docker extensively (n8n was npm, not Docker).

### 9. Puter.js (AI Integration Library) ⭐
- **Videos:** Multiple full tutorials — AI Chat App (`G8CvZD2Znx4`), Multi-Model AI Chat (`xoHWpJKst8U`), AI Interview Coach (`YvIrTlx4h2M`)
- **Transcript:** Build AI-powered web apps with React + Tailwind + Puter.js in under 200 lines. Zero API keys needed, no backend setup, no usage limits. AI runs entirely in the browser.
- **Site:** https://puter.com
- **Use case for you:** Potentially useful for building quick UIs or admin panels without API key management. Could be an alternative to ToolJet for simple AI-powered internal tools.

---

## Top Picks for You (Relevance to Your Stack)

| Rank | Tool | Why It Matters |
|------|------|----------------|
| 1 | **Awesome Agent Skills** | Skills for coding agents — directly applicable to Hermes skill ecosystem |
| 2 | **public-apis** | Free API sources for n8n workflows + Crypto Bot data feeds |
| 3 | **Microsoft Autogen** | Multi-agent orchestration — compare with Hermes delegation |
| 4 | **Upscale** | YouTube thumbnail/image enhancement for Faceless YouTube pipeline |
| 5 | **Puter.js** | Zero-API-key AI integration for quick internal tool UIs |

---

---

## Full Channel Inventory (2026-04-29) — All 48 Shorts

Scraped directly from the /shorts page HTML via `ytInitialData` JSON extraction. 33 newly discovered. Transcripts unavailable (HTTP 429). Star (⭐) = most viewed per category.

### Github Repos You Should Know (27 videos)
| ID | Views | Status |
|----|-------|--------|
| `eeh3-0AI4ek` | **23K** ⭐ | 🔥 NEW |
| `YKIfYvF6AmA` | **15K** ⭐ | 🔥 NEW |
| `dYt1Bltk2GM` | **14K** ⭐ | 🔥 NEW |
| `PwyqgNC85OU` | **14K** ⭐ | 🔥 NEW |
| `PAGzV5r2NMQ` | **13K** ⭐ | 🔥 NEW |
| `JtlgQPNIYvU` | **13K** ⭐ | 🔥 NEW |
| `bMgYBAwPFuQ` | **12K** | 🔥 NEW |
| `LYVg7QK8Q0I` | 12K | Already documented (Awesome Agent Skills) |
| `5ascbXVUBWQ` | 15K | Detected Apr 17 (no transcript) |
| `9ZDvHMId9iY` | **10K** | 🔥 NEW |
| `k_qroTw2sJQ` | **9.8K** | 🔥 NEW |
| `cjHZR9nWvng` | **9.8K** | 🔥 NEW |
| `IbyxmkU38gs` | **9.8K** | 🔥 NEW |
| `jKM6pVYWS8w` | **9.4K** | 🔥 NEW |
| `wIDSUGSrdeo` | **8.9K** | 🔥 NEW |
| `crZqroFlnoM` | **8.4K** | 🔥 NEW |
| `5KSmcYYXXVo` | **8.3K** | 🔥 NEW |
| `ciC2SvH6NVo` | **7.8K** | 🔥 NEW |
| `tmOCy4TZWW0` | **7.5K** | 🔥 NEW |
| `2fXNM8cMfcE` | 7.4K | Detected Apr 14 (no transcript) |
| `dNxkZ_eXYA8` | **7K** | 🔥 NEW |
| `iDafP2S7SeI` | **7K** | 🔥 NEW |
| `zOBVNxYDdlI` | **6.4K** | 🔥 NEW |
| `ej9WtGFEkOk` | **5.9K** | 🔥 NEW |
| `eJIQa2Mt0_I` | **5.5K** | 🔥 NEW |
| `wkNOfrlLDik` | **3.8K** | 🔥 NEW |
| `oFWX2ipYmL8` | **2.8K** | 🔥 NEW |

### AI Tools You Should Know (12 videos)
| ID | Views | Status |
|----|-------|--------|
| `wMbOnhuV0WQ` | **13K** ⭐ | 🔥 NEW |
| `L4S3nhNhv5s` | **13K** ⭐ | 🔥 NEW |
| `dhrCkCoGlVw` | 10K | Detected Apr 14 (no transcript) |
| `RLHCuU1BORw` | **9.9K** | 🔥 NEW |
| `G5bsm4hqUfg` | **9.9K** | 🔥 NEW |
| `X9zPJ_ZXSR8` | **8.4K** | 🔥 NEW |
| `4k3Igt8kO6Y` | 7.1K | Detected Apr 22 (no transcript) |
| `RSqvC7e2B8I` | 6.4K | Detected Apr 20 (no transcript) |
| `THMhLwURO6A` | 6K | Detected Apr 16 (no transcript) |
| `qftTBDaht8Y` | 6K | Detected Apr 15 (no transcript) |
| `3t1Jy8lcrfc` | **4.4K** | 🔥 NEW |
| `aLcbtHtyaoc` | 4.2K | Detected Apr 13 (no transcript) |

### Github Repos for developers (3 videos)
| ID | Views | Notes |
|----|-------|-------|
| `L81fyjnaPQI` | 8.6K | Documented: Upscale |
| `JIC9ZS4kRL8` | 10K | Detected Apr 26 (no transcript) |
| `hGEM5nQttwY` | 10K | Detected Apr 24 (no transcript) |

### Open Source Projects (2 videos)
| ID | Views | Status |
|----|-------|--------|
| `4lCtejFS_7E` | 8.7K | Detected Apr 28 (no transcript) |
| `3Qpv5d6NAPU` | 6.8K | Detected Apr 27 (no transcript) |

### Special Categories (3 videos) — 🔥 ALL NEW
| ID | Title | Views |
|----|-------|-------|
| `s4MBcKUboA4` | **AI Models** You Should Know | 6.9K |
| `q709fLA0oNM` | **AI Tools For Developers** | **10K** ⭐ |
| `VwZrtv9HAqc` | **Powerful Tools** You Should Know | **10K** ⭐ |

### Other Documented (transcripts available)
- `4R5mjCIy1-s` — Agent Zero ⭐
- `KPjhfZUH9P8` — Microsoft Autogen ⭐
- `zXE1NyifRxM` — public-apis ⭐
- `pPURGO8MOg4` — Unsloth ⭐
- `WXmPV_UC-rQ` — opencommit
- `9cXBzQNzIi8` — Awesome Docker
- `G8CvZD2Znx4`, `xoHWpJKst8U`, `YvIrTlx4h2M` — Puter.js tutorials
- `ut0rpm0-XTc` — AI Tools for developers (Apr 29, 953 views)
- Older: `xMomBYZwYiM`, `gqJ3slS-F8U`, `CX3JEcSj4b8`, `uq7N1afUSEE`, `P7ePafSeY_Q`

### Summary Statistics

| Metric | Count |
|--------|-------|
| Total shorts on channel | **48** |
| Previously documented (transcripts) | 7 tools |
| Previously detected (no transcript) | 13 videos |
| **Newly discovered this scrape** | **33 videos** |
| Most viewed new video | `eeh3-0AI4ek` — 23K |
| Most viewed AI Tools video | `wMbOnhuV0WQ` / `L4S3nhNhv5s` — 13K ea. |

> **Next step:** To recover transcripts for the 33 new videos, run the scraper from a residential IP/proxy or use browser automation with a logged-in YouTube session. The video pages themselves are accessible (HTML scrapes fine) but the timedtext caption API is rate-limited per IP.
