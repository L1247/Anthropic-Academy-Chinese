---
title: 4D 框架互動練習
description: 透過選擇題、委派四問情境、提示改寫、盡責聲明產生器，親手操作學會 Delegation、Description、Discernment、Diligence
---

<script setup>
const quizOptions1 = [
  "Delegation（委派）：設定目標，決定是否與 AI 合作",
  "Description（描述）：精準描述目標，引導 AI 產出有用輸出",
  "Discernment（辨識）：準確評估 AI 輸出和行為的有用程度",
  "Diligence（盡責）：對 AI 使用方式與輸出負起責任"
]

const quizOptions2 = [
  "Description（描述）：你在設計提示",
  "Delegation（委派）：你在決定是否與 AI 合作以及如何合作",
  "Discernment（辨識）：你在評估 AI 的輸出",
  "Diligence（盡責）：你在履行對報告的責任"
]

const quizOptions3 = [
  "AI 輸出聽起來專業，就不需要人類負責",
  "盡責代表你對最終輸出負責，包含確保準確性、透明使用 AI，以及符合道德標準",
  "只要在文件末尾標注「AI 輔助」就完成了盡責義務",
  "盡責只適用於涉及敏感資訊的任務"
]

const quizOptions4 = [
  "數字非常精確，可以直接引用在報告中",
  "應查證具體數字來源，因為 AI 可能生成無法核實的統計數據（幻覺）",
  "AI 說的數字雖然看起來合理，但還是刪除比較安全",
  "先用這些數字，之後有空再查"
]

const quizOptions5 = [
  "第一次收到不滿意的輸出，就放棄使用 AI，改自己寫",
  "每次都用完全相同的提示重新提問，等待不同結果",
  "收到 AI 回應後，找出 1–2 個可改善的點，針對這些點調整提示，再試一次",
  "把 AI 的所有輸出都混合起來，取平均"
]

const quizOptions6 = [
  "直接使用，因為 AI 通常比較精確",
  "完全不使用這份分析，全部重寫",
  "把數字和計畫標注為「待核實」，向主管說明資料來源待確認，並在交稿前盡力查證",
  "把 AI 的分析拆散重組，讓它看起來像自己寫的"
]

const emailKeywords = ["背景", "客戶", "目的", "語氣", "主旨", "格式"]
const explainKeywords = ["對象", "程度", "範例", "格式", "長度", "用途"]

const sampleEmail = `請以我（台灣中型科技公司的業務主管）的身份，撰寫一封正式但友善的電子郵件給長期合作的日本客戶田中先生。

背景：上週因內部流程問題，導致他訂購的產品延誤出貨 3 天，客戶已表達不滿。

郵件目的：
1. 誠摯道歉，承認是我方失誤（不推卸責任）
2. 說明我們已採取的補救措施
3. 提出具體補償方案（例：下次訂單 95 折優惠）

格式要求：
- 中文書寫，正式敬語
- 總長度不超過 250 字
- 結尾附上聯絡方式

語氣：誠懇、負責、積極解決問題，避免過度道歉顯得軟弱。`

const sampleExplain = `請針對完全沒有技術背景的行銷部門同事（熟悉商業邏輯，不懂程式），解釋「機器學習」是什麼。

說明要求：
- 用 2–3 個他們日常生活中遇到的真實例子說明（例如：串流服務推薦、信用卡詐騙偵測）
- 避免使用數學公式或程式碼
- 結構：先用一句話定義 → 再給例子 → 最後說明跟我們工作的關聯
- 長度：約 200 字，適合在會議室口頭分享
- 語氣：輕鬆、對話式

目的：讓他們在下週跨部門會議中能聽懂 AI 工具討論。`
</script>

# 🎯 4D 框架互動練習

<Badge type="tip" text="⭐ 初學者" /> <Badge type="info" text="約 30 分鐘" /> <Badge type="warning" text="建議先讀完 4D 基礎再練習" />

> **先修建議**：請先閱讀 [AI 素養：框架與基礎](/ai-fluency/framework-foundations) 了解 4D 的理論後，再來這裡動手練習。

## 📖 練習說明

本頁包含四類互動練習，對應 4D 框架的每個核心能力：

| 練習 | 對應能力 | 說明 |
|------|---------|------|
| 🧩 選擇題暖身 | 4D 全覽 | 確認你對四個 D 的基本概念是否正確 |
| 🎯 委派四問情境 | Delegation（委派） | 用真實情境套用委派四問，得出建議 |
| ✍️ 提示改寫練習 | Description（描述） | 把模糊提示改寫成包含六項技巧的有效提示 |
| 🔍 辨識題組 | Discernment（辨識） | 判斷 AI 回應中潛在的問題與風險 |
| 💎 盡責聲明產生器 | Diligence（盡責） | 填表即時產生格式完整的盡責聲明 |

::: tip 如何使用這些練習
- 每題有即時回饋，答錯可以看解釋後**再試一次**
- 所有練習都是純前端運算，不會傳送任何資料到外部伺服器
- 建議按順序完成，但每個練習都可以獨立使用
:::

---

## 🧩 暖身：4D 概念選擇題

確認你對四個 D 的核心定義有正確的理解。

### 練習 1-1

<Quiz
  question="「準確評估 AI 輸出和行為的有用程度」是哪個 D 的定義？"
  :options="quizOptions1"
  :answer="2"
  explanation="Discernment（辨識）的核心是批判性評估 AI 的輸出——不是懷疑一切，而是有根據地判斷哪些輸出可用、哪些需要修正。委派是決策層面，描述是輸入層面，盡責是責任層面。"
/>

### 練習 1-2

<Quiz
  question="你需要準備一份 20 頁的季度報告，決定哪些章節讓 AI 起草、哪些由自己撰寫。這個決策過程對應哪個 D？"
  :options="quizOptions2"
  :answer="1"
  explanation="Delegation（委派）就是「設定目標，決定是否、何時、以何種方式與 AI 合作」。決定哪些章節委派給 AI、哪些自己寫，正是委派決策。起草提示才是描述，評估輸出才是辨識，聲明 AI 參與才是盡責。"
/>

### 練習 1-3

<Quiz
  question="關於「盡責（Diligence）」，以下哪個說法最正確？"
  :options="quizOptions3"
  :answer="1"
  explanation="Diligence（盡責）不只是貼標籤，而是主動承擔責任的態度：確認輸出的準確性、對使用 AI 的方式保持透明、確保符合倫理與組織規範。無論輸出多專業，最終責任都由使用者承擔。"
/>

---

## 🎯 Delegation｜委派四問情境練習

::: info 如何使用委派四問
對每個情境，依序回答四個關鍵問題，系統將根據你的回答給出建議與分析：
1. 任務是否明確？
2. 出錯後果是否嚴重？
3. 是否需要獨特人類判斷？
4. 你能否有效評估輸出？
:::

### 情境 A：整理會議記錄

<DelegationChecklist scenario="你需要把本次 1 小時會議的逐字稿整理成結構化的會議記錄：條列出討論重點、決議事項、與待辦任務（含負責人與截止日）。逐字稿已由錄音自動轉寫完成，你需要確認格式正確。" />

### 情境 B：醫療建議報告

<DelegationChecklist scenario="一位朋友請你幫忙整理他的病歷資訊，根據他的多種慢性病症狀和目前用藥，提供一份關於可能藥物交互作用的參考報告，供他下週就診時與醫生討論。" />

### 情境 C：產品行銷文案

<DelegationChecklist scenario="你正在為即將發布的新產品撰寫第一批行銷文案。這是品牌首次進入高端市場，對品牌語氣要求極高。你需要三則社群媒體貼文（各 100 字以內），呈現品牌的精緻感與差異化定位。" />

---

## ✍️ Description｜提示改寫練習

::: info 六項有效提示技巧（快速複習）
1. **背景（Context）**：說明任務背景、目的、受眾
2. **範例（Examples）**：用具體例子展示期望
3. **限制（Constraints）**：指定格式、長度、語氣、禁忌
4. **逐步推理（Step-by-step）**：請 AI 一步一步思考
5. **先思考（Think first）**：請 AI 先分析再作答
6. **角色/語氣（Role/Tone）**：指定 AI 的回應角色或風格
:::

### 練習 2-1：商務電子郵件

<PromptRewrite
  original-prompt="幫我寫一封給客戶的郵件"
  :required-keywords="emailKeywords"
  :min-length="80"
  :sample-answer="sampleEmail"
/>

### 練習 2-2：技術概念解釋

<PromptRewrite
  original-prompt="解釋機器學習"
  :required-keywords="explainKeywords"
  :min-length="80"
  :sample-answer="sampleExplain"
/>

---

## 🔍 Discernment｜辨識 AI 輸出的問題

辨識（Discernment）是評估 AI 輸出的能力，包含偵測幻覺、過度確信、邏輯跳躍等問題。

### 練習 3-1

<Quiz
  question="一段 AI 回應寫道：「根據最新的 2024 年數據，全球已有 87.3% 的企業採用了 AI，其中 94.1% 表示生產力提升超過 40%。」你應該如何評估？"
  :options="quizOptions4"
  :answer="1"
  explanation="高度精確的統計數字是 AI 幻覺的常見形式：數字聽起來可信，但可能根本不存在或來源不明。正確的辨識做法是「帶著懷疑的目光」——不是全盤否定，而是對無法核實的具體數字要求來源，再引用。"
/>

### 練習 3-2

<Quiz
  question="以下哪個情境最能說明「描述—辨識循環」的正確使用方式？"
  :options="quizOptions5"
  :answer="2"
  explanation="描述—辨識循環的精髓是「根據辨識結果改善描述」：先用辨識眼光評估 AI 輸出哪裡不夠好（辨識），再用這個判斷調整你的提示（描述），循環迭代。選項 A 跳過了改善機會，選項 B 沒有學習，選項 D 沒有意義。"
/>

### 練習 3-3

<Quiz
  question="你請 AI 撰寫競爭對手分析，AI 回應包含「A 公司市占率約 35%，並計畫在 Q3 推出新產品」等具體數字。你無法立刻驗證，但明天需提交報告。最佳做法是？"
  :options="quizOptions6"
  :answer="2"
  explanation="這是「盡責（Diligence）」與「辨識（Discernment）」協作的情境。正確做法是：使用 AI 的分析結構，但對未經核實的事實數字明確標注不確定性，對上透明說明，並盡力在截止前查證。完全捨棄浪費了 AI 的輔助價值；直接使用則對準確性不負責。"
/>

---

## 💎 Diligence｜盡責聲明產生器

完成任何 AI 輔助的工作後，撰寫一份盡責聲明是透明與負責任使用 AI 的具體行動。填寫下方表單，即時產生你的個人聲明。

::: tip 為什麼需要盡責聲明？
盡責聲明不只是格式，而是讓你主動思考：**你對這份工作承擔了多少責任？** 它幫助讀者、同事或主管了解 AI 在其中扮演的角色，也讓你在提交前更謹慎地檢視輸出品質。
:::

<DiligenceBuilder />

## 💡 練習後建議

完成以上練習後，你可以：

1. **把今天你實際使用 AI 完成的一件事**，試著套用委派四問回頭評估：你的決策合理嗎？
2. **找一段你最近收到的 AI 回應**，用辨識的眼光找出一個可以改進的地方，並修改你的提示再試一次
3. **複製你的盡責聲明**，貼到下次 AI 輔助的作業或報告末尾，養成習慣

持續練習這四個 D，AI 素養就會自然融入你的工作方式。

## 🔗 相關課程

- [AI 素養：框架與基礎](/ai-fluency/framework-foundations)（4D 完整理論）
- [AI 能力與限制](/ai-fluency/capabilities-limitations)（深化辨識能力）
- [學生的 AI 素養](/ai-fluency/for-students)（學術情境的 4D 應用）
- [教育者的 AI 素養](/ai-fluency/for-educators)（教學場景的 4D 應用）

## 📚 延伸閱讀

- [AI Fluency Framework 官方網站](https://aifluencyframework.org/)（英文，含完整 OER 資源）
- [Anthropic AI Fluency 課程](https://anthropic.skilljar.com/ai-fluency-framework-foundations)（英文，原始課程影片）

---

*本頁練習題目依據 [The AI Fluency Framework](https://aifluencyframework.org/)（Rick Dakan & Joseph Feller，與 Anthropic 合作開發）整理，原課程素材以 CC BY-NC-SA 4.0 授權發佈。*
