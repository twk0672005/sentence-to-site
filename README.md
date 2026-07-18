<div align="center">

# ✨ sentence-to-site · Agent Skill Library

**One sentence in. A verified website out.**

Idea Expansion (no questionnaires) · Anti-Generic Visual Direction · Motion Choreography · Real-Browser Evidence · Adversarial Quality Loop

[![CI](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-skills.yml)
[![Agent Skills](https://img.shields.io/badge/Agent-Skills-blueviolet)](skills/catalog.json)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97757)](https://claude.com/claude-code)
[![Codex](https://img.shields.io/badge/Codex-compatible-black)](https://openai.com/codex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**English** | [繁體中文](README_zh-TW.md)

</div>

---

## 🖼️ Live Showcase

> **This site was produced with this exact workflow** — one-sentence brief → visual direction → motion choreography → screenshot-verified delivery. **Click to visit.**

[![ORBITAL — From Earth into deep space](docs/assets/showcase-orbital.png)](https://twk0672005.github.io/orbital-spatial-intelligence/)

🔗 **https://twk0672005.github.io/orbital-spatial-intelligence/**

---

## Why This Kit?

Agents are already good at generating web code. What they get wrong is everything **around** the code:

| Failure mode | Bare agent | **With sentence-to-site** |
|---|---|---|
| Vague idea → questionnaire back at you | ❌ interrogates | ✅ expands into decisions + explicit assumptions |
| Same gradient-and-glass page for every prompt | ❌ generic | ✅ anti-generic visual direction with one visible promise |
| "Done" because the build passed | ❌ never rendered | ✅ real-browser screenshots + readback required |
| Grades its own homework, calls it a "quality loop" | ❌ self-critique | ✅ separated Planner / Builder / Evaluator / Evidence Auditor roles |
| Motion added as decoration, breaks on mobile | ❌ ad-hoc | ✅ choreography lanes + reduced-motion fallback |
| Handoff with no record of assumptions | ❌ silent | ✅ every inferred decision listed and veto-able in one line |

The core rule everywhere: **completion is a browser verdict, never a build exit code.**

You have a vague idea — *"a landing page for my coffee cart, warm, not corporate"*. An AI agent loaded with this kit turns that sentence into a finished website: it expands the idea into a design premise, makes the small decisions on your behalf (and tells you which ones), builds the page, **looks at it in a real browser**, repairs the weakest visible thing, and repeats until the result is honest to show.

This is a **skill library for AI agents** (Claude Code, Codex, and any agent that reads `SKILL.md` files) — not a website builder app, not a giant prompt, not a framework.

---

## Architecture

```text
                        one vague sentence
                                │
                                ▼
                ┌───────────────────────────────┐
                │     one-sentence-website      │  flagship entry point
                │  expand → decide → assume     │
                └───────────────┬───────────────┘
                                │ routes the pipeline
        ┌───────────────┬───────┴───────┬───────────────────┐
        ▼               ▼               ▼                   ▼
┌───────────────┐ ┌─────────────┐ ┌─────────────────┐ ┌────────────────┐
│ visual-story- │ │ website-    │ │ motion-         │ │ browser-       │
│ direction     │ │ motion-     │ │ choreography    │ │ evidence       │
│ premise,      │ │ intake      │ │ CSS/GSAP/WebGL  │ │ screenshots,   │
│ anti-generic  │ │ existing    │ │ lanes, reduced  │ │ readback,      │
│ hierarchy     │ │ repo read   │ │ motion          │ │ honest verdict │
└───────────────┘ └─────────────┘ └─────────────────┘ └───────┬────────┘
                                                              │
                ┌─────────────────────────────────────────────▼───────┐
                │              adversarial-quality-loop               │
                │   Planner → Builder → Evaluator → Evidence Auditor  │
                │   repeat on the weakest visible thing until honest  │
                └─────────────────────────┬───────────────────────────┘
                                          ▼
                              ┌───────────────────────┐
                              │   delivery-handoff    │
                              │ decisions, evidence,  │
                              │ known issues, veto    │
                              └───────────────────────┘
```

### Skill Reference

| Skill | Purpose |
|---|---|
| [`one-sentence-website`](skills/one-sentence-website/SKILL.md) | **Entry point.** Expands one vague sentence into a premise with explicit assumptions, routes the pipeline, loops build → evidence → repair |
| [`adversarial-quality-loop`](skills/adversarial-quality-loop/SKILL.md) | Real quality loop with separated Planner / Builder / Evaluator / Evidence Auditor roles. Self-critique never counts; degraded solo mode must be declared |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | Thin router: sends a website task to the smallest relevant specialist |
| [`visual-story-direction`](skills/visual-story-direction/SKILL.md) | Visible premise, hierarchy, material direction, and visual critique before effects |
| [`website-motion-intake`](skills/website-motion-intake/SKILL.md) | Existing-project stack, ownership, accepted baseline, and verification route |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | Motion lanes (CSS / Motion / GSAP / canvas / WebGL), scroll behavior, cleanup, reduced-motion fallback |
| [`browser-evidence`](skills/browser-evidence/SKILL.md) | Running-artifact proof: screenshots, browser readback, recordings, verdict vocabulary `pass` / `partial` / `blocked` |
| [`delivery-handoff`](skills/delivery-handoff/SKILL.md) | Bounded delivery: scope, evidence locations, known issues, privacy-safe continuation |

The machine-readable map is [`skills/catalog.json`](skills/catalog.json). Each skill ships its own eval fixture; shared guidance has one canonical copy under [`references/`](references/).

---

## 🚀 Install

Copy the skills into your agent's skill directory (see [Installation](docs/INSTALLATION.md) for details):

```bash
git clone https://github.com/twk0672005/sentence-to-site.git
# Claude Code
cp -r sentence-to-site/skills/* ~/.claude/skills/
# or point your agent at skills/catalog.json
```

Then give your agent one sentence:

> *"a landing page for my coffee cart, warm, not corporate"*

Validate the repository before use or release:

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
```

Optional executable browser evidence requires Playwright; scroll recordings also require FFmpeg. See [`references/tooling.md`](references/tooling.md).

---

## Design Principles

- **One skill, one decision boundary.** A tiny CSS fix does not need seven modules; load one decision-shaped skill at a time.
- **Framework-neutral.** CSS, Motion, GSAP, canvas, and WebGL are lanes to choose, not required dependencies. Static HTML/CSS is a valid and often correct output.
- **Evidence is a capability, not a claim.** Verification vocabulary stays in evidence reports, never in shipped page copy.
- **Clean-room public bundle.** No credentials, client assets, private prompts, or internal runtime configuration — enforced by an automated release-contract scan.

Read [Architecture](docs/ARCHITECTURE.md) before adding modules.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). A new skill must have a distinct trigger, decision boundary, catalog entry, focused eval, and validation result; a differently named duplicate is not a contribution.

## Security

Read [SECURITY.md](SECURITY.md). Do not report credentials or exploit details publicly.

## License

[MIT](LICENSE)
