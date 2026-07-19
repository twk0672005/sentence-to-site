#!/usr/bin/env python3
"""Deterministically exercise the public routing contract without an AI runtime."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "routing-cases.json"


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def classify(prompt: str) -> dict[str, str]:
    text = prompt.lower()
    existing = has_any(text, ("existing", "current", "update our", "accepted landing"))
    cinematic = has_any(text, ("webgl", "3d", "cinematic", "immersive", "scroll journey", "canvas"))
    ui_motion = has_any(text, ("hover", "menu transition", "ui transition", "microinteraction"))
    prototype = has_any(text, ("prototype", "internal demo", "internal draft", "experiment"))
    public = has_any(text, ("public", "client", "campaign", "portfolio", "conversion"))

    return {
        "baseRoute": "existing-site" if existing else "new-site",
        "experienceLane": "cinematic-webgl" if cinematic else "ui-motion" if ui_motion else "static",
        "deliveryGate": "prototype" if prototype else "public" if public else "prototype",
    }


def main() -> int:
    data = json.loads(CASES.read_text(encoding="utf-8"))
    assert data["version"] == 1
    cases = data["cases"]
    assert len(cases) >= 6

    for case in cases:
        actual = classify(case["prompt"])
        expected = case["expect"]
        assert actual == expected, f"{case['id']}: expected {expected}, got {actual}"
        print(f"PASS: {case['id']} -> {actual['baseRoute']} / {actual['experienceLane']} / {actual['deliveryGate']}")

    print(f"PASS: bounded routing simulation ({len(cases)} cases, no autonomous review loop)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
