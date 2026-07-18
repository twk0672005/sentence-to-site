# sentence-to-site

**One sentence in. A verified website out.**

You have a vague idea — *"a landing page for my coffee cart, warm, not corporate"*. An AI agent loaded with this kit turns that sentence into a finished website: it expands the idea into a design premise, makes the small decisions on your behalf (and tells you which ones, so you can veto them in one line), builds the page, **looks at it in a real browser**, repairs the weakest visible thing, and repeats until the result is honest to show.

This is a **skill library for AI agents** (Claude Code, Codex, and any agent that reads `SKILL.md` files) — not a website builder app, not a giant prompt, not a framework. It encodes the workflow: how to expand a vague sentence without interrogating the user, how to choose a visual direction that isn't generic, how to choreograph motion responsibly, and how to prove — with screenshots and browser readback, never with a build exit code — that the site actually works.

```text
one vague sentence
→ premise + explicit assumptions   (decisions, not a questionnaire)
→ visual direction                 (anti-generic, one visible promise)
→ build + motion                   (framework-neutral: CSS is a valid lane)
→ browser evidence                 (real render, honest verdict)
→ weakest-issue repair loop
→ bounded handoff                  (what was decided for you, and how to veto it)
```

## The skills

The flagship skill is the entry point; the rest are its pipeline. Load one decision-shaped skill at a time — a tiny CSS fix does not need seven modules.

| Skill | Use it for |
| --- | --- |
| [`one-sentence-website`](skills/one-sentence-website/SKILL.md) | **the entry point** — turn one vague sentence into a shipped, verified site |
| [`adversarial-quality-loop`](skills/adversarial-quality-loop/SKILL.md) | a real quality loop — separated Planner / Builder / Evaluator / Evidence Auditor roles, not self-critique |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | route a website task to the right specialist below |
| [`visual-story-direction`](skills/visual-story-direction/SKILL.md) | premise, hierarchy, material direction, and visual critique |
| [`website-motion-intake`](skills/website-motion-intake/SKILL.md) | existing-project stack, ownership, baseline, and verification discovery |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | UI, scroll, canvas, WebGL, mobile, and reduced-motion behavior |
| [`browser-evidence`](skills/browser-evidence/SKILL.md) | screenshots, browser readback, recordings, and honest verdicts |
| [`delivery-handoff`](skills/delivery-handoff/SKILL.md) | bounded delivery, known issues, and privacy-safe continuation |

The machine-readable map is [`skills/catalog.json`](skills/catalog.json). Each skill has its own evaluation fixture; shared guidance has one canonical copy under [`references/`](references/).

## Why this exists

Agents are already good at generating web code. What they get wrong is everything around the code:

- They answer a vague idea with a questionnaire instead of a decision.
- They produce the same generic gradient-and-glass page for every prompt.
- They claim "done" because the build passed, without ever rendering the page.
- They hand off with no record of what was assumed on the user's behalf.

Each skill in this kit is a countermeasure to one of those failure modes. The core rule everywhere: **completion is a browser verdict, never a build exit code.**

## Install and validate

See [Installation](docs/INSTALLATION.md) for bundle-first installation into your agent's skill directory. Validate the repository before use or release:

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
python3 -m py_compile scripts/*.py
```

Optional executable browser evidence requires Playwright; scroll recordings also require FFmpeg. See [`references/tooling.md`](references/tooling.md).

## Structure and boundaries

Read [Architecture](docs/ARCHITECTURE.md) before adding modules. The kit is deliberately framework-neutral: CSS, a UI motion library, GSAP, canvas, and WebGL are lanes to choose when appropriate, not required dependencies. Static HTML/CSS is a valid and often correct output for a one-sentence site.

The public bundle contains no credentials, client assets, internal runtime configuration, private prompts, or bundled third-party skills. It is a clean-room equivalent core, not a copy of any private operating manual.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). A new skill must have a distinct trigger, decision boundary, catalog entry, focused eval, and validation result; a differently named duplicate is not a contribution.

## Security

Read [SECURITY.md](SECURITY.md). Do not report credentials or exploit details publicly.

## License

[MIT](LICENSE)
