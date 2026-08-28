# Contributing

Thank you for making browser work more intentional, accessible, and verifiable.

## Contribution standard

A useful change improves one of these: visible judgement, existing-project safety, motion ownership, browser evidence, accessibility, or handoff clarity. Effects without a narrative or product job are not improvements.

Keep the daily reading path short: `README.md` plus the relevant website or animation workflow. Optional checklists, prompts, and specialist indexes should remain conditional rather than becoming mandatory context.

## Before opening a pull request

```bash
python -B .github/scripts/validate-release.py
python -B -m unittest discover -s tests
```

If browser behavior or motion changes, also exercise the affected workflow against a runnable artifact and include fresh desktop/mobile and time-sequence evidence. A build, HTTP 200, or one screenshot is not completion proof.

Changes to browser utilities also run:

```bash
python -B .github/scripts/run-browser-smoke.py
```

Describe the user-visible benefit, changed workflow authority, evidence used, and any migration or compatibility impact. Do not include credentials, client material, private prompts, absolute local paths, cache artifacts, or root agent instruction files.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
