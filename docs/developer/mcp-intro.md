---
title: MCP 入門
description: Model Context Protocol 基礎課，使用 Python SDK 建立 MCP Server 和 Client
---

# MCP 入門

<Badge type="warning" text="⭐⭐ 中級" /> <Badge type="info" text="開發者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol)（英文）

## 課程簡介

**Model Context Protocol（MCP）** 是 Anthropic 推出的開放標準，讓 AI 系統能夠更有效地與外部工具和服務互動。

想像你想讓 Claude 能夠讀取你的資料庫、呼叫你的 API、或使用你的內部工具——MCP 就是讓這件事變得標準化、可重用的方式。

## 前置條件

::: warning 前置條件
- **Python 程式設計基礎**（函式、類別、裝飾器）
- **JSON 格式理解**
- **基本 HTTP 請求-回應模型**（理解 GET/POST 請求）
:::

## 學習目標

完成本課程後，你將能夠：

- 理解 MCP 的架構和它如何將工具定義負擔轉移到專用的 MCP Server
- 了解**傳輸無關通訊**（Transport-agnostic）的概念
- 掌握 **MCP 三大核心原語**：工具（Tools）、資源（Resources）、提示（Prompts）
- 使用 Python SDK 建立 **MCP Server**
- 使用內建的 **MCP Server Inspector** 測試和除錯
- 理解何時使用哪種原語

## 課程大綱

### 單元一：MCP 概念與架構
- 為什麼需要 MCP？解決什麼問題？
- MCP 的整體架構：Client、Server、Transport
- 與直接 Tool Use 的比較

### 單元二：三大核心原語

```
MCP 的三個基本構建元件：
┌─────────────────────────────────────────┐
│ 工具（Tools）    → 由模型控制，執行操作  │
│ 資源（Resources）→ 由應用控制，讀取資料  │
│ 提示（Prompts）  → 由使用者控制，引導對話│
└─────────────────────────────────────────┘
```

### 單元三：建立第一個 MCP Server
- Python SDK 安裝與設定
- 使用裝飾器定義工具（不需要手動寫 JSON Schema）
- 實作文件管理工具（讀取、編輯文件）
- 啟動 MCP Server

### 單元四：測試與除錯
- 使用 **MCP Server Inspector**（瀏覽器介面）
- 測試工具呼叫
- 常見錯誤排查

### 單元五：Resources（資源）
- 定義唯讀資源
- 靜態資源 vs. 模板資源
- MIME 類型處理（JSON、文字）

### 單元六：Prompts（提示範本）
- 定義預先制定的工作流程指令
- 自動完成（Autocomplete）整合
- 上下文注入（Context Injection）

### 單元七：整合到 Claude
- 將 MCP Server 連接到 Claude Code
- 將 MCP Server 連接到 Claude.ai
- 整合模式的最佳實踐

## 重點筆記

### 三大原語的使用時機

| 原語 | 控制方 | 用途 | 範例 |
|------|--------|------|------|
| **工具** | 模型（AI）主動呼叫 | 執行操作、查詢資料 | 搜尋資料庫、發送郵件 |
| **資源** | 應用程式提供 | 提供唯讀上下文資料 | 讀取設定檔、文件列表 |
| **提示** | 使用者選擇 | 預先制定的工作流程 | 「幫我審查這段程式碼」 |

### Python SDK 基本範例

```python
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.types as types

# 建立 MCP Server
server = Server("my-server")

# 定義工具（使用裝飾器，不需要手動寫 JSON Schema）
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="read_document",
            description="讀取指定路徑的文件內容",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路徑"}
                },
                "required": ["path"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict):
    if name == "read_document":
        path = arguments["path"]
        with open(path, "r") as f:
            content = f.read()
        return [types.TextContent(type="text", text=content)]
```

### MCP vs. 直接 Tool Use

| 比較 | 直接 Tool Use | MCP |
|------|-------------|-----|
| 工具定義 | 每次呼叫時傳送 | 由 MCP Server 管理 |
| 可重用性 | 低（每個應用各自定義） | 高（一個 Server 多個 Client 共用） |
| 標準化 | 無標準 | Anthropic 開放標準 |
| 複雜度 | 較低 | 較高 |

## 學習建議

**搭配學習：**
- 先完成 [使用 Claude API 開發](/developer/building-with-api) 了解 Tool Use 基礎
- 之後繼續 [MCP 進階主題](/developer/mcp-advanced)

**實作練習：**
1. 建立一個能讀取本地資料夾的 MCP Server
2. 加入一個 Resource，列出可用的文件
3. 用 MCP Server Inspector 測試你的工具

## 相關課程

- [使用 Claude API 開發](/developer/building-with-api)（建議先修，了解 Tool Use）
- [MCP 進階主題](/developer/mcp-advanced)（生產環境部署）
- [Claude Code 實戰](/developer/claude-code-in-action)（在開發工作流程中使用 MCP）
