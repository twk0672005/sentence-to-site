#!/usr/bin/env python3
"""Record truthful 6-12 second scroll/motion evidence for one explicit route.

Real scroll is the default. Set PROGRESS_ADAPTER=app or cosmic only when the
artifact deliberately exposes that diagnostic hook.
"""
from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import time
from pathlib import Path

from browser_common import (
    browser_target,
    env_bool,
    file_receipt,
    identity_expectations,
    output_dir,
    progress_adapter,
    read_status,
    receipt_url,
    set_progress,
    three_state_receipts_are_distinct,
    write_json,
)
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


VIEWPORT = {"width": 1440, "height": 1000}
MOBILE = {"width": 390, "height": 844}


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


def check_identity(page: object, expected: dict[str, str]) -> list[str]:
    title = page.title()
    h1 = page.locator("h1").first.inner_text(timeout=5_000).strip() if page.locator("h1").count() else ""
    body = page.locator("body").inner_text(timeout=5_000)
    issues: list[str] = []
    if expected["title"] and expected["title"] not in title:
        issues.append(f"title marker missing: {expected['title']!r}")
    if expected["h1"] and expected["h1"] not in h1:
        issues.append(f"h1 marker missing: {expected['h1']!r}")
    if expected["body"] and expected["body"] not in body:
        issues.append(f"body marker missing: {expected['body']!r}")
    return issues


def run_media(command: list[str]) -> None:
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    if completed.returncode:
        detail = (completed.stderr or completed.stdout)[-1200:]
        raise RuntimeError(f"media command failed ({command[0]}): {detail}")


def probe_duration(ffprobe: str, path: Path) -> float:
    completed = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return float(completed.stdout.strip())


def make_contact_sheet(browser: object, state_paths: list[Path], out: Path) -> Path:
    cards: list[str] = []
    for path in state_paths:
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        cards.append(
            "<figure><img src='data:image/png;base64,"
            + encoded
            + "'><figcaption>"
            + path.stem
            + "</figcaption></figure>"
        )
    context = browser.new_context(viewport={"width": 1480, "height": 620})
    page = context.new_page()
    try:
        page.set_content(
            "<!doctype html><style>body{margin:0;padding:20px;background:#111;color:#fff;"
            "font:16px system-ui;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}"
            "figure{margin:0}img{display:block;width:100%;height:520px;object-fit:cover;"
            "object-position:top;border:1px solid #555}figcaption{padding-top:8px}</style>"
            + "".join(cards)
        )
        sheet = out / "contact-sheet.jpg"
        page.screenshot(path=str(sheet), full_page=False, type="jpeg", quality=88)
        return sheet
    finally:
        page.close()
        context.close()


def main() -> int:
    expected = identity_expectations()
    duration = float(os.environ.get("MOTION_DURATION_SECONDS", "8"))
    allow_short = env_bool("ALLOW_SHORT_RECORDING", False)
    minimum = 1 if allow_short else 6
    if not minimum <= duration <= 12:
        raise ValueError(f"MOTION_DURATION_SECONDS must be {minimum}..12, got {duration}")
    adapter = progress_adapter()
    require_reduced_static = env_bool("REQUIRE_REDUCED_STATIC", False)
    out = output_dir("scroll-video")
    issues: list[str] = []
    summary: dict[str, object] = {
        "kind": "browser-motion-recording",
        "verdict": "FAIL",
        "issues": issues,
        "durationRequested": duration,
        "progressAdapter": adapter,
        "artifacts": [],
    }

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
                context = None
                page = None
                state_paths: list[Path] = []
                try:
                    context = browser.new_context(
                        viewport=VIEWPORT,
                        record_video_dir=str(out),
                        record_video_size=VIEWPORT,
                        reduced_motion="no-preference",
                    )
                    page = context.new_page()
                    console_errors: list[str] = []
                    console_warnings: list[str] = []
                    page_errors: list[str] = []
                    failed_requests: list[dict[str, object]] = []
                    page.on(
                        "console",
                        lambda msg: console_errors.append(msg.text)
                        if msg.type == "error"
                        else console_warnings.append(msg.text)
                        if msg.type == "warning"
                        else None,
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
                    response = page.goto(target.url, wait_until="domcontentloaded", timeout=45_000)
                    settle(page)
                    issues.extend(check_identity(page, expected))
                    status = response.status if response else None
                    if status is None or status >= 400:
                        issues.append(f"HTTP status is not successful: {status}")

                    states: list[dict[str, object]] = []
                    frames = max(2, round(duration * 30))
                    wait_ms = max(1, round(duration * 1000 / frames))
                    capture_at = {0: "start", frames // 2: "mid", frames: "settled"}
                    started = time.monotonic()
                    for index in range(frames + 1):
                        progress = index / frames
                        set_progress(page, progress, adapter)
                        if index in capture_at:
                            path = out / f"{capture_at[index]}.png"
                            page.screenshot(path=str(path), full_page=False)
                            states.append(
                                {
                                    "name": capture_at[index],
                                    "progress": progress,
                                    "status": read_status(page),
                                    "artifact": file_receipt(path),
                                }
                            )
                            state_paths.append(path)
                        page.wait_for_timeout(wait_ms)
                    elapsed = time.monotonic() - started
                    summary["recordingElapsed"] = elapsed
                    if elapsed < minimum - 0.5:
                        issues.append(f"recording loop ended too early: {elapsed:.2f}s")

                    summary["states"] = states
                    summary["status"] = read_status(page)
                    summary["consoleErrors"] = console_errors
                    summary["consoleWarnings"] = console_warnings
                    summary["pageErrors"] = page_errors
                    summary["requestFailed"] = failed_requests
                    summary["artifacts"].extend(item["artifact"] for item in states)  # type: ignore[union-attr]
                    if not three_state_receipts_are_distinct(states):
                        issues.append("start, mid and settled frames must all be visibly distinct")
                    if console_errors:
                        issues.append(f"console errors: {len(console_errors)}")
                    if page_errors:
                        issues.append(f"page errors: {len(page_errors)}")
                    if failed_requests:
                        issues.append(f"failed requests: {len(failed_requests)}")
                except Exception as exc:
                    issues.append(f"primary recording failed: {type(exc).__name__}: {exc}")
                finally:
                    if page is not None:
                        page.close()
                    if context is not None:
                        context.close()

                if len(state_paths) == 3:
                    try:
                        contact_sheet = make_contact_sheet(browser, state_paths, out)
                        summary["artifacts"].append(file_receipt(contact_sheet))  # type: ignore[union-attr]
                    except Exception as exc:
                        issues.append(f"contact sheet failed: {type(exc).__name__}: {exc}")

                try:
                    reduced_context = browser.new_context(
                        viewport=MOBILE, reduced_motion="reduce"
                    )
                    reduced_page = reduced_context.new_page()
                    try:
                        reduced_page.goto(target.url, wait_until="domcontentloaded", timeout=45_000)
                        settle(reduced_page)
                        reduced = {
                            "preference": reduced_page.evaluate(
                                "matchMedia('(prefers-reduced-motion: reduce)').matches"
                            ),
                            "state": read_status(reduced_page),
                        }
                        reduced_path = out / "mobile-reduced-motion.png"
                        reduced_page.screenshot(path=str(reduced_path), full_page=False)
                        reduced["artifact"] = file_receipt(reduced_path)
                        summary["reducedMotion"] = reduced
                        summary["artifacts"].append(reduced["artifact"])  # type: ignore[union-attr]
                        if not reduced["preference"]:
                            issues.append("reduced-motion context did not activate")
                        running = int(reduced["state"]["runningAnimations"])
                        if require_reduced_static and running:
                            issues.append(f"reduced-motion still has {running} running animations")
                    finally:
                        reduced_page.close()
                        reduced_context.close()
                finally:
                    browser.close()

        webms = sorted(out.glob("*.webm"), key=lambda path: path.stat().st_mtime, reverse=True)
        if not webms:
            issues.append("no Playwright video was recorded")
        else:
            webm = webms[0]
            summary["artifacts"].append(file_receipt(webm))  # type: ignore[union-attr]
            ffmpeg = shutil.which("ffmpeg")
            ffprobe = shutil.which("ffprobe")
            require_mp4 = env_bool("REQUIRE_MP4", False)
            if ffmpeg and ffprobe:
                mp4 = out / "scroll-preview.mp4"
                run_media(
                    [
                        ffmpeg,
                        "-y",
                        "-i",
                        str(webm),
                        "-filter:v",
                        "fps=30,format=yuv420p",
                        "-an",
                        "-c:v",
                        "libx264",
                        "-preset",
                        "veryfast",
                        "-movflags",
                        "+faststart",
                        str(mp4),
                    ]
                )
                actual_duration = probe_duration(ffprobe, mp4)
                summary["durationActual"] = actual_duration
                if not (minimum - 0.5) <= actual_duration <= 14:
                    issues.append(f"recorded duration outside expected range: {actual_duration:.2f}s")
                summary["mp4Status"] = "created"
                summary["artifacts"].append(file_receipt(mp4))  # type: ignore[union-attr]
            else:
                summary["mp4Status"] = "not-run: ffmpeg/ffprobe unavailable"
                if require_mp4:
                    issues.append("REQUIRE_MP4=1 but ffmpeg/ffprobe are unavailable")
    except Exception as exc:
        issues.append(f"{type(exc).__name__}: {exc}")

    summary["verdict"] = "PASS" if not issues else "FAIL"
    receipt = out / "video-readback.json"
    write_json(receipt, summary)
    print(
        json.dumps(
            {
                "verdict": summary["verdict"],
                "issues": len(issues),
                "report": str(receipt),
                "outputs": str(out),
                "durationActual": summary.get("durationActual"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
