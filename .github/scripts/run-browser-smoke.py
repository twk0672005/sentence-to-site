#!/usr/bin/env python3
"""Dogfood both browser utilities against the tracked deterministic fixture."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests" / "fixtures" / "static-site"


def run(script: str, report_root: Path, extra: dict[str, str] | None = None) -> dict:
    env = os.environ.copy()
    env.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "ARTIFACT_ROOT": str(FIXTURE),
            "ARTIFACT_PORT": "0",
            "ARTIFACT_ENTRY": "index.html",
            "ARTIFACT_REPORT_DIR": str(report_root),
            "TITLE_CONTAINS": "Sentence to Site Fixture",
            "H1_CONTAINS": "Workflow Fixture",
            "REQUIRE_REDUCED_STATIC": "1",
        }
    )
    if extra:
        env.update(extra)
    completed = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts" / script)],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if completed.returncode:
        raise AssertionError(
            f"{script} failed\nSTDOUT:\n{completed.stdout[-3000:]}\nSTDERR:\n{completed.stderr[-3000:]}"
        )
    payload = json.loads(completed.stdout)
    report = Path(payload["report"])
    if not report.is_file():
        raise AssertionError(f"{script} did not create its receipt: {report}")
    receipt = json.loads(report.read_text(encoding="utf-8"))
    if receipt.get("verdict") != "PASS":
        raise AssertionError(f"{script} receipt did not pass: {receipt.get('issues')}")
    return {"script": script, "receipt": str(report), "artifacts": len(receipt["artifacts"])}


def run_expected_failure(report_root: Path) -> dict:
    env = os.environ.copy()
    env.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "ARTIFACT_ROOT": str(FIXTURE),
            "ARTIFACT_PORT": "0",
            "ARTIFACT_ENTRY": "index.html",
            "ARTIFACT_REPORT_DIR": str(report_root),
            "H1_CONTAINS": "This marker must not exist",
        }
    )
    completed = subprocess.run(
        [sys.executable, "-B", str(ROOT / "scripts" / "verify_browser_artifact.py")],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if completed.returncode == 0:
        raise AssertionError("wrong identity marker unexpectedly passed")
    payload = json.loads(completed.stdout)
    receipt = Path(payload["report"])
    data = json.loads(receipt.read_text(encoding="utf-8"))
    if data.get("verdict") != "FAIL" or not data.get("issues"):
        raise AssertionError("negative receipt did not preserve the failure")
    return {"script": "verify_browser_artifact.py", "expectedFailure": "wrong-marker", "receipt": str(receipt)}


def main() -> int:
    with tempfile.TemporaryDirectory() as raw:
        report_root = Path(raw)
        results = [
            run("verify_browser_artifact.py", report_root),
            run(
                "record_browser_scroll.py",
                report_root,
                {"MOTION_DURATION_SECONDS": "6", "PROGRESS_ADAPTER": "none"},
            ),
            run_expected_failure(report_root),
        ]
        print(json.dumps({"verdict": "PASS", "results": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
