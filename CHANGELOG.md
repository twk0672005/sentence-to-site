# Changelog

All notable changes to this kit are documented here.

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
