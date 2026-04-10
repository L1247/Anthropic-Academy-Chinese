---
title: 使用 Claude API 開發
description: 最完整的 Claude API 課程，84 堂課 8 小時以上，從 API 設定到代理架構
---

# 🔧 使用 Claude API 開發

<Badge type="danger" text="⭐⭐⭐ 中-高級" /> <Badge type="info" text="84 堂課 · 8 小時+" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)（英文）

## 📖 課程簡介

這是 Anthropic Academy **最大的課程**：84 堂課、超過 8 小時的影片內容，涵蓋從基礎 API 設定到生產級代理架構的完整技術棧。

如果你想把 Claude 整合到你的應用程式，或建立 AI 驅動的產品，這門課是必修的。

## ⚠️ 前置條件

::: warning 前置條件
- **Python 程式設計基礎**（能夠讀寫 Python 函式和類別）
- **JSON 格式理解**（理解鍵值對、陣列結構）
- 建議了解基本的 HTTP 請求-回應模型
:::

## 🎯 學習目標

完成本課程後，你將能夠：

- 設定和驗證 **Anthropic API**，管理 API Key
- 實作**單輪和多輪對話**，正確格式化訊息
- 配置**系統提示（System Prompts）**和控制模型行為
- 應用**提示工程技巧**（XML 標籤、範例學習、明確指令）
- 整合 Claude 的**工具使用（Tool Use）**功能
- 建立**RAG 系統**（文字分塊、Embeddings、向量搜尋）
- 使用**進階功能**：擴展思考、圖片分析、PDF 處理、提示快取
- 設計**代理架構**（平行化、鏈式、路由工作流程）

## 📋 課程大綱

### 🔧 模組一：API 基礎（約 10 堂課）
- API 設定與認證
- 第一個 API 請求
- 訊息格式與角色
- 回應處理與錯誤管理

### 💬 模組二：對話管理（約 8 堂課）
- 單輪對話實作
- 多輪對話與對話歷史
- 上下文視窗管理
- 串流回應（Streaming）

### ⚙️ 模組三：模型配置（約 10 堂課）
- 系統提示的設計與最佳實踐
- Temperature 設定
- 結構化輸出格式
- 回應串流

### ✍️ 模組四：提示工程（約 12 堂課）
- XML 標籤結構化提示
- Few-shot 學習（範例學習）
- 思維鏈（Chain of Thought）
- 清晰指令的設計原則

### 🛠️ 模組五：工具整合（約 15 堂課）
- 工具定義與結構
- 工具呼叫解析
- 自訂工具開發
- 批次操作
- 網路搜尋整合

### 🔍 模組六：RAG 系統（約 12 堂課）
- 文字分塊策略
- Embeddings 生成
- BM25 全文搜尋
- 向量資料庫整合
- 情境檢索（Contextual Retrieval）

### 🚀 模組七：進階功能（約 10 堂課）
- 擴展思考（Extended Thinking）
- 圖片分析
- PDF 文件處理
- 提示快取（Prompt Caching）策略

### 🤖 模組八：代理架構（約 7 堂課）
- 代理設計模式
- 平行化工作流程
- 鏈式工作流程
- 路由工作流程

## 📝 重點筆記

### 🔧 API 請求基本結構

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    system="你是一位專業的技術文件撰寫者。",
    messages=[
        {"role": "user", "content": "請解釋什麼是 API"}
    ]
)

print(message.content[0].text)
```

### 🛠️ 工具使用（Tool Use）概念

```
使用者問：「台北今天天氣如何？」
    ↓
Claude 決定呼叫 get_weather 工具
    ↓
你的程式執行 get_weather("台北")
    ↓
回傳結果給 Claude
    ↓
Claude 用結果回答使用者
```

### 🤖 代理架構的三種模式

| 模式 | 說明 | 適用場景 |
|------|------|---------|
| **鏈式** | 任務 A 輸出 → 任務 B 輸入 | 有順序依賴的任務 |
| **平行化** | 多個任務同時執行 | 獨立的子任務 |
| **路由** | 根據輸入選擇不同的處理路徑 | 分類後差異化處理 |

## 💡 學習建議

**搭配學習：**
- 同時參考 [Anthropic Cookbook](/resources) 的實作範例
- 完成後，可以進入 [MCP 入門](/developer/mcp-intro) 學習工具整合的標準協定
- 想在 AWS 部署，前往 [Amazon Bedrock](/developer/amazon-bedrock)

**實作練習：**
1. 建立一個簡單的多輪對話 CLI 工具
2. 實作一個有 2 個自訂工具的 Claude 應用（例如：天氣查詢 + 計算器）
3. 建立一個簡單的 RAG 系統，讓 Claude 能查詢你的文件

## 🔗 相關課程

- [MCP 入門](/developer/mcp-intro)（工具整合的標準協定）
- [Claude Code 實戰](/developer/claude-code-in-action)（開發工作流程自動化）
- [Amazon Bedrock](/developer/amazon-bedrock)（AWS 雲端部署）
- [Google Vertex AI](/developer/google-vertex)（GCP 雲端部署）
