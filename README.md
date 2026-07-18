# Cinematic Web Motion Workflow Kit

A clean-room, framework-neutral **skill library** for agents and teams building browser-rendered websites where visual direction, motion, evidence, and handoff need to be as intentional as the code.

This is not a giant prompt, a starter app, an AI-video pipeline, or a multi-agent framework. It is a small, composable bundle: choose one decision-shaped skill, load shared guidance only when needed, and prove visible claims on the running artifact.

## Skill map

| Skill | Use it for |
| --- | --- |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | route a website-motion task to the right specialist |
| [`visual-story-direction`](skills/visual-story-direction/SKILL.md) | premise, hierarchy, material direction, and visual critique |
| [`website-motion-intake`](skills/website-motion-intake/SKILL.md) | existing-project stack, ownership, baseline, and verification discovery |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | UI, scroll, canvas, WebGL, mobile, and reduced-motion behavior |
| [`browser-evidence`](skills/browser-evidence/SKILL.md) | screenshots, browser readback, recordings, and honest verdicts |
| [`delivery-handoff`](skills/delivery-handoff/SKILL.md) | bounded delivery, known issues, and privacy-safe continuation |

The machine-readable map is [`skills/catalog.json`](skills/catalog.json). Each module has its own evaluation fixture; shared guidance has one canonical copy under [`references/`](references/).

## The operating loop

```text
visible premise
→ accepted baseline + project intake
→ one useful visible change
→ browser evidence
→ weakest-issue repair
→ bounded handoff
```

Scale that loop to the task. A tiny CSS correction does not need six modules. A public, responsive, scroll-led experience should not claim completion from a successful build or one hero screenshot.

## Install and validate

See [Installation](docs/INSTALLATION.md) for bundle-first installation. Validate the repository before use or release:

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
python3 -m py_compile scripts/*.py
```

Optional executable browser evidence requires Playwright; scroll recordings also require FFmpeg. See [`references/tooling.md`](references/tooling.md).

## Structure and boundaries

Read [Architecture](docs/ARCHITECTURE.md) before adding modules. The kit is deliberately framework-neutral: CSS, a UI motion library, GSAP, canvas, and WebGL are lanes to choose when appropriate, not required dependencies.

The public bundle contains no credentials, client assets, internal runtime configuration, private prompts, or bundled third-party skills. It is a clean-room equivalent core, not a copy of any private operating manual.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). A new skill must have a distinct trigger, decision boundary, catalog entry, focused eval, and validation result; a differently named duplicate is not a contribution.

## Security

Read [SECURITY.md](SECURITY.md). Do not report credentials or exploit details publicly.

## License

[MIT](LICENSE)
