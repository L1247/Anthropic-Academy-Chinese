# 字幕 VTT 變體規範

## 字幕產生流程概覽

`video-subtitle` skill 使用 faster-whisper 轉錄 + Claude API 翻譯，自動在 `.claude/notebooklm-exports/<course>/` 產出以下 5 個檔案：

| 檔案名稱 | 內容 | 用途 |
|---|---|---|
| `video.en.srt` | 純英文字幕（轉錄原始） | 來源真相，可重跑翻譯時快取 |
| `video.zh-Hant.srt` | 雙語 SRT（英上中下） | 備份、手動檢查 |
| `video.zh-Hant.vtt` | 雙語 VTT（英上中下） | 雙語軌道原始檔 |
| `video.zh-Hant-only.vtt` | **純繁體中文** VTT | 發布用：繁中字幕軌道 |
| `video.en.vtt` | **純英文** VTT | 發布用：英文字幕軌道 |

## 發布到課程頁時的命名規則

複製到 `docs/public/videos/<course-name>/` 時，三份 VTT 須依下列規則重新命名：

| raw export 檔名 | 發布命名 | 對應 `<NlmVideo>` prop |
|---|---|---|
| `video.zh-Hant-only.vtt` | `<name>.zh-Hant.vtt` | `zh-vtt` |
| `video.en.vtt` | `<name>.en.vtt` | `en-vtt` |
| `video.zh-Hant.vtt` | `<name>.bilingual.vtt` | `bi-vtt` |

> **注意**：raw export 的 `video.zh-Hant.vtt` 是**雙語內容**，命名有點混淆。  
> 發布時務必改名為 `bilingual.vtt`，並將純繁中的 `zh-Hant-only.vtt` 命名為 `zh-Hant.vtt`。

## 整合到課程頁的 NlmVideo 標準嵌入碼

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

- `zh-vtt`（必填）：純繁中字幕
- `en-vtt`（選填）：純英文字幕；省略時字幕選單中「英文」選項為 disabled
- `bi-vtt`（選填）：中英雙語字幕；省略時「中英」選項為 disabled
- `default-mode`：預設語系（`zh` / `en` / `bi` / `off`），預設為 `zh`

## 字幕選單 UX

點擊控制列的 **CC** 按鈕彈出選單，提供：
1. 繁中（`zh-vtt` prop 存在時啟用）
2. 英文（`en-vtt` prop 存在時啟用）
3. 中英（`bi-vtt` prop 存在時啟用）
4. 無字幕（永遠可選）

選單內可調整字幕字級（14–40px），預設 24px，設定值自動存入 localStorage。
