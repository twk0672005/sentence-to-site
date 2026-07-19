---
name: one-sentence-website
description: Use when a user gives one sentence, a vague idea, or a loose brief and wants a finished website route. Turns "I want something like X" into an explicit bounded route, a verified artifact, and an honest handoff without autonomous review loops.
---

# One-Sentence Website

The entry point of this kit. Input: one sentence. Output: one explicit route and a website that has been seen running in a browser, not just built.

```text
"a landing page for my coffee cart, warm, not corporate"
        │
        ▼
expand → route once → build → prove → hand off
```

## Step 1 — Expand the sentence, don't interrogate the user

A vague sentence is a feature, not a defect. Do not respond with a questionnaire. Expand it yourself into a premise brief:

- **Audience and first impression** — who lands here, what should they feel in the first second.
- **One visible promise** — the single claim the page must make (fast, warm, premium, alive…).
- **Three concrete defaults** — pick a palette, a type direction, and a layout skeleton yourself. State them as decisions ("choosing X because the sentence implies Y"), not questions.
- **Explicit assumptions** — list what you inferred so the user can veto cheaply.

Ask at most **one** question, and only if the sentence is ambiguous about something irreversible (brand name, language, real contact details). Everything else is yours to decide and cheap to change later.

## Step 2 — Route once

Read [`../../references/routing-contract.md`](../../references/routing-contract.md), then make exactly one route record:

```text
Base route: new-site | existing-site
Experience lane: static | ui-motion | cinematic-webgl
Delivery gate: prototype | public
Required evidence: <fixed list>
Stop condition: <fixed condition>
```

Do not change this route because the agent dislikes its own work. A greenfield one-pager normally starts with `visual-story-direction`; an existing site starts with `website-motion-intake`; `ui-motion` and `cinematic-webgl` add `motion-choreography`; every visible claim adds `browser-evidence`.

Use only the specialists the record needs. A small copy correction does not need this full entry route.

## Step 3 — Build and pass the evidence gate

Build the scoped artifact, then collect only the evidence required by the route record. Evidence can establish that the running page, flow, fallback, and claimed motion exist; it does not give an agent permission to keep polishing taste indefinitely.

If an **objective** required check fails, make one scope-preserving repair and repeat that same check once. If it still fails, report `partial` or `blocked` and hand off honestly. Do not enter an open-ended build → review → repair cycle.

`adversarial-quality-loop` is never automatic. It runs only after an explicit user request for an independent review, and its report cannot trigger another build pass by itself.

## Step 4 — Hand back

Deliver with `delivery-handoff`: the route selected, what the sentence became, decisions made on the user's behalf, evidence artifacts, known issues, and the cheapest next improvements. The user chooses whether a new scoped iteration begins.

## Boundaries

- This skill decides and orchestrates; it does not replace specialist guidance.
- No fabricated evidence: a claim without a rendered artifact is `partial` or `blocked`.
- Stay framework-neutral: static HTML/CSS is a valid and often correct lane for a one-sentence site.
- Completion is a route-specific evidence verdict, never a build exit code or an agent's private aesthetic judgement.
