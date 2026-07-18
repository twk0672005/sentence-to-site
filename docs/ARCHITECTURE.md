# Architecture

This is a small skill library, not a monolithic prompt and not an agent framework.

```text
skills/
  catalog.json                 discovery metadata and module map
  cinematic-web-motion/        thin router for the complete bundle
  visual-story-direction/      visual premise and critique
  website-motion-intake/       existing-project discovery and ownership
  motion-choreography/         animation systems and fallback behavior
  browser-evidence/            running-artifact proof and verdicts
  delivery-handoff/            evidence-safe delivery contract
references/                    one canonical copy of long-form guidance
templates/                     copyable working forms
scripts/                       deterministic verification and package checks
evals/                         library-level acceptance cases
```

## Design rules

- **One skill, one decision boundary.** A module must answer a distinct question; it must not be a differently named copy of another skill.
- **Thin entry, deep references.** `SKILL.md` explains when and how to decide. Long checklists, tooling detail, and templates live outside it.
- **Progressive disclosure.** Use the router or one specialist skill first; open only the linked reference needed for the task.
- **Shared guidance is canonical.** Specialist skills link to root `references/`; do not fork the same rule across folders.
- **Evidence is a capability, not a claim.** Browser scripts and templates support proof, but the actual verdict remains `pass`, `partial`, or `blocked`.
- **Framework neutrality is real.** The kit may route CSS, Motion, GSAP, canvas, or WebGL work, but does not require any of them.

## Adding a skill

A new module is justified only when it has a distinct trigger, decision boundary, reference need, and evaluation case. Add its `SKILL.md`, `evals/evals.json`, catalog entry, and focused validation before expanding public installation docs.
