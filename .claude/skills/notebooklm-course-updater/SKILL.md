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

若 Step 4 顯示尚無 `completed` 的 artifacts，先生成再下載。**簡報生成時加入中文品質提示詞**：

```bash
# 簡報（含中文品質提示詞，減少句子黏連與斷句錯誤）
PYTHONIOENCODING=utf-8 notebooklm generate slide-deck "注意每個句子要語意完整，標點符號正確，避免字詞黏連或斷句錯誤。" --wait --json 2>&1

# 測驗
PYTHONIOENCODING=utf-8 notebooklm generate quiz --difficulty hard --wait --json 2>&1

# 影片摘要
PYTHONIOENCODING=utf-8 notebooklm generate video --wait --json 2>&1
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

### Step 9：更新課程主頁（`*-foundations.md` 或主頁）

**先偵測頁面是否已有 NotebookLM 區塊：**

- **新建模式**（頁面無 `## 📺 NotebookLM 生成學習素材`）：在「💡 學習建議」或「📝 重點筆記」區塊之前插入完整區塊
- **追加模式**（頁面已有此區塊）：在現有區塊內，先將現有內容用 `### <第 XX 課 標題>` 子標題包住，再新增一個 `### <新課堂標題>` 子章節

**新建模式格式：**
```markdown
## 📺 NotebookLM 生成學習素材

::: info 🎬 影片摘要
（根據影片畫面萃取的完整摘要，含關鍵引言與故事結構）
:::

::: tip 📊 簡報概覽
（根據 slide_deck 生成的重點表格）
:::

::: tip 🧪 延伸測驗
NotebookLM 自動生成 N 道繁體中文測驗題。
前往 [練習頁 → NotebookLM 延伸測驗](練習頁連結#notebooklm-延伸測驗) 立即挑戰。
:::
```

**追加模式格式（現有區塊追加子章節）：**
```markdown
## 📺 NotebookLM 生成學習素材

### 第 01 課：<原有課堂標題>

（原有內容不動）

---

### 第 XX 課：<新課堂標題>

::: info 🎬 影片摘要
（新課堂影片摘要）
:::

::: tip 📊 簡報概覽
（新課堂簡報重點）
:::

::: tip 🧪 延伸測驗
NotebookLM 自動生成 N 道繁體中文測驗題。
前往 [練習頁 → NotebookLM 延伸測驗：第 XX 課](練習頁連結#notebooklm-延伸測驗-第xx課) 立即挑戰。
:::
```

### Step 10：更新練習頁（`*-practice.md`）

**先偵測是否已有 NotebookLM 測驗區塊：**

- **新建模式**（無現有 NotebookLM 測驗）：在 `<script setup>` 加入 `nlmQ1Options` 起的選項陣列，在頁面末尾新增測驗區塊
- **追加模式**（已有 `## 🎓 NotebookLM 延伸測驗`）：在 `<script setup>` **追加**新選項陣列（接續現有編號），在頁面末尾**追加**新的測驗子區塊

**在 `<script setup>` 區塊**加入選項陣列（新建從 `nlmQ1Options`，追加接續現有最後一個編號）：
```js
const nlmQ1Options = ["選項A", "選項B", "選項C", "選項D"]
// ... 依題數繼續
```

**在頁面末尾**（`💡 練習後建議` 之前）加入：

新建模式：
```markdown
---

## 🎓 NotebookLM 延伸測驗 {#notebooklm-延伸測驗}

::: info 📌 關於這份測驗
以下 N 道題目由 Google NotebookLM 根據「<Notebook 標題>」自動生成。
:::

### 測驗 N-1

<Quiz
  question="題目文字"
  :options="nlmQ1Options"
  :answer="正確答案索引"
  hint="提示文字（來自 questions[].hint）"
  explanation="解析文字（來自 rationale）"
/>
```

追加模式（在現有測驗區塊末尾新增子區塊）：
```markdown
---

## 🎓 NotebookLM 延伸測驗：第 XX 課 {#notebooklm-延伸測驗-第xx課}

::: info 📌 關於這份測驗
以下 N 道題目由 Google NotebookLM 根據「<新 Notebook 標題>」自動生成。
:::

### 測驗 N-1

<Quiz
  question="題目文字"
  :options="nlmQNOptions"
  :answer="正確答案索引"
  hint="提示文字（來自 questions[].hint）"
  explanation="解析文字（來自 rationale）"
/>
```

每道題目都必須加入 `hint` prop（對應 `quiz.json` 的 `questions[].hint` 欄位），讓使用者可以點擊提示按鈕查看。若該題目的 `hint` 為空字串或 null，則省略 `hint` prop。

### Step 11：確認更新完成

回報：
- 已更新的檔案清單
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

# 生成 Podcast
PYTHONIOENCODING=utf-8 notebooklm generate audio "make it engaging" --wait 2>&1

# 等待完成
PYTHONIOENCODING=utf-8 notebooklm artifact wait <artifact-id> 2>&1
```
