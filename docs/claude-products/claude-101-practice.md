---
title: Claude 101 — 互動練習
description: 透過功能配對、提示四要素選擇題、提示改寫練習，鞏固 Claude 核心功能與有效提示的理解
---

<script setup>
const q1Options = [
  "Projects：建立帶有系統指示和參考文件的專案，讓同一專案下的所有對話共享相同上下文",
  "Artifacts：Claude 生成的獨立內容塊，可在對話旁預覽和編輯",
  "Skills：可儲存和重用的指令集，讓你不需重複輸入相同指示",
  "Research Mode：讓 Claude 搜尋網路，補充知識截止日後的最新資訊"
]

const q2Options = [
  "明確說明輸出格式（長度、風格、結構）、提供充足背景、給予具體範例、迭代改進",
  "盡量用英文提問，Claude 對英文的理解比中文好",
  "問題越短越好，AI 喜歡簡潔的指令",
  "每次都在新的對話中提問，避免舊對話的內容影響回應"
]

const q3Options = [
  "Research Mode：讓 Claude 自動搜尋網路補充最新資訊，彌補知識截止日的限制",
  "Projects：在專案中上傳最新的法規文件，讓 Claude 以此為基礎回答",
  "Skills：建立一個「查詢最新法規」的可重用指令",
  "Artifacts：把 Claude 的回應存成獨立的法規摘要文件"
]

const q4Options = [
  "Connectors：讓 Claude 直接連接外部服務（如 Google Drive），無需手動下載上傳",
  "Projects：在 Project 中儲存 Google Drive 的連結",
  "Skills：建立一個「每週從雲端讀取文件」的自動化技能",
  "Artifacts：把 Claude 分析 Google Drive 文件後的結果存成可編輯的產出物"
]

const featureLeftItems = [
  { id: 'memory', text: '你需要 Claude「記住」你的品牌語氣偏好，在未來所有相關任務中保持一致' },
  { id: 'reuse', text: '你每週重複使用同樣的格式整理會議記錄，不想每次都重新輸入格式說明' },
  { id: 'cloud', text: '你想讓 Claude 直接讀取你 Google Drive 中的文件，不想手動複製貼上' },
  { id: 'preview', text: 'Claude 幫你寫了一段 HTML 網頁程式碼，你想立即看到視覺效果' },
]

const featureRightItems = [
  { id: 'r_projects', text: 'Projects（專案）' },
  { id: 'r_skills', text: 'Skills（技能）' },
  { id: 'r_connectors', text: 'Connectors（連結器）' },
  { id: 'r_artifacts', text: 'Artifacts（產出物）' },
]

const featureCorrectPairs = [
  ['memory', 'r_projects'],
  ['reuse', 'r_skills'],
  ['cloud', 'r_connectors'],
  ['preview', 'r_artifacts'],
]

const emailKeywords = ["背景", "目的", "語氣", "格式", "收件人", "長度"]

const emailSample = `請幫我寫一封電子郵件，內容如下：

收件人：我的直屬主管（資深產品經理，關係良好）
我的身份：產品設計師，在公司任職 2 年

目的：我下週需要請假 3 天（週一到週三）去處理家庭緊急事務，需要告知主管並確認工作交接安排。

目前手上的工作狀態：
- 使用者測試報告已完成，可在我休假前交出
- 與工程師的 UI Review 會議預計在週二，需要改期

語氣：正式但誠懇，帶一點歉意（臨時告知），同時展現我已考慮好交接方案

格式：
- 開頭簡短說明原因（不需透露家庭細節）
- 說明目前工作狀態和交接方案
- 確認請假日期並詢問是否方便
- 長度：3–4 段，約 200 字以內`

const q5Options = [
  "Claude Sonnet：效能與速度平衡，適合大多數日常工作任務",
  "Claude Haiku：速度最快，適合快速摘要與即時回應",
  "Claude Opus：推理能力最強，適合多步驟推理與複雜分析",
  "三個模型沒有差別，Claude 會自動選擇最適合的版本回應"
]

const q6Options = [
  "Claude Haiku：速度最快且輕量，適合快速處理大量簡單問答",
  "Claude Sonnet：預設模型，適合大多數任務",
  "Claude Opus：最強推理能力，確保每個問題都有最準確的回應",
  "不需要切換，直接使用 Research Mode 讓 Claude 搜尋答案"
]
</script>

# 💬 Claude 101 — 互動練習

<Badge type="tip" text="⭐ 初學者" /> <Badge type="info" text="約 25 分鐘" /> <Badge type="warning" text="建議先讀完課程再練習" />

> **先修建議**：請先閱讀 [Claude 101](/claude-products/claude-101) 了解 Projects、Artifacts、Skills、Connectors 和 Research Mode，再來這裡動手練習。

## 📖 練習說明

| 練習 | 對應主題 | 說明 |
|------|---------|------|
| 🧩 功能概念暖身 | 核心功能理解 | 確認你對五大核心功能的定義的理解 |
| 🤖 模型選擇 | 模型認識與應用 | 根據使用情境選出最合適的 Claude 模型 |
| 🔧 功能 × 需求配對 | 功能選擇判斷 | 根據使用需求選出最合適的 Claude 功能 |
| 🔍 情境功能選擇 | 實際應用判斷 | 在具體工作情境中選出正確功能 |
| ✍️ 提示改寫 | 有效提示技巧 | 把簡略的請求改寫為包含四要素的有效提示 |

::: tip 如何使用這些練習
- 每題有即時回饋，答錯可以看解釋後**再試一次**
- 配對題：點左側項目再點右側項目完成配對
:::

---

## 🧩 暖身：核心功能概念

### 練習 1-1

<Quiz
  question="你正在負責一個長期客戶項目，每次和 Claude 開始新對話都要重新說明客戶的背景、偏好和品牌規範。哪個 Claude 功能可以解決這個問題？"
  :options="q1Options"
  :answer="0"
  explanation="Projects（專案）正是為了解決「每次開新對話都要重新說明背景」的問題。你可以在 Project 中設定永久性的系統指示（客戶背景、工作偏好）並上傳參考文件，所有在同一 Project 下的對話都會自動共享這些上下文。Artifacts 是管理輸出的工具，Skills 是儲存可重用指令，Research Mode 是即時搜尋——都無法解決「跨對話記憶」的問題。"
/>

### 練習 1-2

<Quiz
  question="以下哪項最準確描述「有效提示」的核心原則？"
  :options="q2Options"
  :answer="0"
  explanation="有效提示的四個核心要素：① 明確說明你要什麼（輸出格式、長度、風格）、② 提供充足的背景（越豐富越精準）、③ 給予具體範例（展示期望的輸出形式）、④ 迭代改進（根據回應調整提示）。語言（中文 vs. 英文）不是關鍵，Claude 對繁體中文的理解很好；簡短問題不等於好問題；新對話不是必要的，Projects 正好讓你保留上下文。"
/>

---

## 🤖 模型選擇：用對工具

### 練習 2-1

<Quiz
  question="你需要請 Claude 協助你撰寫一封日常的工作確認信，確認下週會議時間。你應該使用哪個模型？"
  :options="q5Options"
  :answer="0"
  explanation="日常工作任務（寫信、摘要、格式整理）使用 Claude Sonnet 就已足夠，它是效能與速度的最佳平衡點，也是預設推薦的模型。Haiku 適合更輕量的即時回應；Opus 的強項是複雜推理，用在寫確認信上是「大材小用」。"
/>

### 練習 2-2

<Quiz
  question="你的客服系統每天需要處理數百則簡單的常見問題回覆（例如：「退貨政策是什麼？」「營業時間？」）。在這個高頻、簡單的場景下，哪個模型最合適？"
  :options="q6Options"
  :answer="0"
  explanation="Claude Haiku 是速度最快、最輕量的模型，專為需要大量快速回應的簡單任務設計——正好符合客服常見問題的場景。Sonnet 雖然也可以做，但在這種高頻簡單任務中使用 Sonnet 或 Opus 是不必要的浪費；Research Mode 解決的是知識截止日問題，和模型選擇無關。"
/>

---

## 🔧 功能 × 需求配對

根據四種使用需求，配對到最合適的 Claude 功能。

<MatchingPairs
  :leftItems="featureLeftItems"
  :rightItems="featureRightItems"
  :correctPairs="featureCorrectPairs"
  explanation="四個功能各有其最合適的使用場景：Projects 解決跨對話記憶問題（儲存偏好和背景）；Skills 解決重複指令問題（存成可重用的格式範本）；Connectors 解決外部服務整合問題（直接讀取雲端文件）；Artifacts 解決輸出管理問題（預覽和編輯 Claude 生成的獨立內容）。認清每個功能的用途，才能在正確時機選用正確工具。"
/>

---

## 🔍 情境功能選擇

### 練習 3-1

<Quiz
  question="你需要查詢台灣 2025 年最新的個人資料保護法修正內容，這些資訊可能在 Claude 的訓練截止日之後才發生。哪個功能最能幫助你？"
  :options="q3Options"
  :answer="0"
  explanation="Research Mode 讓 Claude 自動在網路上搜尋最新資訊，直接解決「知識截止日限制」的問題——它讓 Claude 能存取訓練資料截止日後的最新事件和資訊。Projects 中上傳文件也是好方法，但需要你自己先找到並上傳文件；Research Mode 是直接讓 Claude 自己搜尋。"
/>

### 練習 3-2

<Quiz
  question="你每次在 Claude 中整理採購申請書，都需要輸入同樣的格式說明：「請依照以下格式輸出：1. 申請單位 2. 採購品項 3. 預算 4. 效益說明 5. 主管核簽欄」。哪個功能可以讓你不再重複輸入？"
  :options="[
    'Skills（技能）：儲存可重用的指令集，下次直接叫出「採購申請書格式」技能',
    'Projects（專案）：把格式說明存進系統指示',
    'Artifacts（產出物）：把每次的採購書存成 Artifact 重複使用',
    'Connectors（連結器）：連接採購系統自動填入格式'
  ]"
  :answer="0"
  explanation="Skills（技能）是為了解決「不想重複輸入相同指示」的問題——把固定的格式說明儲存成一個技能，下次直接叫出使用。Projects 也可以存格式（在系統指示中），但 Projects 是針對長期項目的整體背景設定；Skills 更適合跨項目、可重複使用的單一指令集（如「採購書格式」可以在任何 Project 中使用）。"
/>

---

## ✍️ 提示改寫：電子郵件請假申請

把模糊的請求改寫為包含「收件人、目的、語氣、格式」四要素的完整有效提示。

<PromptRewrite
  original-prompt="幫我寫一封請假信給主管。"
  :required-keywords="emailKeywords"
  :min-length="80"
  :sample-answer="emailSample"
/>

---

## 💡 練習後建議

完成以上練習後，你可以：

1. **建立你的第一個 Project**：針對你最常做的工作類型（客戶溝通、技術文件、簡報製作），設定系統指示並上傳常用參考文件，然後在 Project 中完成 3 個任務
2. **測試 Research Mode**：用一個你知道答案的最新事件詢問 Claude（不啟動 Research Mode），再開啟 Research Mode 問同一個問題，比較差異
3. **建立一個常用 Skill**：把你工作中最常重複輸入的指令（如會議記錄格式、週報格式），存成你的第一個技能

## 🔗 相關課程

- [Claude 101](/claude-products/claude-101)（本練習對應課程）
- [Claude Cowork 入門](/claude-products/claude-cowork)（桌面本地檔案協作）
- [Claude Code 101](/claude-products/claude-code-101)（開發者工具）
- [AI 素養：框架與基礎](/ai-fluency/framework-foundations)（4D 協作框架）

---

*本練習題目依據 [Claude 101](https://anthropic.skilljar.com/claude-101)（Anthropic Academy）課程內容整理。*
