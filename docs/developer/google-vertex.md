---
title: Claude × Google Vertex AI
description: 在 Google Cloud Platform 上部署 Claude，建立 RAG 管道和企業級 AI 系統
---

# 🌐 Claude × Google Vertex AI

<Badge type="warning" text="⭐⭐ 中級" /> <Badge type="info" text="雲端部署" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Claude with Google Cloud's Vertex AI](https://anthropic.skilljar.com/claude-with-google-vertex)（英文）

## 📖 課程簡介

**Google Cloud Vertex AI** 是 GCP 的統一機器學習平台，讓你可以透過 Google Cloud 的基礎設施使用 Claude，享有 GCP 的安全性、合規性和與 Google 服務的原生整合。

如果你的組織已經使用 Google Workspace、BigQuery 或其他 GCP 服務，這門課提供在 GCP 生態系中部署 Claude 的完整路徑。

## ⚠️ 前置條件

::: warning 前置條件
- **Python 程式設計基礎**
- **GCP 基礎知識**（IAM、Cloud Storage、Cloud Run 等核心服務）
- 建議先完成 [使用 Claude API 開發](/developer/building-with-api)
:::

## 🎯 學習目標

完成本課程後，你將能夠：

- 在 Google Cloud Vertex AI 上設定和存取 Claude
- 設計**提示工程**系統並最佳化
- 建立完整的 **RAG（檢索增強生成）** 管道
- 執行**系統評估**（評估 AI 回應品質）
- 應用 **AI 架構模式**（企業級部署）
- 整合 Claude 與 **Google Cloud 服務**
- 進行**視覺處理、PDF 處理和引用功能**的應用

## 📋 課程大綱

### ⚙️ 單元一：Vertex AI 基礎設定
- Vertex AI 服務介紹
- IAM 權限和服務帳戶
- 啟用 Claude 模型（Model Garden）
- Google Cloud SDK 和客戶端程式庫設定

### 🔧 單元二：基本 API 使用
- 透過 Vertex AI 呼叫 Claude
- 認證機制（Application Default Credentials）
- 與 Anthropic 直接 API 的差異

### ✍️ 單元三：提示工程最佳化
- 系統提示設計
- 提示範本管理
- 多模態提示（文字 + 圖片）

### 👁️ 單元四：視覺處理
- 圖片分析和描述
- 文件版面分析
- 視覺問答（Visual QA）

### 📄 單元五：PDF 處理
- 原生 PDF 解析
- 長文件策略
- 引用功能（Citation Feature）

### 🔍 單元六：RAG 管道建立
- 使用 Vertex AI Search 建立搜尋索引
- 文件攝入和向量化
- 語意搜尋整合
- 回應生成和引用

### 📊 單元七：系統評估
- 評估框架設計
- 自動化評估指標
- 人工評估最佳實踐
- 持續改善循環

### 🏗️ 單元八：AI 架構模式
- Vertex AI 上的代理系統
- 多步驟工作流程
- 企業級安全和合規

## 📝 重點筆記

### ⚖️ Anthropic API vs. Google Vertex AI 的選擇

| 考量 | Anthropic 直接 API | Google Vertex AI |
|------|------------------|-----------------|
| **GCP 整合** | 需要額外設定 | 原生整合 |
| **BigQuery 整合** | 不支援 | 原生支援 |
| **Workspace 整合** | 不支援 | 可整合 |
| **IAM 控制** | 不適用 | 完整 GCP IAM |
| **合規性** | Anthropic 條款 | Google 條款（適合企業） |

### 🐍 Vertex AI 基本呼叫範例

```python
import anthropic
from google.auth import default

# 使用 Application Default Credentials
credentials, project = default()

client = anthropic.AnthropicVertex(
    region="us-east5",
    project_id=project,
)

message = client.messages.create(
    model="claude-opus-4-6@20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "請解釋 Google Vertex AI 的主要功能"
        }
    ]
)

print(message.content[0].text)
```

### 🔍 RAG 管道架構

```
使用者問題
    │
    ↓
1. 向量搜尋（Vertex AI Search）
    │ 找到相關文件片段
    ↓
2. 上下文組裝
    │ 將文件片段和問題組合成提示
    ↓
3. Claude 生成回答
    │ 根據提供的上下文
    ↓
4. 引用標注
    │ 標明回答來源
    ↓
最終回答（含引用）
```

### 📊 系統評估的關鍵指標

| 指標 | 說明 |
|------|------|
| **準確性** | 回答是否事實正確 |
| **相關性** | 回答是否切題 |
| **完整性** | 是否涵蓋所有重要面向 |
| **忠實度** | 是否有虛構不在來源中的資訊 |
| **引用品質** | 引用是否正確對應到回答內容 |

## 💡 學習建議

**搭配學習：**
- 先完成 [使用 Claude API 開發](/developer/building-with-api)
- 如果使用 AWS，參考 [Claude × Amazon Bedrock](/developer/amazon-bedrock)

**實作練習：**
1. 在 Vertex AI 上執行第一個 Claude API 呼叫
2. 建立一個簡單的 PDF 分析工具，使用 Claude 的原生 PDF 處理
3. 使用 Vertex AI Search 建立一個企業文件問答系統

## 🔗 相關課程

- [使用 Claude API 開發](/developer/building-with-api)（建議先修）
- [Claude × Amazon Bedrock](/developer/amazon-bedrock)（AWS 替代方案）
- [MCP 入門](/developer/mcp-intro)（工具整合）
