---
title: Claude Code 101 — 互動練習
description: 透過選擇題、工作流程排序、模式選擇情境題，鞏固 AI 編碼代理概念與 Claude Code 核心工作流程
---

<script setup>
const q1Options = [
  "Agentic AI 能夠自主規劃、執行多步驟任務、操作檔案和執行命令；Chat AI 只能在對話中回應問題",
  "Agentic AI 比 Chat AI 更聰明，回答品質更高",
  "Agentic AI 只能處理程式設計任務；Chat AI 可以處理所有類型的問題",
  "Agentic AI 需要較高的訂閱費用；Chat AI 是免費的"
]

const q2Options = [
  "代理循環（Agentic Loop）：分析任務 → 制定計畫 → 執行步驟 → 觀察結果 → 調整計畫 → 繼續執行，直到完成",
  "代理循環是指 Claude Code 每次啟動時的開機流程",
  "代理循環是多個 Claude 實例同時處理同一個任務的並行機制",
  "代理循環是指上下文視窗達到上限時自動重置對話的機制"
]

const q3Options = [
  "批准模式：每一步都需要人工確認，適合不熟悉的程式碼庫或高風險操作",
  "計畫模式：先讓 Claude 制定完整計畫，你確認後再執行",
  "自動模式：信任 Claude 自動執行，適合簡單且熟悉的任務",
  "除錯模式：讓 Claude 只分析問題而不修改程式碼"
]

const q4Options = [
  "批准模式（Approval Mode）：每一步都需要確認，確保對不熟悉的程式碼庫不做出意外修改",
  "計畫模式（Plan Mode）：先看到完整計畫再決定是否執行",
  "自動模式（Auto Mode）：信任 Claude 自動完成，不需要人工介入",
  "除錯模式：Claude 只分析問題，不修改任何檔案"
]

// 工作流程排序：Explore -> Plan -> Code -> Commit
// items 打亂順序: Code(2), Explore(0), Commit(3), Plan(1)
// correctOrder: [1, 3, 0, 2] -> 第1名是items[1](Explore), 第2名是items[3](Plan), 第3名是items[0](Code), 第4名是items[2](Commit)
const workflowItems = [
  "Code（實作）：執行已批准的計畫，逐步修改程式碼",
  "Explore（探索）：讓 Claude 閱讀程式碼庫，理解現有架構和脈絡",
  "Commit（提交）：確認所有變更符合預期，提交程式碼",
  "Plan（規劃）：根據探索結果制定詳細的實作計畫，待確認後才開始修改"
]
// 打亂後順序: Code(idx=0), Explore(idx=1), Commit(idx=2), Plan(idx=3)
// 正確排列從1到4: Explore(idx=1), Plan(idx=3), Code(idx=0), Commit(idx=2)
const workflowCorrectOrder = [1, 3, 0, 2]

const claudeMdKeywords = ["技術棧", "規範", "不要", "命令", "禁止", "語言"]

const claudeMdSample = `# 電商後台管理系統

## 技術棧
- 語言：TypeScript 5.x
- 框架：Next.js 14（App Router）
- 資料庫：PostgreSQL + Prisma ORM
- 樣式：Tailwind CSS

## 編碼規範
- 所有元件使用 TypeScript，禁止使用 any 類型
- 元件命名：PascalCase；函數命名：camelCase
- 測試：Vitest，關鍵業務邏輯覆蓋率 > 85%
- 所有 API 路由必須有輸入驗證（使用 Zod）

## 不要做的事
- 不要修改 /src/legacy/ 目錄下的任何檔案
- 不要直接連接生產資料庫（只使用 .env.local 中的 DB_URL）
- 不要刪除任何現有的資料庫 migration 檔案

## 常用命令
- 啟動開發伺服器：\`npm run dev\`
- 執行測試：\`npm run test\`
- 資料庫 migration：\`npx prisma migrate dev\``
</script>

# ⚡ Claude Code 101 — 互動練習

<Badge type="warning" text="⭐⭐ 初-中級" /> <Badge type="info" text="開發者" /> <Badge type="info" text="約 25 分鐘" />

> **先修建議**：請先閱讀 [Claude Code 101](/claude-products/claude-code-101) 了解 Agentic Loop 與核心工作流程，再來這裡動手練習。

## 📖 練習說明

| 練習 | 對應主題 | 說明 |
|------|---------|------|
| 🧩 概念暖身 | Agentic AI 與 Agentic Loop | 確認對 AI 代理核心概念的理解 |
| 🔢 工作流程排序 | Explore→Plan→Code→Commit | 把四個步驟排列到正確順序 |
| 🎯 模式選擇情境 | 批准 / 計畫 / 自動模式 | 在具體工作情境中選出正確的執行模式 |
| ✍️ CLAUDE.md 撰寫 | 專案記憶設定 | 把缺乏結構的專案說明改寫為完整的 CLAUDE.md 格式 |

::: tip 如何使用這些練習
- 每題有即時回饋，答錯可以看解釋後**再試一次**
- 排序題：使用上移/下移按鈕調整到正確順序
:::

---

## 🧩 暖身：AI 編碼代理核心概念

### 練習 1-1

<Quiz
  question="「Agentic AI（代理式 AI）」和「Chat AI（聊天式 AI）」最根本的差異是什麼？"
  :options="q1Options"
  :answer="0"
  explanation="根本差異在於「自主執行能力」：Chat AI（如 claude.ai 的對話）在對話框中回應你的問題；Agentic AI（如 Claude Code）能夠自主規劃多步驟計畫、讀取和修改檔案、執行終端機命令、觀察結果後調整計畫，並持續迭代直到完成目標。這不是聰明程度的差異，而是「對話」vs.「行動」的架構差異。"
/>

### 練習 1-2

<Quiz
  question="「Agentic Loop（代理循環）」描述的是什麼？"
  :options="q2Options"
  :answer="0"
  explanation="Agentic Loop 是 AI 代理執行任務的核心模式：接收目標 → 分析並制定計畫 → 執行一個步驟（讀檔、執行命令等）→ 觀察結果 → 根據結果調整計畫 → 繼續下一步，循環直到完成。每個循環的「觀察結果→調整計畫」環節是代理式 AI 比純聊天 AI 更強大的關鍵——它能根據實際執行結果自我修正。"
/>

---

## 🔢 核心工作流程排序

Claude Code 建議遵循四步驟工作流程，以確保安全、有效地完成任務。請把下方步驟排列到正確順序（從第 1 步到第 4 步）。

<RankingExercise
  :items="workflowItems"
  :correctOrder="workflowCorrectOrder"
  explanation="正確順序：① Explore（探索）→ ② Plan（規劃）→ ③ Code（實作）→ ④ Commit（提交）。這個順序的設計邏輯：先讓 Claude 深入理解現有程式碼庫（Explore），才能制定符合現有架構的計畫（Plan）；計畫經過確認後才開始修改（Code），避免走錯方向；所有變更驗證符合預期後才提交（Commit）。跳過 Explore 直接 Code 是最常見的錯誤，會導致 Claude 做出和現有架構不符的變更。"
/>

---

## 🎯 執行模式選擇

### 練習 3-1

<Quiz
  question="你剛接手一個陌生的遺留程式碼庫（Legacy Codebase），需要修改一個業務邏輯複雜的支付模組。哪個 Claude Code 執行模式最適合？"
  :options="q3Options"
  :answer="0"
  explanation="批准模式（Approval Mode）在這個情境是最安全的選擇：你不熟悉程式碼庫，支付模組的業務邏輯複雜，任何錯誤都可能影響真實交易。批准模式讓你在 Claude 每執行一步（讀檔、修改、命令）之前都能看到並確認，避免不知情的意外修改。等你對程式碼庫更熟悉後，可以在低風險任務中切換到自動模式。"
/>

### 練習 3-2

<Quiz
  question="你需要對一個大型功能進行重構，涉及 10 多個檔案的修改。你希望在 Claude 開始動手之前，先看到完整的修改計畫。哪個模式最合適？"
  :options="q4Options"
  :answer="1"
  explanation="計畫模式（Plan Mode）讓 Claude 先制定完整的修改計畫（哪些檔案、怎麼改、順序為何），你審閱並批准後才開始執行。這對於涉及多檔案的大型重構特別重要——可以在實際修改前發現計畫中的問題（如遺漏的依賴關係、順序錯誤）。批准模式雖然安全，但每一步都要確認，效率較低；自動模式對複雜重構而言風險過高。"
/>

### 練習 3-3

<Quiz
  question="以下哪些情境最適合使用「自動模式（Auto Mode）」？（複選）"
  :options="[
    '在你自己的個人項目中，新增一個你完全理解的簡單 UI 元件',
    '對公司生產環境的資料庫 migration 腳本進行修改',
    '為你熟悉的測試框架補充單元測試',
    '重構一個從未見過的第三方 SDK 的核心模組'
  ]"
  :answer="[0, 2]"
  :multi="true"
  explanation="自動模式適合在「信任 Claude 判斷」且「出錯影響有限」的情境。在你自己熟悉的個人項目中新增簡單元件（選項A）和補充熟悉框架的單元測試（選項C），都是低風險、你能評估結果的任務。修改生產資料庫 migration（選項B）風險極高，任何失誤都可能造成資料遺失；修改不熟悉的第三方 SDK（選項D）你無法評估修改的正確性——這兩種情況都應使用批准或計畫模式。"
/>

---

## ✍️ CLAUDE.md 撰寫練習

把非結構化的專案描述改寫為包含「技術棧、規範、禁止事項、常用命令」的標準 CLAUDE.md 格式。

<PromptRewrite
  original-prompt="這是一個 Next.js 的電商後台，用 TypeScript 寫的，資料庫是 PostgreSQL，不要亂改 legacy 的東西，測試要過。"
  :required-keywords="claudeMdKeywords"
  :min-length="120"
  :sample-answer="claudeMdSample"
/>

---

## 💡 練習後建議

完成以上練習後，你可以：

1. **建立你的第一個 CLAUDE.md**：為你目前在做的一個項目，依照今天的練習格式，寫一份包含技術棧、規範、禁止事項、常用命令的 CLAUDE.md
2. **Explore 練習**：在一個你熟悉的程式碼庫中，請 Claude Code 以 Explore 模式閱讀架構，然後問它「這個專案用了哪些設計模式？」觀察它的分析
3. **模式切換體驗**：在一個不重要的練習項目中，分別嘗試三種模式完成同一個任務，感受批准/計畫/自動模式的差異

## 🔗 相關課程

- [Claude Code 101](/claude-products/claude-code-101)（本練習對應課程）
- [Claude Code 實戰](/developer/claude-code-in-action)（進階整合技巧）
- [Agent Skills 入門](/developer/agent-skills)（建立可重用技能）
- [子代理入門](/developer/subagents)（複雜任務委派）
- [MCP 入門](/developer/mcp-intro)（擴展 Claude 的工具）

---

*本練習題目依據 [Claude Code 101](https://anthropic.skilljar.com/claude-code-101)（Anthropic Academy）課程內容整理。*
