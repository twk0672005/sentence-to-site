from __future__ import annotations

import os
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from browser_common import (
    browser_target,
    receipt_url,
    three_state_receipts_are_distinct,
    validate_external_url,
    validate_static_root,
)


class BrowserCommonTests(unittest.TestCase):
    def test_remote_url_requires_explicit_authority(self) -> None:
        with self.assertRaisesRegex(ValueError, "Remote ARTIFACT_URL is disabled"):
            validate_external_url("https://example.com", allow_remote=False)
        self.assertEqual(
            validate_external_url("http://127.0.0.1:5173/", allow_remote=False),
            "http://127.0.0.1:5173/",
        )
        with self.assertRaisesRegex(ValueError, "must not contain username/password"):
            validate_external_url("http://user:password@127.0.0.1:5173/", allow_remote=False)
        self.assertEqual(
            receipt_url("http://127.0.0.1:5173/path?token=secret#state"),
            "http://127.0.0.1:5173/path",
        )

    def test_static_root_rejects_sensitive_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "index.html").write_text("<h1>safe</h1>", encoding="utf-8")
            (root / ".env").write_text("API_KEY=[REDACTED]", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "sensitive or escaping"):
                validate_static_root(root, "index.html")

    def test_static_root_requires_real_entry(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            with self.assertRaisesRegex(ValueError, "does not exist"):
                validate_static_root(Path(raw), "index.html")

    def test_dynamic_static_server_serves_named_root(self) -> None:
        fixture = ROOT / "tests" / "fixtures" / "static-site"
        old = os.environ.copy()
        try:
            os.environ.pop("ARTIFACT_URL", None)
            os.environ["ARTIFACT_ROOT"] = str(fixture)
            os.environ["ARTIFACT_PORT"] = "0"
            os.environ["ARTIFACT_ENTRY"] = "index.html"
            with browser_target() as target:
                body = urlopen(target.url, timeout=5).read().decode("utf-8")
                self.assertIn("Workflow Fixture", body)
                self.assertEqual(target.mode, "static-root")
        finally:
            os.environ.clear()
            os.environ.update(old)

    def test_explicit_occupied_port_fails_instead_of_reusing_wrong_site(self) -> None:
        fixture = ROOT / "tests" / "fixtures" / "static-site"
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        port = listener.getsockname()[1]
        old = os.environ.copy()
        try:
            os.environ.pop("ARTIFACT_URL", None)
            os.environ["ARTIFACT_ROOT"] = str(fixture)
            os.environ["ARTIFACT_PORT"] = str(port)
            with self.assertRaisesRegex(RuntimeError, "may belong to another project"):
                with browser_target():
                    self.fail("occupied port must not be reused")
        finally:
            listener.close()
            os.environ.clear()
            os.environ.update(old)

    def test_motion_requires_three_distinct_named_states(self) -> None:
        valid = [
            {"name": "start", "artifact": {"sha256": "a"}},
            {"name": "mid", "artifact": {"sha256": "b"}},
            {"name": "settled", "artifact": {"sha256": "c"}},
        ]
        self.assertTrue(three_state_receipts_are_distinct(valid))
        repeated = [dict(item) for item in valid]
        repeated[2] = {"name": "settled", "artifact": {"sha256": "b"}}
        self.assertFalse(three_state_receipts_are_distinct(repeated))


if __name__ == "__main__":
    unittest.main()
