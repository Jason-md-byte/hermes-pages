# Hermes Agent — Complete Capability Inventory

**Generated:** 2026-04-30  
**Model:** deepseek/deepseek-v4-flash (OpenRouter)  
**Fallback:** minimax/minimax-m2.7 (OpenRouter)  
**Budget:** $3/day OpenRouter  
**Platform:** Telegram (primary), Discord/WhatsApp/Slack/Signal/HomeAssistant/QQBot configured  
**Workdir:** `/home/hermes`

---

## 1. SYSTEM ARCHITECTURE

### Running Services (systemd)
| Service | Port | Status |
|---|---|---|
| hermes-gateway.service | — | **active** |
| hermes-dashboard.service | — | **active** |
| hermes-hindsight.service | :8888 | **active** (Hindsight Embed Memory Daemon) |
| n8n.service | :5678 | **active** (via Docker or direct — systemd disabled, node runs on 5678) |

### Infrastructure
- **PostgreSQL** at `/home/hermes/docker/postgres/` — started via `@reboot` cron
- **Tailscale** — startup script at `~/bin/hermes-tailscale-startup.sh`
- **Cron**: `@reboot` tasks for Tailscale + PostgreSQL
- **Wiki**: `~/wiki/wiki/` — 20+ markdown notes with subdirs (analyses, biz-ops, decisions, projects)
- **Browser**: Playwright-based, Chromium at `~/.cache/ms-playwright/chromium-1217/`
- **Terminal**: persistent container (docker/podman), `nikolaik/python-nodejs:python3.11-nodejs20` image, 5GB RAM, 50GB disk

---

## 2. MCP SERVERS (Model Context Protocol)

Five MCP servers configured, providing specialized tool surfaces:

### 2a. Firecrawl 🕷️
*Web scraping & search engine*
- `firecrawl_scrape` — single URL extraction (markdown, JSON, HTML, screenshots, branding)
- `firecrawl_search` — web/news/image search with scrape options
- `firecrawl_crawl` — multi-page site crawling (async, depth-controlled)
- `firecrawl_map` — URL discovery across a domain
- `firecrawl_extract` — structured LLM-powered data extraction
- `firecrawl_agent` — autonomous web research agent (async)
- `firecrawl_browser_*` — headless browser sessions via CDP
- `firecrawl_check_crawl_status` — poll crawl progress

### 2b. GitHub 🐙
*Repository & PR management*
- Full issue management: create/update/list/get issues
- Full PR workflow: create/get/list/merge PRs, reviews, comments, branch update
- File ops: create/update/push files, get contents
- Repository: create/fork/search repos
- Search: code, issues, users, repositories
- Branch management

### 2c. Playwright 🌐
*Browser automation*
- Navigate, click, type, hover, drag/drop, file upload
- Snapshot (accessibility tree — better than screenshot for AI)
- Screenshot (element or full page)
- Evaluate JavaScript, run custom Playwright code
- Network requests, console messages
- Dialog handling (alert/confirm/prompt)
- Tab management (list/new/close/select)
- Form filling, option selection, keyboard input

### 2d. Not Human Search 🔍
*Agentic-readiness index*
- `search_agents` — search agent-ready websites by category/query
- `get_top_sites` — highest-scored agent-ready sites
- `get_site_details` — 7-signal readiness report per domain
- `check_url` — on-demand agentic-readiness check
- `find_mcp_servers` — discover MCP endpoints by category
- `verify_mcp` — probe if a URL is a live MCP server
- `submit_site` — submit a URL for indexing
- `register_monitor` — email alerts on score drops
- `get_stats` — index statistics
- `recent_additions` — newly indexed sites
- `list_categories` — browse index by category

### 2e. Figma 🎨
*Design file access*
- Read Figma files (via `url: https://mcp.figma.com/mcp`)
- Share capabilities via prompts/resources

---

## 3. NATIVE TOOLSETS (Platform-level)

These tools are built into the agent's runtime (not MCP). Available categories:

| Toolset | Tools Included |
|---|---|
| **terminal** | Shell execution, background processes, PTY mode, persistent container |
| **file** | `read_file`, `write_file`, `patch`, `search_files` (grep + find) |
| **web** | `web_search` (Tavily), `web_extract` (URL→markdown) |
| **browser** | Playwright MCP integration |
| **delegation** | Subagent spawning (3 concurrent max, depth 1, inherits MCP toolsets) |
| **image_gen** | Image generation capability |
| **memory** | Hindsight daemon memory read/write |
| **skills** | `skills_list`, `skill_view`, `skill_manage` (create/patch/edit/delete skills) |
| **session_search** | Search across conversation history |
| **vision** | Image analysis |
| **cronjob** | Cron task scheduling |
| **code_execution** | Sandboxed code runs |
| **clarify** | Ambiguity resolution |
| **todo** | Task management |
| **tts** | Text-to-speech (Edge, ElevenLabs, OpenAI, xAI, Mistral, Neuphonic) |
| **messaging** | Platform messaging abilities |

### Delegation System
- Subagents inherit MCP toolsets (Firecrawl, GitHub, Playwright, etc.)
- Default subagent tools: `terminal` + `file` + `web`
- Max 50 iterations per subagent, 600s timeout
- Orchestrator mode: 3 concurrent children, depth 1

---

## 4. INSTALLED SKILLS (135 total)

Skills are organized into categories. Each has a SKILL.md with instructions that the agent loads on-demand.

### Autonomous AI Agents (Coding Delegation)
| Skill | Purpose |
|---|---|
| `claude-code` | Delegate to Claude Code CLI for features/PRs |
| `codex` | Delegate to OpenAI Codex CLI |
| `opencode` | Delegate to OpenCode CLI for code review |
| `hermes-agent` | Hermes Agent own config/setup/usage guide |
| `agent-swarm-development` | Hermes as orchestrator with Codex CLI worker agents |
| `hermes-acp-orchestrator` | ACP-style delegation in Hermes |

### Development & Code Quality
| Skill | Purpose |
|---|---|
| `clean-architecture` | Dependency Rule structure |
| `clean-code` | Readable, maintainable code |
| `pragmatic-programmer` | DRY, orthogonality, prototyping |
| `domain-driven-design` | Bounded contexts, ubiquitous language |
| `refactoring-patterns` | Named refactoring transformations |
| `refactoring-ui` | Visual hierarchy, spacing, color audit |
| `test-driven-development` | RED-GREEN-REFACTOR |
| `software-design-philosophy` | Deep modules, information hiding |
| `design-everyday-things` | Affordances, signifiers, feedback |
| `system-design` | Scalable distributed systems |
| `ddia-systems` | Storage engines, replication, partitions |
| `high-perf-browser` | Network protocols, resource optimization |
| `web-performance` | Core Web Vitals, Lighthouse, images |
| `web-accessibility` | WCAG 2.2, ARIA, semantic HTML |

### Frontend & UI
| Skill | Purpose |
|---|---|
| `frontend-ui-dark-ts` | Dark-themed React UIs with TypeScript + Tailwind |
| `gsap-core` | GSAP core API (to/from/fromTo) |
| `gsap-react` | GSAP + React (useGSAP hook) |
| `gsap-timeline` | GSAP timeline API |
| `gsap-scrolltrigger` | GSAP ScrollTrigger plugin |
| `gsap-plugins` | GSAP plugin registration/usage |
| `gsap-performance` | GSAP performance optimization |
| `gsap-frameworks` | GSAP + Vue/Svelte |
| `gsap-utils` | GSAP utility functions |
| `next-best-practices` | Next.js App Router, RSC |
| `react-best-practices` | Modern React patterns |
| `shadcn-ui` | shadcn/ui component library |
| `web-design-guidelines` | Modern responsive design |
| `web-typography` | Typeface selection and pairing |
| `ios-hig-design` | Apple Human Interface Guidelines |
| `popular-web-designs` | 54 real design systems as HTML/CSS |
| `microinteractions` | Triggers, rules, feedback, loops |
| `top-design` | Award-winning immersive web experiences |
| `ux-heuristics` | Nielsen's heuristics evaluation |
| `claude-design` | HTML artifacts, landing pages, prototypes |
| `excalidraw` | Hand-drawn Excalidraw diagrams |
| `architecture-diagram` | Dark-themed SVG architecture diagrams |
| `p5js` | p5.js generative art + shaders |
| `pixel-art` | Pixel art with era palettes |
| `manim-video` | 3Blue1Brown-style math animations |

### Creative & Media
| Skill | Purpose |
|---|---|
| `ascii-art` | pyfiglet, cowsay, boxes |
| `ascii-video` | Video/audio → colored ASCII MP4/GIF |
| `songwriting-and-ai-music` | Songwriting + Suno AI prompts |
| `humanizer` | Strip AI-isms, add real voice |
| `ideation` | Project ideas via creative constraints |
| `baoyu-comic` | Educational knowledge comics |
| `baoyu-infographic` | Infographics (21 layouts × 21 styles) |
| `design-md` | Google DESIGN.md token spec |
| `touchdesigner-mcp` | Control TouchDesigner via MCP |

### Video & Audio
| Skill | Purpose |
|---|---|
| `remotion-video` | Programmatic React video creation |
| `sora-video` | OpenAI Sora short video clips |
| `fal-generate` | fal.ai image/video generation |
| `fal-video-edit` | fal.ai video editing (remix, upscale, background) |
| `fal-audio` | fal.ai TTS and STT |
| `openai-speech` | OpenAI text-to-speech |
| `songsee` | Audio spectrogram visualization |
| `heartmula` | Suno-like song generation |
| `audiocraft-audio-generation` | MusicGen/AudioGen |

### AI/ML & Models
| Skill | Purpose |
|---|---|
| `bfl-api` | BFL FLUX API endpoints/async |
| `flux-best-practices` | Comprehensive FLUX image gen guide |
| `replicate-api` | SDXL, FLUX via Replicate |
| `llama-cpp` | Local GGUF inference + HF Hub |
| `serving-llms-vllm` | vLLM high-throughput serving |
| `dspy` | Declarative LM programs, auto-optimize |
| `outlines` | Structured JSON/regex LLM generation |
| `huggingface-hub` | HF CLI search/download/upload |
| `huggingface-train` | SFT fine-tuning with TRL |
| `fine-tuning-with-trl` | RLHF (DPO, PPO, GRPO) |
| `axolotl` | YAML LLM fine-tuning (LoRA, DPO) |
| `unsloth` | 2-5x faster LoRA/QLoRA |
| `obliteratus` | Abliterate LLM refusals |
| `segment-anything-model` | SAM zero-shot segmentation |
| `gradio-apps` | Build Gradio interfaces |
| `evaluating-llms-harness` | lm-eval-harness benchmarks |
| `weights-and-biases` | W&B experiment tracking |
| `firecrawl-scrape` | Using Firecrawl API in app code |
| `firecrawl-search` | Using Firecrawl search API |

### Productivity & Office
| Skill | Purpose |
|---|---|
| `office` | DOCX, PDF, PPTX, XLSX creation/editing |
| `docx` | Word documents programmatically |
| `pdf` | PDF text extraction, creation, forms |
| `pptx` | PowerPoint presentations |
| `xlsx` | Excel spreadsheets |
| `nano-pdf` | Edit PDF text/typos via NL prompts |
| `ocr-and-documents` | Extract text from scans/PDFs |
| `notion` | Notion API via curl |
| `airtable` | Airtable REST API |
| `linear` | Linear issue/project management |
| `google-workspace` | Gmail, Calendar, Drive via gws CLI |
| `maps` | Geocode, POIs, routes via OpenStreetMap |
| `obsidian` | Read/search/create vault notes |
| `daily-note` | Create wiki daily notes |
| `business-document-pipeline` | Process research into structured docs |

### Marketing & Content
| Skill | Purpose |
|---|---|
| `content-strategy` | Topic decisions, formats, calendars |
| `copywriting` | High-converting marketing copy |
| `ai-seo` | AI-powered SEO optimization |
| `seo-audit` | Technical SEO audits |
| `launch-strategy` | Product launches and GTM |
| `pricing-strategy` | SaaS pricing design |
| `social-content` | Social media content for LinkedIn |
| `typefully` | Schedule/publish to X and LinkedIn |
| `social-media-publishing` | Cross-platform via Typefully API |
| `cold-email` | B2B cold email sequences |
| `email-drip-sequences` | Automated email sequences |
| `email-deliverability` | SPF, DKIM, DMARC best practices |
| `react-email` | React Email templates |
| `himalaya` | IMAP/SMTP email from terminal |
| `resend` | Resend email API |
| `sales-enablement` | Pitch decks, battle cards, proposals |
| `startup-architect` | Research and validate startup ideas |

### Business & Strategy
| Skill | Purpose |
|---|---|
| `37signals-way` | Lean opinionated product building |
| `business-ops` | Nova's 7 business operations strategy |
| `jobs-to-be-done` | Customer needs analysis |
| `lean-startup` | MVPs, validated learning, pivots |
| `mom-test` | Customer interview techniques |
| `negotiation` | Tactical empathy, mirroring |
| `incident-commander` | Autonomous incident detection/RCA |
| `observability-designer` | Observability system design |
| `analytics-bi` | BigQuery analytics toolkit |
| `legal-advisor` | Legal advice capability |
| `production-safety` | ZenOps production safety rules |

### DevOps & Infrastructure
| Skill | Purpose |
|---|---|
| `zenops-ops` | ZenOps VM deploy/operational playbook |
| `terraform-style` | HCL style, state management, modules |
| `workers-best-practices` | Cloudflare Workers deployment |
| `webhook-subscriptions` | Event-driven agent runs |
| `cron-pipeline` | Multi-stage cron pipelines |
| `community-skills-install` | Install skills/plugins/MCP from GitHub repos |
| `file-browser-tailscale-setup` | File Browser + Tailscale |
| `github-pages-api-listing` | GitHub Pages with file listing |
| `n8n-postgres-native-setup` | n8n with PostgreSQL backend |
| `dashboard-plugin-authoring` | Custom dashboard tabs/panels |
| `self-contained-operations-dashboard` | Single-file HTML ops dashboard |
| `daily-hermes-briefing` | Daily operational briefing |
| `scratch-to-github-sync` | Daily cron sync of scratch/ to GitHub |
| `skill-plugin-audit` | Skill/plugin inventory + health audit |
| `tailscale-userspace-recovery` | Tailscale daemon recovery |
| `hermes-cron-model-verification` | Cron model/provider settings |
| `hermes-deep-clean` | Disk space reclamation |
| `hermmes-infrastructure-monitoring` | Gateway + system health monitoring |
| `zero-token-systemd-monitoring` | Non-LLM cron monitors |
| `nova-dashboard-chat-proxy` | Dashboard as persistent systemd service |

### Data & Analytics
| Skill | Purpose |
|---|---|
| `jupyter-live-kernel` | Iterative Python via live Jupyter |
| `crypto-trading` | Binance spot orders, market data |
| `blockchain-cashflow` | Multi-chain cash flow analysis |
| `price-action` | Price action analysis |
| `revenue-intel` | Revenue intelligence |
| `chainlink-ccip-skill` | Cross-chain token transfers |
| `chainlink-cre-skill` | Chainlink Runtime Environment |
| `chainlink-data-feeds-skill` | Chainlink Data Feeds integration |
| `supabase-postgres-best-practices` | PostgreSQL optimization |
| `postgres-best-practices` | Supabase PostgreSQL best practices |
| `neon-postgres` | Neon serverless Postgres |

### Security & Red Teaming
| Skill | Purpose |
|---|---|
| `security-recon` | Security reconnaissance |
| `godmode` | LLM jailbreaking techniques |
| `adversarial-critique` | Stress-test plans/code via adversarial analysis |
| `multi-perspective-analysis` | Multi-perspective analysis |

### Note-Taking & Knowledge Management
| Skill | Purpose |
|---|---|
| `hindsight-architect` | Expert memory architect |
| `hindsight-cloud` | Team knowledge store (cloud) |
| `hindsight-docs` | Complete Hindsight documentation |
| `hindsight-local` | User preferences + learnings (local) |
| `hindsight-self-hosted` | Self-hosted team knowledge |
| `notion-knowledge-capture` | Convert convos to structured notes |
| `notion-meeting-intelligence` | Meeting prep from Notion |
| `notion-research-documentation` | Synthesize Notion findings |
| `qmd` | FlowState-QMD anticipatory project memory |
| `agentic-patterns` | Reconstructed Claude Code internal patterns |
| `bayesian-synthesis` | Bayesian evidence synthesis |
| `autoreason` | Auto-reasoning capability |
| `evolution` | Evolution capability |
| `openspace-evolution` | OpenSpace evolution capability |

### n8n Workflow Automation
| Skill | Purpose |
|---|---|
| `n8n-code-javascript` | JS in n8n Code nodes |
| `n8n-code-python` | Python in n8n Code nodes |
| `n8n-expression-syntax` | n8n expressions ($json, $node, etc.) |
| `n8n-mcp-tools` | MCP tools within n8n |
| `n8n-mcp-tools-expert` | Master n8n MCP tools |
| `n8n-node-configuration` | Node configuration best practices |
| `n8n-validation` | Fix validation errors |
| `n8n-validation-expert` | Advanced error interpretation |
| `n8n-workflow-patterns` | Common workflow patterns |
| `n8n-workflow-generator` | Generate n8n JSON from NL prompts |

### Skill Factory (Meta-Skills)
| Skill | Purpose |
|---|---|
| `skill-factory` | Auto-creates skills by watching workflows |
| `skill-forge` | Skill compilation system |
| `skf-setup` | Initialize forge environment |
| `skf-brief-skill` | Design skill scope through discovery |
| `skf-create-skill` | Compile skill from brief |
| `skf-create-stack-skill` | Consolidated project stack skill |
| `skf-quick-skill` | Fast skill from package/GitHub URL |
| `skf-forger` | Skill compilation specialist |
| `skf-analyze-source` | Discover what to skill in a repo |
| `skf-audit-skill` | Drift detection between skill + code |
| `skf-test-skill` | Cognitive completeness verification |
| `skf-update-skill` | Smart regeneration preserving [MANUAL] |
| `skf-verify-stack` | Pre-code stack feasibility |
| `skf-export-skill` | Package for distribution |
| `skf-drop-skill` | Delete skill versions |
| `skf-rename-skill` | Rename across all versions |
| `skf-refine-architecture` | Improve arch docs from skill data |
| `skill-tester` | Skill testing framework |
| `creating-local-skills` | How to create local Hermes skills |
| `hermes-agent-skill-authoring` | In-repo SKILL.md authoring |
| `install-tool-and-create-skill` | Install CLI tool + create skill |
| `cross-ecosystem-skill-port` | Port skills from Claude Code/Codex |
| `find-skills` | Discover and install agent skills |
| `agent-audit` | Agent capability audit |

### Communication & Social
| Skill | Purpose |
|---|---|
| `xurl` | X/Twitter CLI: post, search, DM |
| `spotify` | Play, search, queue, manage |
| `gif-search` | Tenor GIF search |
| `youtube-channel-scrape` | Scrape YouTube videos/shorts |
| `youtube-content` | YouTube transcripts → summaries |
| `yuanbao` | Yuanbao group @mentions |
| `email-best-practices` | Email deliverability practices |
| `email-sequence` | Email drip campaigns |
| `agentic-mcp` | Three-layer MCP progressive disclosure |
| `native-mcp` | Built-in MCP client integration |
| `mcp-builder` | Build MCP servers |
| `anthropic-mcp-builder` | Anthropic MCP server builder |
| `microsoft-mcp-builder` | Python/TypeScript MCP builder |
| `browserbase` | Browserbase automation |
| `browser-use` | browser-use library AI automation |
| `openrouter-budget-monitor` | Check daily budget, switch models |
| `web-search-fallback` | Multi-tier search (Tavily→DuckDuckGo) |

### Gaming
| Skill | Purpose |
|---|---|
| `minecraft-modpack-server` | Host modded Minecraft servers |
| `pokemon-player` | Play Pokemon via headless emulator |

### Smart Home
| Skill | Purpose |
|---|---|
| `openhue` | Control Philips Hue lights/scenes |

### Special / Experimental
| Skill | Purpose |
|---|---|
| `dogfood` | Exploratory QA of web apps |
| `focused-fix` | Targeted fix/debug workflow |
| `release` | Release management (changelog, version) |
| `release-it` | Production stability patterns |
| `red-teaming` | Red teaming framework |
| `zenda-manager` | Zenda management |
| `zo-swarm-executors` | Local executor for zo-swarm |
| `datadog-logs` | Datadog log search, monitors, APM |

---

## 5. PLUGINS

Two plugins enabled:

### Evey Bridge Plugin (`evey-bridge-plugin`)
A comprehensive agent autonomy framework with sub-plugins:
- `evey-autonomy`, `evey-bridge`, `evey-cache`, `evey-commands`, `evey-cost-guard`
- `evey-council`, `evey-delegate-model`, `evey-delegation-score`, `evey-digest`
- `evey-email-guard`, `evey-github`, `evey-goals`, `evey-habits`, `evey-identity`
- `evey-learner`, `evey-memory-adaptive`, `evey-memory-consolidate`, `evey-moltbook`
- `evey-mqtt`, `evey-news`, `evey-proactive`, `evey-rag`, `evey-reflect`
- `evey-research`, `evey-sandbox`, `evey-scheduler`, `evey-session-guard`
- `evey-status`, `evey-telegram-ux`, `evey-telemetry`, `evey-validate`
- `evey-verification`, `evey-wallet`, `evey-watchdog`
- Plugin skills: `evey-loop`, `evey-status`

**Capabilities:** Proactive agent behavior, goal tracking, habit formation, multi-agent council, RAG, memory consolidation, cost guarding, email guarding, wallet/reputation system, scheduled tasks, reflection, MQTT, research, sandboxed execution, session management, autonomous task chains.

### Web Search Plus (`web-search-plus`)
Enhanced web search capabilities beyond default Tavily integration.

---

## 6. COMMUNITY SKILL REPOSITORIES

Loaded from external directories:

| Source | Path |
|---|---|
| Hermes Agent Skills | `~/hermes/community-skills/hermes-agent-skills/skills/` |
| Incident Commander | `~/hermes/community-skills/hermes-incident-commander/skills/` |
| BFL FLUX Skills | `~/hermes/community-skills/bfl-flux-skills/skills/` |
| Chainlink Agent Skills | `~/hermes/community-skills/chainlink-agent-skills/` |
| GSAP Skills | `~/hermes/community-skills/gsap-skills/skills/` |

Additional skills contributed by these repos (supplementing the 135+ local skills):
- `incident-commander`, `agent-audit`, `agent-tools`, `agentic-patterns`, `autoreason`, `blacksmith`, `evolution`, `focused-fix`, `observability-designer`, `openspace-evolution`, `price-action`, `production-safety`, `revenue-intel`, `security-recon`, `skill-tester`, `system-health`, `zenda-manager`, `zenops-ops`
- Chainlink: `chainlink-ccip-skill`, `chainlink-cre-skill`, `chainlink-data-feeds-skill`
- GSAP: `gsap-core`, `gsap-frameworks`, `gsap-performance`, `gsap-plugins`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-utils`
- BFL: `bfl-api`, `flux-best-practices`

---

## 7. MEMORY SYSTEMS

### Hindsight (Active)
- **Daemon:** `hermes-hindsight.service`, port 8888
- **Type:** Embed Memory Daemon
- **Function:** Stores user preferences, task learnings, project context across sessions
- **4 variants:** `hindsight-local` (personal), `hindsight-cloud` (team), `hindsight-self-hosted` (self-managed), `hindsight-architect` (advanced)

### Model Memory (Config)
- Memory enabled: yes
- User profile enabled: yes
- Context engine: `compressor`
- Prompt caching: 5min TTL
- Checkpoints: 50 max, 7-day retention, auto-prune

### Wiki (`~/wiki/wiki/`)
20+ markdown files covering:
- Daily notes (systematic logging)
- Project documentation (biz-ops, analyses, decisions)
- Technical notes (Tailscale, n8n, GitHub Pages)
- OpenRouter budget tracking
- Session logs and configurations

### Skills as Memory
135+ procedural memory files that the agent loads on-demand — this IS the primary knowledge storage.

---

## 8. PLATFORM INTEGRATIONS

| Platform | Toolset | Features |
|---|---|---|
| **Telegram** (primary) | `hermes-telegram` | Messaging, reactions, channel prompts |
| **Discord** | `hermes-discord` | Messaging, threads, reactions, channel prompts, server actions |
| **WhatsApp** | `hermes-whatsapp` | Messaging |
| **Slack** | `hermes-slack` | Messaging, channel prompts |
| **Signal** | `hermes-signal` | Messaging |
| **HomeAssistant** | `hermes-homeassistant` | Smart home control |
| **QQ Bot** | `hermes-qqbot` | QQ platform messaging |

---

## 9. VOICE & SPEECH

- **TTS Providers:** Edge (default), ElevenLabs, OpenAI, xAI, Mistral, Neuphonic
- **STT:** Local Whisper (base model), OpenAI Whisper, Mistral Voxtral
- **Voice recording:** Ctrl+b trigger, 120s max, auto-silence detection

---

## 10. AGENT PERSONALITIES

11 built-in personas: helpful, concise, technical, creative, teacher, kawaii, catgirl, pirate, shakespeare, surfer, noir, uwu, philosopher, hype

---

## 11. KEY WORKFLOW PATTERNS

1. **Two-Agent System**: Claude Chat (planning/strategy) ↔ Hermes (persistent execution)
2. **Skill-First Architecture**: Every task type → load matching skill → follow instructions
3. **Subagent Delegation**: Complex tasks → spawn subagents with MCP tools
4. **Cron Automation**: Scheduled tasks via cron + webhooks
5. **Memory Persistence**: Hindsight daemon stores cross-session context
6. **MCP Tool Composition**: 5 MCP servers providing 50+ specialized tools
7. **Dashboard Visualization**: Hermes dashboard for monitoring and interaction
8. **Auto-Skill Creation**: Skill Factory auto-creates skills from workflows (prompted after 5+ calls)

---

## 12. LIMITATIONS & BOUNDARIES

- **Budget cap:** $3/day OpenRouter — falls back to `minimax/minimax-m2.7` on limit
- **Max turns:** 90 per session
- **Subagent depth:** 1 level (can't spawn agents that spawn agents)
- **Concurrent subagents:** 3 max
- **File read limit:** 100K chars per file
- **Tool output limit:** 50KB / 2000 lines
- **Session auto-reset:** after 24 hours idle (4 AM)
- **Session retention:** 90 days with auto-prune
