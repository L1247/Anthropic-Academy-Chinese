---
paths:
  - "docs/**"
---

# VitePress 內容規則

## 檔案與路由
- 檔案名稱使用英文小寫 kebab-case（如 `framework-foundations.md`），直接對應 URL slug
- 新增頁面後必須同步更新 `docs/.vitepress/config.mts` 的 sidebar，否則頁面存在但無法從導覽到達
- 新增課程後必須同步更新 `docs/index.md` 的課程總覽表格

## Markdown 規範
- 每頁只有一個 H1（`#`），作為頁面標題
- 使用 H2（`##`）和 H3（`###`）分層，config.mts 的 outline 設定會自動呈現 H2-H3 於目錄
- 難度標示統一格式：⭐ 初學者 / ⭐⭐ 中級 / ⭐⭐⭐ 高級

## Mermaid 圖表
- 直接使用 \`\`\`mermaid 語法塊，不需額外設定
- 主題已全域設定為 `default`，不在各頁面重複設定 `%%{init: ...}%%`
- 流程圖使用 `flowchart TD`（由上往下），節點文字超過 15 字時加換行 `<br/>`

## VitePress 元件
- 使用 `::: tip`、`::: info`、`::: warning` 標注重要提示
- 自訂 HTML（如角色卡片 `<div class="role-cards">`）與 `docs/index.md` 現有格式保持一致
