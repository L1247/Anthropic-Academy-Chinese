---
title: Claude Cowork 入門 — 互動練習
description: 透過產品定位選擇題、任務描述改寫、長任務技巧配對，鞏固 Cowork 任務循環與高品質任務描述的能力
---

<script setup>
const q1Options = [
  "Claude Cowork：桌面應用程式，能讀取和操作你電腦上的真實本地檔案",
  "claude.ai（網頁版）：在瀏覽器中和 Claude 對話，適合單次問答",
  "Claude Code：命令列工具，適合開發者的程式碼工作和自動化腳本",
  "以上三者功能完全相同，只是介面形式不同"
]

const q2Options = [
  "claude.ai（網頁版）：直接在瀏覽器中聊天，最適合單次問答和提示測試",
  "Claude Cowork：在桌面應用程式中，讓 Claude 直接存取和修改你的本地檔案",
  "Claude Code：在終端機中，讓 Claude 讀取整個程式碼庫並執行命令列操作",
  "以上任何一個都可以，效果相同"
]

const q3Options = [
  "描述 → 規劃 → 執行 → 引導：你描述任務，Claude 規劃步驟，執行後你在過程中給予回饋",
  "詢問 → 回答 → 再詢問：和 claude.ai 一樣的問答循環",
  "安裝 → 設定 → 自動執行：設定好就讓 Claude 完全自主運作",
  "探索 → 計畫 → 程式碼 → 提交：和 Claude Code 的工作流程相同"
]

const taskKeywords = ["目標", "輸入", "輸出", "限制", "格式", "資料夾"]

const taskSample = `請幫我整理本季的業績報告：

目標：把每位銷售人員的月度業績整理成一份季度總結，供主管月底報告使用

輸入：讀取 Documents/Sales/Q2/ 資料夾中的 6 份 Excel 檔案（每位銷售人員每月各一份，共 6 個人 × 1 個月 = 先以本月為例）

輸出：
- 格式：新的 Excel 檔案
- 內容：包含每位銷售人員的當月目標、實際業績、達成率，以及團隊總計
- 儲存到：桌面，命名為 2025_Q2_June_Sales_Summary.xlsx

限制：
- 不要修改 Documents/Sales/Q2/ 中的任何原始檔案
- 如果某位銷售人員的檔案找不到，在表格中標注「資料缺失」而非自動填 0`

const longTaskLeftItems = [
  { id: 'small', text: '你擔心 Claude 處理整個資料夾時可能出錯，想先確認結果再擴大範圍' },
  { id: 'overwrite', text: '你需要讓 Claude 修改一批重要文件，擔心原始版本被覆蓋' },
  { id: 'scope', text: 'Claude 在執行任務時不小心存取了你不希望它碰的個人資料夾' },
  { id: 'plan', text: '你想在 Claude 開始執行前，先確認它是否理解了你的目標' },
]

const longTaskRightItems = [
  { id: 'r_small', text: '先測試小範圍：先在 1–2 個檔案上測試，確認沒問題再擴大到整個資料夾' },
  { id: 'r_backup', text: '保留原始備份：涉及修改檔案前，先確認有備份（或告知 Claude 只能讀取、不能修改）' },
  { id: 'r_boundary', text: '設定存取邊界：在任務描述中明確告訴 Claude 哪些資料夾可以操作、哪些不行' },
  { id: 'r_plan', text: '先確認計畫：要求 Claude 先說明執行計畫，你確認後再開始執行' },
]

const longTaskCorrectPairs = [
  ['small', 'r_small'],
  ['overwrite', 'r_backup'],
  ['scope', 'r_boundary'],
  ['plan', 'r_plan'],
]
</script>

# 🤝 Claude Cowork 入門 — 互動練習

<Badge type="tip" text="⭐ 初學者" /> <Badge type="info" text="約 25 分鐘" /> <Badge type="warning" text="建議先讀完課程再練習" />

> **先修建議**：請先閱讀 [Claude Cowork 入門](/claude-products/claude-cowork) 了解任務循環與任務描述四要素，再來這裡動手練習。

## 📖 練習說明

| 練習 | 對應主題 | 說明 |
|------|---------|------|
| 🧩 產品定位暖身 | Cowork vs. claude.ai vs. Claude Code | 確認三個 Claude 產品的定位差異 |
| 🎯 情境產品選擇 | 使用場景判斷 | 根據工作需求選擇正確的工具 |
| ✍️ 任務描述改寫 | 高品質任務描述四要素 | 把模糊指令改寫為含目標、輸入、輸出、限制的完整描述 |
| 🔧 長任務技巧配對 | 引導長任務 | 把常見問題配對到對應的應對技巧 |

::: tip 如何使用這些練習
- 每題有即時回饋，答錯可以看解釋後**再試一次**
- 配對題：點左側項目再點右側項目完成配對
:::

---

## 🧩 暖身：三個 Claude 產品的定位差異

### 練習 1-1

<Quiz
  question="以下哪個描述最準確說明 Claude Cowork 的定位？"
  :options="q1Options"
  :answer="0"
  explanation="Claude Cowork 的核心差異是「直接操作你電腦上的真實本地檔案」——這不是在瀏覽器聊天窗口中對話，而是 Claude 在你的桌面環境中實際讀取、修改、產出文件。claude.ai 網頁版適合單次問答；Claude Code 適合開發者在命令列工作。三者定位不同，不能互相替代。"
/>

### 練習 1-2

<Quiz
  question="Cowork 的核心工作模式「任務循環（Task Loop）」最準確的描述是什麼？"
  :options="q3Options"
  :answer="0"
  explanation="Cowork 的任務循環是：你描述目標（含背景、輸入、輸出、限制）→ Claude 制定並確認計畫 → 逐步執行（讀取檔案、處理、輸出）→ 你在過程中觀察並適時引導方向。關鍵特點是「你在過程中引導」而非設定好就放手——Cowork 不是全自動，而是人機協作的工作模式。"
/>

---

## 🎯 情境產品選擇

### 練習 2-1

<Quiz
  question="你想快速測試一個新的提示模板效果，不需要讀取任何本地檔案，只是想看看 Claude 對特定問題的回應風格。應該用哪個工具？"
  :options="q2Options"
  :answer="0"
  explanation="claude.ai（網頁版）是最適合「單次問答」和「提示測試」的工具——它無需安裝，直接在瀏覽器中開始對話。Cowork 的強項是處理本地檔案和多步驟任務，但這個情境不需要這些能力；Claude Code 需要命令列環境，對這個情境來說過於複雜。選擇正確的工具可以節省時間。"
/>

### 練習 2-2

<Quiz
  question="以下哪些使用情境最適合 Claude Cowork？（複選）"
  :options="[
    '每月把 20 份 PDF 業績報告整理成一份 Excel 摘要表',
    '在瀏覽器中問 Claude 一個關於台灣歷史的問題',
    '自動讀取桌面上所有客戶回饋 Word 文件，分類整理並存成新文件',
    '為你的 Python 後端 API 新增一個 REST 端點'
  ]"
  :answer="[0, 2]"
  :multi="true"
  explanation="Cowork 最適合的情境是「處理本地檔案」和「多步驟任務」。整理 PDF 報告（選項A）和整理 Word 文件（選項C）都是典型的 Cowork 使用場景——涉及本地檔案操作、批次處理、多步驟任務。瀏覽器問答（選項B）用 claude.ai 即可；Python API 開發（選項D）屬於程式碼工作，更適合 Claude Code。"
/>

---

## ✍️ 任務描述改寫：高品質任務描述

把模糊的任務描述改寫為包含「目標、輸入、輸出、限制」四要素的高品質 Cowork 任務描述。

<PromptRewrite
  original-prompt="幫我整理一下業績報告。"
  :required-keywords="taskKeywords"
  :min-length="100"
  :sample-answer="taskSample"
/>

---

## 🔧 長任務技巧配對

課程提供了五個引導長任務的技巧。把四個常見的風險情境配對到最合適的應對技巧。

<MatchingPairs
  :leftItems="longTaskLeftItems"
  :rightItems="longTaskRightItems"
  :correctPairs="longTaskCorrectPairs"
  explanation="每個風險情境有其對應的防範技巧：「擔心出錯」→ 先在小範圍測試再擴大；「怕原始檔被覆蓋」→ 先備份並告知 Claude 只讀取；「Claude 存取了不該碰的資料夾」→ 在任務描述中設定明確的存取邊界；「不確定 Claude 是否理解任務」→ 要求它先說明計畫再執行。這些技巧的共通邏輯是：在任務開始或擴大前先確認，比事後修正錯誤成本低得多。"
/>

---

## 💡 練習後建議

完成以上練習後，你可以：

1. **四要素改寫你的下一個任務**：把你下週需要用 Cowork 完成的一個任務，用「目標、輸入、輸出、限制」四要素框架重新描述，感受低上下文 vs. 高上下文描述的差異
2. **設定第一個 Skill**：找到你每週至少重複一次的任務，把完整的高上下文描述存成一個 Skill，下次一鍵觸發
3. **先測試小範圍**：你下次用 Cowork 處理批量文件時，先只用 1–2 個檔案測試，確認結果符合預期後再擴大範圍

## 🔗 相關課程

- [Claude Cowork 入門](/claude-products/claude-cowork)（本練習對應課程）
- [Claude 101](/claude-products/claude-101)（Claude 基礎功能）
- [Claude Code 101](/claude-products/claude-code-101)（開發者版代理工具）
- [AI 素養：框架與基礎](/ai-fluency/framework-foundations)（4D 協作框架）

---

*本練習題目依據 [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork)（Anthropic Academy）課程內容整理。*
