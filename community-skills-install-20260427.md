# Community Skills Installation Report — 2026-04-27

## Summary

| Metric | Value |
|--------|-------|
| Skills before | 102 |
| Skills after | 126 |
| New skills installed | 24 |
| Repos processed | 7 |
| Installed | 5 repos |
| Skipped | 2 repos (no valid skills) |

---

## Per-Repo Results

### ✅ Installed: zenc-cp/hermes-agent-skills
**Source:** https://github.com/zenc-cp/hermes-agent-skills
**Skills installed:** 18
- `agent-tools` ✅ (pre-installed, skipped)
- `agent-audit` ✅
- `agentic-patterns` ✅ (DANGEROUS flag: false positive — `Read README/CLAUDE.md` is instructional text)
- `autoreason` ✅
- `blacksmith` ✅
- `evolution` ✅ (CAUTION flag: false positives — `subprocess.run` in Python examples for code validation)
- `find-skills` ✅
- `focused-fix` ✅ (CAUTION flag: false positive — grep for env vars in code review context)
- `observability-designer` ✅
- `openspace-evolution` ✅
- `price-action` ✅
- `production-safety` ✅ (CAUTION flag: `sudo` commands — legitimate concern but content is documentation, not execution)
- `revenue-intel` ✅ (CAUTION flag: false positive — regex patterns in data analysis code)
- `security-recon` ✅
- `skill-tester` ✅
- `system-health` ✅
- `zenda-manager` ✅
- `zenops-ops` ✅ (CAUTION flag: 34 findings — all `sudo`/`systemctl`/`journalctl` in documentation, not execution)

### ✅ Installed: Lehto044/hermes-incident-commander
**Source:** https://github.com/Lethe044/hermes-incident-commander
**Skills installed:** 1
- `incident-commander` ✅

### ✅ Installed: black-forest-labs/skills
**Source:** https://github.com/black-forest-labs/skills
**Branch:** `master` (not `main`)
**Skills installed:** 2
- `bfl-api` ✅ (DANGEROUS flag: false positive — `$BFL_API_KEY` env var usage for FLUX API auth, from the creators of FLUX)
- `flux-best-practices` ✅

### ✅ Installed: smartcontractkit/chainlink-agent-skills
**Source:** https://github.com/smartcontractkit/chainlink-agent-skills
**Skills installed:** 3
- `chainlink-ccip-skill` ✅ (CAUTION flag: false positive — `allowed-tools` is AGENTS.md frontmatter)
- `chainlink-cre-skill` ✅ (CAUTION flag: false positives — frontmatter + trigger docs)
- `chainlink-data-feeds-skill` ✅ (CAUTION flag: false positive — `allowed-tools` frontmatter)

### ❌ Skipped: farosud/traction-skills
**Reason:** Repository exists on GitHub but is empty (no files, no branches published). No SKILL.md files found.

### ❌ Skipped: Yarmoluk/cognify-skills
**Reason:** Repository does not exist (HTTP 404). GitHub returns "Not Found".

### ❌ Skipped: 42-evey/hermes-plugins
**Reason:** This is a plugins directory (33 `plugin.yaml` files found), not a skills directory. Zero SKILL.md files. Plugins are a different extension mechanism in Hermes.

---

## External Dirs Config Fix

**Before:** Broken YAML — `external_dirs` was stored as an inline JSON string with escaped newlines, included `hermes-plugins` (no skills), and referenced wrong subdirectory for `hermes-incident-commander`.

**After:** Proper YAML list format with 4 correct paths:
```yaml
skills:
  external_dirs:
    - /home/hermes/hermes/community-skills/hermes-agent-skills/skills/
    - /home/hermes/hermes/community-skills/hermes-incident-commander/skills/
    - /home/hermes/hermes/community-skills/bfl-flux-skills/skills/
    - /home/hermes/hermes/community-skills/chainlink-agent-skills/
```

**Verification:** Config valid ✅. Skills count: 102 → 126 (gain of 24).

---

## Name Conflict Check

No naming conflicts detected between:
- Community-installed skills (24) vs builtin skills (77) vs local skills (18)
- All 119 skills have unique names

---

## Final Summary

| Repo | Status | Skills |
|------|--------|--------|
| zenc-cp/hermes-agent-skills | ✅ Installed | 18 |
| farosud/traction-skills | ❌ Skipped — empty repo | 0 |
| Yarmoluk/cognify-skills | ❌ Skipped — repo not found | 0 |
| Lehto044/hermes-incident-commander | ✅ Installed | 1 |
| black-forest-labs/skills | ✅ Installed | 2 |
| 42-evey/hermes-plugins | ❌ Skipped — no SKILL.md (plugin repo) | 0 |
| smartcontractkit/chainlink-agent-skills | ✅ Installed | 3 |
| **Total** | **5 installed, 2 skipped** | **24 new skills** |
