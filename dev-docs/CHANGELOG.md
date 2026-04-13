# 更新日誌

## [1.3.0] - 2026-04-13

### 新增
- `SlideViewer.vue`：投影片翻頁瀏覽器元件，支援上下頁、全螢幕、鍵盤 ◀▶ 控制
- NLM-01（`framework-nlm-01.md`）整合 SlideViewer 元件，展示新版投影片

### 修改
- NLM-02（`framework-nlm-02.md`）更新為新版影片、投影片與 SlideViewer 元件
- `.gitignore` 新增 Python `__pycache__` 忽略規則

---

## [1.2.0] - 2026-04-12

### 新增
- `docs/ai-fluency/framework-nlm-01.md`：AI 素養第 01 課 NotebookLM 延伸學習素材
- `docs/ai-fluency/framework-nlm-02.md`：AI 素養第 02 課 4D 框架詳解延伸學習素材
- `docs/references.md`：專案參考連結頁面，含可點擊卡片連結設計
- `TypewriterBadge.vue`：首頁打字機動畫徽章元件 + AI 素養精選卡片區塊
- `.claude/agents/course-image-integrator.md`：截圖/PDF 整合為中文視覺化課程元件的 Agent
- `.claude/skills/notebooklm-course-updater/`：從 NotebookLM 匯出自動更新課程頁面的 Skill
- `.claude/skills/video-subtitle/`：課程影片自動產生雙語字幕（英文 + 繁中 SRT/VTT）的 Skill

### 修改
- AI 素養六門課程新增 Mermaid 概念圖與投影片重製 CSS 元件
- `docs/roadmap.md` 新增官方推薦學習路徑總覽圖，AI 素養列為路線一
- 開發者課程 sidebar 依主題分組（API、MCP、Claude Code、Agent）
- `notify-done.sh` 改善顯示方式，改從 `history.jsonl` 取得 Claude 最後回覆摘要
- `vitepress-content.md` 規則補充並列清單分行規則與 Blockquote 換行規則

### 設定
- `.claude/settings.json` 補充 Stop hook 加入 git 狀態前置檢查與防遞迴觸發機制
- `settings.json` 新增 `CLAUDE_SUBPROCESS` 環境變數防止 Stop hook 遞迴觸發

---

## [1.1.0] - 2026-04-11

### 新增
- `docs/ai-fluency/4d-practice.md`：4D 框架互動練習頁，含 Vue 互動元件（自我評估問卷）
- 全面擴充 AI 素養系列課程內容（框架基礎、能力限制、教育者、學生、教授、非營利）

### 修改
- 全站 17 門課程頁面標題與小節統一加入 emoji 標示
- 強化 AI 素養課程說明細節，新增學習目標與重點摘要段落

### 移除 / 修正
- 移除不必要的 PowerShell 通知 hook 設定（改由 `Stop` 事件觸發）

---

## [1.0.1] - 2026-04-10

### 新增
- `dev-docs/` AI 輔助開發文件結構（ARCHITECTURE、DEVELOPMENT、FEATURES、TESTING、CHANGELOG）
- `CLAUDE.md` 專案 AI 輔助開發指引
- `.claude/agents/`：7 個客製化 Agent（code-reviewer、debugger、doc-writer、git-commit、refactor-assistant、security-auditor、test-runner）
- `.claude/rules/`：git-commit、vitepress-content 規則
- `.claude/hooks/`：protect-files.sh、notify-done.sh

---

## [1.0.0] - 2026-04-10

### 新增
- 完整 17 門課程的繁體中文學習指南
- VitePress 靜態網站建置（含 Mermaid 圖表支援）
- 三大分類：AI 素養（6 門）、Claude 產品（3 門）、開發者（8 門）
- 首頁角色引導卡（初學者 / 開發者 / 教育者 / 學生）
- 學習路線圖（4 條路線，含 Mermaid 流程圖）
- 課程前置條件速查表
- 額外學習資源頁面
- 本地搜尋功能（繁體中文介面）
- VitePress 完整中文化 UI（上一頁 / 下一頁 / 搜尋提示）
