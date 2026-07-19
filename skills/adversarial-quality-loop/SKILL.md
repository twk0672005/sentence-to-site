---
name: adversarial-quality-loop
description: Use when a user explicitly requests an independent review, challenge pass, or second opinion on a rendered website or animation artifact. Produces one bounded evaluator report and evidence verdict; it never auto-starts another build pass.
---

# Bounded Independent Review

This legacy-named skill is **not** a default quality loop. It is an optional, one-time independent review after a route has produced the required evidence.

## Preconditions

- The user explicitly requested independent review, a challenge pass, or a second opinion.
- Acceptance criteria and current rendered evidence are available.
- Separate reviewers are available. If not, report that independent review is unavailable; do not simulate it as a solo role-play.

## Run one review pass

1. Give an independent Evaluator the acceptance criteria and rendered artifact only.
2. Give an independent Evidence Auditor the selected route's evidence requirements and artifacts.
3. Return the Evaluator's finite report plus the Auditor's `pass`, `partial`, or `blocked` verdict.
4. Offer the user's choices: accept, reject, defer, or start a new explicitly scoped implementation task.

The Evaluator may identify one visible concern and one recommendation. Neither reviewer edits code, asks for another review round, or authorizes another build pass.

## Stop condition

Stop after the report and verdict. A new implementation pass begins only through a new user decision, not because an agent wants to improve its own output.

## Boundaries

- Self-critique does not count as independent review.
- A missing reviewer is `unavailable`, not a reason to silently downgrade to solo review.
- A `partial` or `blocked` evidence verdict propagates to delivery; it does not trigger retry automation.
- See [`../../references/quality-loop-roles.md`](../../references/quality-loop-roles.md) for the bounded evaluator and auditor contracts.
