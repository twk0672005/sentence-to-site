# Changelog

All notable changes to this kit are documented here.

## 0.5.0 — 2026-07-19

### Changed

- Replaced the default open-ended build → review → repair loop with a bounded routing contract: one base route (`new-site` or `existing-site`), one experience lane, one delivery gate, fixed evidence, and a fixed stop condition.
- `one-sentence-website` now routes once, collects route-specific browser evidence, and hands control back to the user rather than autonomously re-entering implementation because of private aesthetic judgement.
- `cinematic-web-motion` now reads the same routing contract and selects only the specialists required by the chosen route.
- Reframed `adversarial-quality-loop` as an explicit, one-time independent review. It cannot be selected automatically, simulated as solo role-play, or used to start another build pass without a new user decision.

### Added

- `references/routing-contract.md`: a public, framework-neutral route matrix for new/existing websites, static/UI/cinematic work, prototype/public delivery gates, evidence, and stop conditions.
- Deterministic routing simulation with six acceptance cases, including public WebGL and existing-project routes.

## 0.4.1 — 2026-07-18

Findings from a full end-to-end dogfood run (fresh clone → install → one sentence → verified site).

### Fixed

- `verify_browser_artifact.py` attached console/pageerror/requestfailed listeners **after** `page.goto`, so load-time errors were silently missed. Listeners now attach before navigation.
- The README quick-install copied skill folders without the shared `references/` they link to, leaving dangling `../../references/…` links after installation. Install commands now copy `references/` beside the skills and no longer copy the stray `catalog.json` into the skill directory.

### Added

- Windows note in install docs: use `python` instead of `python3`; one-time `playwright install chromium` for the optional browser tooling.

## 0.4.0 — 2026-07-18

### Added

- New skill `adversarial-quality-loop`: a real quality loop with separated Planner, Builder, Evaluator, and Evidence Auditor roles. Self-critique never counts as the loop, and any degraded solo mode must be declared explicitly.
- `references/quality-loop-roles.md`: prompt contracts for the four loop roles.
- `references/reference-recreation.md`: reference-driven recreation discipline — verify the source, sample real frames, extract mechanics with confidence labels, never copy brand identity.
- `references/evidence-and-handoff.md` now covers public UI vs internal evidence separation (no QA vocabulary in shipped pages) and WebGL/canvas runtime readback fields.

### Changed

- `one-sentence-website` Step 3 routes to `adversarial-quality-loop` when multi-agent tooling is available; solo self-critique must be labelled as such.

## 0.3.0 — 2026-07-18

### Changed

- Repositioned and renamed the kit to **sentence-to-site**: one sentence in, a verified website out.
- Rewrote the README around the one-sentence entry point; existing skills are now presented as its pipeline.

### Added

- Flagship skill `one-sentence-website`: expands a vague one-line idea into a premise with explicit assumptions, routes the specialist pipeline, and loops build → browser evidence → repair until the result is honest to show.

## 0.2.0 — 2026-07-18

### Added

- Six composable skills: routing, visual direction, existing-project intake, motion choreography, browser evidence, and delivery handoff.
- Machine-readable catalog, per-skill eval fixtures, shared templates, package validator, and local CI workflow.
- Public contribution surfaces for bug reports, skill requests, and pull requests.

### Changed

- The original single `cinematic-web-motion` skill is now the thin router for a complete bundle rather than an overloaded all-in-one instruction file.

### Security

- Release validation now checks the full public payload, catalog consistency, frontmatter, required eval fixtures, and common secret/private-marker patterns.

## 0.1.0 — 2026-07-18

- Initial clean-room website-motion workflow kit with browser verification and scroll-video utilities.
