---
paths:
  - "docs/**"
---

# 外部連結安全規則

## HTTPS 強制
- 所有外部連結必須使用 `https://`，不接受 `http://`

## 新分頁安全屬性
- 在 Markdown 中使用 HTML `<a>` 標籤開啟新分頁時，必須加上 `rel="noopener noreferrer"`
  ```html
  <!-- ✅ 正確 -->
  <a href="https://example.com" target="_blank" rel="noopener noreferrer">連結</a>
  
  <!-- ❌ 缺少 rel，有 tab-napping 風險 -->
  <a href="https://example.com" target="_blank">連結</a>
  ```
- VitePress Markdown 語法 `[文字](URL)` 不開新分頁，不需加 rel

## API Key 範例
- 課程內容中出現的 API Key 範例一律使用虛構值，如 `sk-ant-xxxxx`
- 禁止出現任何真實的 `sk-ant-` 開頭金鑰

## 信任網域
課程中引用的外部資源應限於以下可信任網域：
- `anthropic.com`（含子網域）
- `claude.ai`
- `github.com/anthropics`
- `docs.anthropic.com`
- 知名學術或教育機構網域

若需連結到其他網域，請在 PR / commit 說明中說明原因。
