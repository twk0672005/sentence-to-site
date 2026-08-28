from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / ".github" / "scripts" / "validate-release.py"


def copy_repository(destination: Path) -> None:
    shutil.copytree(
        ROOT,
        destination,
        ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__", "distribution", "reports"),
        dirs_exist_ok=True,
    )


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["WORKFLOW_KIT_ROOT"] = str(root)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, "-B", str(VALIDATOR)],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


class ReleaseValidatorTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        completed = run_validator(ROOT)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["verdict"], "PASS")

    def test_unexpected_distribution_file_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            (candidate / "unexpected.md").write_text("not declared", encoding="utf-8")
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("unexpected repository files", completed.stdout)

    def test_version_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            manifest_path = candidate / "kit-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["version"] = "9.9.9"
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("version must be 1.4.0", completed.stdout)

    def test_english_readme_version_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            readme = candidate / "README.en.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace("v1.4.0", "v9.9.9"),
                encoding="utf-8",
            )
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("README.en.md does not declare v1.4.0", completed.stdout)

    def test_broken_relative_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            readme = candidate / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\n[broken](docs/does-not-exist.md)\n",
                encoding="utf-8",
            )
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("missing link target", completed.stdout)

    def test_cache_artifact_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            cache = candidate / "scripts" / "__pycache__"
            cache.mkdir()
            (cache / "stale.pyc").write_bytes(b"not-a-real-pyc")
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("cache artifacts found", completed.stdout)

    def test_sensitive_file_inside_allowed_prefix_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            (candidate / ".github" / "private.pem").write_text(
                "[REDACTED]", encoding="utf-8"
            )
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("sensitive or escaping entries found", completed.stdout)

    def test_missing_fragment_fails(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            candidate = Path(raw) / "kit"
            copy_repository(candidate)
            readme = candidate / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n[missing fragment](README.md#definitely-not-a-heading)\n",
                encoding="utf-8",
            )
            completed = run_validator(candidate)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("missing fragment target", completed.stdout)


if __name__ == "__main__":
    unittest.main()
