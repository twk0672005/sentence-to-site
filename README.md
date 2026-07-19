<div align="center">

# ✨ sentence-to-site · Agent Skill Library

**One sentence in. A verified website out — and it knows when to stop.**

Fills in your requirements instead of asking 20 questions · Picks one bounded route before building · No cookie-cutter AI-looking pages · Motion is planned, not sprinkled on · Only "done" after real-browser screenshot checks

*Vibe coding runs on feel; software engineering runs on discipline. This kit makes the route, evidence, and stop condition explicit — one sentence, even from someone who has never written code, becomes a bounded website task that can be verified honestly.*

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
| Quietly keeps retrying because it wants the page to look better | ❌ open-ended loop | ✅ one explicit route, fixed evidence, and a stop condition |
| Motion added as decoration, breaks on mobile | ❌ ad-hoc | ✅ choreography lanes + reduced-motion fallback |
| Handoff with no record of assumptions | ❌ silent | ✅ every inferred decision listed and veto-able in one line |

The core rule everywhere: **completion is a browser verdict, never a build exit code.**

You have a vague idea — *"a personal website for my clothing brand, refined, not a template"*. An AI agent loaded with this kit turns that sentence into a bounded website task: it expands the idea into a design premise, records one route, makes the small decisions on your behalf (and tells you which ones), builds the page, **looks at it in a real browser**, collects the evidence that route requires, and hands it back at a fixed stop condition. A new visual iteration starts only when the user chooses one.

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
                                                              ▼
                              ┌───────────────────────┐
                              │   delivery-handoff    │
                              │ route, evidence,      │
                              │ known issues, choices │
                              └───────────────────────┘

```

Optional only after an explicit user request: `adversarial-quality-loop` returns one independent review report; it cannot start another build pass.

### Skill Reference

| Skill | Purpose |
|---|---|
| [`one-sentence-website`](skills/one-sentence-website/SKILL.md) | **Entry point.** Expands one vague sentence into a premise, selects one bounded route, collects route-specific evidence, and hands off |
| [`adversarial-quality-loop`](skills/adversarial-quality-loop/SKILL.md) | Explicit-only, one-time independent review. Returns a finite report and cannot automatically start another build pass |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | Thin router: selects the smallest bounded route and relevant specialist |
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
# Claude Code — copy the skill folders AND the shared references they link to
cp -r sentence-to-site/skills/*/ ~/.claude/skills/
cp -r sentence-to-site/references ~/.claude/
# or point your agent at skills/catalog.json inside the cloned bundle
```

> Windows: use `python` instead of `python3` in the commands below. For the optional browser-evidence scripts, also run `pip install -r requirements.txt && playwright install chromium` once.

Then give your agent one sentence:

> *"a personal website for my clothing brand, refined, not a template"*

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
- **Route once, then stop.** Each non-trivial task selects one base route, one experience lane, and one delivery gate. Evidence closes the selected route; it does not authorize autonomous taste loops.
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
