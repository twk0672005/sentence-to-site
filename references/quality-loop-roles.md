# Bounded independent review contracts

`adversarial-quality-loop` is a legacy skill name for a **single, explicit independent review**. It is not part of the default route and it never starts another build pass automatically.

## When it may run

Run it only when the user explicitly asks for an independent review, challenge pass, or second opinion. The requester supplies the acceptance criteria and the rendered evidence to review.

If separate reviewers are unavailable, report that the independent review is unavailable. Do not role-play a solo review and present it as independent judgement.

## Independent evaluator

Review only the rendered artifact and the stated acceptance criteria.

- State whether the evidence supports each criterion.
- Identify at most one visible concern, if any.
- Return one finite recommendation for the user to accept, reject, or defer.
- Do not edit code, request a repeat, or decide that another review round is necessary.

## Evidence auditor

Audit whether the reported artifact is real and current:

- expected title, main heading, and key body marker are present;
- each required desktop/mobile/interaction/motion artifact exists for the selected route;
- console, page-error, and failed-request evidence is present when the route requires it;
- the primary flow was exercised when the route requires it.

Return exactly one verdict: `pass`, `partial`, or `blocked`, naming any missing evidence. The auditor does not make aesthetic decisions or authorize more implementation.

## Stop condition

The review ends after the evaluator report and auditor verdict. The user, not the reviewer, decides whether to start a new scoped implementation task.
