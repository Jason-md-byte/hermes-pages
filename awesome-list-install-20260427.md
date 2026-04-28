# Awesome Hermes Agent — Install Report
**Date:** 2026-04-27
**Source:** [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)

---

## Summary

| Metric | Value |
|--------|-------|
| Skills before this session | 126 |
| Skills after this session | 156 |
| **Net new** | **30** |
| Plugins installed | 2 |
| Total repos processed | 15 (priority list) + 3 (known to skip) |

---

## Installed: Skills (14 repos, 30 skills)

### ✅ Romanescu11/hermes-skill-factory — 1 skill
- `skill-factory` — Meta-skill that auto-generates reusable skills from workflows

### ✅ marlandoj/zouroboros-swarm-executors — 1 skill
- `zo-swarm-executors` — Local executor bridge for Claude Code + Hermes integration

### ✅ Rainhoole/hermes-agent-acp-skill — 1 skill
- `hermes-acp-orchestrator` — Multi-agent delegation skill bridging Hermes, Codex, and Claude Code

### ✅ tiann/execplan-skill — 1 skill
- `execplan` — Manages complex, long-running task execution with lifecycles, checkpoints, and recovery

### ✅ dlkakbs/hermes-startup-architect — 1 skill
- `startup-architect` — Generates investor-ready kits from startup ideas

### ✅ Lethe044/hermes-legal — 1 skill
- `legal-advisor` — Contract risk analysis (English + Turkish)

### ✅ hxsteric/mercury — 1 skill
- `blockchain-cashflow` — Multi-chain blockchain cash flow analyzer (forced: false positive on "analyze wallet" description)

### ✅ Lethe044/hermes-skill-marketplace — 1 skill
- `skill-forge` — Agent that writes, tests, and publishes new skills autonomously

### ✅ Yonkoo11/hermes-dojo — 1 skill
- `hermes-dojo` — Self-improvement system that monitors agent performance (forced: false positive on `allowed-tools` frontmatter)

### ✅ armelhbobdad/bmad-module-skill-forge — 15 skills
- `skf-analyze-source`, `skf-audit-skill`, `skf-brief-skill`, `skf-create-skill`, `skf-create-stack-skill`, `skf-drop-skill`, `skf-export-skill` (forced), `skf-forger` (forced), `skf-quick-skill`, `skf-refine-architecture`, `skf-rename-skill`, `skf-setup`, `skf-test-skill`, `skf-update-skill`, `skf-verify-stack`
- Transforms repos and docs into agentskills.io-compliant skills

### ✅ amanning3390/flowstate-qmd — 2 skills
- `qmd` — Anticipatory memory with RAG and vector search (forced: false positive on `allowed-tools` frontmatter)
- `release` — Release management skill

### ✅ Ridwannurudeen/hermes-council — 3 skills
- `adversarial-critique` — Adversarial multi-perspective council
- `bayesian-synthesis` — Bayesian synthesis of council viewpoints
- `multi-perspective-analysis` — Multi-perspective analysis skill

### ❌ gizdusum/hermes-blockchain-oracle — Skipped
**Reason:** MCP server (Python package at `src/`), not a skill. No SKILL.md files. It's a Solana blockchain MCP server that should be configured in `mcp_servers` in config.yaml, not installed as a skill.

---

## Installed: Plugins (2 repos)

### ✅ 42-evey/evey-bridge-plugin
**Status:** Installed but not enabled
**Type:** Plugin (Claude Code bridge for Hermes)
**Note:** Warning about no `plugin.yaml` but installed anyway

### ✅ robbyczgw-cla/hermes-web-search-plus
**Status:** Installed but not enabled
**Type:** Plugin (v1.6.0 — multi-provider web search: Serper, Brave, Tavily, Exa, Querit, Perplexity, SearXNG)

---

## Already Installed (from previous session)

These were installed in the previous community skills session and were not re-installed:

- `zenc-cp/hermes-agent-skills` — 18 skills (agent-tools, agent-audit, agentic-patterns, autoreason, blacksmith, evolution, find-skills, focused-fix, observability-designer, openspace-evolution, price-action, production-safety, revenue-intel, security-recon, skill-tester, system-health, zenda-manager, zenops-ops)
- `Lethe044/hermes-incident-commander` — 1 skill (incident-commander)
- `black-forest-labs/skills` — 2 skills (bfl-api, flux-best-practices)
- `smartcontractkit/chainlink-agent-skills` — 3 skills (chainlink-ccip-skill, chainlink-cre-skill, chainlink-data-feeds-skill)

---

## Skipped (No SKILL.md / Not a Skills Repo)

### ❌ farosud/traction-skills — from previous session
Empty repo, no files published

### ❌ Yarmoluk/cognify-skills — from previous session
Repo doesn't exist (404)

### ❌ 42-evey/hermes-plugins — from previous session
Plugins repo (33 `plugin.yaml` files), not skills

### ❌ KYC-rip/ripley-xmr-gateway — explicitly excluded
Monero blockchain gateway — instructed not to install

### ❌ mukul975/Anthropic-Cybersecurity-Skills — explicitly excluded
753+ security skills — instructed not to install

### ❌ outsourc-e/hermes-workspace — explicitly excluded
Hermes GUI workspace — instructed not to install

---

## Name Conflict Check

No naming conflicts detected. All 156 skills have unique names across builtin (77), local (20), and community (52) sources.

---

## Plugin Status

| Plugin | Status | Source | Action Needed |
|--------|--------|--------|---------------|
| disk-cleanup | not enabled | bundled | Enable if desired |
| google_meet | not enabled | bundled | Enable if Google Meet access needed |
| spotify | not enabled | bundled | Enable if Spotify control needed |
| **web-search-plus** | **not enabled** | **git** | `hermes plugins enable web-search-plus` + gateway restart |
| **evey-bridge-plugin** | **not enabled** | **git** | `hermes plugins enable evey-bridge-plugin` + gateway restart |

---

## Final Skill Breakdown

```
Builtin:  77
Local:    20
Community (URL): 52
Total:    156
```
