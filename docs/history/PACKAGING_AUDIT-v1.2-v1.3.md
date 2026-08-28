# Packaging Audit

## v1.2 with included skills

This package includes the workflow kit plus the Hermes skills required or commonly used by the website workflow and animation workflow.

## Scope

Included:

- Core website / frontend / browser artifact skills
- Animation / WebGL / Reel reference skills
- Evidence / verification skills
- MCP setup skill
- Optional support skills for ClawTeam, parallel agents, image generation, brand direction, and redesign

Excluded:

- Trading skills
- Media/video production skills unrelated to browser website animation
- Personal memories
- SOUL / identity files
- Hermes config
- Secrets / tokens / cron / service files
- node_modules / caches / pycache

## Scan notes

Secret-like placeholders in included public docs are redacted to `[REDACTED_*]`.

Some included verification skills intentionally contain mojibake marker examples such as replacement-character or encoded-looking snippets. These are not corruption in the package; they are detection examples used by the skill to teach agents how to scan handoff bundles.

## Installation note

Do not blindly overwrite existing Hermes skills. Treat `included-skills/` as a research and portable reference bundle unless the user explicitly asks to install them into an active profile.


## v1.2.1 manifest refresh

`SKILLS_MANIFEST.json` was regenerated after bundled skill sanitization so file sizes and SHA256 hashes match the actual package contents. Absolute local source paths were removed from the manifest for cleaner external sharing.


## v1.2.2 Codex / Claude Code adapter

Added `AGENTS.md`, `CLAUDE.md`, and `docs/codex-claude-usage.md` so the package can be used by Codex and Claude Code as a portable workflow/reference bundle. Clarified that `hermes-agent` is Hermes-only support and not required for normal website or animation execution by non-Hermes agents.


## v1.2.3 no root agent instruction files

Removed root `AGENTS.md` and `CLAUDE.md` to avoid influencing a recipient repo's own instructions, soul, memory, or agent rules. Cross-agent guidance is kept as a normal reference document at `docs/codex-claude-usage.md`.

## v1.3.3 clean result core

- release tree 保留 30 個實際檔案；日常 reading path 仍然只係 README + 一份 domain workflow；
- `included-skills/` 變成 index-only：23 個 unique optional skill 名稱，不內嵌 active skill bodies；
- `THREEJS_SOURCE_LOCK.json` 另外鎖定 10 個技術 topic、最多每階段 3 個 specialist、禁止 bulk loading；
- Refero 只作概念研究，分 Product UI screens／flows 同 Refero Styles；reference／accepted baseline 仍為權威；
- Refero public pages 不可自動 scrape／crawl／bulk-download；官方 MCP／API、登入、上載與付款保持批准邊界；
- release tree 不含 `__pycache__`、`*.pyc`、root `AGENTS.md`／`CLAUDE.md`、live key/token pattern 或 private-key block；
- Python、JSON、required-file、source-lock、route、Refero boundary、ZIP integrity 與 tree parity 都在 canonical pointer 切換前驗證。
