# High-End Public Website Review Scorecard

## Purpose and trigger

Use this scorecard only when the route is explicitly `public` and the user asks for a high-end, flagship, flawless, award-grade, client-ready, or publish-ready result. Ordinary corrections and prototypes do not load it.

This is one rigorous independent review, not an autonomous taste loop. Build the
strongest scoped candidate first, complete the required coverage in
[evidence-gate.md](evidence-gate.md), then give the locked contract, baseline,
candidate and fresh evidence to an evaluator who is not the builder. Score once,
repair the single highest-impact defect at most once, re-check affected evidence,
then stop and ask whether the intended effect has been reached.

## Evidence required before scoring

Do not score from source code, a build exit code, HTTP 200, or one hero screenshot. Use the current artifact and collect what the route actually claims:

- desktop and mobile first viewport plus the important content/CTA region;
- primary navigation, CTA, form, menu, and error/loading states when present;
- console, page-error, failed-request, overflow, and broken-asset readback;
- keyboard/focus and relevant reduced-motion behavior;
- representative start/mid/settled states or a 6–12 second recording for motion;
- for an explorable 3D scene: front, side, back, high/low or equivalent orbit viewpoints, pointer and touch behavior, loading/fallback, WebGL errors, and mobile quality tier;
- comparison with the locked verbal brief, image reference, mixed brief, or strongest accepted baseline.

A verbal brief is a complete input. Do not invent fidelity to a reference that does not exist; judge coherence against the locked scene and visual premise.

## Hard blockers

Any item below blocks a `public-ready` claim regardless of total score:

1. The first viewport, main message, visual protagonist, or primary action contradicts the locked brief.
2. The primary flow is broken; there is a blocking runtime/console error, failed critical request, loading trap, missing asset, or misleading state.
3. Mobile has clipped content, horizontal overflow, unusable controls, unreadable hierarchy, or a materially weaker first impression without a deliberate alternative.
4. Keyboard focus is missing/obscured, essential contrast or legibility fails, motion essential to meaning has no suitable reduced-motion alternative, or autoplaying movement cannot be controlled where required.
5. A claimed explorable 3D scene reveals holes, fake flat backs, broken occlusion, unstable camera/orbit controls, unusable touch interaction, WebGL failure without fallback, or an unplanned low-end collapse.
6. Assets, generated material, data, attribution, rights, secrets, or public claims are unsafe, unverifiable, or not cleared for the intended use.
7. Public deployment, payment, account creation, external upload, or publishing would be required but has not been approved.

## 100-point rubric

Score every subcriterion from 0 to its stated maximum. Every deduction must name visible evidence, not taste adjectives.

### A. Design and art direction — 40

| Subcriterion | Max | High score means |
|---|---:|---|
| Visual premise and brand distinctiveness | 10 | A specific visual idea is understandable within five seconds; it does not resemble a generic template or effects demo. |
| Composition and hierarchy | 10 | Scale, spacing, rhythm, focal order, density, and negative space direct attention deliberately across desktop and mobile. |
| Typography | 8 | Typeface role, size, line length, leading, weight, contrast, and optical alignment feel authored and remain readable. |
| Colour, material, imagery and lighting | 8 | Palette and materials support the premise; images, 3D surfaces, light, shadow, texture, and generated assets feel coherent rather than pasted together. |
| Finish and consistency | 4 | Edges, radii, icons, alignment, transitions, crops, empty states, and micro-details survive close inspection. |

### B. UX and interface quality — 30

| Subcriterion | Max | High score means |
|---|---:|---|
| Five-second clarity and navigation | 8 | Users understand what this is, why it matters, where they are, and what to do next. |
| Interaction feedback, control and recovery | 7 | States are visible and predictable; users can enter, exit, pause, reset, recover, and avoid mistakes without guessing. |
| Responsive and input adaptation | 7 | Layout and controls are designed for desktop, mobile, pointer, touch, keyboard, resize, and re-entry rather than merely scaled down. |
| Accessibility and signal-to-noise | 5 | Focus, contrast, semantics, reflow, target size, readable text, and intentional motion preserve use; decorative complexity never buries meaning. |
| Primary flow and conversion confidence | 3 | The CTA or main task is trustworthy, friction is proportionate, and no visual spectacle weakens completion. |

### C. Creativity and motion/spatial storytelling — 20

| Subcriterion | Max | High score means |
|---|---:|---|
| Concept originality and relevance | 8 | The idea is memorable because it belongs to this content/brand, not because a fashionable library was added. |
| Motion, scroll or camera causality | 7 | Movement establishes mood, advances story, represents state, guides attention, or adds credibility; start, hold, turn, and settle have purpose. |
| Signature moment and restraint | 5 | One or two authored moments are memorable; secondary motion, sound, particles, bloom, shaders, and 3D are restrained when they do not help. Static restraint may score fully when it is the stronger creative decision. |

### D. Content and credibility — 10

| Subcriterion | Max | High score means |
|---|---:|---|
| Message, proof and voice | 5 | Copy is specific, credible, well ordered, and aligned with the visible promise; proof appears where doubt occurs. |
| Content/asset integrity | 3 | Names, links, data, labels, alt text, crops, captions, generated assets, and states are correct and internally consistent. |
| Provenance and public honesty | 2 | Rights, credits, generated material, claims, privacy, and public-facing statements are honest and suitable for release. |

## Score anchors

Use the same standard within each subcriterion:

- **90–100% of max:** distinctive, deliberate, evidence-backed, no material weakness;
- **75–89%:** strong and publishable, with a visible but non-blocking weakness;
- **60–74%:** competent but generic, uneven, or under-resolved;
- **40–59%:** obvious quality problem that weakens the intended effect;
- **0–39%:** absent, broken, contradictory, or misleading.

## Verdict thresholds

- **93–100:** exceptional / award-calibre candidate;
- **88–92:** high-end public candidate;
- **80–87:** strong, but not yet high-end;
- **below 80:** not public-ready.

A `public-ready` candidate requires all of the following:

- total score at least 88;
- Design at least 34/40;
- UX/UI at least 25/30;
- no hard blocker;
- fresh route-specific evidence;
- a reviewer who is independent of the builder;
- final user confirmation that the intended effect has been reached.

An explicit “flawless”, “no-compromise”, or equivalent request sets a **flagship target of 92+**. The score is a disciplined diagnostic, not permission for the agent to approve its own taste or publish the work.

## Technical readiness gate

Technical readiness is a hard gate, not bonus points that can be offset by visual quality:

- use real runtime and browser evidence;
- where meaningful measurement is available, aim for Core Web Vitals good thresholds: LCP no more than 2.5s, INP no more than 200ms, and CLS no more than 0.1 at the 75th percentile, segmented by mobile and desktop;
- do not claim field-percentile performance from a local lab run; label lab evidence honestly;
- verify loading, fallback, resize, cleanup, failed requests, console/WebGL errors, responsive behavior, and weak-device quality tier as required by the route;
- for heavy 3D, inspect geometry/material memory, draw calls, texture/model payload, interaction latency, and sustained motion rather than quoting one warm-frame FPS.

## Cinematic/WebGL scoring overlay

Use the same 100 points; do not create a second score that hides defects.

- **Design:** inspect silhouette, depth, material/light cause, texture scale, scene completeness, and all claimed viewpoints. For an image reference, score fidelity to visible invariants; for a verbal brief, score coherence to the locked world.
- **UX:** inspect orbit/reset constraints, pointer/touch parity, camera comfort, loading/fallback, control discoverability, and whether the page remains usable without WebGL.
- **Creativity:** score spatial storytelling, camera motivation, causality, timing, and restraint—not shader count, particle count, or library count.
- **Content:** check labels, scene claims, generated asset consistency, credits, and whether the experience communicates more than a technical demo.

ThreeUI is optional. Use it only when a verified Community component directly supports the locked scene or interface. ImageGen is optional and gap-driven; generated imagery cannot silently redefine the brief.

## The one-review protocol

1. Freeze the route, visual/scene lock, technical lock, baseline, candidate and
   evidence set.
2. Collect fresh browser evidence and clear any hard blocker required for honest scoring.
3. A fresh evaluator, not the builder, scores all applicable rows once. Record
   the total, four pillar scores, evidence, and exact deductions.
4. Select the single highest-impact repair: the defect with the strongest combination of visibility, route importance, and weighted score loss.
5. Make at most one same-route polish pass. Do not add an unrelated feature, framework, dependency, evaluator, or effect.
6. Re-run only the affected evidence plus regression checks. Update only the affected rubric rows and final total.
7. Stop. Ask whether the intended effect has been reached.
8. If the user says no, derive up to four choices from the actual lowest-scoring dimensions—for example composition/fidelity, atmosphere/material/light, motion/camera, or content/mobile/interaction. Ask for the missing detail and start a new iteration only after the user selects or describes it.

Never review the review. Never run a private second taste pass under another
name. If independence is unavailable, report PARTIAL rather than self-awarding a
public-ready label.

## Review output

```text
High-end review: <final score>/100 — <verdict>
Design: <x>/40 | UX/UI: <x>/30 | Creativity: <x>/20 | Content: <x>/10
Hard blockers: none | <exact blocker>
Strongest qualities: <2 evidence-backed points>
Largest deduction: <one visible issue and evidence>
One repair made: <visible change>
Re-check: <fresh evidence and affected score change>
User effect check: pending
```

The 100-point score is a high-end diagnostic label, not a second terminal status.
Final workflow state still uses PASS／PARTIAL／FAIL／WAITING_FOR_NOVA from
[evidence-gate.md](evidence-gate.md).

## Research basis

Accessed 2026-08-26:

- [Awwwards Evaluation System](https://www.awwwards.com/about-evaluation/) — official 40% Design, 30% Usability, 20% Creativity, 10% Content weighting.
- [CSS Design Awards: About](https://www.cssdesignawards.com/about) — official UI, UX, and Innovation award categories; WOTD consideration uses an average judge score above 8.0, subject to submission quality.
- [Nielsen Norman Group: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) — system status, user control, consistency, error prevention, recognition over recall, and aesthetic/minimalist design.
- [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) — contrast, reflow, visible/unobscured focus, pointer target size, motion control, and pause/stop requirements.
- [web.dev: Web Vitals](https://web.dev/articles/vitals) — current Core Web Vitals definitions and good thresholds for LCP, INP, and CLS.
