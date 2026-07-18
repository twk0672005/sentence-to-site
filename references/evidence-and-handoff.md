# Evidence and handoff

Evidence should match the claim. It is not a ritual and it is not a substitute for looking at the artifact.

## Minimum evidence

| Claim | Minimum evidence |
| --- | --- |
| small local correction | focused readback or relevant build/test |
| visible page | running-page readback, key desktop view, one visual critique |
| responsive or interactive change | desktop + mobile, primary flow, serious console/page errors |
| motion, scroll, WebGL, or canvas | representative states, short clip or multi-state frames, reduced-motion/fallback check |
| handoff/archive | README, run/verify steps, evidence locations, known issues, next recommendation |

A build, HTTP 200, or one screenshot does not prove motion, responsiveness, interaction, or visual quality.

## Verdicts

- **pass** — fresh evidence covers the promised scope and no blocking problem remains.
- **partial** — a usable result exists, but a relevant evidence layer, viewport, interaction, fallback, or quality concern is missing. Say what is missing.
- **blocked** — a needed runtime, dependency, permission, data source, or browser capability is unavailable. Say what is blocking it.
- **next batch** — this scope is complete; further polish is a separate request, not a hidden unfinished task.

## Public UI vs internal evidence

Verification language belongs in evidence artifacts, never in the shipped page. Words like *mock*, *browser tested*, *readback*, *console clean*, *verification*, *bundle*, engine or tooling names, and QA status counters are internal vocabulary. If any of them appear in public-facing UI copy, move them to the evidence report or the handoff bundle. The visitor sees the product's own story; the reviewer sees the proof — two different documents.

## WebGL and canvas readback

A screenshot of a canvas can be a frozen or black frame. For WebGL/canvas claims, also read state back from the running page and store it as JSON alongside the screenshots. Useful fields:

```json
{
  "webglOk": true,
  "renderer": "reported renderer string",
  "progress": 0.62,
  "currentScene": "identifier of the active beat/scene",
  "keyElementsVisible": true,
  "forbiddenElementsAbsent": true
}
```

`keyElementsVisible` / `forbiddenElementsAbsent` are per-project: encode the scene's own red lines (e.g. "no leftover debug HUD", "no placeholder cards", "no default selector UI") as booleans the page itself reports, so the Auditor checks facts instead of squinting.

## Motion-specific review

Check the beginning, a meaningful middle state, and the end state. A recorded file is not enough: it must not be black, frozen, unsynchronized with page state, or hiding important copy. Mobile motion should be designed as its own smaller story when desktop choreography is too dense.

## Handoff bundle

Give the next person:

```text
Goal:
Accepted baseline:
What changed:
How to run:
How to verify:
Evidence location:
Known issues:
Recommended next step:
```

Do not include credentials, environment files, private caches, dependency directories, or unrelated personal material.
