---
name: video-subtitle
description: 為 .claude/notebooklm-exports/ 中的課程影片自動產生雙語字幕（英文 + 繁中 SRT/VTT），使用 faster-whisper 轉錄 + Claude API 翻譯。
triggers:
  - /subtitle
  - /video-subtitle
user-invocable: true
---

# 影片字幕產生 Skill

## 使用方式

```
/subtitle                                          # 批次處理所有未完成的影片
/subtitle <course-name>                            # 指定課程名稱（目錄名）
/subtitle <course-name> --force                    # 強制重跑（覆寫已有字幕）
/subtitle --skip-translate                         # 只產英文字幕（不需 API Key）
/subtitle <course-name> --model large-v3           # 使用較大模型
```

**範例：**
```
/subtitle
/subtitle 4ds-ai-fluency
/subtitle the-4d-framework --force
/subtitle 4ds-ai-fluency --skip-translate
```

---

## 執行步驟

### Step 1：解析參數

從使用者輸入解析以下參數：

| 參數 | 說明 | 預設值 |
|---|---|---|
| `<course-name>` | notebooklm-exports 下的目錄名稱，省略則批次處理全部 | — |
| `--force` | 強制重跑，覆寫已有字幕 | false |
| `--skip-translate` | 跳過翻譯，只產英文 SRT/VTT | false |
| `--model` | Whisper 模型大小 | `medium` |
| `--device` | 推論裝置 | `auto` |

---

### Step 2：確認環境

**2a. 確認 SCRIPT_DIR**

腳本位於：`.claude/scripts/subtitle/generate_subtitles.py`

**2b. 確認 Python venv**

檢查 `.claude/scripts/subtitle/.venv/` 是否存在：

```bash
# 如果不存在，先建立並安裝
python -m venv ".claude/scripts/subtitle/.venv"
".claude/scripts/subtitle/.venv/Scripts/pip" install -r ".claude/scripts/subtitle/requirements.txt"
```

> 首次執行會下載 Whisper medium 模型（約 1.5 GB），請耐心等候。

**2c. 確認影片存在**

若指定了 `<course-name>`，確認 `.claude/notebooklm-exports/<course-name>/video.mp4` 存在。
若找不到，列出現有的課程目錄供使用者選擇。

**2d. 確認 API Key（若非 --skip-translate）**

檢查環境變數 `ANTHROPIC_API_KEY` 是否設定。若未設定，提示使用者：
```
請先設定 API Key：export ANTHROPIC_API_KEY=sk-ant-...
或使用 --skip-translate 跳過翻譯步驟。
```
直接詢問使用者是否繼續（只產英文字幕）或中止。

---

### Step 3：組合指令並執行

依解析的參數組合 CLI 指令：

```bash
# 批次處理
".claude/scripts/subtitle/.venv/Scripts/python" \
  ".claude/scripts/subtitle/generate_subtitles.py" \
  [--force] [--model MODEL] [--device DEVICE] [--skip-translate]

# 指定單一課程
".claude/scripts/subtitle/.venv/Scripts/python" \
  ".claude/scripts/subtitle/generate_subtitles.py" \
  --input ".claude/notebooklm-exports/<course-name>/video.mp4" \
  [--force] [--model MODEL] [--device DEVICE] [--skip-translate]
```

以 Bash 工具執行。影片轉錄需時較長（medium 模型約 1:1 即時比），耐心等候。

---

### Step 4：報告結果

執行完成後，根據腳本輸出的摘要表，整理回報：

1. **成功的課程**：列出產出的檔案（`video.en.srt`、`video.zh-Hant.srt`、`video.zh-Hant.vtt`）
2. **跳過的課程**：說明原因（已有 .vtt）
3. **失敗的課程**：顯示錯誤原因並提供排解建議

若產出了 `.vtt` 檔案，提示整合到 VitePress 的下一步（可用 `/subtitle-embed <course-name>` 觸發嵌入，見下方附錄）。

成功回報範例（三份 VTT 產出）：
- `video.en.srt`
- `video.zh-Hant.srt`（雙語 SRT）
- `video.zh-Hant.vtt`（雙語 VTT：英上中下）
- `video.zh-Hant-only.vtt`（純繁中 VTT）
- `video.en.vtt`（純英文 VTT）

---

## 附錄：產出的字幕整合到 VitePress 頁面

> 此步驟**不在本 Skill 自動執行範圍內**，須手動確認後再操作。

字幕驗證無誤後，若要在課程頁面嵌入播放器：

1. 將 `video.mp4`、`video.zh-Hant-only.vtt`、`video.en.vtt`、`video.zh-Hant.vtt` 複製到 `docs/public/videos/<course-name>/`，並依課程命名慣例重新命名（如 `nlm01-summary.*.vtt`）。
2. 命名對應規則：
   - `video.zh-Hant-only.vtt` → `<name>.zh-Hant.vtt`（對應 `zh-vtt` prop，純繁中）
   - `video.en.vtt`            → `<name>.en.vtt`（對應 `en-vtt` prop，純英文）
   - `video.zh-Hant.vtt`       → `<name>.bilingual.vtt`（對應 `bi-vtt` prop，雙語）
3. 在課程 Markdown 頁面插入 `<NlmVideo>` 元件：

```html
<NlmVideo
  src="/videos/<course-name>/<name>.mp4"
  poster="/images/<course-name>/<name>-poster.png"
  zh-vtt="/videos/<course-name>/<name>.zh-Hant.vtt"
  en-vtt="/videos/<course-name>/<name>.en.vtt"
  bi-vtt="/videos/<course-name>/<name>.bilingual.vtt"
  default-mode="zh"
/>
```

4. `npm run docs:dev` 驗證播放、三種字幕語系切換、字幕大小調整及播放速度控制均正常。

> **注意**：`video.mp4` 檔案較大，建議放 CDN 後只保留 `.vtt` 進 git；或將 `docs/public/videos/` 加入 `.gitignore`。
