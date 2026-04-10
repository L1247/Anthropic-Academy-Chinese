# 開發者課程總覽

本分類共 **8 門課程**，從 Claude API 整合到 MCP 協定、代理架構、雲端部署，完整覆蓋開發者所需的技術棧。

## 課程列表

### 核心開發課程

<div class="role-cards">
  <div class="role-card">
    <div class="role-icon">🔧</div>
    <h3><a href="/developer/building-with-api">使用 Claude API 開發</a></h3>
    <p>開發者最重要的課程。84 堂課、8 小時以上。涵蓋 API 設定、對話管理、提示工程、工具整合、RAG、代理架構。</p>
    <p>⭐⭐⭐ 中-高級 · 前置：Python、JSON 基礎</p>
  </div>
  <div class="role-card">
    <div class="role-icon">⚡</div>
    <h3><a href="/developer/claude-code-in-action">Claude Code 實戰</a></h3>
    <p>將 Claude Code 整合進開發工作流程，掌握工具系統、上下文管理、MCP 整合、GitHub 自動化。</p>
    <p>⭐⭐ 中級 · 前置：終端操作、Git</p>
  </div>
</div>

### MCP 協定課程

<div class="role-cards">
  <div class="role-card">
    <div class="role-icon">🔌</div>
    <h3><a href="/developer/mcp-intro">MCP 入門</a></h3>
    <p>Model Context Protocol 基礎。用 Python SDK 建立 MCP Server 和 Client，掌握工具、資源、提示三大原語。</p>
    <p>⭐⭐ 中級 · 前置：Python、JSON、HTTP 基礎</p>
  </div>
  <div class="role-card">
    <div class="role-icon">🚀</div>
    <h3><a href="/developer/mcp-advanced">MCP 進階主題</a></h3>
    <p>生產環境的 MCP 實作：取樣機制、傳輸方式（stdio/HTTP）、根目錄存取、水平擴展部署。</p>
    <p>⭐⭐⭐ 高級 · 前置：MCP 入門 + async 程式設計</p>
  </div>
</div>

### Claude Code 擴充課程

<div class="role-cards">
  <div class="role-card">
    <div class="role-icon">🤖</div>
    <h3><a href="/developer/agent-skills">Agent Skills 入門</a></h3>
    <p>建立可重用的 SKILL.md 指令檔，讓 Claude 自動套用在正確的任務上。支援團隊共享。</p>
    <p>⭐⭐ 中級 · 前置：Claude Code 基本使用經驗</p>
  </div>
  <div class="role-card">
    <div class="role-icon">👥</div>
    <h3><a href="/developer/subagents">子代理入門</a></h3>
    <p>將複雜任務委派給獨立的子代理，保持主上下文視窗乾淨，提升長任務的效率。</p>
    <p>⭐⭐ 中級 · 前置：Claude Code 基本使用經驗</p>
  </div>
</div>

### 雲端平台課程

<div class="role-cards">
  <div class="role-card">
    <div class="role-icon">☁️</div>
    <h3><a href="/developer/amazon-bedrock">Claude × Amazon Bedrock</a></h3>
    <p>在 AWS 基礎設施上部署 Claude，建立提示工程系統和代理工作流程。</p>
    <p>⭐⭐ 中級 · 前置：Python、AWS 基礎</p>
  </div>
  <div class="role-card">
    <div class="role-icon">🌐</div>
    <h3><a href="/developer/google-vertex">Claude × Google Vertex AI</a></h3>
    <p>在 GCP 上部署 Claude，建立 RAG 管道、系統評估，並應用企業級 AI 架構模式。</p>
    <p>⭐⭐ 中級 · 前置：Python、GCP 基礎</p>
  </div>
</div>

## 建議學習路線

**從零開始的開發者：**
使用 Claude API 開發 → MCP 入門 → MCP 進階 → 雲端平台

**Claude Code 開發者：**
Claude Code 實戰 → Agent Skills → 子代理

**特定平台：**
- AWS 用戶：Claude API → Amazon Bedrock
- GCP 用戶：Claude API → Google Vertex AI

## 技術先備知識

| 技術 | 需要它的課程 |
|------|------------|
| Python 基礎 | Claude API、MCP 入門/進階、Bedrock、Vertex AI |
| JSON / HTTP | Claude API、MCP 入門 |
| 非同步程式設計（async） | MCP 進階 |
| 命令列 / Git | Claude Code 實戰、Agent Skills、子代理 |
| AWS 基礎 | Amazon Bedrock |
| GCP 基礎 | Google Vertex AI |
