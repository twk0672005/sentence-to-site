---
name: adversarial-quality-loop
description: Use when a website or animation task needs a real quality loop — separated judgement through distinct Planner, Builder, Evaluator, and Evidence Auditor roles — instead of one agent grading its own work. Also use when a user asks for a "quality loop", "review loop", or "100%" pass and it must not be satisfied by private self-critique.
---

# Adversarial Quality Loop

One agent reviewing its own output is a preflight, not a loop. A loop creates **separation of judgement**: the mind that built the thing is not the mind that grades it, and the mind that grades taste is not the mind that audits evidence.

## The four roles

| Role | Owns | Must not |
| --- | --- | --- |
| **Planner** | defines what "high quality" means for this task: target user, first-five-seconds feeling, primary action, trust cue, must-have visible changes, stop-ship risks, evidence required | write code; say vague things like "more premium" |
| **Builder** | one bounded visible patch: keep working flows, fix the weakest thing, report what changed and how to verify it | large refactors uninvited; internal QA wording in public UI; pretending a blocker is done |
| **Evaluator** | cold-user verdict on the rendered artifact: first-glance quality, weakest spot, template/demo smell, CTA clarity, mobile issues — and exactly **one** highest-impact patch recommendation | broad plans; grading its own build |
| **Evidence Auditor** | proof the artifact actually runs: title/H1/body markers, desktop + mobile screenshots, console and page errors, failed requests, primary flow; recordings and readback for animation | aesthetics; covering for the Builder when evidence is missing |

Role contracts are in [`../../references/quality-loop-roles.md`](../../references/quality-loop-roles.md). The Auditor's verdict vocabulary (`pass` / `partial` / `blocked`) is defined in [`../../references/evidence-and-handoff.md`](../../references/evidence-and-handoff.md).

## Running the loop

1. Planner sets the quality bar and required evidence **before** building.
2. Builder ships one bounded visible patch.
3. Evaluator and Evidence Auditor review the **rendered artifact** independently.
4. The orchestrating agent verifies their findings against the evidence, applies the highest-impact patch, and repeats.
5. Stop when the Auditor returns `pass` and the Evaluator has no highest-impact patch left that a cold user would notice — or when the loop stops producing visible improvement (then hand off honestly).

## Hard rules

- **Self-critique does not count as the loop.** If the user asked for a loop or review pass, internal role-play ("I opposed myself") does not satisfy the request.
- **Degradation must be declared.** If your environment cannot spawn separate agents (no subagent tool, cost limits, tool failure), say so explicitly and run the role contracts sequentially as a labelled *solo mode* — never silently, and never presented as the full loop.
- **A direction discussion is not a loop.** Reviewers who only debated the plan did not review the build; the roles must touch the actual build/critique/evidence cycle to be claimed.
- **The Auditor outranks optimism.** A `partial` or `blocked` verdict propagates to the delivery claim; see `delivery-handoff`.
