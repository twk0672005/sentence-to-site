#!/usr/bin/env python3
"""Validate the public v1.3.3 clean-result-core repository."""
from __future__ import annotations

import json
import py_compile
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_FILES = {
    "CURRENT_BASELINE.md",
    "PACKAGING_AUDIT.md",
    "README.md",
    "V126_MERGE_VERIFICATION.md",
    "WORKFLOW_COMPLETENESS_AUDIT.md",
    "checklists/animation-preflight.md",
    "checklists/delivery-checklist.md",
    "checklists/frontend-preflight.md",
    "checklists/handoff-bundle.md",
    "checklists/project-intake.md",
    "docs/codex-claude-usage.md",
    "docs/tooling-setup.md",
    "docs/troubleshooting.md",
    "docs/workflow-kit-maintenance-map.md",
    "examples/orbital-jake-effects-case-study.md",
    "included-skills/README.md",
    "included-skills/SKILLS_MANIFEST.json",
    "included-skills/THREEJS_SOURCE_LOCK.json",
    "prompts/visual-reference-extractor.md",
    "requirements.txt",
    "scripts/record_browser_scroll.py",
    "scripts/verify_browser_artifact.py",
    "workflows/animation-workflow.md",
    "workflows/evidence-gate.md",
    "workflows/evidence-scoring.md",
    "workflows/file-architecture-workflow.md",
    "workflows/high-end-public-review.md",
    "workflows/mcp-and-skills-install.md",
    "workflows/refero-inspiration.md",
    "workflows/website-workflow.md",
}

missing = sorted(path for path in CANONICAL_FILES if not (ROOT / path).is_file() or not (ROOT / path).stat().st_size)
assert not missing, f"missing canonical v1.3.3 files: {', '.join(missing)}"

for path in (ROOT / "included-skills").glob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))

canonical_text = "\n".join(
    (ROOT / relative).read_text(encoding="utf-8", errors="ignore")
    for relative in sorted(CANONICAL_FILES)
    if Path(relative).suffix.lower() in {".md", ".py", ".json", ".txt"}
)
assert "/root/" not in canonical_text, "absolute private path found"
assert "Nova" not in canonical_text, "private maintainer name found"
assert "-----BEGIN PRIVATE KEY-----" not in canonical_text, "private key block found"
assert not re.search(r"(?:sk|ghp|github_pat)_[A-Za-z0-9_\-]{20,}", canonical_text), "secret-like token found"
assert not (ROOT / "AGENTS.md").exists() and not (ROOT / "CLAUDE.md").exists(), "root agent instruction file found"
assert not any(path.name == "__pycache__" or path.suffix == ".pyc" for path in ROOT.rglob("*")), "cache artifact found"

animation = (ROOT / "workflows/animation-workflow.md").read_text(encoding="utf-8")
for phrase in (
    "Choreographed Motion",
    "UI Motion",
    "Scroll Story",
    "Motion direction",
    "Beat sheet",
    "Timeline",
    "Architecture",
    "Scene choreography",
    "Timing polish",
    "停手與交付",
):
    assert phrase in animation, f"animation semantic contract missing: {phrase}"

refero = (ROOT / "workflows/refero-inspiration.md").read_text(encoding="utf-8")
for phrase in ("Product UI", "Refero Styles", "supplied reference", "Do not scrape"):
    assert phrase in refero, f"Refero boundary missing: {phrase}"

with tempfile.TemporaryDirectory() as cache:
    for relative in ("scripts/verify_browser_artifact.py", "scripts/record_browser_scroll.py"):
        py_compile.compile(str(ROOT / relative), doraise=True, cfile=str(Path(cache) / (Path(relative).stem + ".pyc")))

print("PASS: complete v1.3.3 clean-result-core, public boundary, JSON, and Python syntax")
