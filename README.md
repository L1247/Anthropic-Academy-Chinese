# Anthropic Academy 中文學習指南

> Anthropic Academy 免費課程的完整繁體中文導覽網站

[![部署狀態](https://img.shields.io/badge/部署-Cloudflare%20Pages-orange)](https://anthropic-academy-chinese.pages.dev)

## 關於本專案

[Anthropic Academy](https://anthropic.skilljar.com/) 提供 17 門免費課程，但全為英文。本專案將課程內容整理成**完整繁體中文學習指南**，協助中文使用者快速理解課程架構、重點概念與實作方式。

- 17 門課程 · 3 大分類
- 每門課程附有學習目標、概念圖（Mermaid）、重點摘要
- 完全免費，原始碼開放

## 課程分類

| 分類 | 課程數 | 適合對象 |
|------|--------|---------|
| 🧠 AI 素養 | 6 門 | 教育者、學生、非營利組織、所有人 |
| 💬 Claude 產品 | 3 門 | 一般使用者 |
| 🛠️ 開發者 | 8 門 | 開發者、工程師 |

## 課程列表

| 課程名稱 | 分類 | 難度 |
|---------|------|------|
| AI 素養：框架與基礎 | AI 素養 | ⭐ 初學者 |
| AI 能力與限制 | AI 素養 | ⭐ 初學者 |
| 教育者的 AI 素養 | AI 素養 | ⭐ 初學者 |
| 學生的 AI 素養 | AI 素養 | ⭐ 初學者 |
| 教授 AI 素養 | AI 素養 | ⭐⭐ 中級 |
| 非營利組織的 AI 素養 | AI 素養 | ⭐ 初學者 |
| Claude 101 | Claude 產品 | ⭐ 初學者 |
| Claude Code 101 | Claude 產品 | ⭐⭐ 初-中級 |
| Claude Cowork 入門 | Claude 產品 | ⭐ 初學者 |
| 使用 Claude API 開發 | 開發者 | ⭐⭐⭐ 中-高級 |
| MCP 入門 | 開發者 | ⭐⭐ 中級 |
| MCP 進階主題 | 開發者 | ⭐⭐⭐ 高級 |
| Claude Code 實戰 | 開發者 | ⭐⭐ 中級 |
| Agent Skills 入門 | 開發者 | ⭐⭐ 中級 |
| 子代理入門 | 開發者 | ⭐⭐ 中級 |
| Claude × Amazon Bedrock | 開發者 | ⭐⭐ 中級 |
| Claude × Google Vertex AI | 開發者 | ⭐⭐ 中級 |

## 技術棧

- [VitePress](https://vitepress.dev/) — 靜態網站生成器
- [vitepress-plugin-mermaid](https://github.com/emersonbottero/vitepress-plugin-mermaid) — Mermaid 圖表支援
- [Cloudflare Pages](https://pages.cloudflare.com/) — 部署與 CDN

## 本地開發

```bash
# 安裝依賴
npm install

# 啟動開發伺服器（http://localhost:5173）
npm run docs:dev

# 建置靜態網站
npm run docs:build

# 預覽建置結果
npm run docs:preview
```

## 目錄結構

```
docs/
├── index.md              # 首頁
├── roadmap.md            # 學習路線圖
├── ai-fluency/           # AI 素養課程
├── claude-products/      # Claude 產品課程
├── developer/            # 開發者課程
└── .vitepress/
    └── config.mts        # VitePress 設定（sidebar、主題等）
```

## 貢獻

歡迎提交 Issue 回報錯誤或建議改善內容。如需貢獻內容，請參考 [dev-docs/DEVELOPMENT.md](dev-docs/DEVELOPMENT.md)。

## 聲明

本專案為非官方社群整理，內容基於 [Anthropic Academy](https://anthropic.skilljar.com/) 公開課程。課程著作權歸 Anthropic 所有。
