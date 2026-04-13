---
name: notebooklm-course-updater
description: 從 NotebookLM 讀取指定 Notebook 的測驗、簡報、影片摘要，並更新對應的 VitePress 課程頁面。
triggers:
  - /notebooklm-update
  - /nlm-update
---

# NotebookLM → VitePress 課程更新 Skill

## 使用方式

```
/notebooklm-update <notebook名稱或ID|Skilljar-URL> [課程檔案路徑]
/notebooklm-update <course-key> <lesson-number>
```

**範例：**
```
/notebooklm-update "The 4Ds of AI Fluency"
/notebooklm-update 208e3044 docs/ai-fluency/framework-foundations.md
/notebooklm-update https://anthropic.skilljar.com/ai-fluency-framework-foundations/291876

# 課程編號模式（自動查表 → 建立 NLM → 產出延伸頁）
/notebooklm-update framework 03
/notebooklm-update framework 07
```

**`course-key` 對應表**：

| course-key | 課程 | 目錄檔 |
|---|---|---|
| `framework` | AI 素養：框架與基礎 | `.claude/skills/notebooklm-course-updater/lessons/framework-foundations.json` |

> 未來新增課程系列只需在 `lessons/` 放入對應的 JSON 檔，並使用相同格式。

---

## 執行步驟

### Step 0.0：偵測輸入格式（優先判斷）

在所有步驟之前，先判斷輸入類型：

1. **若輸入為 `<course-key> <lesson-number>` 格式**（如 `framework 03`）→ **進入課程編號模式**（見下方）
2. **若輸入以 `https://` 開頭** → 進入 Step 0（Skilljar URL 模式）
3. **其他** → 進入 Step 1-3（現有 Notebook 名稱 / ID 模式）

---

### 🆕 課程編號模式：`/notebooklm-update framework 03`

當輸入符合 `<course-key> <lesson-number>` 格式時，執行以下專屬流程：

**0.A 讀取課程目錄 JSON**

```
.claude/skills/notebooklm-course-updater/lessons/<course-key>.json
```

- 若檔案不存在 → 回報路徑，說明需要建立目錄檔後終止
- 讀取 JSON，找到 `number === "<lesson-number>"` 的條目（如 `"03"`）
- 若找不到條目 → 列出所有可用課號後終止

**0.B 驗證必要欄位**

從 JSON 條目中取得：
- `title_zh`：課堂中文標題（必要）
- `videos`：影片陣列，每個元素含 `part`、`url`、`title`、`duration_minutes`
- `description_zh`：一行簡介（必要）
- `nlm_page_exists`：若為 `true` → 提示 NLM 頁已存在，詢問是否繼續覆蓋

**videos 陣列驗證規則**：
- 必須至少有一個元素；只取 `videos[0]`，多元素視為設定錯誤並終止
- `videos[0].url` 不可為空，為空時終止並提示填寫
- `part` 欄位已棄用，每課只允許單一影片來源

若 `videos[0].url` 為空，提示：
```
❌ 第 NN 課的影片 URL 尚未填寫：
  - videos[0].url: ❌ 未填寫
請至 YouTube 播放清單找到對應影片 URL，填入：
.claude/skills/notebooklm-course-updater/lessons/<course-key>.json
播放清單：https://www.youtube.com/playlist?list=PLf2m23nhTg1NjL3-jL3s0qZCYzO07ZQPv
```

**0.C 建立 NotebookLM 筆記本**

使用 `course_title` + `title_zh` 組合筆記本名稱（整堂課共用一個筆記本）：
```
筆記本名稱 = "<course_title> - 第 <NN> 課：<title_zh>"
例如：AI 素養：框架與基礎 - 第 03 課：深度探討一：什麼是生成式 AI？
```

```bash
PYTHONIOENCODING=utf-8 notebooklm create "<筆記本名稱>" --json 2>&1
```

記錄回傳的 Notebook ID。

**0.D 切換到新筆記本並加入所有影片來源**

```bash
PYTHONIOENCODING=utf-8 notebooklm use <新筆記本ID前8碼> 2>&1
```

加入 `videos[0]` 的影片來源：

```bash
PYTHONIOENCODING=utf-8 notebooklm source add "<videos[0].url>" --type youtube 2>&1
```

加入完成後執行 `notebooklm source list` 確認來源已就緒，再進入 Step 1。

**0.E 確認後跳至 Step 1**

記錄以下資訊供後續步驟使用：
- `COURSE_KEY`：如 `framework`
- `LESSON_NUM`：如 `03`（兩位數字串）
- `LESSON_TITLE`：`title_zh`
- `LESSON_DESC`：`description_zh`
- `TARGET_PAGE`：`nlm_page_pattern` 套用課號（如 `docs/ai-fluency/framework-nlm-03.md`）
- `MAIN_PAGE`：`main_page`（如 `docs/ai-fluency/framework-foundations.md`）

確認後繼續 **Step 1**（已在新筆記本中，可跳過 Step 2-3）。

---

### Step 0：從 Skilljar URL 建立新筆記本（若輸入為 URL）

若使用者提供的是 Skilljar 課程 URL（以 `https://` 開頭），執行以下流程：

**0.1 嘗試 WebFetch 提取影片標題：**

由於 Skilljar 頁面採動態載入且需要認證，WebFetch 通常無法取得影片標題。若失敗，請直接詢問使用者：
- 影片/課堂的標題（用來作為筆記本名稱）
- 影片來源（YouTube URL、直接 URL 或本地 .mp4 路徑）

**AI Fluency 課程影片參考來源（若 Skilljar 頁面無法取得影片 URL）：**

可根據課堂標題在以下 YouTube 播放清單中尋找對應影片：
- [AI Fluency Course YouTube 播放清單](https://www.youtube.com/playlist?list=PLf2m23nhTg1NjL3-jL3s0qZCYzO07ZQPv)

> 注意：此播放清單僅適用於 AI Fluency Course 課程內的影片。

**0.2 建立新筆記本：**
```bash
PYTHONIOENCODING=utf-8 notebooklm create "<影片標題>" --json 2>&1
```
記錄回傳的 Notebook ID。

**0.3 切換到新筆記本：**
```bash
PYTHONIOENCODING=utf-8 notebooklm use <新筆記本ID前8碼> 2>&1
```

**0.4 加入影片來源：**
```bash
# YouTube URL
PYTHONIOENCODING=utf-8 notebooklm source add "<youtube-url>" --type youtube 2>&1

# 一般 URL
PYTHONIOENCODING=utf-8 notebooklm source add "<url>" --type url 2>&1

# 本地檔案
PYTHONIOENCODING=utf-8 notebooklm source add "<local-path>" --type file --title "<標題>" 2>&1
```

確認來源加入後，繼續 Step 1（此時可跳過 Step 2-3，已在新筆記本中）。

### Step 1：確認 NotebookLM 登入狀態

```bash
PYTHONIOENCODING=utf-8 notebooklm status 2>&1
```

若未登入，提示使用者執行 `! notebooklm login`。

### Step 2：列出所有 Notebooks，找到目標

```bash
PYTHONIOENCODING=utf-8 notebooklm list --json 2>&1
```

根據使用者提供的名稱（模糊匹配）或 ID 找到目標 Notebook。輸出 Notebook ID 與標題供確認。

### Step 3：切換到目標 Notebook

```bash
PYTHONIOENCODING=utf-8 notebooklm use <ID前8碼> 2>&1
```

### Step 4：列出現有 Artifacts

```bash
PYTHONIOENCODING=utf-8 notebooklm artifact list --json 2>&1
```

記錄所有已完成的 artifacts，類型包括：
- `video` — 影片摘要
- `slide_deck` — 簡報
- `quiz` — 測驗
- `audio` — Podcast
- `mind_map` — 心智圖

### Step 5：下載素材

建立輸出目錄（依 notebook 標題命名，使用 kebab-case）：
```bash
OUTDIR=".claude/notebooklm-exports/<notebook-slug>"
mkdir -p "$OUTDIR"
```

依序下載可用的素材：
```bash
# 測驗（JSON + Markdown）
PYTHONIOENCODING=utf-8 notebooklm download quiz --format json "$OUTDIR/quiz.json" 2>&1
PYTHONIOENCODING=utf-8 notebooklm download quiz --format markdown "$OUTDIR/quiz.md" 2>&1

# 簡報
PYTHONIOENCODING=utf-8 notebooklm download slide-deck "$OUTDIR/slides.pdf" 2>&1

# Podcast（若有）
PYTHONIOENCODING=utf-8 notebooklm download audio "$OUTDIR/podcast.mp3" 2>&1
```

### Step 5.1（選用）：生成 Artifacts（若尚未生成）

若 Step 4 顯示尚無 `completed` 的 artifacts，先生成再下載。

**⚠️ 防止重複生成的標準流程（每種 artifact 類型都適用）：**

**Step 5.1a：檢查是否已有 in_progress 的簡報**

```bash
PYTHONIOENCODING=utf-8 notebooklm artifact list --json 2>&1
```

- 若已有 `status: "in_progress"` 的 `slide_deck`：**跳過 generate，直接進行 5.1b 等待**
- 若無任何 `slide_deck`（或只有 `completed` 的舊版英文簡報需重建）：執行 generate

**Step 5.1b：生成簡報（無 --wait，避免 Bash timeout）**

```bash
# 簡報（強制繁體中文輸出 + 品質提示詞）
PYTHONIOENCODING=utf-8 notebooklm generate slide-deck "請以繁體中文（Traditional Chinese）撰寫所有簡報內容，包含標題、說明文字、條列項目與補充說明。注意每個句子要語意完整，標點符號正確，避免字詞黏連或斷句錯誤。禁止使用英文，所有術語應以繁體中文呈現並可在括號內附上英文原文。" --json 2>&1
```

記錄回傳的 `artifact_id`（或從 `artifact list` 取得）。

**Step 5.1c：輪詢等待完成（每 30 秒檢查一次，最多等 10 分鐘）**

```bash
# 反覆執行，直到 status 變為 "completed"
PYTHONIOENCODING=utf-8 notebooklm artifact list --json 2>&1
```

- `status: "in_progress"` → 繼續等待，再次查詢
- `status: "completed"` → 進入 Step 5 下載
- 若超過 10 分鐘仍未完成 → 提示使用者確認 NotebookLM 後台狀態

**同理，測驗與影片摘要也使用相同的「先檢查再生成」流程：**

```bash
# 測驗（同樣先確認無 in_progress 才執行）
PYTHONIOENCODING=utf-8 notebooklm generate quiz --difficulty hard --json 2>&1

# 影片摘要（同樣先確認無 in_progress 才執行）
PYTHONIOENCODING=utf-8 notebooklm generate video "請以繁體中文（Traditional Chinese）撰寫所有影片摘要內容，包含標題、重點整理、條列項目與說明文字。注意每個句子要語意完整，標點符號正確，避免字詞黏連或斷句錯誤。禁止使用英文，所有術語應以繁體中文呈現並可在括號內附上英文原文。" --json 2>&1
```

生成完成後繼續 Step 5 下載。

### Step 5.5：將 slides.pdf 轉為圖片並嵌入 SlideViewer

使用 PyMuPDF（需 Python 3.10+）將每頁轉為 PNG：

```bash
py -3.11 -c "
import fitz, os, sys
sys.stdout.reconfigure(encoding='utf-8')
with fitz.open('$OUTDIR/slides.pdf') as doc:
    n = doc.page_count
    os.makedirs('$OUTDIR/slides', exist_ok=True)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=200)
        pix.save(f'$OUTDIR/slides/slide_{i+1:02d}.png')
print(f'OK: {n} slides')
"
```

接著使用 Read 工具讀取每張 PNG（Claude 多模態能力），判斷每頁是否符合**直接嵌入**條件：

| 條件 | 結果 |
|------|------|
| 繁體中文內容 + 無真實人臉 | ✅ 複製到 `docs/public/images/<category>/nlm<NN>-slide-NN-<semantic>.png` |
| 含英文文字 或 含真實人臉照片 | ❌ 使用 `.slide-card` CSS/HTML 元件以中文重製（不放入 SlideViewer） |

**命名規則**：`nlm<NN>-slide-<序號>-<語意名>.png`（序號為兩位數，語意名取英文小寫 kebab-case，例如 `delegation`、`interaction-spectrum`）。

**嵌入方式（SlideViewer 元件）**：

在 `<script setup>` 加入 slides 陣列：
```js
const nlmNNSlides = [
  { src: '/images/<category>/nlm<NN>-slide-01-<name>.png', caption: '<中文說明（25-60 字，凝練該頁核心訊息）>' },
  // ... 全部頁數
]
```

在簡報概覽區塊使用：
```markdown
## 📊 簡報概覽

::: tip 📊 簡報：<簡報標題>（由 NotebookLM 生成）
共 N 張投影片，使用左右按鈕或縮圖列切換；點擊主圖或全螢幕鈕可放大檢視。
:::

<SlideViewer :slides="nlmNNSlides" />
```

**規則補充**：
- **必須納入全部頁數**，不可只挑代表性的幾張
- 含真實人臉的頁面：改為 `.slide-card` HTML 元件，獨立列在 SlideViewer 上方或下方
- 第一次使用 `<SlideViewer>` 前，確認 `docs/.vitepress/theme/index.ts` 已有 `app.component('SlideViewer', SlideViewer)` 且 `SlideViewer.vue` 已存在於 `components/`

若 PyMuPDF 未安裝：`py -3.11 -m pip install pymupdf`

### Step 6：讀取 quiz.json，解析題目

從 `quiz.json` 提取：
- `title`：測驗標題
- `questions[].question`：題目文字
- `questions[].answerOptions[]`：選項（含 `text`、`isCorrect`、`rationale`）
- `questions[].hint`：提示

正確答案 index = `answerOptions` 中 `isCorrect: true` 的 0-based 索引。

### Step 7：找到對應的 VitePress 課程檔案

若使用者未指定課程路徑，根據 Notebook 標題進行推斷：
- 搜尋 `docs/` 目錄下所有 `.md` 檔案
- 比對檔案的 `title`、`description` frontmatter 或 H1 標題
- 同時尋找對應的 `-practice.md` 練習頁

確認找到的檔案後回報給使用者。

### Step 8：下載影片、讀取畫面、嵌入頁面

#### 8.a 下載影片到 exports 目錄

```bash
PYTHONIOENCODING=utf-8 notebooklm download video "$OUTDIR/video.mp4" 2>&1
```

#### 8.b 擷取 poster 封面圖（第 2 秒畫面）

```bash
PROJ_ROOT="<專案絕對路徑>"
CATEGORY="<分類目錄名，如 ai-fluency>"
NN="<課號，如 02>"

ffmpeg -i "$OUTDIR/video.mp4" \
  -ss 00:00:02 -vframes 1 -update 1 \
  "$PROJ_ROOT/docs/public/images/$CATEGORY/nlm${NN}-video-poster.png" -y 2>&1
```

#### 8.c 壓縮影片至 720p / CRF 28（≤ 10MB 後才 commit）

```bash
mkdir -p "$PROJ_ROOT/docs/public/videos/$CATEGORY"

ffmpeg -i "$OUTDIR/video.mp4" \
  -vcodec libx264 -crf 28 -preset medium \
  -vf "scale=-2:720" \
  -acodec aac -b:a 96k \
  "$PROJ_ROOT/docs/public/videos/$CATEGORY/nlm${NN}-summary.mp4" -y 2>&1
```

- 目標輸出 ≤ 10MB；若仍過大，將 `-crf` 調高至 30 或將解析度降為 540p（`scale=-2:540`）。
- 原始 `video.mp4` 留在 `$OUTDIR`（已 gitignore），**不 commit**。

> **影片資源放置規則**：壓縮後的 mp4 放 `docs/public/videos/<category>/nlm<NN>-summary.mp4`，poster 圖放 `docs/public/images/<category>/nlm<NN>-video-poster.png`，兩者都需 commit 進 git（非 gitignore 的 exports 目錄）。

#### 8.d 擷取關鍵畫面供 Claude 讀取（選用，用於生成文字摘要）

```bash
mkdir -p "$OUTDIR/frames"
ffmpeg -i "$OUTDIR/video.mp4" -vf "fps=1/5" "$OUTDIR/frames/frame_%03d.png" -y 2>&1
```

使用 Read 工具逐張讀取 PNG 畫面，萃取文字與視覺內容，整理成影片重點。

### Step 9：建立獨立 NLM 頁面

為本次課堂建立獨立的 NotebookLM 延伸學習頁面（每堂課一個 `.md` 檔）。

**檔案命名**：
- **課程編號模式**：使用 `TARGET_PAGE`（即 `nlm_page_pattern` 套用課號），例如 `docs/ai-fluency/framework-nlm-03.md`
- **其他模式**：`docs/<category>/<course-slug>-nlm-<NN>.md`，其中 `<course-slug>` 取課程主頁檔名第一段（如 `framework`）、`<NN>` 為兩位數課號

**頁面結構：**
```markdown
---
title: 'NLM 延伸：<課堂標題>'
description: 'Google NotebookLM 根據第 NN 課影片自動生成的延伸學習素材'
---

<script setup>
const nlmQ1Options = ["選項A", "選項B", "選項C", "選項D"]
// ... 依題數繼續（此頁從 nlmQ1Options 開始，獨立計號）
</script>

# 📓 第 NN 課：<課堂標題>

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[<課程名稱>](/<category>/<course-main-page>)

## 📋 課程概覽

### 第 NN 課：<課堂標題>

<LESSON_DESC>（來自 JSON 的 description_zh）

---

（🆕 課程編號模式專屬）

## 📖 課程大綱深度說明

（從主課程頁 MAIN_PAGE 萃取對應的 H3 標題 + `<details>` 深度說明區塊，完整複製。若主課程頁無對應區塊則省略此節。）

---

## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要：<課堂標題>
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<video controls preload="metadata" playsinline class="nlm-video" src="/videos/<category>/nlm<NN>-summary.mp4" poster="/images/<category>/nlm<NN>-video-poster.png" />

### 📝 影片重點整理

（根據影片畫面萃取的重點表格與金句。）

> **CSS 依賴**：第一次使用 `<video>` 嵌入前，確認 `docs/.vitepress/theme/custom.css` 已有 `.nlm-video` 樣式（深淺模式）：
> ```css
> .nlm-video {
>   width: 100%;
>   max-width: 860px;
>   border-radius: 12px;
>   box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
>   margin: 16px auto;
>   display: block;
>   background: var(--vp-c-bg-alt);
> }
> .dark .nlm-video {
>   box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
> }
> ```

## 📊 簡報概覽

::: tip 📊 簡報：<簡報標題>（由 NotebookLM 生成）
（簡短說明）
:::

（slide-card 元件 或 slide-image-gallery，依嵌入判斷規則）

## 🧪 延伸測驗

::: info 📌 關於這份測驗
以下 N 道題目由 Google NotebookLM 根據「<Notebook 標題>」自動生成。
:::

### 測驗 <課號>-1

<Quiz
  question="題目文字"
  :options="nlmQ1Options"
  :answer="正確答案索引"
  hint="提示文字（來自 questions[].hint）"
  explanation="解析文字（來自 rationale）"
/>
```

**測驗編號規則**：每個 NLM 頁面內部從 `測驗 <課號>-1` 開始（如第 03 課為 `3-1`、`3-2`；第 04 課為 `4-1`、`4-2`）。`nlmQ*Options` 陣列在各頁面內部從 `nlmQ1Options` 開始，互不干涉。

---

#### 🆕 課程編號模式專屬：Step 9.1 大綱搬遷

完成 NLM 頁面產出後，進行主課程頁的大綱搬遷：

**9.1.A 從主課程頁萃取課程大綱區塊**

使用 Read 工具讀取 `MAIN_PAGE`，找到對應 `### 第 <LESSON_NUM> 課：` H3 標題區塊（包含其下的 `<details>...</details>` 全部內容）。

若找不到對應區塊（如 01、02 課在主頁無 H3），跳過 9.1.B，僅在 NLM 頁的 `## 📋 課程概覽` 填入 `LESSON_DESC`。

**9.1.B 修改主課程頁**

將主課程頁中原有的 H3 + `<details>` 區塊替換為精簡版（標題 + 一行簡介 + 連結），格式如下：

```markdown
### 第 NN 課：<title_zh>

<description_zh>

→ [深度說明與 NotebookLM 延伸學習](./framework-nlm-NN.md)
```

**注意**：
- 保留區塊前後的空行，確保 H3 順序與 Markdown 結構不被破壞
- 僅替換對應課號的區塊，不動其他課號
- 若主課程頁的 `<details>` 區塊後還有 slide-card 等元件，保持原位不動

---

**課程主頁 NLM 導引連結處理**：
- 若課程主頁尚無 NLM 導引連結，在 `## 💡 學習建議` 之前加入：
  ```markdown
  ::: tip 📓 NotebookLM 延伸學習
  Google NotebookLM 已根據本課程影片自動生成濃縮學習素材：
  - [第 NN 課：<標題>](/<category>/<course-slug>-nlm-NN)
  :::
  ```
- 若已有導引區塊，在清單內追加新一行連結。

### Step 10：更新 Sidebar

每次建立新 NLM 頁面後，將連結插入 `docs/.vitepress/config.mts` 中**對應課程的最後一個 `└ 📓` 條目之後**（保持課號升序）：

```typescript
{ text: 'AI 素養：框架與基礎', link: '/ai-fluency/framework-foundations' },
{ text: '└ 🎯4D 互動練習', link: '/ai-fluency/4d-practice' },
{ text: '└ 📓 第 01 課：AI 素養簡介', link: '/ai-fluency/framework-nlm-01' },
{ text: '└ 📓 第 02 課：4D 框架詳解', link: '/ai-fluency/framework-nlm-02' },
// 新增（依課號順序插入）：
{ text: '└ 📓 第 03 課：深度探討一：什麼是生成式 AI？', link: '/ai-fluency/framework-nlm-03' },
```

**插入規則**：
- 新條目**依課號升序**插入現有 `└ 📓` 群組末尾
- `text` 格式：`└ 📓 第 <NN> 課：<title_zh>`（`title_zh` 取自 JSON 目錄檔）
- `link` 格式：`/ai-fluency/<course-key>-nlm-<NN>`（不含 `.md`）
- NLM 頁面屬於對應課程的延伸內容，放在課程項目底下，而非獨立分組

每道測驗題必須加入 `hint` prop（對應 `quiz.json` 的 `questions[].hint`）。若 `hint` 為空或 null，省略該 prop。

### Step 11：確認更新完成

回報：
- 已建立的 NLM 頁面路徑
- 已更新的 sidebar 項目
- 新增的題目數量
- 下載的素材清單與位置

---

## 注意事項

- 所有 `notebooklm` 指令必須加 `PYTHONIOENCODING=utf-8` 前綴（Windows 編碼問題）
- 使用 `--json` flag 取得結構化資料（避免 rich 渲染 Unicode 錯誤）
- 如果 artifact 尚未生成（status 非 `completed`），先執行 `generate` 指令再等待
- 不要修改 `docs/.vitepress/dist/`（建置產物）
- 練習頁的 Quiz 元件索引從 0 開始（`:answer="0"` 表示第一個選項）
- ffmpeg 需已安裝（`where ffmpeg` 確認）
- 影片摘要檔案需先用 ffmpeg 壓縮（CRF 28、720p、AAC 96k）再 commit 到 `docs/public/videos/<category>/`；原始 `video.mp4` 留在 `.claude/notebooklm-exports/`（已 gitignore），不進版控
- 所有 bash 命令使用**絕對路徑**（避免因 `cd` 造成相對路徑跑到錯誤目錄）
- 每課只支援單一影片來源；若課程有多支影片，請選擇主要影片，**不再支援多 source 自動合併流程**

### 重新生成同一課的「清空 → 放入」規則

每次為**同一課**重新生成 NotebookLM 內容時，必須採用「**先清空目標位置、再把新內容放進去**」的流程，禁止使用 `-v2`、`-new`、`-old` 等版本後綴並列。

**標準流程**：

1. **暫存可用內容**（若新內容已下載到別處，跳過此步）：將欲保留的素材複製到 `/tmp/nlm<NN>-backup/` 或專案外暫存區。

2. **清空 exports 目錄**：
   ```bash
   rm -rf .claude/notebooklm-exports/<notebook-slug>/
   rm -rf .claude/notebooklm-exports/<notebook-slug>-v2/   # 若有殘留也一併清掉
   mkdir -p .claude/notebooklm-exports/<notebook-slug>/
   ```

3. **清空該課所有 public 素材**：
   ```bash
   rm -f docs/public/images/<category>/nlm<NN>-slide-*.png
   rm -f docs/public/images/<category>/nlm<NN>-v2-slide-*.png   # 若有殘留也一併清掉
   rm -f docs/public/images/<category>/nlm<NN>-video-poster.png
   rm -f docs/public/videos/<category>/nlm<NN>-summary.mp4
   ```

4. **重新放入新內容**：簡報 PNG 用 `nlm<NN>-slide-NN-<semantic>.png` 命名；影片走 ffmpeg 壓縮輸出到固定路徑。

5. **頁面 (.md) 同步更新**：用 Edit 工具把 `script setup` 內的 `nlmNNSlides` 陣列重建，並 grep 全頁確認無殘留版本後綴字串。

6. **引用完整性檢查（必跑，任何 MISS 都要處理後才能 build）**：
   ```bash
   PAGE="docs/<category>/<page>.md"
   grep -oE '/(images|videos)/[a-zA-Z0-9./_-]+\.(png|jpg|jpeg|webp|mp4)' "$PAGE" \
     | sort -u \
     | while read ref; do
         [ -f "docs/public${ref}" ] && echo "OK  $ref" || echo "MISS $ref"
       done
   ```

7. **build 驗證**：`npm run docs:build` 通過，無 dead link、無 Vue parser 警告。

> **為何禁用版本後綴**：每課累積 v2、v3、v4 會讓 `docs/public/` 迅速失控；同名覆蓋搭配 git history 即可追溯歷史，引用完整性檢查確保網站不會指向已清空的素材。

### 中英文處理規則

從 NotebookLM 素材擷取的英文內容，依類型採用不同處理方式：

#### 步驟 / 條列項目 → 只保留中文，刪除英文

英文步驟名稱與說明句直接翻譯為中文，原英文刪除。格式：`步驟N 中文名稱：中文說明`

```markdown
<!-- ✅ 正確：只顯示中文 -->
步驟1 委派：何時由人類執行？何時交給 AI？
步驟2 描述：如何與 AI 系統進行清晰、有效的溝通？

<!-- ❌ 不可：保留英文步驟 -->
Step 1 Delegation — When should humans do work and when should AI?
委派：何時由人類執行？何時交給 AI？
```

#### 引言 / 金句 → 只保留中文翻譯，刪除英文原文

引言直接以中文呈現，英文原文刪除。

```markdown
<!-- ✅ 正確：只顯示中文翻譯 -->
> 「以有效、高效、合乎道德且安全的方式與 AI 系統互動的能力。」

<!-- ❌ 不可：保留英文原文 -->
> *"The ability to engage with AI systems in ways that are effective, efficient, ethical, and safe."*
> 「以有效、高效、合乎道德且安全的方式與 AI 系統互動的能力。」
```

#### 標題標籤（如 What You Gain）→ 刪除英文標籤，只保留中文說明

```markdown
<!-- ✅ 正確 -->
學完這門課你將獲得：

<!-- ❌ 不可：保留英文標籤 -->
**What You Gain**（影片畫面）
學完這門課你將獲得：
```

#### 表格欄位 → 英文在前，中文括號補充（表格無法換行）

```markdown
| 思維轉變 | **THINKING ABOUT AI → THINKING WITH AI**（從旁觀者到協作者） |
```

---

## 生成新 Artifact（如尚未存在）

```bash
# 生成測驗
PYTHONIOENCODING=utf-8 notebooklm generate quiz --difficulty hard 2>&1

# 生成簡報
PYTHONIOENCODING=utf-8 notebooklm generate slide-deck 2>&1

# 生成影片摘要（繁體中文）
PYTHONIOENCODING=utf-8 notebooklm generate video "請以繁體中文（Traditional Chinese）撰寫所有影片摘要內容，包含標題、重點整理、條列項目與說明文字。注意每個句子要語意完整，標點符號正確，避免字詞黏連或斷句錯誤。禁止使用英文，所有術語應以繁體中文呈現並可在括號內附上英文原文。" --json 2>&1

# 生成 Podcast
PYTHONIOENCODING=utf-8 notebooklm generate audio "make it engaging" --wait 2>&1

# 等待完成
PYTHONIOENCODING=utf-8 notebooklm artifact wait <artifact-id> 2>&1
```
