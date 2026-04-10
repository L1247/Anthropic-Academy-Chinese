---
title: MCP 進階主題
description: 生產環境的 MCP 實作，涵蓋取樣機制、傳輸方式、通知系統和水平擴展
---

# 🚀 MCP 進階主題

<Badge type="danger" text="⭐⭐⭐ 高級" /> <Badge type="info" text="開發者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics)（英文）

## 📖 課程簡介

本課程深入探討 Model Context Protocol 的進階功能，聚焦於**生產環境的實作模式**。如果你已經能建立基本的 MCP Server，這門課幫助你處理更複雜的場景：伺服器要求 AI 執行任務、長操作的即時回饋、不同的傳輸機制選擇、以及如何水平擴展。

## ⚠️ 前置條件

::: danger 前置條件
- **必須先完成** [MCP 入門](/developer/mcp-intro)
- **Python 非同步程式設計（async/await）** 的實際使用經驗
- **JSON 訊息格式和 HTTP 協議**的熟悉度
- **伺服器發送事件（SSE）的基礎知識**（Server-Sent Events）
:::

## 🎯 學習目標

完成本課程後，你將能夠：

- 實作 **MCP 取樣機制**（讓 Server 要求 LLM 執行任務）
- 建立**進度和記錄通知系統**（長操作的即時回饋）
- 配置**根目錄檔案存取**（安全的目錄權限系統）
- 理解完整的 **JSON 訊息架構**（請求/結果配對 vs. 通知）
- 選擇和實作 **Stdio 傳輸**（本地環境）
- 選擇和實作 **StreamableHTTP 傳輸**（網路環境）
- 判斷何時使用**無狀態 HTTP 進行水平擴展**

## 📋 課程大綱

### 🎯 單元一：取樣機制（Sampling）
- 什麼是取樣？Server 如何要求 Client 執行 LLM 呼叫
- 取樣請求的結構
- 實作 Server 端的取樣邏輯
- 安全考量

### 📡 單元二：進度與通知系統
- MCP 的通知（Notification）訊息類型
- 使用 `context` 物件發送即時回饋
- 記錄回調（Logging Callbacks）
- 長操作的進度報告

### 📁 單元三：根目錄檔案存取
- 根目錄（Roots）的概念
- 授予特定目錄存取權限
- 安全邊界設計
- 在 Claude Code 中設定根目錄

### 🏗️ 單元四：MCP JSON 訊息架構

MCP 訊息分兩類：

```
請求-結果配對（同步）：
  Client → Server: {"id": 1, "method": "tools/call", ...}
  Server → Client: {"id": 1, "result": {...}}

通知（非同步，單向）：
  Server → Client: {"method": "notifications/progress", ...}
  （無 id，不需要回應）
```

### 📡 單元五：Stdio 傳輸機制
- Stdio 如何透過標準輸入/輸出串流通訊
- 初始化握手序列
- 適合場景：本地工具、命令列整合

### 🌐 單元六：StreamableHTTP 傳輸
- HTTP + SSE（伺服器發送事件）
- 啟用伺服器到客戶端的推送通訊
- 配置標誌對功能的影響

### 🚀 單元七：生產環境部署
- 無狀態 HTTP 的優缺點
- 水平擴展的時機與方法
- 傳輸選擇決策框架

## 📝 重點筆記

### 🗺️ 傳輸機制選擇指南

```
你的 MCP Server 要部署在哪裡？
│
├─ 本地機器（同一台電腦）
│  └─ 使用 Stdio 傳輸
│     • 最簡單，無需網路配置
│     • Claude Code 的預設方式
│
└─ 遠端伺服器（不同機器）
   └─ 使用 StreamableHTTP 傳輸
      │
      ├─ 需要伺服器推送通知？
      │  └─ 啟用 SSE（stateful）
      │
      └─ 只需請求-回應，要水平擴展？
         └─ 使用無狀態 HTTP（stateless）
```

### 🎯 取樣機制的使用場景

取樣（Sampling）讓 MCP Server 能夠：
- 在工具執行過程中請求 AI 做決策
- 構建遞迴的 AI 工作流程
- 讓 Server 端的邏輯更智能

```python
# Server 端請求 Client（通常是 Claude）執行 LLM 呼叫
async def tool_that_needs_ai(context):
    result = await context.sample(
        messages=[{"role": "user", "content": "分析這段資料：..."}],
        max_tokens=500
    )
    return result.content
```

### 🛡️ 生產環境的安全考量

| 項目 | 建議 |
|------|------|
| 根目錄存取 | 最小權限原則，只開放必要目錄 |
| 取樣請求 | 在 Client 端設置請求頻率限制 |
| 通知 | 避免洩漏敏感資訊在日誌中 |
| HTTP 傳輸 | 使用 HTTPS，設置適當的 CORS |

## 💡 學習建議

**搭配學習：**
- 必須先完成 [MCP 入門](/developer/mcp-intro)
- 參考 [Anthropic 官方 MCP 文件](https://docs.anthropic.com/en/docs/mcp)

**實作練習：**
1. 為你的 MCP Server 加入進度通知，讓長操作有即時回饋
2. 實作根目錄存取，限制只能讀取專案目錄
3. 將你的本地 MCP Server 改為 HTTP 部署，測試兩種傳輸的差異

## 🔗 相關課程

- [MCP 入門](/developer/mcp-intro)（必先修）
- [使用 Claude API 開發](/developer/building-with-api)（Tool Use 基礎）
- [子代理入門](/developer/subagents)（另一種複雜任務管理方式）
