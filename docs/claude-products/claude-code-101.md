---
title: Claude Code 101
description: 開發者必修課，了解 AI 編碼代理架構、安裝 Claude Code 並掌握核心工作流程
---

# ⚡ Claude Code 101

<Badge type="warning" text="⭐⭐ 初-中級" /> <Badge type="info" text="開發者" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101)（英文）

## 📖 課程簡介

Claude Code 是 Anthropic 推出的 **AI 編碼代理（Agentic Coding Assistant）**，直接在你的終端機中運行，能夠理解整個程式碼庫的上下文，執行複雜的多步驟程式設計任務。

它不只是一個「聊天機器人」，而是一個能夠真正操作你的程式碼、執行命令、讀寫檔案的 AI 代理。

## ⚠️ 前置條件

::: warning 前置條件
- **基本的程式碼編輯器操作**（VS Code、Cursor 等）
- **基本的命令列操作**（能夠在終端機輸入指令）
- **Claude Pro、Max 或 Enterprise 訂閱**，或 Anthropic API Key
:::

## 🎯 學習目標

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

## 📋 課程大綱

### 🤖 單元一：AI 編碼代理的概念

- 聊天式 AI vs. 代理式 AI 的差異

  <details>
  <summary>詳細說明</summary>

  聊天式 AI（如 claude.ai）是「問答模式」：你提問，AI 回答，你再決定如何行動。**代理式 AI 則會自己採取行動**：它可以讀取你的程式碼、執行命令、修改檔案，然後根據結果自動決定下一步——不需要你逐步確認每個動作。這個差異讓代理式 AI 能處理需要多步驟、需要觀察環境狀態才能完成的複雜工程任務。

  </details>

- Claude Code 的定位與核心優勢

  <details>
  <summary>詳細說明</summary>

  Claude Code 直接在你的終端機中運行，能夠存取整個程式碼庫而非單一檔案，理解專案的完整結構和脈絡。它的核心優勢在於：能執行 shell 指令、讀寫任意檔案、搜尋程式碼、執行測試並根據輸出結果自我修正。相比只能生成程式碼片段的聊天 AI，Claude Code 可以端對端地完成一個功能——從理解需求、規劃架構、寫程式碼，到執行測試確認結果。

  </details>

- 適合和不適合的使用場景

  <details>
  <summary>詳細說明</summary>

  **最適合**：重構既有程式碼、新增功能、偵錯與修復、撰寫或更新測試、閱讀陌生程式碼庫以理解架構、撰寫文件。**不適合或需謹慎**：需要即時性的生產環境操作（建議在測試環境使用）、涉及高度敏感資料的任務（注意授予的權限範圍）、創意性的架構決策（Claude 可以提供選項，但最終決策應由你主導）。

  </details>

### 🏗️ 單元二：核心架構理解

- **Agentic Loop（代理循環）**：Claude 如何規劃和執行任務

  <details>
  <summary>詳細說明</summary>

  Agentic Loop 是 Claude Code 的核心運作機制：Claude 接收任務後，會**反覆循環「思考 → 使用工具 → 觀察結果 → 再思考」**，直到任務完成。每一輪迴圈中，Claude 可能讀取一個檔案、執行一段測試、根據錯誤訊息調整策略，然後繼續下一步。這個機制讓 Claude 能夠處理事先無法完全預知每個步驟的複雜任務。詳細流程圖見下方「重點筆記」區段。

  </details>

- **上下文視窗（Context Window）**：理解 AI 的「記憶範圍」

  <details>
  <summary>詳細說明</summary>

  上下文視窗是 Claude 在一次對話中能「記住」的資訊總量（以 Token 計算）。一旦對話歷史、讀取的程式碼、工具輸出加總超過這個上限，Claude 就無法看到最早的部分，可能導致輸出不一致。在長時間的編碼任務中，需要主動管理上下文（使用 `/compact` 或 `/clear`），避免關鍵資訊被推出視窗外。

  </details>

- **工具系統（Tools）**：檔案操作、終端機執行、網路搜尋

  <details>
  <summary>詳細說明</summary>

  Claude Code 透過一組**內建工具**與你的環境互動，主要包括：讀取和寫入任意檔案（`Read`/`Write`/`Edit`）、在終端機執行 Shell 命令（`Bash`）、在程式碼庫中搜尋關鍵字（`Grep`/`Glob`）。每次 Claude 使用工具時，你都可以在輸出中看到它呼叫了哪個工具和傳入了什麼參數，讓整個過程透明可稽核。

  </details>

- **權限系統（Permissions）**：控制 Claude 可以做什麼

  <details>
  <summary>詳細說明</summary>

  Claude Code 設計了多層級的權限控制：
  **批准模式（Approval Mode）** 下，每個工具呼叫都需要你手動確認才能執行；
  **自動接受模式** 下，Claude 可以不需確認自動執行；
  你也可以只允許特定類型的工具（如只允許讀取，不允許寫入）。
  建議在不熟悉的程式碼庫或執行破壞性操作前，使用批准模式，確保 Claude 的每個動作都在你的掌控之中。

  </details>

### ⚙️ 單元三：安裝與設定

- 多平台安裝指南（macOS、Windows、Linux）——透過 `npm install -g @anthropic-ai/claude-code` 安裝，需要 Node.js 18+；Windows 使用者建議搭配 WSL 2 以獲得最佳體驗。
- API Key 設定——在 Anthropic Console 建立 API Key，執行 `claude` 後依照提示設定；或使用 Claude Pro/Max 帳號透過瀏覽器授權登入，不需要手動管理 API Key。
- 首次執行測試——在任意專案目錄執行 `claude`，輸入「解釋這個目錄的結構」，確認 Claude 能正確讀取並描述你的程式碼庫，即代表安裝成功。

### 🔄 單元四：核心工作流程

- **Explore → Plan → Code → Commit** 四步驟

  <details>
  <summary>詳細說明</summary>

  這是使用 Claude Code 完成功能的最佳實踐流程：
  **Explore（探索）** — 先讓 Claude 閱讀相關程式碼、理解現有架構，不急著動手；
  **Plan（規劃）** — 要求 Claude 說明它的實作方案（可使用計畫模式），你審核並確認方向；
  **Code（實作）** — Claude 按計畫逐步執行，你在批准模式下監督每個關鍵步驟；
  **Commit（提交）** — 確認結果正確後，讓 Claude 撰寫清楚的 commit message 並提交。
  跳過前兩步直接進入 Code，是導致輸出偏離預期的最常見原因。

  </details>

- 批准模式（Approval Mode）的使用時機——每個工具呼叫都需手動確認，適合在不熟悉的程式碼庫中操作、執行可能影響生產環境的指令，或學習 Claude 如何思考和分解任務時使用。
- 計畫模式（Plan Mode）的使用時機——Claude 先列出完整執行計畫但不實際執行，適合在複雜重構或大型功能開始前，讓你審核整體策略是否符合預期。詳見下方「重點筆記」的比較表。
- 如何給予有效的任務描述——說明**目標**（要達成什麼）、**現況**（哪裡出了問題、已有哪些嘗試）、**限制**（不要動哪些檔案、需符合哪些規範）。越具體的描述，Claude 越不需要猜測，產出的計畫也越準確。

### 🧠 單元五：上下文管理

- 使用 `/clear` 清理上下文

  <details>
  <summary>詳細說明</summary>

  `/clear` 會**完全清空**目前的對話歷史，讓 Claude 重新開始，不保留任何之前的討論脈絡。適合在完成一個功能後開始另一個不相關的任務、或是當前對話已充斥太多無關訊息導致 Claude 開始混淆時使用。清空後 CLAUDE.md 的專案記憶仍然有效，Claude 不會忘記專案的基本設定。

  </details>

- 使用 `/compact` 壓縮上下文

  <details>
  <summary>詳細說明</summary>

  `/compact` 讓 Claude **自動摘要並壓縮**目前的對話歷史，保留關鍵資訊但減少 Token 用量，讓同一個對話可以繼續更長時間。適合在長時間的任務中途、對話已很長但任務還未完成時使用。與 `/clear` 的差別是：`/compact` 保留了工作脈絡，`/clear` 則是全部清空。

  </details>

- 監控上下文使用量——Claude Code 在介面上會顯示目前上下文使用比例；當使用量超過 80% 時，建議主動執行 `/compact` 或考慮拆分任務。

- 避免上下文溢出的策略——將大型任務拆成獨立的小任務分批完成；
每個任務完成後用 `/clear` 重設；
讀取大型檔案時指定只讀取相關的函數或區段，而非整個檔案。

### 📋 單元六：CLAUDE.md 專案記憶

- 什麼是 CLAUDE.md？——放在專案根目錄的 Markdown 檔案，Claude 每次啟動時都會自動讀取。作用是告訴 Claude 這個專案的基本設定：技術棧、編碼規範、常用指令、哪些檔案不能動、哪些是特殊慣例，取代每次對話都要重新說明背景的麻煩。

- 如何編寫有效的 CLAUDE.md

  <details>
  <summary>詳細說明</summary>

  一個有效的 CLAUDE.md 應該包含：**技術棧與版本**（語言、框架、資料庫）、**編碼規範**（命名慣例、格式、測試要求）、**常用指令**（如何啟動開發伺服器、如何跑測試）、**禁止事項**（不能修改哪些目錄或檔案）。避免把 CLAUDE.md 寫成說明文件——只放 Claude 在工作中真正需要的操作性資訊。詳見下方「重點筆記」的範例結構。

  </details>

- 全域 vs. 專案層級的 CLAUDE.md——**專案層級**（`./CLAUDE.md`）只對當前專案有效，存入版控後整個團隊共享；**全域層級**（`~/.claude/CLAUDE.md`）對你所有專案有效，適合存放個人偏好（如你慣用的語言、回應風格）。兩者可以並存，內容會合併。

### 🚀 單元七：進階功能

- 建立自訂子代理

  <details>
  <summary>詳細說明</summary>

  子代理（Subagent）讓你可以**把特定任務委派給獨立的 Claude 實例**，讓主對話的上下文視窗保持乾淨。例如：主代理負責規劃整體功能，再叫一個子代理專門去執行「閱讀並摘要所有測試檔案」這個子任務。在 Claude Code 中，可以透過自定義的 Agent 定義檔建立有特定角色和工具權限的子代理，實現複雜的多代理工作流程。

  </details>

- 連接 MCP 伺服器

  <details>
  <summary>詳細說明</summary>

  MCP（Model Context Protocol）是 Anthropic 推出的開放協定，讓 Claude 能夠透過標準化介面連接外部工具和資料來源。設定 MCP 伺服器後，Claude Code 可以直接存取：資料庫查詢、瀏覽器自動化、第三方 API（GitHub、Slack、Jira 等）、本地應用程式。相比手動複製貼上資料，MCP 讓 Claude 能在任務中即時取得和操作外部資訊。詳見 [MCP 入門](/developer/mcp-intro) 課程。

  </details>

- 自訂命令（Slash Commands）

  <details>
  <summary>詳細說明</summary>

  Slash Commands 讓你可以**把常用的複雜提示儲存成簡短指令**。例如，把「閱讀目前的 git diff，撰寫一份符合本專案規範的 commit message」這個提示存成 `/commit`，之後只需要輸入 `/commit` 就能觸發。自訂命令儲存在 `.claude/commands/` 目錄下，可以加入版控與團隊共享，統一整個團隊的工作流程。

  </details>

## 📝 重點筆記

### 🔄 Agentic Loop 運作原理

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

### 📋 CLAUDE.md 範例結構

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

### ⚖️ 批准模式 vs. 計畫模式

| 模式 | 適合場景 |
|------|---------|
| **批准模式** | 每一步都需要確認，適合不熟悉的程式碼庫 |
| **計畫模式** | 先看計畫再執行，適合複雜的重構任務 |
| **自動模式** | 信任 Claude 自動執行，適合簡單且熟悉的任務 |

## 💡 學習建議

**搭配學習：**
- 完成後繼續 [Claude Code 實戰](/developer/claude-code-in-action) 深化技巧
- 學習 [Agent Skills 入門](/developer/agent-skills) 建立可重用的技能

**實作練習：**
1. 安裝 Claude Code，用它閱讀一個現有的程式碼庫，請它解釋架構
2. 建立一個簡單的 CLAUDE.md 描述你的一個專案
3. 用「Explore → Plan → Code」流程完成一個小功能

## 🔗 相關課程

- [Claude Code 實戰](/developer/claude-code-in-action)（進階整合）
- [Agent Skills 入門](/developer/agent-skills)（建立可重用技能）
- [子代理入門](/developer/subagents)（委派複雜任務）
- [MCP 入門](/developer/mcp-intro)（擴展 Claude 的工具）

## 🎯 互動練習

準備好測試你的理解了嗎？前往 [Claude Code 101 互動練習](/claude-products/claude-code-101-practice)，透過 Agentic Loop 概念、工作流程排序、模式選擇情境題等鞏固本課程的核心概念。

## 📚 延伸閱讀

- [Claude Code 101 課程頁面](https://anthropic.skilljar.com/claude-code-101)（英文，原始課程）
- [Claude Code 官方文件](https://docs.anthropic.com/en/docs/claude-code/overview)（英文，完整技術文件）
- [Anthropic Academy 課程總覽](https://www.anthropic.com/learn)（英文，所有課程的入口）
