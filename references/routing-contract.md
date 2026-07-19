# Bounded Routing Contract

## Purpose

Route a website task once. The router selects the smallest honest recipe; it does not act as an autonomous art director, retry engine, or quality loop.

## Make one route record

Before implementation, record:

```text
Base route: new-site | existing-site
Experience lane: static | ui-motion | cinematic-webgl
Delivery gate: prototype | public
Required evidence: <fixed list from the matrix>
Stop condition: <fixed condition from the matrix>
```

Choose exactly one base route, one experience lane, and one delivery gate. Do not reclassify because the agent dislikes its own output. Ask at most one question only when an irreversible detail prevents classification.

## Classification rules

| Signal in the request | Selection |
| --- | --- |
| New idea, blank project, "make me a site" | `new-site` |
| Existing repo, current page, accepted baseline, targeted change | `existing-site` |
| No meaningful movement beyond normal browser behavior | `static` |
| UI transitions, hover, menu, modest scroll behavior | `ui-motion` |
| 3D, canvas, WebGL, cinematic camera, immersive scroll journey | `cinematic-webgl` |
| Experiment, draft, internal demo | `prototype` |
| Public page, client work, campaign, portfolio, conversion-sensitive page | `public` |

An explicit user direction overrides keyword inference. If the request is only a tiny copy or CSS correction, use the smallest relevant specialist instead of this full contract.

## Required evidence and stop conditions

| Route / gate | Required evidence | Stop condition |
| --- | --- | --- |
| `prototype` + `static` or `ui-motion` | Running-page readback and one representative browser view | Evidence exists or is honestly `partial` / `blocked`; then hand off. |
| `public` + `static` or `ui-motion` | Desktop and mobile views, primary flow, console/page-error review | Required evidence is recorded; then hand off. |
| Any `cinematic-webgl` route | Public-page evidence plus representative scroll states or motion recording, reduced-motion check, and runtime/fallback readback | Required motion evidence is recorded; then hand off. |
| Any `existing-site` route | Intake plus the evidence required by its experience lane and delivery gate | The scoped change and evidence are recorded; then hand off. |

A failed **objective** check may receive one scope-preserving repair and one re-check. A second failure is `partial` or `blocked`; do not begin an open-ended repair cycle. Visual preference is not an objective failure: return the evidence and let the user choose whether to start another iteration.

## Specialist selection

- `new-site` → start with `one-sentence-website`; add `visual-story-direction` when the visual premise matters.
- `existing-site` → start with `website-motion-intake`.
- `ui-motion` or `cinematic-webgl` → add `motion-choreography`.
- Any visible claim → add `browser-evidence`.
- Any bounded finish → add `delivery-handoff`.
- `adversarial-quality-loop` is **never automatic**. Use it only when the user explicitly requests an independent review; it returns one report and cannot trigger another build pass by itself.
