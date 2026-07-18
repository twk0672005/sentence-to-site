# Contributing

Thank you for making browser work more intentional, accessible, and verifiable.

## Contribution standard

A useful change improves one of these: visible judgement, existing-project safety, motion ownership, browser evidence, accessibility, or handoff clarity. Effects without a narrative or product job are not improvements.

## Adding or changing a skill

Every installable skill must have:

1. a distinct trigger and decision boundary;
2. a concise `SKILL.md` with `name` and a `Use when...` description;
3. a `skills/<name>/evals/evals.json` fixture with both a positive decision and a boundary case;
4. one catalog entry and only the shared references/tools it truly needs;
5. passing package, library, privacy, and syntax validation.

Do not introduce a differently named duplicate, private prompt, client material, credential, framework mandate, or host-specific instruction unless it is actually tested and documented as optional.

## Before opening a pull request

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
python3 -m py_compile scripts/*.py
```

Describe the user-visible benefit, decision boundary, evaluation case, and evidence used. By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
