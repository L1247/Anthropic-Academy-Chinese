---
title: Claude × Amazon Bedrock
description: 在 AWS 基礎設施上部署 Claude，建立企業級 AI 應用
---

# ☁️ Claude × Amazon Bedrock

<Badge type="warning" text="⭐⭐ 中級" /> <Badge type="info" text="雲端部署" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Claude with Amazon Bedrock](https://anthropic.skilljar.com/claude-in-amazon-bedrock)（英文）

## 📖 課程簡介

**Amazon Bedrock** 是 AWS 提供的全托管基礎模型服務，讓你可以透過 AWS 的基礎設施使用 Claude，享有 AWS 生態系的安全性、合規性和可擴展性。

如果你的組織已經深度使用 AWS，或有 AWS 合規要求，這門課是在 AWS 環境中部署 Claude 的完整指南。

## ⚠️ 前置條件

::: warning 前置條件
- **Python 程式設計基礎**
- **AWS 基礎知識**（IAM、S3、Lambda 等核心服務的基本概念）
- 建議先完成 [使用 Claude API 開發](/developer/building-with-api) 了解 Claude API 的概念
:::

## 🎯 學習目標

完成本課程後，你將能夠：

- 在 Amazon Bedrock 上設定和使用 Claude
- 設計有效的**提示工程**系統
- 建立 **RAG（檢索增強生成）** 系統
- 使用 Bedrock 的**代理工作流程（Agent Workflows）**
- 將 Claude 整合進 **AWS 服務**（Lambda、S3、DynamoDB）
- 管理**成本和效能**最佳化

## 📋 課程大綱

### ⚙️ 單元一：Amazon Bedrock 基礎設定
- Bedrock 服務介紹和定價
- IAM 權限配置
- 啟用 Claude 模型存取
- Boto3 SDK 設定

### 🔧 單元二：基本 API 呼叫
- Bedrock Runtime API
- 與 Anthropic 直接 API 的差異
- 錯誤處理和重試機制

### ✍️ 單元三：提示工程
- 在 Bedrock 環境中的提示設計
- 系統提示和對話管理
- 提示範本管理

### 🛠️ 單元四：工具使用（Tool Use）
- 在 Bedrock 中定義和使用工具
- 與 AWS Lambda 的整合（工具後端）
- 多工具的協調

### 🔍 單元五：RAG 系統建立
- 使用 Amazon Bedrock Knowledge Bases
- 文件攝入（Document Ingestion）
- 向量搜尋配置
- 回應生成最佳化

### 🤖 單元六：Bedrock 代理
- Amazon Bedrock Agents 介紹
- 代理的動作組（Action Groups）
- 代理的知識庫整合
- 部署和監控

### 🚀 單元七：生產環境部署
- 效能最佳化
- 成本控制策略
- CloudWatch 監控
- 安全最佳實踐

## 📝 重點筆記

### ⚖️ Anthropic API vs. Amazon Bedrock 的選擇

| 考量 | Anthropic 直接 API | Amazon Bedrock |
|------|------------------|----------------|
| **AWS 整合** | 需要額外設定 | 原生整合 |
| **合規性** | Anthropic 條款 | AWS 條款（適合企業） |
| **IAM 控制** | 不適用 | 完整 IAM 整合 |
| **VPC 私有連線** | 不支援 | 支援 |
| **成本管理** | Anthropic 帳單 | AWS 統一帳單 |
| **最新模型** | 最快獲得 | 略慢（需 AWS 端啟用） |

### 🐍 Bedrock 基本呼叫範例（Python Boto3）

```python
import boto3
import json

client = boto3.client('bedrock-runtime', region_name='us-east-1')

response = client.invoke_model(
    modelId='anthropic.claude-opus-4-6-20250514-v1:0',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "請解釋什麼是 Amazon Bedrock"
            }
        ]
    })
)

result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

### 💰 成本最佳化技巧

1. **選擇正確的模型**：不是所有任務都需要 Opus，Claude Haiku 對簡單任務更經濟
2. **提示快取（Prompt Caching）**：對重複使用的系統提示啟用快取
3. **批次處理**：使用 Bedrock Batch API 處理大量非即時任務
4. **監控與告警**：設定 CloudWatch 告警防止意外超支

## 💡 學習建議

**搭配學習：**
- 先完成 [使用 Claude API 開發](/developer/building-with-api) 了解核心概念
- 如果使用 GCP，參考 [Claude × Google Vertex AI](/developer/google-vertex)

**實作練習：**
1. 在 Bedrock 上執行第一個 Claude API 呼叫
2. 建立一個使用 Lambda 作為工具後端的簡單應用
3. 使用 Bedrock Knowledge Bases 建立一個企業文件問答系統

## 🔗 相關課程

- [使用 Claude API 開發](/developer/building-with-api)（建議先修）
- [Claude × Google Vertex AI](/developer/google-vertex)（GCP 替代方案）
- [MCP 入門](/developer/mcp-intro)（工具整合的另一種方式）
