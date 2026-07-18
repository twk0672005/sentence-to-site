---
name: one-sentence-website
description: Use when a user gives one sentence, a vague idea, or a loose brief and wants a finished, verified website out of it. Turns "I want something like X" into a shipped site by expanding the idea into a premise, driving the specialist pipeline, and looping build → browser evidence → repair until the result is honest to show.
---

# One-Sentence Website

The entry point of this kit. Input: one sentence. Output: a website that has been seen running in a browser, not just built.

```text
"a personal website for my clothing brand, refined, not a template"
        │
        ▼
 expand → direct → build → prove → repair → hand off
```

## Step 1 — Expand the sentence, don't interrogate the user

A vague sentence is a feature, not a defect. Do not respond with a questionnaire. Expand it yourself into a premise brief:

- **Audience and first impression** — who lands here, what should they feel in the first second.
- **One visible promise** — the single claim the page must make (fast, warm, premium, alive…).
- **Three concrete defaults** — pick a palette, a type direction, and a layout skeleton yourself. State them as decisions ("choosing X because the sentence implies Y"), not questions.
- **Explicit assumptions** — list what you inferred so the user can veto cheaply.

Ask at most **one** question, and only if the sentence is ambiguous about something irreversible (brand name, language, real contact details). Everything else is yours to decide and cheap to change later.

## Step 2 — Route through the specialists

Use the pipeline skills in this kit; skip stages the claim doesn't need:

| Stage | Skill |
| --- | --- |
| premise, hierarchy, anti-generic direction | `visual-story-direction` |
| existing repo or baseline to respect | `website-motion-intake` |
| scroll, UI motion, canvas, reduced motion | `motion-choreography` |
| proof on the running page | `browser-evidence` |
| bounded delivery | `delivery-handoff` |

A greenfield one-pager typically needs direction → build → evidence. An existing site needs intake first. Never skip evidence.

## Step 3 — The quality loop

Build in small visible increments, then loop until the promise holds.

**If you can spawn separate agents, run `adversarial-quality-loop`**: distinct Planner, Builder, Evaluator, and Evidence Auditor roles, so the mind that built the page is never the only mind that grades it. This is the full form of the loop.

**If you cannot** (no subagent tooling, cost limits), declare *solo mode* explicitly and run the same role contracts sequentially yourself:

1. Render the real page in a real browser (see `browser-evidence`).
2. Name the **weakest visible thing** on the screenshot — not the easiest thing to fix.
3. Repair it. Re-render.
4. Stop when a stranger seeing the page would believe the one visible promise from Step 1 — or when the loop stops producing visible improvement (then hand off honestly).

Never present solo self-critique as the adversarial loop. Completion is a browser verdict, never a build exit code.

## Step 4 — Hand back

Deliver with `delivery-handoff`: what the sentence became, the decisions made on the user's behalf, evidence artifacts, known issues, and the cheapest next improvements. The user should be able to veto any inferred decision in one line — which restarts the loop, not the project.

## Boundaries

- This skill decides and orchestrates; it does not replace the specialist skills' guidance.
- No fabricated evidence: a claim without a rendered artifact is reported as `partial` or `blocked`.
- Stay framework-neutral: static HTML/CSS is a valid and often correct lane for a one-sentence site.
