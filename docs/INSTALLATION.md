# Installation

## Use the complete bundle

Clone or download a tagged release, then keep the repository together. Specialist skills link to shared references and executable tools in the bundle.

```bash
git clone <repository-url> sentence-to-site
cd sentence-to-site
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
```

Install the `skills/` directories into your agent host's skill location using that host's documented method. Skills link to shared guidance via `../../references/…`, so `references/` must land two levels above each installed skill folder (for Claude Code: `~/.claude/references/` next to `~/.claude/skills/`):

```bash
cp -r skills/*/ ~/.claude/skills/
cp -r references ~/.claude/
```

Keep `templates/` and `scripts/` in the cloned bundle and run them from there. On Windows, replace `python3` with `python`.

## Selective use

The smallest useful entry points are:

| Need | Skill |
| --- | --- |
| Choose the right module for a website-motion task | `cinematic-web-motion` |
| Create a visible premise and hierarchy | `visual-story-direction` |
| Work safely in an existing project | `website-motion-intake` |
| Build scroll, UI, canvas, or WebGL motion | `motion-choreography` |
| Prove the running result | `browser-evidence` |
| Hand work to another person or release a result | `delivery-handoff` |

## Optional browser tooling

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

`record_browser_scroll.py` also requires FFmpeg. If a required runtime is unavailable, report `partial` or `blocked`; do not replace browser evidence with a build result.

## Update discipline

Pin a release tag or commit for repeatable behavior. Before upgrading, read `CHANGELOG.md`, run the package validator, and keep the previous accepted version as rollback until the new one has been used successfully.
