---
title: 'NLM 延伸：實踐工作場景 5：策劃與執行'
description: 'Google NotebookLM 根據第 12 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ111Options = {
  question: "在進行「目前能力評估」時，建議用戶針對 4D 職能的哪三個等級進行自我評分？",
  options: [
    { text: "新手、發展中、有信心", explanation: "教材明確建議對 4D 職能的熟練程度分為新手（novice）、發展中（developing）與有信心（confident）。" },
    { text: "初學者、進階者、專家", explanation: "雖然這些也是描述熟練度的詞彙，但並非教材中針對 4D 職能評估所使用的特定分類。" },
    { text: "不熟悉、基本了解、完全掌握", explanation: "這組詞彙在描述知識程度時很常見，但與教材中設計的發展層次結構不符。" },
    { text: "觀察、參與、領導", explanation: "這描述的是參與角色而非職能熟練度等級。" },
  ],
  correctAnswer: 0
};
const nlmQ112Options = {
  question: "AI 互動的三種主要方式是什麼？",
  options: [
    { text: "自動化、增強、代理", explanation: "教材指出應識別目前最有效及最無效使用的三種互動模式：Automation、Augmentation 以及 Agency。" },
    { text: "描述、辨別、發展", explanation: "描述（Description）與辨別（Discernment）是課程中提到的技巧，而非 AI 互動的模式。" },
    { text: "輸入、處理、輸出", explanation: "這是一般資訊處理的通用流程，並非教材中定義的 AI 流暢度互動模式。" },
    { text: "指令、反饋、修正", explanation: "這描述的是對話的過程，而非互動的本質模式。" },
  ],
  correctAnswer: 0
};
const nlmQ113Options = {
  question: "在建立個人提示詞與模式庫時，建議為 5 到 10 個常規任務開發什麼？",
  options: [
    { text: "模板提示詞", explanation: "教材建議為常規任務開發模板提示詞（template prompt），以確保持續產生高品質的結果。" },
    { text: "程式碼段落", explanation: "雖然程式碼可能有幫助，但教材強調的是針對 AI 互動的提示詞結構。" },
    { text: "長篇大論的指令", explanation: "有效的提示詞庫應強調模式與模板，而非僅僅是字數眾多的指令。" },
    { text: "固定的回答清單", explanation: "重點在於如何與 AI 互動（提示詞），而非保存 AI 給出的靜態答案。" },
  ],
  correctAnswer: 0
};
const nlmQ114Options = {
  question: "下列哪一項屬於「產品辨別力」（Product Discernment）的評估範圍？",
  options: [
    { text: "答案是否具有邏輯性並符合一致的主題", explanation: "產品辨別力專注於評估 AI 輸出的最終結果是否符合邏輯且內容連貫。" },
    { text: "AI 解決謎題的思考路徑", explanation: "觀察 AI 採取的路徑屬於程序辨別力（Process Discernment），而非產品本身。" },
    { text: "AI 溝通其思維的清晰度", explanation: "溝通表現屬於表現辨別力（Performance Discernment）。" },
    { text: "AI 是否能主動提出好問題", explanation: "這屬於對 AI 互動表現的評估，歸類在表現辨別力。" },
  ],
  correctAnswer: 0
};
const nlmQ115Options = {
  question: "在「交換謎題」遊戲中，當 AI 猜錯時，用戶應該採取什麼行動？",
  options: [
    { text: "輕輕引導 AI 朝向正確的思維鏈和脈絡", explanation: "教材強調不直接給答案，而是透過引導其思維鏈（chain-of-thought）來練習引導技巧。" },
    { text: "立即告訴它正確答案並結束遊戲", explanation: "這無法達到練習「引導」和「辨別」思維過程的學習目的。" },
    { text: "更換一個更簡單的謎題", explanation: "遊戲的目的在於練習與 AI 的互動，而非單純追求猜中題目。" },
    { text: "指出它的錯誤並要求它重新開始", explanation: "單純的指責缺乏引導性，無法讓用戶練習如何優化 AI 的思考路徑。" },
  ],
  correctAnswer: 0
};
const nlmQ116Options = {
  question: "「合作填字遊戲」練習的主要核心價值是什麼？",
  options: [
    { text: "學習引導和改進 AI 的思考", explanation: "透過限制字數或首字母等具體反饋，用戶可以學習如何在實際專案中精確引導 AI。" },
    { text: "測試用戶與 AI 誰的詞彙量更大", explanation: "教材明確表示重點不在於誰更擅長填字，而在於思考的引導與精煉。" },
    { text: "讓 AI 單獨完成困難的謎題", explanation: "這是一項協作活動，目的是為了鍛鍊用戶的「導航」技能。" },
    { text: "取代傳統的語言學習軟體", explanation: "這是一項 AI 流暢度練習，並非通用的語言學習工具。" },
  ],
  correctAnswer: 0
};
const nlmQ117Options = {
  question: "在「程序辨別力」（Process Discernment）中，我們主要觀察什麼？",
  options: [
    { text: "AI 解決問題的方法以及是否考慮多種可能性", explanation: "程序辨別力關注 AI 的方法論、關注範圍是否過窄，以及處理問題的邏輯步驟。" },
    { text: "AI 輸出的美觀程度", explanation: "視覺呈現並非教材中定義的程序辨別力重點。" },
    { text: "AI 運算的執行速度", explanation: "辨別力側重於內容與邏輯的評估，而非技術性能指標。" },
    { text: "提示詞庫的組織結構", explanation: "這是管理資源的能力，與觀察 AI 思考過程的辨別力不同。" },
  ],
  correctAnswer: 0
};
const nlmQ118Options = {
  question: "「概念與約束」（Concepts & Constraints）練習建議用戶如何設定挑戰？",
  options: [
    { text: "選擇複雜概念並加入嚴格的限制條件", explanation: "教材舉例「僅使用烹飪隱喻來解釋」，這體現了複雜概念與嚴格約束的結合。" },
    { text: "盡可能提供詳細的背景資料而不設限", explanation: "這與該練習強調「約束」以練習描述精確度的初衷相反。" },
    { text: "讓 AI 自由發揮不加限制", explanation: "缺乏約束無法有效鍛鍊用戶精確描述需求的能力。" },
    { text: "專注於簡單概念的快速解釋", explanation: "挑戰通常來自於處理複雜概念時的創意束縛。" },
  ],
  correctAnswer: 0
};
const nlmQ119Options = {
  question: "在建立個人 AI 流暢度計畫時，建議將 Claude 當作什麼角色？",
  options: [
    { text: "思考夥伴", explanation: "教材建議與 Claude 作為「thinking partner」合作，分享自我評估並獲得計畫反饋。" },
    { text: "自動化評分機", explanation: "Claude 的作用是協助思考與反饋，而非單純給予一個分數。" },
    { text: "儲存計畫的資料庫", explanation: "雖然它可以處理資訊，但其核心角色在於協作與提供建議。" },
    { text: "完全替代人類的計畫制定者", explanation: "計畫應是個人的，Claude 是輔助角色，而非主導者。" },
  ],
  correctAnswer: 0
};
const nlmQ120Options = {
  question: "為什麼謎題（Puzzles）是練習「精確描述」和「敏銳辨別」的優良工具？",
  options: [
    { text: "因為謎題有特定的指令和明確的評估準則", explanation: "教材提到謎題不像開放式任務，其具備特定指令且往往設計得很棘手，非常適合練習清晰溝通與評估。" },
    { text: "因為謎題不需要任何邏輯思考", explanation: "謎題高度依賴邏輯思考，這正是它們被選中的原因。" },
    { text: "因為 AI 總是能比人類更快解開謎題", explanation: "練習的重點在於「引導過程」而非速度或勝負。" },
    { text: "因為謎題通常與實際工作完全無關", explanation: "雖然謎題本身可能具趣味性，但其鍛鍊的引導技巧與實際專案息息相關。" },
  ],
  correctAnswer: 0
};

const nlm12Slides = [
  { src: '/images/ai-fluency/nlm12-slide-01-slide1.png', caption: '投影片 1' },
  { src: '/images/ai-fluency/nlm12-slide-02-slide2.png', caption: '投影片 2' },
  { src: '/images/ai-fluency/nlm12-slide-03-slide3.png', caption: '投影片 3' },
  { src: '/images/ai-fluency/nlm12-slide-04-slide4.png', caption: '投影片 4' },
  { src: '/images/ai-fluency/nlm12-slide-05-slide5.png', caption: '投影片 5' },
  { src: '/images/ai-fluency/nlm12-slide-06-slide6.png', caption: '投影片 6' },
  { src: '/images/ai-fluency/nlm12-slide-07-slide7.png', caption: '投影片 7' },
  { src: '/images/ai-fluency/nlm12-slide-08-slide8.png', caption: '投影片 8' },
  { src: '/images/ai-fluency/nlm12-slide-09-slide9.png', caption: '投影片 9' },
  { src: '/images/ai-fluency/nlm12-slide-10-slide10.png', caption: '投影片 10' },
  { src: '/images/ai-fluency/nlm12-slide-11-slide11.png', caption: '投影片 11' },
  { src: '/images/ai-fluency/nlm12-slide-12-slide12.png', caption: '投影片 12' },
  { src: '/images/ai-fluency/nlm12-slide-13-slide13.png', caption: '投影片 13' },
  { src: '/images/ai-fluency/nlm12-slide-14-slide14.png', caption: '投影片 14' },
]
</script>

# 📓 第 12 課：實踐工作場景 5：策劃與執行

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 12 課：實踐工作場景 5：策劃與執行

深入探討如何運用 AI 進行計畫制定、專案管理與執行優化，提升組織效率。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm12-summary.mp4"
  poster="/images/ai-fluency/nlm12-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm12-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm12-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm12-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理
本課程涵蓋的核心主題與議題概要。
---
## 📊 簡報概覽

<SlideViewer :slides="nlm12Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ111Options" />

<Quiz :options="nlmQ112Options" />

<Quiz :options="nlmQ113Options" />

<Quiz :options="nlmQ114Options" />

<Quiz :options="nlmQ115Options" />

<Quiz :options="nlmQ116Options" />

<Quiz :options="nlmQ117Options" />

<Quiz :options="nlmQ118Options" />

<Quiz :options="nlmQ119Options" />

<Quiz :options="nlmQ120Options" />
