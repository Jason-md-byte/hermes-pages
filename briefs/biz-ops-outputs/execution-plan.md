# Biz Ops Execution Plan — n8n Agency + Appointment Setting + Personal Brand

> **For Hermes:** Use subagent-driven-development to execute task-by-task in YOLO mode.
>
> **Goal:** Complete all YOLO-safe action items for Streams 1 (n8n Agency), 2 (Appointment Setting), and 3 (Personal Brand).
>
> **YOLO Safety:** No actions require API keys we don't have, credit cards, DNS changes, or external service signups. Everything is local files, Docker, content drafting, and Browserbase workflows.
>
> **Output directory:** `~/hermes/scratch/briefs/biz-ops-outputs/`

---

## Task 1: Install n8n via Docker

**Objective:** Get n8n running on localhost:5678 as a self-hosted instance.

**Action:**
```bash
docker run -d --restart unless-stopped -p 5678:5678 --name n8n n8nio/n8n
```

**Verify:** `curl -s -o /dev/null -w "%{http_code}" http://localhost:5678/` returns 200.

---

## Task 2: Build n8n-workflow-generator Hermes Skill

**Objective:** Create a Hermes skill at `~/.hermes/skills/n8n-workflow-generator/SKILL.md` that takes a business problem description and outputs a deployable n8n workflow JSON.

**The skill should:**
- Frontmatter with name, description, triggers
- Instructions for using Codex to generate workflow JSON
- Template for common workflow patterns (webhook → filter → transform → output)
- Pitfalls section (n8n node limits, credential handling)
- Example prompt flow

**Output file:** `~/.hermes/skills/n8n-workflow-generator/SKILL.md`

---

## Task 3: Build 3 Demo n8n Workflow JSONs

**Objective:** Create 3 deployable n8n workflow JSON files in `~/hermes/scratch/briefs/biz-ops-outputs/n8n-demos/`.

**Workflow 1: Lead Capture → CRM** (`lead-capture-to-crm.json`)
- Webhook receives lead data (name, email, phone, message)
- Filter validates required fields
- HTTP Request node posts to a CRM endpoint (parameterized)
- Respond with success/failure

**Workflow 2: Invoice → Email Notification** (`invoice-to-notify.json`)
- Webhook receives invoice data
- Format email body with invoice details
- Send via SMTP (parameterized)
- Log to a local file

**Workflow 3: Form → Slack Alert** (`form-to-slack.json`)
- Webhook receives form submission
- Format Slack message blocks
- POST to Slack webhook URL (parameterized)
- Respond with confirmation

Each file should be valid n8n JSON with `"nodes"` and `"connections"` arrays, parameterized where credentials are needed (use `{{ $vars.XXX }}` placeholders).

---

## Task 4: Write Sales Pipeline Automation Pitch

**Objective:** Create a unified sales pitch document that bundles n8n Agency + Appointment Setting into a single "Sales Pipeline Automation" offering.

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/sales-pipeline-pitch.md`

**Structure:**
- Problem statement (leaky pipelines, missed follow-ups)
- Solution: end-to-end automation
- Package A: Workflow Automation (n8n — $2K/project)
- Package B: Lead Generation + Outreach (Appointment Setting — $1.5K/mo retainer)
- Package C: Full Pipeline (both — $3K/mo)
- ROI calculation
- Case study placeholder
- Contact CTA

---

## Task 5: Write 5-Touch Outreach Sequence

**Objective:** Create a 5-email cold outreach sequence targeting ops-heavy SMBs (HVAC, roofing, dental, real estate).

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/outreach-sequence.md`

**Each email:**
- Subject line
- Body (3-5 sentences, benefit-focused)
- CTA

**Sequence flow:**
1. **Touch 1:** Problem awareness — "Are leads falling through the cracks?"
2. **Touch 2:** Value prop — case study teaser
3. **Touch 3:** Social proof — "Here's what similar businesses are doing"
4. **Touch 4:** Direct offer — "Let me build a free 1-workflow audit"
5. **Touch 5:** Breakup — "I'll stop reaching out, but my door's open"

---

## Task 6: Build LinkedIn Scraper Workflow

**Objective:** Create a Browserbase workflow script for ICP-matched lead extraction from LinkedIn.

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/linkedin-scraper/`

**Contents:**
- `README.md` — setup instructions, target criteria
- `config.yaml` — search parameters (title, location, industry)
- `scraper.js` or `scraper.py` — play script using Browserbase
- `output-schema.json` — what data gets extracted

---

## Task 7: Write First 3 Personal Brand Posts

**Objective:** Write 3 posts for the personal brand launch on Twitter/X + LinkedIn.

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/personal-brand-posts.md`

**Post 1 — "Why I'm Building an AI Agency Solo on a $200/mo Stack"**
- Hook: "Most agencies spend $500-600/mo on tools. I run 7 revenue streams on $200."
- Body: Stack breakdown, flywheel model
- CTA: follow for build logs

**Post 2 — "I Put My Startup Ideas Through an AI Council. Here's What It Caught."**
- Hook: "I ran my biz ops plan through an adversarial AI council. The Skeptic eviscerated my revenue projections."
- Body: Council critique highlights, how it improved the plan
- CTA: subscribe to newsletter

**Post 3 — "The n8n Workflow That Replaced My CRM"**
- Hook: "I built a lead capture workflow in n8n that does what HubSpot does — for $0/mo."
- Body: Simple walkthrough, before/after
- CTA: download the workflow template

---

## Task 8: Create Lead Magnet PDF

**Objective:** Create a lead magnet: "7 AI Workflows Under $200/mo" — a markdown doc that can be exported to PDF.

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/lead-magnet-7-workflows.md`

**Structure:**
- Title page
- Introduction (why $200/mo? stack efficiency)
- Workflow 1: Lead Capture → CRM
- Workflow 2: Invoice → Automated Notification
- Workflow 3: Form → Slack Alert
- Workflow 4: Social Media Monitoring → Digest
- Workflow 5: Email Follow-up Sequence
- Workflow 6: Competitor Price Tracking
- Workflow 7: Daily Ops Dashboard
- CTA: book a free workflow audit

---

## Task 9: Set Up Cal.com + Webhook → Notion Pipeline

**Objective:** Configure Cal.com free account and set up webhook integration to Notion for auto-logging booked meetings.

**Note:** This requires creating a Cal.com account (email-only, no payment needed) and a Notion integration. Since this needs a browser session and external signup, do what you can:
- Document the Notion integration setup steps
- Create the webhook payload schema
- Document the Notion MCP pipeline config
- Flag that Cal.com account creation is a manual step (email-based)

**Output:** `~/hermes/scratch/briefs/biz-ops-outputs/cal-notion-pipeline.md`

---

## Execution Order

1. Task 1 (n8n install) — quick, verify immediately
2. Task 2 (n8n skill) — builds on Task 1
3. Task 3 (3 workflow JSONs) — builds on Task 2
4. Task 4 (pitch doc) — independent
5. Task 5 (outreach sequence) — builds on Task 4
6. Task 6 (LinkedIn scraper) — independent
7. Task 7 (brand posts) — independent
8. Task 8 (lead magnet) — uses content from Tasks 3+5
9. Task 9 (Cal.com + Notion) — independent, partial

**Parallel groups:** Tasks 1+4+6+7 can run in parallel. Tasks 2+5+8+9 can run after. Task 3 depends on Task 2.
