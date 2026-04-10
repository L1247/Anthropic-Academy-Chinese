---
title: Claude Code 實戰
description: 將 Claude Code 深度整合進開發工作流程，涵蓋工具系統、上下文管理和 GitHub 整合
---

# Claude Code 實戰

<Badge type="warning" text="⭐⭐ 中級" /> <Badge type="info" text="開發者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)（英文）

## 課程簡介

本課程是 [Claude Code 101](/claude-products/claude-code-101) 的進階延伸，聚焦於**實際的開發工作流程整合**。如果說 Claude Code 101 是「學開車」，這門課就是「在真實道路上駕駛」。

課程涵蓋 Claude Code 的工具系統架構、進階上下文管理、視覺輸入工作流程、GitHub 自動化，以及如何在不同複雜度的任務中選擇正確的思考模式。

## 前置條件

::: warning 前置條件
- **命令列介面操作**（能夠在終端機使用基本指令）
- **Git 基礎**（能夠執行 commit、push、PR 等操作）
- 建議已完成 [Claude Code 101](/claude-products/claude-code-101)
:::

## 學習目標

完成本課程後，你將能夠：

1. 理解 **Claude Code 工具系統**的底層架構
2. 掌握**上下文管理技術**，維持任務相關性
3. 使用**視覺輸入**進行介面設計和規劃
4. 建立可重用的**自訂命令（Slash Commands）**
5. 整合 **MCP 伺服器**擴展功能（如瀏覽器自動化）
6. 設定 **GitHub 工作流程**：自動程式碼審查和 PR 助手
7. 選擇正確的**思考和規劃模式**

## 課程大綱

### 單元一：工具系統架構
- Claude Code 有哪些內建工具？
- 工具如何讓 Claude 「看到」你的程式碼庫
- 工具呼叫的執行流程
- 工具的成本（上下文消耗）考量

### 單元二：上下文管理進階
- 有效引用程式碼和檔案的技巧
- 使用 `@` 符號引用特定檔案
- 何時使用 `/clear` 和 `/compact`
- 維持長任務的相關上下文

### 單元三：視覺輸入工作流程
- 上傳設計稿讓 Claude 實作 UI
- 截圖除錯：讓 Claude 看到問題
- 結合思考模式和視覺輸入的進階規劃

### 單元四：自訂命令
- 什麼是 Slash Commands？
- 在 CLAUDE.md 中定義自訂命令
- 建立可重用的工作流程命令範例

### 單元五：MCP 伺服器整合
- 在 Claude Code 中配置 MCP Server
- 瀏覽器自動化整合（Playwright MCP）
- 資料庫查詢整合
- 外部 API 整合

### 單元六：GitHub 整合
- 設定 GitHub Actions 中的 Claude Code
- 自動程式碼審查工作流程
- PR 描述自動生成
- Issue 分類和回應

### 單元七：思考和規劃模式
- 一般模式 vs. 思考模式（Think Mode）
- 何時啟用擴展思考（Extended Thinking）
- 計畫模式（Plan Mode）的最佳使用時機
- 不同複雜度任務的模式選擇策略

## 重點筆記

### Claude Code 工具系統

Claude Code 內建的工具類型：

| 工具類型 | 用途 |
|---------|------|
| **讀取工具** | 讀取檔案、列出目錄、搜尋程式碼 |
| **寫入工具** | 建立/修改/刪除檔案 |
| **執行工具** | 執行終端指令、執行測試 |
| **網路工具** | 搜尋文件、抓取網頁 |
| **MCP 工具** | 透過 MCP Server 連接的外部工具 |

### 有效的上下文管理策略

```bash
# 引用特定檔案（@符號）
> 請看 @src/api/users.py 和 @src/models/user.py，
> 優化這兩個檔案之間的資料流

# 重置上下文（任務完成後）
> /clear

# 壓縮上下文（任務進行中但上下文太長）
> /compact
```

### GitHub 自動程式碼審查設定

```yaml
# .github/workflows/code-review.yml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Claude Code Review
        run: |
          claude -p "請審查這個 PR 的程式碼變更，
          指出潛在的 bug、效能問題和可讀性改善空間"
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## 學習建議

**搭配學習：**
- 先完成 [Claude Code 101](/claude-products/claude-code-101)
- 結合 [MCP 入門](/developer/mcp-intro) 擴展工具能力
- 之後學習 [Agent Skills 入門](/developer/agent-skills) 建立可重用技能

**實作練習：**
1. 在你的一個真實專案中安裝 Claude Code，讓它解釋整個專案架構
2. 設定 Playwright MCP，讓 Claude 能夠幫你測試網頁功能
3. 建立一個自訂命令 `/review`，讓 Claude 自動審查最近的程式碼變更

## 相關課程

- [Claude Code 101](/claude-products/claude-code-101)（基礎，建議先修）
- [MCP 入門](/developer/mcp-intro)（擴展工具系統）
- [Agent Skills 入門](/developer/agent-skills)（建立可重用技能）
- [子代理入門](/developer/subagents)（委派複雜子任務）
