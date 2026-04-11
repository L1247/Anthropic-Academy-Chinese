# 架構說明

## 目錄結構

```
anthropic-academy-chinese/
├── CLAUDE.md                          # AI 輔助開發指引
├── package.json                       # 依賴與 scripts（ESM 模式）
├── package-lock.json
├── .gitignore
├── .claude/
│   ├── settings.json                  # Claude Code 權限與 Hook 設定
│   ├── settings.local.json            # 本地覆蓋設定（不納入版控）
│   ├── agents/                        # 客製化 Sub-agent 定義
│   │   ├── code-reviewer.md           # 內容品質與規範審查
│   │   ├── debugger.md                # 建置錯誤診斷與修復
│   │   ├── doc-writer.md              # 繁體中文課程頁面撰寫
│   │   ├── git-commit.md              # 符合規範的 commit 產生
│   │   ├── refactor-assistant.md      # 內容結構重構
│   │   ├── security-auditor.md        # 外部連結與依賴安全審查
│   │   └── test-runner.md             # VitePress 建置驗證
│   ├── rules/                         # 路徑感知的開發規則
│   │   ├── git-commit.md              # Commit message 格式規則
│   │   └── vitepress-content.md       # VitePress 內容撰寫規則（作用於 docs/**）
│   ├── hooks/                         # 自動化 Hook 腳本
│   │   ├── protect-files.sh           # PreToolUse：阻止編輯敏感檔案
│   │   └── notify-done.sh             # Stop：任務完成 Windows 氣球通知
│   └── skills/                        # 自訂 Skill 腳本
├── dev-docs/                          # AI 輔助開發文件（不進入網站建置）
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   ├── FEATURES.md
│   ├── CHANGELOG.md
│   └── plans/
│       └── archive/
└── docs/                              # VitePress 內容根目錄
    ├── .vitepress/
    │   └── config.mts                 # VitePress 核心設定（導覽、側邊欄、Mermaid）
    ├── index.md                       # 首頁（layout: home，含課程總覽表格）
    ├── roadmap.md                     # 學習路線圖（含 Mermaid 流程圖）
    ├── resources.md                   # 額外學習資源
    ├── ai-fluency/
    │   ├── index.md                   # AI 素養課程總覽
    │   ├── framework-foundations.md   # AI 素養：框架與基礎
    │   ├── capabilities-limitations.md # AI 能力與限制
    │   ├── for-educators.md           # 教育者的 AI 素養
    │   ├── for-students.md            # 學生的 AI 素養
    │   ├── teaching.md                # 教授 AI 素養
    │   └── for-nonprofits.md          # 非營利組織的 AI 素養
    ├── claude-products/
    │   ├── index.md                   # Claude 產品課程總覽
    │   ├── claude-101.md              # Claude 101
    │   ├── claude-code-101.md         # Claude Code 101
    │   └── claude-cowork.md           # Claude Cowork 入門
    └── developer/
        ├── index.md                   # 開發者課程總覽
        ├── building-with-api.md       # 使用 Claude API 開發
        ├── mcp-intro.md               # MCP 入門
        ├── mcp-advanced.md            # MCP 進階主題
        ├── claude-code-in-action.md   # Claude Code 實戰
        ├── agent-skills.md            # Agent Skills 入門
        ├── subagents.md               # 子代理入門
        ├── amazon-bedrock.md          # Claude × Amazon Bedrock
        └── google-vertex.md           # Claude × Google Vertex AI
```

## VitePress 路由機制

VitePress 使用**檔案系統路由**（File-based Routing）：

| 檔案路徑 | 對應 URL |
|---------|---------|
| `docs/index.md` | `/` |
| `docs/roadmap.md` | `/roadmap` |
| `docs/ai-fluency/index.md` | `/ai-fluency/` |
| `docs/developer/building-with-api.md` | `/developer/building-with-api` |

規則：`index.md` 對應目錄根路徑，其餘檔名直接成為 URL slug。

## VitePress 設定架構（config.mts）

設定檔位於 `docs/.vitepress/config.mts`，使用 `withMermaid()` 包裝 `defineConfig()`。

### 關鍵設定項目

| 設定 | 值 | 說明 |
|------|-----|------|
| `lang` | `zh-TW` | HTML lang 屬性，影響 SEO |
| `title` | Anthropic Academy 中文指南 | 網站標題 |
| `mermaid.theme` | `default` | 全域 Mermaid 主題，勿在各頁面重複設定 |

### 導覽列（nav）結構

```
首頁  /
課程分類
  ├── AI 素養（6 門）     /ai-fluency/
  ├── Claude 產品（3 門） /claude-products/
  └── 開發者（8 門）     /developer/
學習路線    /roadmap
額外資源    /resources
官方課程    https://anthropic.skilljar.com/（新分頁）
```

### 側邊欄（sidebar）結構

側邊欄依路徑前綴分組，各分類路徑完全獨立：

- `/ai-fluency/` → 顯示 AI 素養課程 sidebar
- `/claude-products/` → 顯示 Claude 產品 sidebar
- `/developer/` → 顯示開發者課程 sidebar
- 首頁、roadmap、resources → 無側邊欄

**關鍵約束**：sidebar 的 `link` 值必須與實際檔案路徑完全對應（去掉 `.md` 副檔名），否則連結失效但不會有建置錯誤。

## 頁面類型

### 首頁（layout: home）

`docs/index.md` 使用 `layout: home` frontmatter，透過 VitePress Hero + Features 元件呈現，並附有自訂 HTML（角色卡片 + 課程總覽表格）。

### 課程總覽頁（index.md）

各分類的 `index.md` 使用自訂 HTML `<div class="role-cards">` 卡片佈局（定義於 VitePress 主題 CSS 或行內樣式）。

### 一般課程頁

標準 Markdown 頁面，可包含 Mermaid 流程圖（`roadmap.md` 大量使用此功能）。

## Mermaid 整合

透過 `vitepress-plugin-mermaid` 整合，在 `config.mts` 的最外層設定：

```ts
mermaid: {
  theme: 'default',
}
```

使用方式：在任何 Markdown 頁面中直接使用 \`\`\`mermaid 語法塊。`roadmap.md` 有 4 個 flowchart TD 範例可參考。

## 建置產物

`npm run docs:build` 輸出至 `docs/.vitepress/dist/`：
- 完全靜態的 HTML/CSS/JS
- 不需要伺服器，可直接部署至靜態主機（GitHub Pages、Cloudflare Pages 等）
