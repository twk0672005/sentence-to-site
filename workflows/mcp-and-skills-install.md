# Skills and MCP Install Guide

## 必裝 Skills

建議在 Hermes active profile 安裝或確認以下 skills：

```text
design-taste-frontend
creative-browser-artifacts
adversarial-quality-loop
verification-before-completion
frontend-technical-architecture-gate
social-reel-agent-system-recon
chinese-documentation
```

可選但常用：

```text
clawteam
dispatching-parallel-agents
imagegen-frontend-web
brandkit
native-mcp
mcporter
```

真 Three.js／WebGL scene 先載入 `threejs-cinematic-motion`。遇到窄技術題目，再按需載入 `threejs-fundamentals`、`threejs-geometry`、`threejs-materials`、`threejs-lighting`、`threejs-textures`、`threejs-animation`、`threejs-loaders`、`threejs-shaders`、`threejs-postprocessing` 或 `threejs-interaction`；一次只揀有用部分，唔好全包注入。

CloudAI-X pack 係私人本機技術參考，冇身份／workflow authority；上游repo未有可核實 `LICENSE` 檔，不應公開再分發。API與production做法以官方Three.js r185、現有專案stack同真browser evidence為準。

## MCP 角色

MCP 不是人格，也不是審美來源。MCP 是外部能力入口。

常用 MCP：

- 21st Magic MCP：UI inspiration / component builder / component refiner
- Logo search MCP：找 SVG / TSX / JSX logo
- GitHub MCP：repo / issue / PR / code search
- Filesystem MCP：給外部 agent 指定資料夾操作
- Figma MCP：從 design source 抽 component / token

## Hermes native MCP 範例

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "[REDACTED_GITHUB_TOKEN]"

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/projects"]

  time:
    command: "uvx"
    args: ["mcp-server-time"]
```

## 21st Magic 使用規則

1. 先用 inspiration / search，不要一開始用 credit-consuming builder。
2. 抽 pattern，不要貼 incompatible TSX。
3. 保留現有 stack。
4. 整合後一定要 screenshot / smoke test。
5. 21st 是靈感，不是 taste authority。Taste authority 仍是 `design-taste-frontend`。

## Secrets 安全

- 不輸出完整 key。
- README 裡只放 `[REDACTED]`。
- MCP server env 只傳必要變數，不傳整個 shell env。
- 公開包不要包含 `.env`、token、cookie、session。
