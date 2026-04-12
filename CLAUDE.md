# CLAUDE.md

## 專案概述

**Anthropic Academy 中文指南** — VitePress 靜態文件網站，提供 Anthropic Academy 免費課程的完整繁體中文學習指南（17 門課程，3 大分類）。

## 常用指令

```bash
npm run docs:dev       # 啟動開發伺服器（預設 http://localhost:5173）
npm run docs:build     # 建置靜態網站至 docs/.vitepress/dist/
npm run docs:preview   # 預覽建置結果
```

## 關鍵規則

- **新增課程**：在對應分類目錄建立 `.md` 檔案，並同步更新 `docs/.vitepress/config.mts` 的 sidebar 設定
- **路由即檔案**：VitePress 使用檔案路徑作為 URL，檔案名稱決定 URL slug（使用英文小寫 kebab-case）
- **繁體中文優先**：所有頁面內容使用繁體中文，包含 UI 文字（已在 config.mts 統一設定）
- **Mermaid 圖表**：使用 vitepress-plugin-mermaid，直接在 Markdown 中使用 \`\`\`mermaid 語法
- 功能開發使用 `dev-docs/plans/` 記錄計畫；完成後移至 `dev-docs/plans/archive/`

## 詳細文件

- `./dev-docs/README.md` — 項目介紹與快速開始
- `./dev-docs/ARCHITECTURE.md` — 架構、目錄結構、VitePress 設定說明
- `./dev-docs/DEVELOPMENT.md` — 開發規範、新增課程步驟
- `./dev-docs/FEATURES.md` — 功能列表與完成狀態
- `./dev-docs/TESTING.md` — 建置驗證與品質確認流程
- `./dev-docs/CHANGELOG.md` — 更新日誌

## 必要遵守項目

- 不要修改 `docs/.vitepress/dist/`（建置產物，不納入版控）
- 新增課程時必須同時更新 `docs/index.md` 的課程總覽表格
- `config.mts` 的 sidebar 路徑需與實際檔案路徑完全對應，否則連結失效
- Mermaid 圖表使用 `theme: default`（已在 config.mts 設定），不需在各頁面重複設定
