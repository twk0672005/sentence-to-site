from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected_skills = {
    "cinematic-web-motion",
    "visual-story-direction",
    "website-motion-intake",
    "motion-choreography",
    "browser-evidence",
    "delivery-handoff",
}
required_root_files = {
    "VERSION",
    "CHANGELOG.md",
    "docs/ARCHITECTURE.md",
    "docs/INSTALLATION.md",
    "skills/catalog.json",
    "templates/project-intake.md",
    "templates/motion-brief.md",
    "templates/evidence-report.md",
    "templates/handoff.md",
    "scripts/validate_skill_package.py",
    ".github/workflows/validate-skills.yml",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/skill-request.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
}
missing = sorted(path for path in required_root_files if not (root / path).is_file())
assert not missing, f"incomplete skill-library surface: {', '.join(missing)}"

catalog_path = root / "skills" / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
assert catalog["schemaVersion"] == 1
assert catalog["version"] == (root / "VERSION").read_text(encoding="utf-8").strip()
entries = catalog["skills"]
assert {entry["name"] for entry in entries} == expected_skills
for entry in entries:
    assert entry["path"] == f"skills/{entry['name']}/SKILL.md"
    assert entry["summary"].strip(), f"catalog summary missing for {entry['name']}"

actual_skills = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
assert actual_skills == expected_skills, f"catalog/skill tree drift: {actual_skills ^ expected_skills}"
for name in expected_skills:
    skill_dir = root / "skills" / name
    assert (skill_dir / "SKILL.md").is_file(), f"missing {name}/SKILL.md"
    eval_path = skill_dir / "evals" / "evals.json"
    assert eval_path.is_file(), f"missing {name} eval fixture"
    evals = json.loads(eval_path.read_text(encoding="utf-8"))
    assert evals.get("skill") == name and evals.get("cases"), f"invalid eval fixture for {name}"

check = subprocess.run(
    [sys.executable, "scripts/validate_skill_package.py"],
    cwd=root,
    capture_output=True,
    text=True,
)
assert check.returncode == 0, check.stdout + check.stderr
assert "PASS" in check.stdout
print("PASS: composable skill-library architecture")
