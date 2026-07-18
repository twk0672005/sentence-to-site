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
