---
title: Claude Code 101
description: 開發者必修課，了解 AI 編碼代理架構、安裝 Claude Code 並掌握核心工作流程
---

# Claude Code 101

<Badge type="warning" text="⭐⭐ 初-中級" /> <Badge type="info" text="開發者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101)（英文）

## 課程簡介

Claude Code 是 Anthropic 推出的 **AI 編碼代理（Agentic Coding Assistant）**，直接在你的終端機中運行，能夠理解整個程式碼庫的上下文，執行複雜的多步驟程式設計任務。

它不只是一個「聊天機器人」，而是一個能夠真正操作你的程式碼、執行命令、讀寫檔案的 AI 代理。

## 前置條件

::: warning 前置條件
- **基本的程式碼編輯器操作**（VS Code、Cursor 等）
- **基本的命令列操作**（能夠在終端機輸入指令）
- **Claude Pro、Max 或 Enterprise 訂閱**，或 Anthropic API Key
:::

## 學習目標

完成本課程後，你將能夠：

1. 理解 **AI 編碼代理 vs. 聊天式 AI** 的根本差異
2. 了解 **Agentic Loop（代理循環）** 的運作原理
3. 在你的系統上**安裝 Claude Code**
4. 撰寫有效的提示，使用**批准模式（Approval Mode）和計畫模式（Plan Mode）**
5. 遵循 **Explore → Plan → Code → Commit** 工作流程
6. 管理**上下文視窗**（避免超出限制）
7. 建立 **CLAUDE.md** 檔案為專案設定記憶
8. 建立**自訂子代理**
9. 透過 **MCP 伺服器**連接外部工具

## 課程大綱

### 單元一：AI 編碼代理的概念
- 聊天式 AI vs. 代理式 AI 的差異
- Claude Code 的定位與核心優勢
- 適合和不適合的使用場景

### 單元二：核心架構理解
- **Agentic Loop（代理循環）**：Claude 如何規劃和執行任務
- **上下文視窗（Context Window）**：理解 AI 的「記憶範圍」
- **工具系統（Tools）**：檔案操作、終端機執行、網路搜尋
- **權限系統（Permissions）**：控制 Claude 可以做什麼

### 單元三：安裝與設定
- 多平台安裝指南（macOS、Windows、Linux）
- API Key 設定
- 首次執行測試

### 單元四：核心工作流程
- **Explore → Plan → Code → Commit** 四步驟
- 批准模式（Approval Mode）的使用時機
- 計畫模式（Plan Mode）的使用時機
- 如何給予有效的任務描述

### 單元五：上下文管理
- 使用 `/clear` 清理上下文
- 使用 `/compact` 壓縮上下文
- 監控上下文使用量
- 避免上下文溢出的策略

### 單元六：CLAUDE.md 專案記憶
- 什麼是 CLAUDE.md？
- 如何編寫有效的 CLAUDE.md
- 全域 vs. 專案層級的 CLAUDE.md

### 單元七：進階功能
- 建立自訂子代理
- 連接 MCP 伺服器
- 自訂命令（Slash Commands）

## 重點筆記

### Agentic Loop 運作原理

```
使用者輸入任務
    ↓
Claude 分析任務，制定計畫
    ↓
執行步驟 1（讀取檔案、執行命令等）
    ↓
觀察結果，調整計畫
    ↓
執行步驟 2 ...
    ↓
任務完成，回報結果
```

每一步都可以要求人工批准（批准模式），或自動執行（自動模式）。

### CLAUDE.md 範例結構

```markdown
# 專案名稱

## 技術棧
- 語言：Python 3.11
- 框架：FastAPI
- 資料庫：PostgreSQL

## 編碼規範
- 使用 type hints
- 函數命名：snake_case
- 測試：pytest，coverage > 80%

## 不要做的事
- 不要修改 legacy/ 目錄下的檔案
- 不要直接連接生產資料庫

## 常用命令
- 執行測試：`pytest tests/`
- 啟動開發伺服器：`uvicorn main:app --reload`
```

### 批准模式 vs. 計畫模式

| 模式 | 適合場景 |
|------|---------|
| **批准模式** | 每一步都需要確認，適合不熟悉的程式碼庫 |
| **計畫模式** | 先看計畫再執行，適合複雜的重構任務 |
| **自動模式** | 信任 Claude 自動執行，適合簡單且熟悉的任務 |

## 學習建議

**搭配學習：**
- 完成後繼續 [Claude Code 實戰](/developer/claude-code-in-action) 深化技巧
- 學習 [Agent Skills 入門](/developer/agent-skills) 建立可重用的技能

**實作練習：**
1. 安裝 Claude Code，用它閱讀一個現有的程式碼庫，請它解釋架構
2. 建立一個簡單的 CLAUDE.md 描述你的一個專案
3. 用「Explore → Plan → Code」流程完成一個小功能

## 相關課程

- [Claude Code 實戰](/developer/claude-code-in-action)（進階整合）
- [Agent Skills 入門](/developer/agent-skills)（建立可重用技能）
- [子代理入門](/developer/subagents)（委派複雜任務）
- [MCP 入門](/developer/mcp-intro)（擴展 Claude 的工具）
