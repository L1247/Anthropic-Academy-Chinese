# 開發規範

## 新增課程：完整步驟

### Step 1：建立 Markdown 檔案

在對應分類目錄建立 `.md` 檔案，命名使用英文小寫 kebab-case：

```
docs/ai-fluency/new-course-name.md
docs/claude-products/new-product.md
docs/developer/new-dev-course.md
```

### Step 2：更新 config.mts sidebar

開啟 `docs/.vitepress/config.mts`，在對應分類的 sidebar 陣列加入新項目：

```ts
// 範例：加入 AI 素養新課程
'/ai-fluency/': [
  {
    text: '🧠 AI 素養課程',
    items: [
      // ... 現有項目 ...
      { text: '新課程名稱', link: '/ai-fluency/new-course-name' },
      //                          ↑ 不含 .md 副檔名
    ],
  },
],
```

### Step 3：更新 docs/index.md 課程總覽表格

`docs/index.md` 底部有「全部 17 門課程一覽」表格，需同步新增一列：

```markdown
| [新課程名稱](/ai-fluency/new-course-name) | AI 素養 | ⭐ 初學者 | 無 |
```

### Step 4：更新 dev-docs/FEATURES.md

在對應分類的課程列表中新增課程資訊。

---

## 命名規則

| 類型 | 規則 | 範例 |
|------|------|------|
| 檔案名稱（URL slug） | 英文小寫 kebab-case | `framework-foundations.md` |
| 分類目錄 | 英文小寫 kebab-case | `ai-fluency/`, `claude-products/` |
| 頁面標題（H1） | 繁體中文 | `# AI 素養：框架與基礎` |
| sidebar text | 繁體中文（可含 emoji） | `AI 素養：框架與基礎` |

## 課程頁面建議結構

```markdown
# 課程名稱

> 一句話描述課程核心價值

## 課程概覽

- **難度**：⭐ 初學者 / ⭐⭐ 中級 / ⭐⭐⭐ 高級
- **前置條件**：XXX
- **預計時間**：X 小時

## 學習目標

## 核心概念

## 重點摘要

## 相關資源
```

## 難度標示規範

| 符號 | 說明 | 對應課程類型 |
|------|------|------------|
| ⭐ 初學者 | 無技術背景要求 | AI 素養、Claude 101 |
| ⭐⭐ 中級 | 需要基礎技術知識 | Claude Code、MCP 入門 |
| ⭐⭐⭐ 高級 | 需要扎實技術背景 | MCP 進階、Claude API |

## Mermaid 圖表使用方式

在 Markdown 中直接使用，不需額外設定：

````markdown
```mermaid
flowchart TD
    A["起點"] --> B["下一步"]
    B --> C{判斷}
    C --> D["路徑一"]
    C --> E["路徑二"]

    style A fill:#fef3c7,stroke:#d97706
```
````

參考 `docs/roadmap.md` 的 4 個流程圖範例。

## 新增 Vue 互動元件

### 建立元件檔案

在 `docs/.vitepress/theme/components/` 建立 `.vue` 檔案（Vue 3 `<script setup>` 語法）。

### 全域註冊

開啟 `docs/.vitepress/theme/index.ts`，在 `enhanceApp` 中註冊：

```ts
app.component('MyComponent', MyComponent)
```

### 在 Markdown 中使用

元件全域註冊後，直接在任何 `.md` 檔案中使用標籤，無需 import：

```markdown
<MyComponent
  :items="['A', 'B', 'C']"
  explanation="解析文字"
/>
```

### 設計規範

- 使用 VitePress CSS 變數（`var(--vp-c-*)`），確保深色/淺色模式自動切換
- Props 型別需明確聲明（TypeScript-friendly），必填 props 加 `required: true`
- 互動狀態（選擇、提交）使用 `ref()`，計算結果使用 `computed()`
- 不依賴外部 UI 函式庫，保持輕量

## 環境變數

本專案為純靜態文件網站，**不使用任何環境變數**。所有設定均在 `config.mts` 中硬編碼。

## Skills 使用方式

Skills 是預先定義在 `.claude/skills/` 的可呼叫工作流程，在 Claude Code 提示列輸入斜線指令觸發。

### 現有 Skills

| Skill | 觸發指令 | 說明 |
|---|---|---|
| `video-subtitle` | `/subtitle [course] [--force] [--skip-translate]` | 以 faster-whisper 轉錄 + Claude Haiku 翻譯，產出三份 VTT（純繁中、純英文、雙語） |
| `notebooklm-course-updater` | `/notebooklm-update <course>` | 讀取 NotebookLM 匯出（測驗、簡報、影片摘要），更新對應課程頁 |

### 影片字幕工作流程

```
1. /subtitle <course>          → 在 .claude/notebooklm-exports/<course>/ 產出 5 個字幕檔
2. 複製三份 VTT 到 docs/public/videos/<course>/，依命名規則改名
3. 在課程 .md 中使用 <NlmVideo> 元件嵌入（見下方）
```

### NlmVideo 元件嵌入方式

```html
<NlmVideo
  src="/videos/<course>/<name>.mp4"
  poster="/images/<course>/<name>-poster.png"
  zh-vtt="/videos/<course>/<name>.zh-Hant.vtt"
  en-vtt="/videos/<course>/<name>.en.vtt"
  bi-vtt="/videos/<course>/<name>.bilingual.vtt"
  default-mode="zh"
/>
```

- `zh-vtt`（必填）：純繁中字幕
- `en-vtt`、`bi-vtt`（選填）：省略則 Popover 中對應選項為 disabled

---

## 計畫歸檔流程

1. **命名格式**：`dev-docs/plans/YYYY-MM-DD-<feature-name>.md`
2. **文件結構**：User Story → Spec → Tasks
3. **功能完成後**：移至 `dev-docs/plans/archive/`
4. 同步更新 `dev-docs/FEATURES.md` 和 `dev-docs/CHANGELOG.md`

## 版控注意事項

- `docs/.vitepress/dist/` 已在 `.gitignore` 中（建置產物不納入版控）
- `node_modules/` 已在 `.gitignore` 中
- commit message 格式：`type: 描述`（如 `docs: 新增 MCP 進階課程頁面`）
