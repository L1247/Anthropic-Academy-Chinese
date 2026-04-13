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
│   │   ├── content-translator.md      # 英文課程翻譯為繁體中文學習指南
│   │   ├── course-image-integrator.md # 截圖/PDF 整合為中文視覺化課程元件
│   │   ├── debugger.md                # 建置錯誤診斷與修復
│   │   ├── doc-writer.md              # 繁體中文課程頁面撰寫
│   │   ├── explorer.md                # 專案結構探索與現狀查詢
│   │   ├── git-commit.md              # 符合規範的 commit 產生
│   │   ├── practice-builder.md        # 互動練習頁建立（Vue 元件組合）
│   │   ├── refactor-assistant.md      # 內容結構重構
│   │   ├── security-auditor.md        # 外部連結與依賴安全審查
│   │   ├── sidebar-updater.md         # 新增課程後同步更新三個設定檔
│   │   └── test-runner.md             # VitePress 建置驗證
│   ├── rules/                         # 路徑感知的開發規則
│   │   ├── git-commit.md              # Commit message 格式規則
│   │   ├── vitepress-content.md       # VitePress 內容撰寫規則（docs/** 作用範圍）
│   │   ├── design-standards.md        # Emoji 使用規則、深色/淺色模式設計規範
│   │   ├── external-links.md          # HTTPS 強制、noopener noreferrer、可信任網域
│   │   └── subtitle-variants.md       # 字幕三份 VTT 命名規範與 NlmVideo 整合流程
│   ├── hooks/                         # 自動化 Hook 腳本
│   │   ├── protect-files.sh           # PreToolUse：阻止編輯敏感檔案（.env, *.lock）
│   │   └── notify-done.sh             # Stop：任務完成 Windows 氣球通知
│   └── skills/                        # 自訂 Skill 定義（user-invocable）
│       ├── video-subtitle/            # /subtitle：影片轉錄 + Claude API 翻譯 → 三份 VTT
│       │   └── SKILL.md
│       └── notebooklm-course-updater/ # /notebooklm-update：從 NLM 匯出更新課程頁
│           └── SKILL.md
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
    │   ├── config.mts                 # VitePress 核心設定（導覽、側邊欄、Mermaid）
    │   └── theme/
    │       ├── index.ts               # 自訂主題入口，全域註冊 Vue 元件
    │       └── components/            # 互動式 Vue 元件（用於練習頁）
    │           ├── Quiz.vue           # 單選/多選題（question, options, answer, multi）
    │           ├── MatchingPairs.vue  # 左右配對題（leftItems, rightItems, correctPairs）
    │           ├── RankingExercise.vue# 排序題（items, correctOrder, explanation）
    │           ├── PromptRewrite.vue  # Prompt 改寫練習（originalPrompt, requiredKeywords）
    │           ├── DelegationChecklist.vue # AI 委派四問決策樹（scenario）
    │           ├── DiligenceBuilder.vue    # AI 使用聲明建立器（工具選擇 + 用途 + 審查程度）
    │           ├── HeroCertBadge.vue  # 首頁證書徽章裝飾元件（連結至 /certificates）
    │           ├── MermaidLightbox.vue# Mermaid 圖表放大燈箱（滾輪縮放、拖曳、ESC 關閉）
    │           ├── TypewriterBadge.vue# 首頁打字機動畫徽章元件
    │           ├── SlideViewer.vue    # 投影片翻頁瀏覽器（上下頁、全螢幕、鍵盤控制）
    │           └── NlmVideo.vue       # 自訂影片播放器（三語字幕 Popover、速度 Bar、字級調整）
    ├── index.md                       # 首頁（layout: home，含課程總覽表格）
    ├── roadmap.md                     # 學習路線圖（含 Mermaid 流程圖）
    ├── resources.md                   # 額外學習資源
    ├── references.md                  # 專案參考連結清單
    ├── ai-fluency/
    │   ├── index.md                   # AI 素養課程總覽
    │   ├── framework-foundations.md   # AI 素養：框架與基礎
    │   ├── framework-nlm-01.md        # NLM 延伸：第 01 課學習素材
    │   ├── framework-nlm-02.md        # NLM 延伸：第 02 課 4D 框架詳解
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

### 互動練習頁（*-practice.md）

互動練習頁在 Markdown 中直接使用全域註冊的 Vue 元件：

```markdown
<Quiz
  question="問題文字"
  :options="['選項A', '選項B']"
  :answer="0"
  explanation="解析文字"
/>
```

**元件一覽：**

| 元件 | Props | 用途 |
|------|-------|------|
| `Quiz` | `question`, `options`, `answer`(Number/Array), `explanation`, `multi`(Boolean) | 單選/多選題，作答後顯示解析 |
| `MatchingPairs` | `leftItems`({id,text}[]), `rightItems`({id,text}[]), `correctPairs`([leftId,rightId][]), `explanation` | 左右配對拖曳題 |
| `RankingExercise` | `items`(String[]), `correctOrder`(Number[]), `explanation` | 拖曳排序題 |
| `PromptRewrite` | `originalPrompt`, `requiredKeywords`(String[]), `minLength`, `sampleAnswer` | Prompt 改寫文字輸入練習 |
| `DelegationChecklist` | `scenario` | AI 委派四問決策樹，逐題引導判斷 |
| `DiligenceBuilder` | 無 Props | AI 使用聲明建立器，多選工具/用途後產出聲明文字 |
| `HeroCertBadge` | 無 Props | 裝飾性證書徽章，連結至 `/certificates` |
| `MermaidLightbox` | 無 Props | 自動掛載於所有 Mermaid 圖表，點擊可放大 |
| `TypewriterBadge` | 無 Props | 首頁打字機動畫徽章，顯示 AI 素養精選標語 |
| `SlideViewer` | `slides`({src,caption}[]) | 投影片翻頁瀏覽器，支援上下頁、全螢幕、鍵盤 ◀▶ 控制 |
| `NlmVideo` | `src`, `poster`, `zhVtt`(必填), `enVtt?`, `biVtt?`, `defaultMode?`('zh'\|'en'\|'bi'\|'off') | 自訂影片播放器，CC 按鈕彈出字幕 Popover（繁中/英文/中英/無字幕），字幕字級 14–40px（localStorage 持久化），播放速度 1–2x Bar |

**全域註冊位置**：`docs/.vitepress/theme/index.ts`，不需要在各頁面 import。

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

## 字幕與影片系統

### 字幕產生流程

```
.claude/notebooklm-exports/<course>/video.mp4
        ↓  /subtitle skill（faster-whisper + Claude API）
video.en.srt              # 英文轉錄（來源真相）
video.zh-Hant.srt         # 雙語 SRT（英上中下）
video.zh-Hant.vtt         # 雙語 VTT（整合用）
video.zh-Hant-only.vtt    # 純繁中 VTT（發布用）
video.en.vtt              # 純英文 VTT（發布用）
```

### 發布到課程頁的命名規則

複製到 `docs/public/videos/<course>/` 時：

| raw export 檔名 | 發布命名 | NlmVideo prop |
|---|---|---|
| `video.zh-Hant-only.vtt` | `<name>.zh-Hant.vtt` | `zh-vtt` |
| `video.en.vtt` | `<name>.en.vtt` | `en-vtt` |
| `video.zh-Hant.vtt` | `<name>.bilingual.vtt` | `bi-vtt` |

> 注意：raw export 的 `video.zh-Hant.vtt` 是雙語內容，發布時必須改名為 `bilingual.vtt`，並以 `zh-Hant-only.vtt` 作為純繁中軌道。

### NlmVideo 標準嵌入碼

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

### 字幕腳本位置

- 主腳本：`.claude/scripts/subtitle/generate_subtitles.py`
- 翻譯模組：`.claude/scripts/subtitle/translate.py`（Claude Haiku API，批次 40 條）
- 工具函式：`.claude/scripts/subtitle/srt_utils.py`（parse / write / split_bilingual_cues）
- Python venv：`.claude/scripts/subtitle/.venv/`（首次使用 /subtitle skill 自動建立）
