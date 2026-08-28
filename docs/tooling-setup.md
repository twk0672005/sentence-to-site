# Tooling Setup

Workflow文件本身零dependency。以下只係optional browser evidence utilities。

## Supported baseline

- Python 3.11／3.12；
- Playwright 1.62.0（requirements pin）；
- matching Chromium installed by Playwright；
- FFmpeg／ffprobe optional，只在REQUIRE_MP4=1時需要。

## POSIX

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    python -m playwright install chromium

## Windows PowerShell

    py -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe -m playwright install chromium

## Static build／staging

ARTIFACT_ROOT必須係sanitized build output，不係有.git／.env／private key嘅
source root。ARTIFACT_ENTRY預設index.html；ARTIFACT_PORT預設0，由OS分配。

POSIX：

    ARTIFACT_ROOT=/path/to/dist \
    TITLE_CONTAINS="Product" \
    python scripts/verify_browser_artifact.py

PowerShell：

    $env:ARTIFACT_ROOT = "C:\path\to\dist"
    $env:TITLE_CONTAINS = "Product"
    .\.venv\Scripts\python.exe -B scripts\verify_browser_artifact.py

Identity marker至少一個：

- TITLE_CONTAINS
- H1_CONTAINS
- BODY_CONTAINS

## Existing dev server

預設只准loopback：

    ARTIFACT_URL=http://127.0.0.1:5173/ \
    H1_CONTAINS="Product" \
    python scripts/verify_browser_artifact.py

外部URL只有喺network/browser scope已獲授權時先設ALLOW_REMOTE_URL=1。

## Motion record

    ARTIFACT_ROOT=/path/to/dist \
    H1_CONTAINS="Product" \
    MOTION_DURATION_SECONDS=8 \
    python scripts/record_browser_scroll.py

Default輸出：WebM、start/mid/settled PNG、contact-sheet JPG、
reduced-motion PNG、JSON receipt。FFmpeg存在時另產MP4；硬性需要MP4時設
REQUIRE_MP4=1。

PROGRESS_ADAPTER預設none，代表真scroll。只有artifact明確暴露diagnostic
hook時先用app／cosmic；hook evidence唔代替real scroll wiring。

## Optional renderer flags

Chromium sandbox預設保留。Headless WebGL因已知環境限制需要SwiftShader時，
先在隔離、可信artifact設ENABLE_SWIFTSHADER=1，並喺receipt標示；呢個唔係
production GPU proof。

## Maintainer validation

    python .github/scripts/validate-release.py
    python -m unittest discover -s tests
    python .github/scripts/run-browser-smoke.py

Release package：

    python .github/scripts/validate-release.py --output-dir distribution

distribution係generated／ignored。Validator會建deterministic ZIP、
SHA256SUMS、package hash並讀返每個entry做byte parity。

## Failure interpretation

- Wrong／missing identity：FAIL，可能驗錯server／route；
- Explicit static port occupied：FAIL，唔重用；
- sensitive/static source root：FAIL，改用sanitized build；
- Playwright/Chromium unavailable：environment blocker；
- runtime exception／failed asset／overflow：issues -> PARTIAL／FAIL；
- FFmpeg unavailable：仍可交WebM/contact sheet；REQUIRE_MP4=1先FAIL。
