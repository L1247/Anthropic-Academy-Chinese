# Anthropic Academy 中文指南

Anthropic Academy 免費課程的完整繁體中文學習指南。

## 快速開始

```bash
# 安裝依賴
npm install

# 啟動開發伺服器
npm run docs:dev
# → http://localhost:5173

# 建置靜態網站
npm run docs:build
# → 輸出至 docs/.vitepress/dist/

# 預覽建置結果
npm run docs:preview
```

## 技術棧

| 工具 | 版本 | 用途 |
|------|------|------|
| VitePress | ^1.6.4 | 靜態網站生成器（Vue 3 基礎） |
| vitepress-plugin-mermaid | ^2.0.17 | Mermaid 流程圖支援 |
| mermaid | ^11.14.0 | 圖表渲染引擎 |
| Node.js | ESM（`"type": "module"`） | 執行環境 |

## 常用指令

| 指令 | 說明 |
|------|------|
| `npm run docs:dev` | 啟動本地開發伺服器，支援熱更新 |
| `npm run docs:build` | 建置靜態網站 |
| `npm run docs:preview` | 本地預覽建置結果 |

## 內容結構

17 門課程分為 3 大分類：

| 分類 | 課程數 | 目錄 |
|------|--------|------|
| AI 素養 | 6 門 | `docs/ai-fluency/` |
| Claude 產品 | 3 門 | `docs/claude-products/` |
| 開發者 | 8 門 | `docs/developer/` |

## 文件索引

| 文件 | 說明 |
|------|------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 架構、目錄結構、VitePress 設定說明 |
| [DEVELOPMENT.md](./DEVELOPMENT.md) | 開發規範、新增課程的完整步驟 |
| [FEATURES.md](./FEATURES.md) | 功能清單與完成狀態 |
| [CHANGELOG.md](./CHANGELOG.md) | 更新日誌 |
| [plans/](./plans/) | 開發計畫目錄 |
