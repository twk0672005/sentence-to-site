#!/usr/bin/env python3
"""Validate the public cinematic-web-motion skill library without network access."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".venv", "_internal", "tests", "__pycache__"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt"}
PRIVATE_MARKERS = (
    "/" + "root" + "/",
    "A" + "fuu",
    "N" + "ova",
    "H" + "ermes",
    "Gold" + "Pilot",
    "__" + "COSMIC" + "_",
)
SECRET_PATTERNS = (
    re.compile(r"(?:sk|ghp|github_pat)_[A-Za-z0-9_\-]{20,}"),
    re.compile(r"(?i)(?:api[_-]?key|bot[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing closing frontmatter")
    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def public_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or EXCLUDED_PARTS.intersection(path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name == "LICENSE":
            files.append(path)
    return files


def main() -> int:
    errors: list[str] = []
    required = [
        "README.md", "LICENSE", "VERSION", "CHANGELOG.md", "docs/ARCHITECTURE.md", "docs/INSTALLATION.md",
        "templates/project-intake.md", "templates/motion-brief.md", "templates/evidence-report.md", "templates/handoff.md",
        "scripts/verify_browser_artifact.py", "scripts/record_browser_scroll.py",
    ]
    for item in required:
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").is_file() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must be semantic version x.y.z")

    catalog_path = ROOT / "skills" / "catalog.json"
    if not catalog_path.is_file():
        errors.append("missing skills/catalog.json")
        catalog = {"skills": []}
    else:
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"invalid catalog JSON: {error}")
            catalog = {"skills": []}

    if catalog.get("schemaVersion") != 1:
        errors.append("catalog schemaVersion must be 1")
    if catalog.get("version") != version:
        errors.append("catalog version must match VERSION")
    entries = catalog.get("skills")
    if not isinstance(entries, list) or not entries:
        errors.append("catalog skills must be a non-empty list")
        entries = []

    names: set[str] = set()
    for entry in entries:
        name = entry.get("name") if isinstance(entry, dict) else None
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"invalid catalog skill name: {name!r}")
            continue
        if name in names:
            errors.append(f"duplicate catalog skill: {name}")
        names.add(name)
        expected_path = f"skills/{name}/SKILL.md"
        if entry.get("path") != expected_path:
            errors.append(f"catalog path mismatch for {name}")
        if not isinstance(entry.get("summary"), str) or not entry["summary"].strip():
            errors.append(f"catalog summary missing for {name}")
        for relative in entry.get("references", []):
            if not isinstance(relative, str) or not (ROOT / relative).is_file():
                errors.append(f"catalog reference missing for {name}: {relative}")
        for relative in entry.get("tools", []):
            if not isinstance(relative, str) or not (ROOT / relative).is_file():
                errors.append(f"catalog tool missing for {name}: {relative}")

    skill_root = ROOT / "skills"
    actual = {path.name for path in skill_root.iterdir() if path.is_dir()} if skill_root.is_dir() else set()
    if actual != names:
        errors.append(f"catalog/tree mismatch: catalog={sorted(names)} tree={sorted(actual)}")

    for name in sorted(names):
        skill_path = ROOT / "skills" / name / "SKILL.md"
        eval_path = ROOT / "skills" / name / "evals" / "evals.json"
        if not skill_path.is_file():
            errors.append(f"missing SKILL.md for {name}")
            continue
        try:
            fields = parse_frontmatter(skill_path)
        except ValueError as error:
            errors.append(f"{name}: {error}")
            continue
        if fields.get("name") != name:
            errors.append(f"{name}: frontmatter name mismatch")
        description = fields.get("description", "")
        if not description.startswith("Use when"):
            errors.append(f"{name}: description must start with 'Use when'")
        if len(description) > 700:
            errors.append(f"{name}: description exceeds 700 characters")
        if not eval_path.is_file():
            errors.append(f"missing eval fixture for {name}")
        else:
            try:
                fixture = json.loads(eval_path.read_text(encoding="utf-8"))
                if fixture.get("skill") != name or not isinstance(fixture.get("cases"), list) or not fixture["cases"]:
                    errors.append(f"invalid eval fixture for {name}")
            except json.JSONDecodeError as error:
                errors.append(f"invalid eval JSON for {name}: {error}")

    for path in public_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in PRIVATE_MARKERS:
            if marker in text:
                errors.append(f"private marker {marker!r} in {path.relative_to(ROOT)}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"secret-like content in {path.relative_to(ROOT)}")

    if errors:
        print("FAIL: skill package validation")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"PASS: validated {len(names)} skills at version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
