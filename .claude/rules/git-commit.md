---
# 全域規則，無 paths 限制
---

# Git Commit 規則

## Commit Message 格式

```
type: 簡短描述（繁體中文，50 字以內）
```

## Type 類型

| Type | 用途 | 範例 |
|------|------|------|
| `docs` | 新增或修改課程內容 | `docs: 新增 MCP 進階課程頁面` |
| `feat` | 新增網站功能 | `feat: 加入本地搜尋功能` |
| `fix` | 修正錯誤（連結失效、內容錯誤） | `fix: 修正 sidebar 開發者課程連結` |
| `style` | 排版、格式調整（不影響內容） | `style: 統一課程難度標示格式` |
| `chore` | 設定檔、依賴更新 | `chore: 更新 VitePress 至 1.7.0` |
| `refactor` | 重構內容結構（不新增功能） | `refactor: 拆分 resources.md 為多頁` |

## 禁止 commit 的檔案
- `docs/.vitepress/dist/`（建置產物）
- `node_modules/`
- `.env`（若未來新增）
