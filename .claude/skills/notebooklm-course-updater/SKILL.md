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
```

**範例：**
```
/notebooklm-update "The 4Ds of AI Fluency"
/notebooklm-update 208e3044 docs/ai-fluency/framework-foundations.md
/notebooklm-update https://anthropic.skilljar.com/ai-fluency-framework-foundations/291876
```

---

## 執行步驟

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

### Step 5.5：將 slides.pdf 轉為圖片並判斷是否可直接嵌入

使用 PyMuPDF（需 Python 3.10+）將每頁轉為 PNG：

```bash
py -3.11 -c "
import fitz, os
doc = fitz.open('$OUTDIR/slides.pdf')
os.makedirs('$OUTDIR/slides', exist_ok=True)
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=200)
    pix.save(f'$OUTDIR/slides/slide_{i+1:02d}.png')
doc.close()
"
```

接著使用 Read 工具讀取每張 PNG（Claude 多模態能力），判斷每頁是否符合**直接嵌入**條件：

| 條件 | 結果 |
|------|------|
| 繁體中文內容 + 無真實人臉 | ✅ 複製到 `docs/public/images/<category>/` 直接嵌入 |
| 含英文文字 或 含真實人臉照片 | ❌ 使用 `.slide-card` CSS/HTML 元件以中文重製 |

**嵌入語法**（Markdown）：
```markdown
![簡報說明文字](/images/<category>/slide-XX-<name>.png)
```

**容器樣式**（搭配 custom.css 的 `.slide-image-gallery` / `.slide-image-item`）：
```html
<div class="slide-image-gallery">
  <div class="slide-image-item">
    <img src="/images/<category>/slide-XX.png" alt="說明" loading="lazy" />
    <div class="slide-image-caption">簡短中文說明</div>
  </div>
</div>
```

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

### Step 8：讀取影片畫面（若有 video artifact）

下載影片並用 ffmpeg 擷取關鍵畫面：
```bash
PYTHONIOENCODING=utf-8 notebooklm download video "$OUTDIR/video.mp4" 2>&1
mkdir -p "$OUTDIR/frames"
ffmpeg -i "$OUTDIR/video.mp4" -vf "fps=1/5" "$OUTDIR/frames/frame_%03d.png" -y 2>&1
```

使用 Read 工具逐張讀取 PNG 畫面，萃取文字與視覺內容，整理成影片摘要。

### Step 9：建立獨立 NLM 頁面

為本次課堂建立獨立的 NotebookLM 延伸學習頁面（每堂課一個 `.md` 檔）。

**檔案命名**：`docs/<category>/<course-slug>-nlm-<NN>.md`
- `<course-slug>`：取課程主頁檔名的第一段（如 `framework` 來自 `framework-foundations`）
- `<NN>`：兩位數課號（如 `01`、`02`）

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

## 🎬 影片摘要

::: info 🎬 影片摘要：<影片標題>
（根據影片畫面萃取的完整摘要，含關鍵引言與故事結構）
:::

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

**測驗編號規則**：每個 NLM 頁面內部從 `測驗 <課號>-1` 開始（如第 01 課為 `1-1`、`1-2`；第 02 課為 `2-1`、`2-2`）。`nlmQ*Options` 陣列在各頁面內部從 `nlmQ1Options` 開始，互不干涉。

**課程主頁處理**：
- 若課程主頁尚無 NLM 導引連結，在 `## 💡 學習建議` 之前加入：
  ```markdown
  ::: tip 📓 NotebookLM 延伸學習
  Google NotebookLM 已根據本課程影片自動生成濃縮學習素材：
  - [第 NN 課：<標題>](/<category>/<course-slug>-nlm-NN)
  :::
  ```
- 若已有導引區塊，在清單內追加新一行連結。

### Step 10：更新 Sidebar

每次建立新 NLM 頁面後，將連結插入 `docs/.vitepress/config.mts` 中**對應課程的 items 清單**，緊接在該課程的互動練習連結（`└ 🎯`）之後：

```typescript
{ text: 'AI 素養：框架與基礎', link: '/ai-fluency/framework-foundations' },
{ text: '└ 🎯4D 互動練習', link: '/ai-fluency/4d-practice' },
{ text: '└ 📓 第 01 課：AI 素養簡介', link: '/ai-fluency/framework-nlm-01' },
{ text: '└ 📓 第 02 課：4D 框架詳解', link: '/ai-fluency/framework-nlm-02' },
// 新增：
{ text: '└ 📓 第 NN 課：<標題>', link: '/ai-fluency/<course-slug>-nlm-NN' },
```

NLM 頁面屬於對應課程的延伸內容，應放在課程項目底下，而非獨立分組。

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
