# Workflow Kit Maintenance Map

## 定位

這份文件只供維護套件本身時使用。日常網站／動畫工作請由 `README.md` 進入，不需要讀本文件。

## Single source of truth

- 日常入口：`README.md`
- 網站核心：`workflows/website-workflow.md`
- 動畫核心：`workflows/animation-workflow.md`
- 架構問題：`workflows/file-architecture-workflow.md`
- Browser 工具：`scripts/verify_browser_artifact.py`、`scripts/record_browser_scroll.py`
- 深度／歷史資料：其他 docs、prompts、checklists、included-skills（按需）

## 維護原則

1. 核心 reading path 保持短：README + 一份 domain workflow。
2. 新規則應取代或收斂舊規則，不可只追加。
3. Project/session incident 不直接升格成永久 core gate。
4. Specialist 細節放 optional reference；不要令每個任務都讀。
5. 多角色只在真並行、獨立 judgement 或用戶明確要求時使用。
6. 技術證據服務成品判斷，不可取代成品判斷。
7. 新版本 visibly worse 時保留舊 approved baseline。

## 變更 Gate

更新套件前只需回答：

- 今次解決邊個重複出現的問題？
- 能否透過刪除、合併或縮短解決？
- 會否增加正常任務的預設讀取量？
- 有冇真實 artifact／workflow smoke 證明改善？

若答案只係「更完整」「多一層保障」「方便未來」，但沒有實際失敗案例，先不要加。

## Package sections

### Core

- README
- website workflow
- animation workflow
- concise file architecture workflow
- two executable browser QA scripts

### Optional

- detailed checklists
- role prompts
- evidence scoring
- MCP/tooling docs
- included skill source copies
- packaging/audit history

Optional 不等於無用；只代表唔應預設注入 context。

## Verification after maintenance

- Markdown/frontmatter 可讀；
- scripts syntax/tests 通過；
- README links 指向存在檔案；
- static/browser smoke 可執行；
- canonical symlink／ZIP 指向正確版本；
- default reading path 沒有重新膨脹。

## 禁止事項

- 為修復複雜度建立另一份治理框架；
- 複製完整 active skills 作日常必讀；
- 將 maintenance history 當 production workflow；
- 用檔案數、角色數、checklist 數量證明品質；
- 未驗證就覆蓋 canonical baseline。
