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

const nlmQ1Options = ["深入探討 AI 的底層技術架構與演算法", "人類如何與 AI 系統互動與協作", "學習最新的提示工程（Prompt Engineering）技巧", "研究 AI 歷史上的發展里程碑"]
const nlmQ2Options = ["能夠編寫複雜的程式碼來開發 AI 系統的能力", "以有效、高效、倫理且安全的方式與 AI 系統互動的能力", "熟記所有 AI 相關的技術術語與定義", "在所有工作流程中完全以 AI 取代人類勞動的能力"]
const nlmQ3Options = ["從「學習 AI」轉變為「使用 AI」", "從「思考 AI」轉變為「與 AI 一起思考」", "從「恐懼 AI」轉變為「無視 AI」", "從「手動操作」轉變為「全自動化」"]
const nlmQ4Options = ["如何確保 AI 的產出符合法律規範", "如何將複雜的任務分解為細小的步驟", "何時應該由人類執行工作，何時應交由 AI 處理", "如何調整 AI 的參數以提高效率"]
const nlmQ5Options = ["我們如何與 AI 系統進行清晰的溝通", "如何用文字描述 AI 的底層邏輯", "如何評估 AI 給出的資訊是否準確", "如何將 AI 的產出結果解釋給其他利害關係人"]
const nlmQ6Options = ["選擇適合的 AI 模型進行部署", "判斷 AI 的回答是否具有創意", "評估與驗證 AI 所提供的產出結果", "區分人類寫的作品與 AI 寫的作品"]
const nlmQ7Options = ["快速的反應時間與低延遲的產出", "負責任、透明且具備問責制", "產出結果的多樣性與豐富度", "能夠不間斷地 24 小時運行任務"]
const nlmQ8Options = ["戰術性技能過於簡單，不值得教授", "戰術性技能（如特定設置或提示）很快就會過時", "建立框架是為了增加學術研究的嚴肅性", "目前的 AI 系統還不需要戰術性技能"]
const nlmQ9Options = ["過度依賴 AI 導致硬體設備損毀", "人們對不完全理解的系統感到挫折感", "AI 會自動產生出超過人類理解能力的策略", "這能讓組織更快地達成數位轉型"]
const nlmQ10Options = ["一種更進階的拼字檢查工具", "用於解決創意與創新問題的協作者", "完全不需要人類監督的獨立決策者", "儲存所有人類知識的靜態資料庫"]

// NotebookLM 延伸測驗：第 02 課（The 4D Framework）
const nlmQ11Options = ["將所有繁瑣且耗時的工作完全交由 AI 處理，以節省人類體力。", "基於對目標的清晰願景，策略性地選擇 AI 在流程中的定位與職責。", "利用 AI 的自主代理權 (Agency) 來自動執行決策，無需人類干預。", "僅在 AI 技術成熟度達到 100% 時，才將關鍵任務交給機器人執行。"]
const nlmQ12Options = ["因為 AI 無法理解簡短的指令，只能處理超過一定字數的文字。", "為了讓 AI 學習使用者的個人語言風格，以便在未來取代使用者的寫作職責。", "這能建立期望的輸出格式、任務處理方式及互動語調，確保協作產出符合願景。", "透過增加指令長度，可以強制 AI 消耗更多運算資源以提升邏輯推理能力。"]
const nlmQ13Options = ["利用個人領域專業知識來評估 AI 產出的事實準確性、邏輯合理性與品牌一致性。", "自動化篩選 AI 產出的工具，旨在完全消除人工審核的必要性。", "僅關注 AI 產出的格式是否美觀，而不涉及內容的實質分析。", "在 AI 提供建議後，無條件接受其邏輯，以確保跨部門決策的客觀性。"]
const nlmQ14Options = ["在所有 AI 產生的內容上標注「由 AI 生成」字樣，無論內容是否經過修改。", "為 AI 協作過程建立嚴謹的驗證流程，確保資料安全、公平性，並對最終產出負責。", "頻繁地更換 AI 工具，以確保始終使用市面上運算能力最強的技術。", "將 AI 協助完成的任務視為 AI 的作品，從而減輕個人的法律責任負擔。"]
const nlmQ15Options = ["這是一個單向過程：先進行描述，然後進行辨識並完成任務。", "使用者根據辨識後的結果來精煉描述，進而引導 AI 產出更符合需求的內容。", "此循環旨在排除「委派」的步驟，直接進入技術層面的調整。", "只要「描述」足夠精確，就無需進入「辨識」的階段。"]
const nlmQ16Options = ["因為這些能力是基於底層軟體架構而設計的，不會隨版本更新改變。", "因為掌握 4D 框架後，使用者將不再需要學習任何新的 AI 操作界面。", "它們是與具體工具無關的基本技能，能幫助使用者隨技術演進持續成長。", "這些能力能讓使用者預測未來五年內所有 AI 技術的發展走向。"]
const nlmQ17Options = ["對 AI 處理大量數據能力的「描述」(Description)。", "在「委派」(Delegation) 中對人類與 AI 工作職責的深思熟慮劃分。", "「辨識」(Discernment) 能力在任務開始前的預防性應用。", "為了符合「盡責」(Diligence) 要求而故意增加工作的困難度。"]
const nlmQ18Options = ["確保 AI 的回覆聽起來更具人性化，以減輕使用者的孤獨感。", "測試 AI 的語言模型限制，看它是否能模仿特定的歷史人物。", "設定與當前任務相符的對話氛圍，例如作為「導師」或「專業顧問」。", "隱藏 AI 的身份，讓輸出的內容看起來完全不像是由機器生成的。"]
const nlmQ19Options = ["勤勉 (Diligence)", "描述 (Description)", "辨識 (Discernment)", "委派 (Delegation)"]
const nlmQ20Options = ["自動化、數位化、現代化、全球化", "有效性、效率、倫理性、安全性", "精確度、反應速度、成本控制、使用者增長", "編程、數據分析、硬體維護、模型訓練"]

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

---

## 🎓 NotebookLM 延伸測驗 {#notebooklm-延伸測驗}

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「The 4Ds of AI Fluency: A Foundation for Human-AI Partnership」課程影片自動生成，涵蓋 4D 框架的核心概念、定義與思維轉變。

完成上方的基礎練習後，用這份測驗檢驗你對完整框架的理解深度。
:::

### 測驗 4-1

<Quiz
  question="根據課程內容，「AI 流暢力」（AI Fluency）課程的核心焦點主要在於什麼？"
  :options="nlmQ1Options"
  :answer="1"
  explanation="課程強調這門課是關於「我們」以及人類與 AI 之間的合作關係。課程明確提到重點不在 AI 作為一種技術，而是人類如何與其互動。"
/>

### 測驗 4-2

<Quiz
  question="課程中提到的「AI 流暢力」定義為何？"
  :options="nlmQ2Options"
  :answer="1"
  explanation="這是課程中對「AI 流暢力」的明確定義，涵蓋了效率與責任感。流暢力不是技術開發能力，而是廣泛的互動能力——有效、高效、倫理且安全。"
/>

### 測驗 4-3

<Quiz
  question="課程希望幫助學員達成哪種思維轉變？"
  :options="nlmQ3Options"
  :answer="1"
  explanation="這反映了將 AI 從外部工具視為合作夥伴的根本性轉變。「與 AI 一起思考」意味著 AI 是思考過程的參與者，而非被動工具。"
/>

### 測驗 4-4

<Quiz
  question="在 AI 流暢力框架的「4D」核心能力中，「委派」（Delegation）主要處理什麼問題？"
  :options="nlmQ4Options"
  :answer="2"
  explanation="「委派」關乎於人類與 AI 之間的工作權責分配——何時由人做、何時交給 AI、何時人機協作。這是 4D 中決策層面的能力。"
/>

### 測驗 4-5

<Quiz
  question="關於「描述」（Description）這項能力，其核心探討的問題是什麼？"
  :options="nlmQ5Options"
  :answer="0"
  explanation="「描述」的核心在於溝通的清晰度，以便 AI 理解人類的意圖。這是 4D 中資訊輸入階段的能力，涵蓋如何設計有效提示。"
/>

### 測驗 4-6

<Quiz
  question="「辨識」（Discernment）能力在 AI 流暢力框架中扮演什麼角色？"
  :options="nlmQ6Options"
  :answer="2"
  explanation="「辨識」要求使用者批判性地審視 AI 的回答，而非盲目接受。這包含事實查核、邏輯評估、以及持續改善協作品質。"
/>

### 測驗 4-7

<Quiz
  question="「勤勉」（Diligence）能力要求我們在與 AI 互動時確保哪些特質？"
  :options="nlmQ7Options"
  :answer="1"
  explanation="「勤勉」旨在確保 AI 的使用是合乎倫理並對結果負責的。這包含透明揭露 AI 的參與、承擔最終責任、以及防範偏見與錯誤資訊。"
/>

### 測驗 4-8

<Quiz
  question="為什麼課程強調建立「基礎框架」而非僅學習戰術性技能（如特定提示語）？"
  :options="nlmQ8Options"
  :answer="1"
  explanation="AI 領域變化極快，唯有核心能力能幫助使用者應對未來的技術迭代。特定的提示語或設定在模型更新後可能完全失效，但 4D 思維框架具有持久價值。"
/>

### 測驗 4-9

<Quiz
  question="課程提到的「組織採用 AI 但缺乏明確策略」會導致什麼後果？"
  :options="nlmQ9Options"
  :answer="1"
  explanation="缺乏策略與理解會導致工具與人的期待之間產生斷層，使員工對不熟悉的系統感到挫折，反而降低效率與信任感。"
/>

### 測驗 4-10

<Quiz
  question="課程中提到的「信任夥伴」（Trusted Partner）概念，是希望將 AI 視為："
  :options="nlmQ10Options"
  :answer="1"
  explanation="這反映了 AI 在更高階的思維與創新任務中所扮演的角色。信任夥伴不是被動工具，而是能與人類共同解決創意與複雜問題的協作者。"
/>

---

## 🎓 NotebookLM 延伸測驗：第 02 課 {#notebooklm-延伸測驗-第02課}

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「The 4D Framework」課程影片自動生成，深度考驗 4D 各能力的精確定義、應用情境與協作循環機制。

建議完成上方第 01 課測驗後，再挑戰這份更進階的題目。
:::

### 測驗 5-1

<Quiz
  question="根據 4D 框架，下列何者最能準確描述「委派」(Delegation) 的核心概念？"
  :options="nlmQ11Options"
  :answer="1"
  hint="思考這項能力與「願景」以及「策略性選擇」之間的關係。"
  explanation="委派的核心在於理解任務目標與 AI 的能力邊界，進而有目的地劃分人類與 AI 的職責。"
/>

### 測驗 5-2

<Quiz
  question="在「描述」(Description) 的能力中，為什麼與 AI 進行「富含背景資訊的對話」比「撰寫簡單提示詞」更為重要？"
  :options="nlmQ12Options"
  :answer="2"
  hint="回想文中提到的公司價值觀、目標受眾及特定教學模式的例子。"
  explanation="有效的描述涉及闡明需求、願景及運作背景，從而為雙方的成功協作奠定基礎。"
/>

### 測驗 5-3

<Quiz
  question="關於「辨識」(Discernment) 能力，下列哪一項描述反映了其在 AI 協作中的關鍵作用？"
  :options="nlmQ13Options"
  :answer="0"
  hint="思考當 AI 給出行銷策略建議時，人類專家應該扮演什麼樣的角色。"
  explanation="辨識要求使用者運用自身判斷力來篩選有用資訊，並識別何時需要修正或捨棄 AI 的產出。"
/>

### 測驗 5-4

<Quiz
  question="在 4D 框架中，「盡責」(Diligence) 的實踐最能體現在下列哪種行為中？"
  :options="nlmQ14Options"
  :answer="1"
  hint="考慮在招聘流程中使用 AI 時，如何確保過程既安全又符合倫理規範。"
  explanation="盡責涉及負責任的互動，包括控制偏差、保護敏感數據以及願意承擔作品的最終責任。"
/>

### 測驗 5-5

<Quiz
  question="大多數 AI 互動涉及「描述」(Description) 與「辨識」(Discernment) 之間的循環。關於此循環的運作，下列敘述何者正確？"
  :options="nlmQ15Options"
  :answer="1"
  hint="想想你在使用 AI 時，如果第一次結果不理想，你會採取什麼行動。"
  explanation="透過評估 AI 的初步產出並重新定義需求，使用者能在這種微循環中不斷優化結果。"
/>

### 測驗 5-6

<Quiz
  question="為什麼 4D 框架被視為一種能對抗技術過時 (future-proof) 的核心能力？"
  :options="nlmQ16Options"
  :answer="2"
  hint="回顧 AI 素養 (AI Fluency) 的定義，重點在於技能的本質。"
  explanation="4D 框架側重於知識、見解與價值觀，這些原則不論 AI 工具如何更迭都能適用。"
/>

### 測驗 5-7

<Quiz
  question="在研究專案的案例中，建議將「分析長篇文件」交給 AI，但將「最終結論」保留給自己。這主要體現了什麼？"
  :options="nlmQ17Options"
  :answer="1"
  hint="關鍵在於「分工」以及「誰負責處理什麼樣的工作」。"
  explanation="這展示了委派的本質：理解 AI 的強項（處理大數據）並保留人類核心價值（批判分析與結論）。"
/>

### 測驗 5-8

<Quiz
  question="在「描述」(Description) 階段中提到的「互動語調與風格」(Tone and style of interaction)，其目的是什麼？"
  :options="nlmQ18Options"
  :answer="2"
  hint="回想導師 (tutor) 的例子，使用者如何要求 AI 引導解決問題。"
  explanation="透過定義語調，可以更精確地引導 AI 以適合該場景的角色進行工作，例如以導師（tutor）的方式引導學習者逐步理解，而非直接給出答案。"
/>

### 測驗 5-9

<Quiz
  question="在評估 AI 的行銷建議時，若發現建議不符合品牌價值，這屬於 4D 框架中的哪一環？"
  :options="nlmQ19Options"
  :answer="2"
  hint="這涉及對 AI 給出的「答案」進行批判性思考與價值觀比對。"
  explanation="辨識涉及判斷 AI 的建議是否與使用者的專業知識、品牌價值觀及受眾目標一致。"
/>

### 測驗 5-10

<Quiz
  question="關於 AI 素養 (AI Fluency) 的定義，下列哪四項指標是 4D 框架旨在幫助我們達成的目標？"
  :options="nlmQ20Options"
  :answer="1"
  hint="思考課程開頭提到的那四個以「e」和「s」開頭的英文單字含義。"
  explanation="AI 素養的核心在於發展實踐技能，以達成有效 (effectively)、高效 (efficiently)、倫理 (ethically) 且安全 (safely) 的協作。"
/>

---

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
