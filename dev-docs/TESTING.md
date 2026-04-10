# 測試規範

## 測試現況

本專案為純靜態文件網站，**目前沒有自動化測試框架**。品質驗證依賴以下手動流程。

## 建置驗證（必做）

每次對 `config.mts` 或課程結構進行修改後，執行建置確認無錯誤：

```bash
npm run docs:build
```

常見建置錯誤：
- **Dead links**：VitePress 建置時會報告失效連結（sidebar link 與實際檔案不符）
- **Mermaid 語法錯誤**：圖表語法有誤時建置會警告
- **Frontmatter 錯誤**：YAML 格式不正確時會失敗

## 本地預覽驗證

```bash
npm run docs:dev
```

新增或修改頁面後，在瀏覽器確認：

- [ ] 頁面正確顯示，無版面跑版
- [ ] sidebar 連結正確且可點擊
- [ ] Mermaid 流程圖正常渲染
- [ ] 課程總覽表格連結有效
- [ ] 搜尋功能可找到新內容

## 新增課程的驗證清單

新增課程頁面後，確認以下項目：

- [ ] `config.mts` sidebar 已更新，連結指向正確路徑（無 `.md`）
- [ ] `docs/index.md` 課程總覽表格已新增該課程
- [ ] `dev-docs/FEATURES.md` 課程清單已更新
- [ ] 建置無錯誤（`npm run docs:build`）
- [ ] 分類 `index.md` 已加入課程卡片（若適用）

## 未來可考慮加入的測試

若內容規模擴大，可考慮：
- **連結驗證**：使用 `markdown-link-check` 批次驗證所有內部 / 外部連結
- **Lighthouse CI**：自動化效能與 SEO 檢查
