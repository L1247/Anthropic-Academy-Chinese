# 影片字幕產生器

為 `.claude/notebooklm-exports/` 中的英文課程影片自動產生雙語（英文 + 繁中）字幕。

## 產出檔案

每支影片目錄下會新增：

```
video.en.srt          # 英文原文（Whisper 轉錄）
video.zh-Hant.srt     # 雙語：英文上、繁中下
video.zh-Hant.vtt     # WebVTT 格式（供 HTML5 <video><track> 使用）
```

## 環境設定

### 1. 建立 Python 虛擬環境（建議 Python 3.11）

```bash
cd .claude/scripts/subtitle
python -m venv .venv
# Windows bash
.venv/Scripts/activate
# macOS/Linux
source .venv/bin/activate
```

### 2. 安裝依賴

```bash
pip install -r requirements.txt
```

> 首次執行時 faster-whisper 會自動下載 Whisper 模型（medium ≈ 1.5 GB）。

### 3. 設定 API Key

翻譯功能需要 Anthropic API Key：

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

或在 Windows PowerShell：

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

## 使用方式

### 批次處理所有影片

```bash
python generate_subtitles.py
```

已有 `.vtt` 的影片自動跳過（冪等）。

### 指定單一影片

```bash
python generate_subtitles.py --input ../../notebooklm-exports/4ds-ai-fluency/video.mp4
```

### 強制重跑（覆寫已有字幕）

```bash
python generate_subtitles.py --force
# 或指定單一影片
python generate_subtitles.py --input ../../notebooklm-exports/the-4d-framework/video.mp4 --force
```

### 只產英文字幕（跳過翻譯，不需 API Key）

```bash
python generate_subtitles.py --skip-translate
```

### 使用較大模型提高準確度

```bash
python generate_subtitles.py --model large-v3
```

## 完整參數

| 參數 | 預設 | 說明 |
|---|---|---|
| `--input PATH` | — | 指定單一影片（mp4 或含 video.mp4 的目錄） |
| `--force` | false | 強制重跑，覆寫已有字幕 |
| `--model` | `medium` | Whisper 模型大小（tiny/base/small/medium/large-v2/large-v3） |
| `--device` | `auto` | 推論裝置（auto/cpu/cuda） |
| `--skip-translate` | false | 跳過翻譯，只產英文 SRT/VTT |

## 整合到 VitePress 頁面

字幕產出後，在課程 Markdown 頁面插入原生 HTML：

```html
<video controls width="100%" style="border-radius: 8px;">
  <source src="/videos/<course>/video.mp4" type="video/mp4">
  <track default kind="subtitles" srclang="zh-Hant"
         src="/videos/<course>/video.zh-Hant.vtt" label="繁中＋英文">
</video>
```

> 注意：需將 `video.mp4` 和 `video.zh-Hant.vtt` 複製到 `docs/public/videos/<course>/`，
> 或將影片放 CDN 只保留 `.vtt` 在 git 中。

## 疑難排解

### `faster-whisper` 無法找到 CUDA

安裝 GPU 版：
```bash
pip install faster-whisper
# 如需 CUDA 支援另安裝 torch：
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

或改用 CPU：
```bash
python generate_subtitles.py --device cpu
```

### Claude API 回傳解析失敗

腳本會自動重試 2 次。若持續失敗，可先用 `--skip-translate` 取得英文字幕，
再手動執行 `translate.py` 單獨測試。

### FFmpeg 找不到

確認 FFmpeg 在 `PATH` 中：
```bash
ffmpeg -version
```
