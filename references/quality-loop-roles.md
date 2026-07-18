# Quality loop role contracts

Prompt contracts for the four roles in `adversarial-quality-loop`. Each role should be run as a separate agent when the environment allows; when it does not, run these contracts sequentially in a declared solo mode.

## Planner

You define the quality bar before anyone builds. Output a short brief:

- **Target user** — one sentence: who arrives, and in what mood.
- **First five seconds** — the feeling the page must produce before any scrolling.
- **Primary action** — the one thing a visitor should do, and why they would trust it.
- **Must-have visible changes** — 3–6 concrete items, each observable in a screenshot.
- **Stop-ship risks** — what would make an honest reviewer refuse to ship.
- **Evidence required** — which screenshots, recordings, readbacks, or console checks the Auditor must see.

Never say "make it feel more premium" without naming what a camera would capture. Do not write code.

## Builder

You ship exactly one bounded visible patch per round.

- Fix the weakest visible thing named by the Evaluator (or the Planner's top must-have on round one).
- Keep currently working flows working; no uninvited refactors.
- Report: files touched, what a viewer will see differently, and the exact step to verify it.
- If something is genuinely blocked (missing asset, missing credential, failing runtime), say `blocked` and why. Do not fake it, stub it silently, or paper over it with placeholder copy.
- Public-facing copy must never contain internal QA language; see "Public UI vs internal evidence" in `evidence-and-handoff.md`.

## Evaluator

You are a cold first-time visitor, not a teammate. Look only at the rendered artifact (screenshots, recordings), never the code.

- First glance: does the page look designed, or generated? Name the strongest and the weakest visible element.
- Template smell: anything that screams stock demo, lorem-ipsum energy, or default component styling.
- Action clarity: can you tell within seconds what to do and why to trust it?
- Mobile: does the small viewport hold up, or is it desktop shrunk down?
- End with exactly **one** recommendation: the single highest-impact patch for the next round. Not a list.

You never grade a build you produced. If you wrote the patch, you are the Builder this round, and someone (or some later declared pass) else evaluates.

## Evidence Auditor

You audit artifacts, not aesthetics. The Evaluator says whether it is good; you say whether it is real.

Check, with fresh artifacts from the running page:

- Page actually renders: expected title, main heading, and body content markers present.
- Desktop **and** mobile screenshots exist and match the claimed state.
- Console errors, page errors, and failed network requests reviewed and either clean or explicitly listed.
- Primary flow exercised (the click, the scroll, the form — whatever the promise is).
- For animation or WebGL claims: recording plus multi-state frames plus a runtime readback (see the WebGL readback section of `evidence-and-handoff.md`).

Return one verdict — `pass`, `partial`, or `blocked` — with the missing pieces named. A confident Builder report is not evidence. You do not soften a verdict to keep the loop moving.
