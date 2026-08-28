# Afuu Website + Animation Workflow Kit

🌐 **Language / 語言:** [繁體中文](README.md) · **English**

[![Version](https://img.shields.io/badge/version-v1.4.0-1f6feb.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-d4a72c.svg)](LICENSE)
[![Workflows](https://img.shields.io/badge/workflows-website%20%2B%20animation-8b5cf6.svg)](#whats-included)
[![Playwright](https://img.shields.io/badge/browser%20QA-Playwright%201.62.0-2eAD33.svg)](requirements.txt)
[![Validate Release](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-release.yml/badge.svg)](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-release.yml)

> Turn a one-sentence website request into a responsive, product-specific result
> that preserves real behavior and can be verified with browser evidence.

**v1.4.0 — Truthful Evidence Core** is a website and motion decision workflow for
coding agents and human developers, accompanied by a set of fail-closed browser
QA utilities. It addresses the most common failures in AI-generated websites:
template-like visuals, purposeless animation, mobile layouts that merely shrink
desktop, attractive screenshots hiding broken behavior, and build success being
reported as product completion.

This repository is **not** a component library, starter app, Agent Skill
collection, MCP installer, or deployment authorization. It provides a method
that can be applied to an existing stack: understand the product before
designing, preserve behavior before rebuilding the surface, and report only what
the evidence can genuinely prove.

---

## Why use this

- **Remove the generic AI look:** derive the visual language from the product's
  content, instruments, data shapes, and cultural context—not from a generic
  hero, gradient, or card grid.
- **Preserve working behavior:** write a
  `PRESERVE / EVOLVE / RETIRE / DECISION` preservation map before a redesign.
- **Scale the process to the task:** use Tiny for a local fix, Normal for one
  page, and Serious or Redesign only for public, high-risk, or substantial work.
- **Require motion to earn its place:** animation must provide feedback,
  orientation, continuity, hierarchy, progress, or emphasis. Do not escalate to
  WebGL when CSS is sufficient.
- **Recompose mobile intentionally:** reconsider priority, order, density, crop,
  controls, and resource budgets instead of shrinking desktop.
- **Verify with real evidence:** test route identity, desktop and mobile,
  interactions, keyboard use, console errors, overflow, reduced motion, and
  temporal behavior as separate claims.

## What's included

| Capability | What it does | Entry |
|---|---|---|
| Website Workflow | New sites, existing sites, and redesigns: product truth, design lock, responsive behavior, and review | [website-workflow.md](workflows/website-workflow.md) |
| Animation Workflow | Micro motion, UI choreography, scroll stories, and cinematic WebGL | [animation-workflow.md](workflows/animation-workflow.md) |
| Evidence Gate | The single authority for evidence coverage, statuses, and terminal verdicts | [evidence-gate.md](workflows/evidence-gate.md) |
| Browser Verifier | Desktop, mobile, narrow viewport, focus, overflow, console, and reduced-motion checks | [verify_browser_artifact.py](scripts/verify_browser_artifact.py) |
| Motion Recorder | WebM, start/mid/settled states, contact sheet, and optional MP4 | [record_browser_scroll.py](scripts/record_browser_scroll.py) |
| Skill Routing | Add design, Three.js, browser, and source-verification capabilities only when needed | [mcp-and-skills-install.md](workflows/mcp-and-skills-install.md) |
| Release Validator | Exact files, links, versions, secret scanning, deterministic ZIP, and SHA-256 | [validate-release.py](.github/scripts/validate-release.py) |

## Core workflow

```text
result lock
  -> product truth + protected baseline
  -> smallest useful lane
  -> product-specific design lock
  -> one complete static slice
  -> responsive recomposition
  -> motion only when it earns a job
  -> real browser / temporal evidence
  -> independent review when scope requires it
  -> one bounded repair
  -> PASS / PARTIAL / FAIL / WAITING_FOR_NOVA
```

### Work depth

| Depth | Use when | Minimum route |
|---|---|---|
| Tiny | One objective local correction | Affected state plus the narrowest relevant verification |
| Normal | One visible page or component | Compact contract plus wide and narrow renders |
| Serious | Public, multi-page, reference-led, or trust-sensitive work | Baseline, full contract, and independent review |
| Redesign | A substantial change to an existing product | Serious plus a preservation map and baseline comparison |

### Experience lane

```text
static
├─ semantic content, layout, states, and responsive composition
ui-motion
├─ micro feedback
├─ choreographed UI
└─ scroll story
cinematic-webgl
└─ camera, depth, or explorable space is essential to the result
```

“Premium” is not a reason to use Three.js. Enter the cinematic WebGL lane only
when camera, depth, space, or spatial interaction carries an essential part of
the product result.

---

## Getting started

### 1. Website work

For an everyday website task, read only:

1. this `README.en.md`;
2. the [Website Workflow](workflows/website-workflow.md).

Minimal instruction for a coding agent:

```text
Use this workflow kit as reference only. Preserve the target project's own
instructions, product truth, stack and accepted behavior. Choose the smallest
useful work depth, complete one visible slice, verify the real artifact, and
report only what fresh evidence supports.
```

### 2. Animation or WebGL work

Read the [Animation Workflow](workflows/animation-workflow.md) only when motion
is part of the promised result. For Three.js work, inspect the host project's
package and lockfile first, then follow the official
[mrdoob/three.js](https://github.com/mrdoob/three.js) source, manual, API docs,
and examples that match the exact installed version.

### 3. Working with `design-taste-frontend`

When `design-taste-frontend` is available in the agent environment:

- an ordinary request to build, modify, or redesign a website can automatically
  invoke it for product-specific art direction and visual judgement;
- this kit owns scope, preservation, implementation sequence, evidence, and the
  terminal verdict;
- the animation workflow joins only when motion has a real job;
- a Tiny correction is never forced through a full Serious or Redesign process.

This repository remains a reference kit. It does not silently install a Skill,
override another project's instructions, or deploy anything automatically.

---

## Browser QA

The browser utilities use pinned `playwright==1.62.0`. Install Chromium
separately. FFmpeg is needed only when MP4 is explicitly required.

### POSIX

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

ARTIFACT_ROOT=/path/to/dist \
TITLE_CONTAINS="Product" \
python3 scripts/verify_browser_artifact.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium

$env:ARTIFACT_ROOT = "C:\path\to\dist"
$env:TITLE_CONTAINS = "Product"
.\.venv\Scripts\python.exe -B scripts\verify_browser_artifact.py
```

Provide at least one identity marker: `TITLE_CONTAINS`, `H1_CONTAINS`, or
`BODY_CONTAINS`. A static root containing `.env`, a private key, `.git`, or a
symlink fails closed. External URLs are rejected by default to avoid verifying
an old server or the wrong website.

### Motion evidence

```bash
ARTIFACT_ROOT=/path/to/dist \
H1_CONTAINS="Product" \
MOTION_DURATION_SECONDS=8 \
python3 scripts/record_browser_scroll.py
```

The recorder produces WebM, three distinct start/mid/settled states, and a
contact sheet. To make MP4 a hard gate, set `REQUIRE_MP4=1` and provide
`ffmpeg` and `ffprobe`.

---

## Evidence model

[evidence-gate.md](workflows/evidence-gate.md) is the single authority for
evidence types, coverage, statuses, and terminal verdicts.

| Evidence | Can prove | Cannot prove alone |
|---|---|---|
| Build exit 0 | The source or build command completed | Real runtime behavior, appearance, or journey |
| HTTP 200 | An endpoint responded | That it served the correct website |
| Screenshot | Pixels at one viewport, state, and moment | Interaction, motion, or accessibility |
| Video/WebM | Temporal behavior during the recorded interval | Cleanup, offscreen lifecycle, or every state |
| Agent report | The agent claims completion | Implementation or product PASS |

Store raw screenshots, video, HTML, JSON, and traces on disk. In the
conversation, return paths, hashes, viewport and state, key metrics, and the
verdict instead of transporting large evidence payloads through the session.

---

## Repository validation

```bash
python3 .github/scripts/validate-release.py
python3 -m unittest discover -s tests
python3 .github/scripts/run-browser-smoke.py
```

Validation covers:

- exact repository and distribution allowlists;
- strict UTF-8, relative links, language/version parity;
- secret, credential, private-path, sensitive-filename, and symlink checks;
- Python compilation;
- positive browser verifier and motion-recorder smoke tests;
- a wrong-site marker negative test;
- deterministic ZIP generation, SHA-256, and ZIP byte parity.

## Repository map

```text
kit-manifest.json       version + exact distribution authority
workflows/              website, animation, evidence, and optional references
scripts/                fail-closed browser QA utilities
checklists/             proportional intake, preflight, and delivery reminders
included-skills/        optional capability index + source provenance only
prompts/                visual-reference extraction prompt
docs/                   setup, usage, troubleshooting, maintenance, and history
tests/                  deterministic unit tests + browser fixture
.github/                CI, release validation, issue, and PR templates
```

## Source and safety boundaries

- The target project's latest instructions, product truth, and accepted
  baseline always take precedence.
- The kit contains no credentials, identity, memory, cron, service, or client
  material.
- It does not automatically install, sign in, upload, pay, push, deploy, or
  publish.
- Reference and generated assets require provenance and usage rights.
- Audit the source, immutable version, license, scripts or hooks, permissions,
  and rollback path before using an optional Skill, plugin, or MCP.
- `kit-manifest.json` is the machine authority for the version, distribution
  file list, and repository-only contract.

## Contributing and support

- For usage questions or bugs, open a
  [GitHub issue](https://github.com/twk0672005/sentence-to-site/issues).
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before making changes.
- Follow the private reporting route in [SECURITY.md](SECURITY.md) for security
  issues.
- See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

This project is available under the [MIT License](LICENSE).
