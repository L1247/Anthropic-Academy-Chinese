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
| 官方證書頁 | ✅ 完成 | 17 門課程的證書資訊、CCA 認證說明、常見問題 |
| HeroCertBadge | ✅ 完成 | 首頁裝飾性證書徽章元件，連結至 /certificates |
| MermaidLightbox | ✅ 完成 | 點擊 Mermaid 圖表可放大，支援滾輪縮放與拖曳 |
| TypewriterBadge | ✅ 完成 | 首頁打字機動畫徽章，顯示 AI 素養精選標語 |
| SlideViewer | ✅ 完成 | 投影片翻頁瀏覽器，上下頁 + 全螢幕 + 鍵盤 ◀▶ 控制 |
| NlmVideo 播放器 | ✅ 完成 | 自訂影片播放器，CC 字幕 Popover + 字幕字級調整（14–40px，localStorage 持久化）+ 播放速度 Bar（1–2×）|
| NlmVideo 三語字幕 | ✅ 完成 | 繁中 / 英文 / 中英 三種字幕軌道，依 prop 提供決定 Popover 選項是否 enabled |

## 內容功能

### 首頁（docs/index.md）

- **Hero 區塊**：標語 + 兩個 CTA 按鈕（學習路線圖、官方課程）
- **Features 區塊**：三大分類卡片含連結
- **角色引導卡**：初學者 / 開發者 / 教育者 / 學生，各自導向最適合的起點課程
- **AI 素養精選卡片**：TypewriterBadge 打字機動畫 + 精選課程推薦區塊
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

### AI 素養（6 門 + NLM 延伸頁 + 互動練習頁）

| 課程 | 檔案 | 狀態 |
|------|------|------|
| AI 素養：框架與基礎 | `ai-fluency/framework-foundations.md` | ✅ |
| NLM 延伸：第 01 課學習素材 | `ai-fluency/framework-nlm-01.md` | ✅ |
| NLM 延伸：第 02 課 4D 框架詳解 | `ai-fluency/framework-nlm-02.md` | ✅ |
| AI 能力與限制 | `ai-fluency/capabilities-limitations.md` | ✅ |
| 教育者的 AI 素養 | `ai-fluency/for-educators.md` | ✅ |
| 學生的 AI 素養 | `ai-fluency/for-students.md` | ✅ |
| 教授 AI 素養 | `ai-fluency/teaching.md` | ✅ |
| 非營利組織的 AI 素養 | `ai-fluency/for-nonprofits.md` | ✅ |
| 4D 框架互動練習 | `ai-fluency/4d-practice.md` | ✅ |

**NLM 延伸頁功能說明：**
- 由 `notebooklm-course-updater` skill 從 NotebookLM 匯出內容自動更新
- 包含：影片摘要（繁體中文結構化時間軸）、投影片（SlideViewer 翻頁瀏覽器）、延伸測驗（Quiz 元件）
- 嵌入於對應主課程的 sidebar 項目之下，採折疊式設計
- 影片透過 `NlmVideo` 元件嵌入，支援三種字幕軌道（繁中 / 英文 / 中英雙語）
- 字幕由 `/subtitle` skill（faster-whisper 轉錄 + Claude Haiku 翻譯）自動產出三份 VTT

**4D 框架互動練習頁功能說明：**
- 使用 VitePress + Vue 3 `<script setup>` 嵌入互動式自我評估問卷
- 讓學習者透過情境題實際演練 4D 框架（Discover、Decide、Design、Deliver）
- 題目作答後即時顯示解析說明

### Claude 產品（3 門 + 互動練習頁）

| 課程 | 檔案 | 狀態 |
|------|------|------|
| Claude 101 | `claude-products/claude-101.md` | ✅ |
| Claude Code 101 | `claude-products/claude-code-101.md` | ✅ |
| Claude Cowork 入門 | `claude-products/claude-cowork.md` | ✅ |
| Claude 101 互動練習 | `claude-products/claude-101-practice.md` | ✅ |
| Claude Code 101 互動練習 | `claude-products/claude-code-101-practice.md` | ✅ |
| Claude Cowork 互動練習 | `claude-products/claude-cowork-practice.md` | ✅ |

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
