# 功能清單

## 網站功能

| 功能 | 狀態 | 說明 |
|------|------|------|
| 繁體中文介面 | ✅ 完成 | lang: zh-TW，所有 UI 文字已中文化 |
| 本地搜尋 | ✅ 完成 | VitePress 內建 local search，中文搜尋提示文字 |
| 響應式設計 | ✅ 完成 | VitePress 預設主題支援 |
| Mermaid 流程圖 | ✅ 完成 | vitepress-plugin-mermaid 整合 |
| 導覽列 | ✅ 完成 | 課程分類下拉選單、官方課程外部連結 |
| 分類側邊欄 | ✅ 完成 | 三個分類各有獨立 sidebar |
| 頁面大綱 | ✅ 完成 | 顯示 H2-H3 層級，標籤「本頁目錄」 |
| 上下頁導覽 | ✅ 完成 | 頁尾顯示「上一頁 / 下一頁」 |
| 社群連結 | ✅ 完成 | GitHub 連結至 anthropics/courses |
| 頁尾聲明 | ✅ 完成 | 非官方指南聲明 + 版權資訊 |
| OG / SEO meta | ✅ 完成 | og:title、og:description、theme-color |

## 內容功能

### 首頁（docs/index.md）

- **Hero 區塊**：標語 + 兩個 CTA 按鈕（學習路線圖、官方課程）
- **Features 區塊**：三大分類卡片含連結
- **角色引導卡**：初學者 / 開發者 / 教育者 / 學生，各自導向最適合的起點課程
- **課程總覽表格**：17 門課程一覽，含分類、難度、前置條件欄位

### 學習路線圖（docs/roadmap.md）

4 條學習路線，各以 Mermaid flowchart TD 呈現：

| 路線 | 目標受眾 | 課程數 | 預計時間 |
|------|---------|--------|---------|
| 初學者 / 一般使用者 | 無技術背景 | 4 門 | 3–5 小時 |
| 開發者 | 有程式基礎 | 最多 9 門 | 15–30 小時 |
| 教育者 | 教師 / 教學設計師 | 4 門 | 4–6 小時 |
| 學生 | 在學中 | 4 門 | 3–4 小時 |

頁尾附**課程前置條件速查表**（17 門課程的必要 / 建議前置條件）。

### 課程分類頁（各 index.md）

- AI 素養：6 門課程的角色卡片佈局
- Claude 產品：3 門課程的角色卡片佈局
- 開發者：8 門課程的角色卡片佈局，含「建議學習路線」和「技術先備知識表」

### 額外資源（docs/resources.md）

- Anthropic 官方文件連結（Claude API 文件、Claude Code 文件、模型版本清單、研究部落格）
- Anthropic Cookbook GitHub 倉庫說明（5 個主題）
- GitHub 開源課程 anthropics/courses（5 組 Jupyter Notebooks）
- 第三方中文與英文學習資源
- 實作練習建議（對應 5 門課程）
- 學習進度追蹤建議

## 課程內容清單

### AI 素養（6 門 + 互動練習頁）

| 課程 | 檔案 | 狀態 |
|------|------|------|
| AI 素養：框架與基礎 | `ai-fluency/framework-foundations.md` | ✅ |
| AI 能力與限制 | `ai-fluency/capabilities-limitations.md` | ✅ |
| 教育者的 AI 素養 | `ai-fluency/for-educators.md` | ✅ |
| 學生的 AI 素養 | `ai-fluency/for-students.md` | ✅ |
| 教授 AI 素養 | `ai-fluency/teaching.md` | ✅ |
| 非營利組織的 AI 素養 | `ai-fluency/for-nonprofits.md` | ✅ |
| 4D 框架互動練習 | `ai-fluency/4d-practice.md` | ✅ |

**4D 框架互動練習頁功能說明：**
- 使用 VitePress + Vue 3 `<script setup>` 嵌入互動式自我評估問卷
- 讓學習者透過情境題實際演練 4D 框架（Discover、Decide、Design、Deliver）
- 題目作答後即時顯示解析說明

### Claude 產品（3 門）

| 課程 | 檔案 | 狀態 |
|------|------|------|
| Claude 101 | `claude-products/claude-101.md` | ✅ |
| Claude Code 101 | `claude-products/claude-code-101.md` | ✅ |
| Claude Cowork 入門 | `claude-products/claude-cowork.md` | ✅ |

### 開發者（8 門）

| 課程 | 檔案 | 狀態 |
|------|------|------|
| 使用 Claude API 開發 | `developer/building-with-api.md` | ✅ |
| MCP 入門 | `developer/mcp-intro.md` | ✅ |
| MCP 進階主題 | `developer/mcp-advanced.md` | ✅ |
| Claude Code 實戰 | `developer/claude-code-in-action.md` | ✅ |
| Agent Skills 入門 | `developer/agent-skills.md` | ✅ |
| 子代理入門 | `developer/subagents.md` | ✅ |
| Claude × Amazon Bedrock | `developer/amazon-bedrock.md` | ✅ |
| Claude × Google Vertex AI | `developer/google-vertex.md` | ✅ |
