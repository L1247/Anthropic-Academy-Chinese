---
title: Agent Skills 入門
description: 建立可重用的 SKILL.md 指令檔，讓 Claude Code 自動套用在正確任務上
---

# Agent Skills 入門

<Badge type="warning" text="⭐⭐ 中級" /> <Badge type="info" text="Claude Code 擴充" /> <Badge type="warning" text="完成可獲證書" />

> **原始課程**：[Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills)（英文）

## 課程簡介

你是否總是在告訴 Claude Code 同樣的事情？「每次 commit 前先跑測試」、「程式碼審查時檢查這五個面向」、「文件要用這個格式」……

**Agent Skills** 是解決這個問題的方案：一次教會 Claude，它就永遠記住了。

Skills 是可重用的 Markdown 指令檔，Claude Code 會**自動識別並在正確的任務中套用**，不需要每次手動提醒。

## 前置條件

::: warning 前置條件
- **Claude Code 的基本使用經驗**（至少完成過幾個任務）
- 建議先完成 [Claude Code 101](/claude-products/claude-code-101)
:::

## 學習目標

完成本課程後，你將能夠：

- 理解 Skills 與其他自訂選項（CLAUDE.md、Hooks、子代理）的差異
- **從零開始建立 Skill**（包含 SKILL.md 前置標記）
- 撰寫有效的**描述（description）**觸發自動匹配
- 組織 **Skill 目錄結構**
- 配置**進階選項**：限制工具存取、使用無上下文消耗的指令碼
- **跨團隊分享和部署** Skills
- 除錯常見的 Skill 問題

## 課程大綱

### 單元一：Skills 的概念
- 什麼情況下應該建立 Skill？
- Skills vs. CLAUDE.md vs. Hooks vs. 子代理的使用時機
- Skills 的工作原理：如何觸發、如何執行

### 單元二：建立第一個 Skill
- SKILL.md 的檔案結構
- Frontmatter 的必要欄位
- 描述欄位：如何讓 Claude 自動識別

### 單元三：有效的 Skill 描述

Skill 的觸發依賴 `description` 欄位的品質：

```markdown
---
name: code-review
description: >
  當使用者要求審查程式碼、進行 code review、
  或想要找出程式碼中的問題時，使用這個技能。
  也適用於 PR 審查和提交前的最終檢查。
---

# 程式碼審查指南

## 審查面向
1. 安全性：是否有潛在的安全漏洞？
2. 效能：是否有明顯的效能問題？
3. 可讀性：程式碼是否易於理解？
4. 測試覆蓋：是否有足夠的測試？
5. 文件：是否有必要的注釋？
```

### 單元四：Skills 目錄結構
- 專案層級 vs. 使用者層級 Skills
- 推薦的目錄組織方式
- 命名規範

### 單元五：進階配置
- 限制 Skill 可用的工具（工具存取限制）
- 使用不消耗上下文的指令碼（Headless Scripts）
- 條件性觸發

### 單元六：團隊共享與部署
- 將 Skills 加入版本控制（Git）
- 共享 Skills 的最佳實踐
- 企業環境的 Skills 分發

### 單元七：除錯
- Skill 不觸發的常見原因
- 測試 Skill 觸發條件
- 日誌和追蹤

## 重點筆記

### Skills vs. 其他自訂選項的比較

| 工具 | 使用場景 |
|------|---------|
| **CLAUDE.md** | 整個專案的持久性上下文和規則 |
| **Skills（SKILL.md）** | 特定任務類型的可重用指令 |
| **Hooks** | 事件觸發的自動化（commit 前、工具呼叫後） |
| **子代理** | 將複雜任務委派給獨立的 Claude 實例 |

### SKILL.md 完整結構範例

```markdown
---
name: commit-message
description: >
  當使用者要 commit 程式碼、準備 git commit、
  或需要幫忙撰寫 commit message 時使用。
tools: ["bash", "read"]  # 限制可用工具
---

# Commit Message 撰寫規範

## 格式要求
使用 Conventional Commits 格式：
`<type>(<scope>): <description>`

## 類型清單
- feat: 新功能
- fix: 修復 bug
- docs: 文件更新
- refactor: 程式碼重構
- test: 測試相關

## 步驟
1. 查看 `git diff --staged` 了解變更內容
2. 識別主要變更類型
3. 撰寫清晰、簡潔的描述（不超過 72 字元）
4. 如有必要，加入詳細說明段落
```

### 好的 Skill 描述 vs. 差的 Skill 描述

```markdown
# 差的描述（太模糊）
description: "程式碼相關任務"

# 好的描述（具體、包含觸發關鍵字）
description: >
  當使用者要審查程式碼品質、進行 code review、
  提交 PR 前做最終檢查，或想識別程式碼中的
  bug、安全漏洞、效能問題時，使用這個技能。
```

## 學習建議

**搭配學習：**
- 先完成 [Claude Code 101](/claude-products/claude-code-101)
- 結合 [Claude Code 實戰](/developer/claude-code-in-action)

**實作練習：**
1. 識別你在 Claude Code 中最常重複告訴它的 3 件事
2. 為其中一件事建立第一個 Skill
3. 建立一個 `review-pr` Skill，讓 Claude 按照你的標準審查 PR

## 相關課程

- [Claude Code 101](/claude-products/claude-code-101)（基礎，建議先修）
- [Claude Code 實戰](/developer/claude-code-in-action)（深度整合）
- [子代理入門](/developer/subagents)（另一種擴展方式）
