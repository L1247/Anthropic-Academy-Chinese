---
title: Claude Cowork 入門
description: 學習與 Claude 協作處理真實的本地檔案、資料夾和應用程式
---

# Claude Cowork 入門

<Badge type="tip" text="⭐ 初學者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork)（英文）

## 課程簡介

Claude Cowork 是 Claude 的**桌面協作工具**，讓 Claude 能夠直接與你的本地檔案、資料夾和應用程式互動——閱讀文件、編輯內容、產生真實輸出。

不同於 claude.ai 的網頁版聊天介面，Cowork 讓 Claude 能夠真正「看到」和「操作」你電腦上的檔案，執行端到端的任務。

## 前置條件

::: info 前置條件
**無需技術背景。** 任何能夠使用桌面應用程式的人都可以學習。
:::

## 學習目標

完成本課程後，你將能夠：

- 從零開始安裝並設定 Claude Cowork
- 理解 **Cowork 任務循環**（Task Loop）的運作方式
- 配置適合你工作的**插件（Plugins）和技能（Skills）**
- 使用 Cowork 執行**檔案工作流程**
- 進行**研究與資訊彙整**工作流程
- 引導 Claude 負責任地完成**多步驟長任務**

## 課程大綱

### 單元一：認識 Claude Cowork
- Cowork vs. claude.ai 網頁版的差異
- Cowork vs. Claude Code 的差異
- Cowork 的適合使用場景

### 單元二：Cowork 任務循環
- 任務循環（Task Loop）的概念
- 如何描述任務讓 Claude 正確理解
- 上下文如何影響 Claude 的計畫
- 中途介入與修正方向

### 單元三：插件與技能設定
- 什麼是插件（Plugins）？
- 什麼是技能（Skills）？
- 如何選擇和配置適合你工作的插件
- 管理插件的存取權限

### 單元四：檔案工作流程
- 閱讀和分析本地文件
- 批次處理多個檔案
- 跨應用程式的資料流動
- 輸出管理

### 單元五：研究工作流程
- 蒐集和整合多來源資訊
- 自動化重複性研究任務
- 建立知識庫

### 單元六：引導長任務
- 設定清楚的任務目標
- 在任務進行中提供回饋
- 處理意外情況
- 審查和驗證 Claude 的工作

## 重點筆記

### Cowork vs. claude.ai vs. Claude Code 的比較

| 產品 | 使用方式 | 最適合 |
|------|---------|--------|
| **claude.ai（網頁版）** | 瀏覽器聊天介面 | 單次問答、對話式任務 |
| **Claude Cowork** | 桌面應用程式 | 處理本地檔案、多步驟任務 |
| **Claude Code** | 命令列工具 | 開發者的程式碼工作 |

### 有效任務描述的要素

好的任務描述應該包含：

1. **目標**：你想達成什麼？
2. **輸入**：Claude 需要處理哪些檔案或資訊？
3. **輸出**：結果應該是什麼格式？放在哪裡？
4. **限制**：有什麼不能做、不能改的？

**範例：**
> 「請讀取 Documents/reports/ 資料夾中所有 PDF 檔案，提取每份報告的標題、日期和主要結論，整理成一個 Excel 表格，存放在桌面上，命名為 reports_summary.xlsx」

### 管理長任務的技巧

長任務容易偏離方向，以下技巧幫助你保持控制：

- **定期檢查點**：每完成一個主要步驟，確認方向正確再繼續
- **明確邊界**：告訴 Claude 哪些資料夾可以存取，哪些不能
- **小步驟測試**：先在小範圍測試，確認沒問題再擴大
- **保留備份**：讓 Claude 修改檔案前，先確認有備份

## 學習建議

**搭配學習：**
- 先完成 [Claude 101](/claude-products/claude-101) 了解 Claude 的基本能力
- 如果你需要處理程式碼，考慮 [Claude Code 101](/claude-products/claude-code-101)

**實作練習：**
1. 安裝 Cowork 後，試著讓它整理你桌面上的一個資料夾
2. 讓 Claude 讀取一份你的工作文件，產生一個執行摘要
3. 設計一個你每週重複做的任務，試著用 Cowork 自動化

## 相關課程

- [Claude 101](/claude-products/claude-101)（Claude 基礎）
- [Claude Code 101](/claude-products/claude-code-101)（開發者版本的代理工具）
- [Agent Skills 入門](/developer/agent-skills)（建立可重用的技能）
