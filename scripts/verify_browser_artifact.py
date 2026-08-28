#!/usr/bin/env python3
"""Fail-closed browser evidence for one explicit website route.

Static build/staging directory:
  ARTIFACT_ROOT=/path/to/dist TITLE_CONTAINS=Product python scripts/verify_browser_artifact.py

Existing localhost server:
  ARTIFACT_URL=http://127.0.0.1:5173/ H1_CONTAINS=Product python scripts/verify_browser_artifact.py

At least one identity marker is mandatory. Remote URLs require ALLOW_REMOTE_URL=1.
"""
from __future__ import annotations

import json

from browser_common import (
    browser_target,
    env_bool,
    file_receipt,
    identity_expectations,
    output_dir,
    read_status,
    receipt_url,
    write_json,
)
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


VIEWPORTS = {
    "desktop": {"width": 1440, "height": 1000},
    "mobile": {"width": 390, "height": 844},
    "narrow": {"width": 320, "height": 800},
}


def launch_args() -> list[str]:
    args = ["--disable-dev-shm-usage"]
    if env_bool("ENABLE_SWIFTSHADER", False):
        args.extend(["--enable-webgl", "--ignore-gpu-blocklist", "--enable-unsafe-swiftshader"])
    return args


def settle(page: object) -> None:
    page.wait_for_load_state("domcontentloaded", timeout=20_000)
    try:
        page.wait_for_load_state("networkidle", timeout=8_000)
    except PlaywrightError:
        pass
    page.wait_for_timeout(500)


def identity_issues(title: str, h1: str, body: str, expected: dict[str, str]) -> list[str]:
    issues: list[str] = []
    if expected["title"] and expected["title"] not in title:
        issues.append(f"title marker missing: {expected['title']!r}")
    if expected["h1"] and expected["h1"] not in h1:
        issues.append(f"h1 marker missing: {expected['h1']!r}")
    if expected["body"] and expected["body"] not in body:
        issues.append(f"body marker missing: {expected['body']!r}")
    return issues


def inspect_keyboard(page: object, interactive_count: int) -> list[dict[str, object]]:
    sequence: list[dict[str, object]] = []
    if interactive_count <= 0:
        return sequence
    for _ in range(min(12, interactive_count + 2)):
        page.keyboard.press("Tab")
        focused = page.evaluate(
            """() => {
              const el = document.activeElement;
              if (!el || el === document.body) return null;
              const rect = el.getBoundingClientRect();
              const style = getComputedStyle(el);
              return {
                tag: el.tagName.toLowerCase(),
                id: el.id || null,
                name: el.getAttribute('aria-label') || el.getAttribute('name') ||
                  (el.textContent || '').trim().slice(0, 80) || null,
                visible: rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' &&
                  style.display !== 'none'
              };
            }"""
        )
        if focused and focused not in sequence:
            sequence.append(focused)
    return sequence


def main() -> int:
    expected = identity_expectations()
    require_reduced_static = env_bool("REQUIRE_REDUCED_STATIC", False)
    out = output_dir("browser-verify")
    summary: dict[str, object] = {
        "kind": "browser-artifact-verification",
        "verdict": "FAIL",
        "issues": [],
        "warnings": [],
        "viewports": {},
        "artifacts": [],
    }
    issues: list[str] = summary["issues"]  # type: ignore[assignment]
    warnings: list[str] = summary["warnings"]  # type: ignore[assignment]

    try:
        with browser_target() as target:
            summary.update(
                {
                    "url": receipt_url(target.url),
                    "serveMode": target.mode,
                    "root": str(target.root) if target.root else None,
                    "identity": expected,
                    "outputs": str(out),
                }
            )
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=True, args=launch_args())
                try:
                    for label, viewport in VIEWPORTS.items():
                        context = browser.new_context(viewport=viewport, reduced_motion="no-preference")
                        page = context.new_page()
                        console_errors: list[dict[str, str]] = []
                        console_warnings: list[dict[str, str]] = []
                        page_errors: list[str] = []
                        failed_requests: list[dict[str, object]] = []
                        page.on(
                            "console",
                            lambda msg: (
                                console_errors.append({"type": msg.type, "text": msg.text})
                                if msg.type == "error"
                                else console_warnings.append({"type": msg.type, "text": msg.text})
                                if msg.type == "warning"
                                else None
                            ),
                        )
                        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
                        page.on(
                            "requestfailed",
                            lambda request: failed_requests.append(
                                {
                                    "url": request.url,
                                    "resourceType": request.resource_type,
                                    "failure": request.failure,
                                }
                            ),
                        )
                        try:
                            response = page.goto(target.url, wait_until="domcontentloaded", timeout=45_000)
                            settle(page)
                            title = page.title()
                            h1 = (
                                page.locator("h1").first.inner_text(timeout=5_000).strip()
                                if page.locator("h1").count()
                                else ""
                            )
                            body = page.locator("body").inner_text(timeout=5_000)
                            readback = page.evaluate(
                                """() => {
                                  const root = document.documentElement;
                                  const interactive = document.querySelectorAll(
                                    'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])'
                                  );
                                  return {
                                    viewport: {width: innerWidth, height: innerHeight},
                                    document: {width: root.scrollWidth, height: root.scrollHeight},
                                    overflowX: root.scrollWidth > innerWidth,
                                    h1Count: document.querySelectorAll('h1').length,
                                    canvasCount: document.querySelectorAll('canvas').length,
                                    interactiveCount: interactive.length,
                                    runningAnimations: document.getAnimations().filter(
                                      a => a.playState === 'running'
                                    ).length
                                  };
                                }"""
                            )
                            keyboard = inspect_keyboard(page, int(readback["interactiveCount"]))
                            viewport_path = out / f"{label}-viewport.png"
                            full_path = out / f"{label}-full.png"
                            page.screenshot(path=str(viewport_path), full_page=False, animations="disabled")
                            page.screenshot(path=str(full_path), full_page=True, animations="disabled")
                            artifacts = [file_receipt(viewport_path), file_receipt(full_path)]
                            summary["artifacts"].extend(artifacts)  # type: ignore[union-attr]

                            scoped_issues = identity_issues(title, h1, body, expected)
                            status = response.status if response else None
                            if status is None or status >= 400:
                                scoped_issues.append(f"HTTP status is not successful: {status}")
                            if readback["overflowX"]:
                                scoped_issues.append("horizontal overflow detected")
                            if console_errors:
                                scoped_issues.append(f"console errors: {len(console_errors)}")
                            if page_errors:
                                scoped_issues.append(f"page errors: {len(page_errors)}")
                            if failed_requests:
                                scoped_issues.append(f"failed requests: {len(failed_requests)}")
                            if int(readback["interactiveCount"]) > 0 and not keyboard:
                                scoped_issues.append("interactive controls exist but keyboard focus was not observed")
                            if console_warnings:
                                warnings.append(f"{label}: console warnings: {len(console_warnings)}")
                            issues.extend(f"{label}: {item}" for item in scoped_issues)
                            summary["viewports"][label] = {  # type: ignore[index]
                                "status": status,
                                "title": title,
                                "h1": h1,
                                "readback": readback,
                                "keyboardSequence": keyboard,
                                "consoleErrors": console_errors,
                                "consoleWarnings": console_warnings,
                                "pageErrors": page_errors,
                                "requestFailed": failed_requests,
                                "issues": scoped_issues,
                                "artifacts": artifacts,
                            }
                        finally:
                            page.close()
                            context.close()

                    reduced_context = browser.new_context(
                        viewport=VIEWPORTS["mobile"], reduced_motion="reduce"
                    )
                    reduced_page = reduced_context.new_page()
                    try:
                        reduced_response = reduced_page.goto(
                            target.url, wait_until="domcontentloaded", timeout=45_000
                        )
                        settle(reduced_page)
                        reduced = {
                            "status": reduced_response.status if reduced_response else None,
                            "preference": reduced_page.evaluate(
                                "matchMedia('(prefers-reduced-motion: reduce)').matches"
                            ),
                            "state": read_status(reduced_page),
                        }
                        reduced_path = out / "mobile-reduced-motion.png"
                        reduced_page.screenshot(
                            path=str(reduced_path), full_page=False, animations="disabled"
                        )
                        reduced["artifact"] = file_receipt(reduced_path)
                        summary["artifacts"].append(reduced["artifact"])  # type: ignore[union-attr]
                        if not reduced["preference"]:
                            issues.append("reduced-motion context did not activate")
                        running = int(reduced["state"]["runningAnimations"])
                        if require_reduced_static and running:
                            issues.append(f"reduced-motion still has {running} running animations")
                        summary["reducedMotion"] = reduced
                    finally:
                        reduced_page.close()
                        reduced_context.close()
                finally:
                    browser.close()
    except Exception as exc:
        issues.append(f"{type(exc).__name__}: {exc}")

    summary["verdict"] = "PASS" if not issues else "FAIL"
    receipt = out / "readback.json"
    write_json(receipt, summary)
    print(
        json.dumps(
            {
                "verdict": summary["verdict"],
                "issues": len(issues),
                "warnings": len(warnings),
                "report": str(receipt),
                "outputs": str(out),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
