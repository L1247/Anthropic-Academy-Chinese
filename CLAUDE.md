# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概述

**Anthropic Academy 中文指南** — VitePress 靜態文件網站，提供 Anthropic Academy 免費課程的完整繁體中文學習指南（3 大分類：AI 素養、Claude 產品、開發者）。

## 常用指令

```bash
npm run docs:dev       # 啟動開發伺服器（預設 http://localhost:5173）
npm run docs:build     # 建置靜態網站至 docs/.vitepress/dist/
npm run docs/preview   # 預覽建置結果
```

建置後的 dead link 報告是偵測 sidebar 路徑錯誤的唯一方式，新增課程後必跑。

## 關鍵規則

- **新增課程三步驟**：① 建立 `docs/<category>/<slug>.md` → ② 更新 `docs/.vitepress/config.mts` sidebar → ③ 更新 `docs/index.md` 課程總覽表格（缺一不可）
- **路由即檔案**：VitePress 使用檔案路徑作為 URL，slug 使用英文小寫 kebab-case
- **繁體中文優先**：所有頁面內容與 UI 文字使用繁體中文（已在 config.mts 統一設定）
- **Mermaid 圖表**：使用 vitepress-plugin-mermaid，直接在 Markdown 中使用 \`\`\`mermaid；主題已全域設定 `default`，不需在各頁面重複
- **Sidebar 層級符號**：`└ 📓` 前綴為視覺縮排慣例（非 VitePress 原生 API），新增子頁時須手動維持一致
- 功能開發使用 `dev-docs/plans/` 記錄計畫；完成後移至 `dev-docs/plans/archive/`

## Vue 元件系統

所有元件在 `docs/.vitepress/theme/index.ts` 全域註冊，任何 `.md` 檔案可直接使用標籤，**無需 import**。

| 元件 | 主要 Props | 用途 |
|------|-----------|------|
| `Quiz` | `question`, `options`, `answer`(Number/Array), `explanation`, `multi` | 單選 / 多選題 |
| `MatchingPairs` | `leftItems`, `rightItems`, `correctPairs`, `explanation` | 左右配對拖曳題 |
| `RankingExercise` | `items`, `correctOrder`, `explanation` | 拖曳排序題 |
| `PromptRewrite` | `originalPrompt`, `requiredKeywords`, `minLength`, `sampleAnswer` | Prompt 改寫輸入練習 |
| `DelegationChecklist` | `scenario` | AI 委派四問決策樹 |
| `DiligenceBuilder` | — | AI 使用聲明建立器 |
| `SlideViewer` | `slides`({src,caption}[]) | 投影片翻頁瀏覽器（全螢幕 + 鍵盤 ◀▶）|
| `NlmVideo` | `src`, `poster`, `zh-vtt`(必填), `en-vtt?`, `bi-vtt?`, `default-mode?` | 影片播放器（三語字幕 CC Popover + 字級 + 速度 Bar）|
| `MermaidLightbox` | — | 自動掛載，點擊 Mermaid 圖表放大（滾輪縮放 + 拖曳）|
| `HeroCertBadge` | — | 首頁證書徽章裝飾（自動掛載於 `home-hero-image` slot）|
| `TypewriterBadge` | — | 首頁打字機動畫徽章 |

新增元件步驟：① `docs/.vitepress/theme/components/<Name>.vue` → ② 在 `index.ts` import 並 `app.component()` 註冊 → ③ 使用 `var(--vp-c-*)` CSS 變數確保深 / 淺模式。

## Agents

`.claude/agents/` 內的 agents 可透過 `@agent-name` 直接呼叫：

| Agent | 用途 |
|-------|------|
| `content-translator` | 英文原始素材 → 繁體中文課程頁 |
| `course-image-integrator` | 截圖/PDF → CSS 元件或圖片引用 + Mermaid 概念圖 |
| `doc-writer` | 撰寫 / 更新課程 Markdown 頁面 |
| `sidebar-updater` | 新增課程後同步 config.mts、index.md、FEATURES.md |
| `practice-builder` | 為課程產生 `*-practice.md` 互動練習頁 |
| `notebooklm-course-updater` | 讀取 NLM 匯出（測驗 / 簡報 / 影片摘要）更新課程頁 |
| `test-runner` | 執行建置驗證，分析 dead link 與 Mermaid 錯誤 |
| `debugger` | 診斷 VitePress 建置錯誤 |
| `explorer` | 快速查詢專案結構（sidebar 與檔案是否對齊等）|
| `refactor-assistant` | 改善內容結構、消除重複、統一格式 |
| `git-commit` | 分析變更產生符合規範的 commit message 並執行 |

## Hooks 行為

| 事件 | 觸發條件 | 行為 |
|------|---------|------|
| `PreToolUse` | Edit / Write | `protect-files.sh`：阻止編輯 `.env`、`*.lock`、`.sqlite` 等敏感檔案 |
| `PostCompact` | Context 壓縮後 | 自動 `cat CLAUDE.md`，重新注入專案規則 |
| `Stop` | 任務結束 | ① Windows 氣球通知（PowerShell）② 若有未提交變更，自動執行 `git add + commit` |

## 詳細文件

- `./dev-docs/ARCHITECTURE.md` — 完整目錄結構、VitePress 路由、元件 Props 一覽、字幕系統
- `./dev-docs/DEVELOPMENT.md` — 新增課程步驟、命名規則、Vue 元件開發規範、計畫歸檔流程
- `./dev-docs/FEATURES.md` — 功能清單與課程完成狀態
- `./dev-docs/TESTING.md` — 建置驗證、NlmVideo 與字幕資產驗證清單
- `./dev-docs/CHANGELOG.md` — 版本更新日誌
- `./dev-docs/README.md` — 項目介紹與快速開始

## 必要遵守項目

- 不要修改 `docs/.vitepress/dist/`（建置產物，不納入版控）
- `config.mts` sidebar 的 `link` 值須與實際檔案路徑完全對應（去掉 `.md`），路徑錯誤不會有建置錯誤，只有 dead link
- 新增互動練習頁（`*-practice.md`）時，同步在 sidebar 中用 `└ 🎯` 前綴放在對應課程之下
- 字幕 VTT 發布命名規則：`zh-Hant-only.vtt` → `<name>.zh-Hant.vtt`，`video.zh-Hant.vtt`（雙語）→ `<name>.bilingual.vtt`（見 `.claude/rules/subtitle-variants.md`）
