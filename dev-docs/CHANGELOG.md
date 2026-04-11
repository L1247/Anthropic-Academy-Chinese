# 更新日誌

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
