---
title: 'NLM 延伸：深度探討二：AI 與人類合作的未來'
description: 'Google NotebookLM 根據第 07 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ61Options = {
  question: "根據教材，提問（Prompting）的核心本質可以被理解為下列哪一種能力的實際應用？",
  options: [
    { text: "程式碼編寫能力", explanation: "雖然提問有時看起來很技術化，但教材強調它更多是關於溝通而非撰寫程式碼。" },
    { text: "數據分析能力", explanation: "雖然可以利用 AI 進行數據分析，但提問本身的本質並非分析數據的過程。" },
    { text: "描述能力（Description competency）", explanation: "提問是將描述能力應用於實踐，清楚地溝通我們想要什麼、如何完成以及如何與 AI 互動。" },
    { text: "計算思維能力", explanation: "提問確實涉及邏輯，但教材明確將其核心定義為描述能力的展現。" },
  ],
  correctAnswer: 2
};
const nlmQ62Options = {
  question: "在與 AI 溝通時，哪一點是與人類對話最顯著的不同之處，需要特別注意？",
  options: [
    { text: "需要使用非常禮貌的語氣", explanation: "雖然禮貌無妨，但這並非 AI 溝通中特有的技術性差異。" },
    { text: "對於人類能自然推論的事物需要更明確地說明", explanation: "AI 缺乏人類的自然推論能力，因此必須顯化那些在人類對話中通常被省略的隱含資訊。" },
    { text: "必須完全避免使用任何專業術語", explanation: "AI 通常能理解專業術語，關鍵在於提供足夠的上下文而非避開術語。" },
    { text: "AI 完全不需要任何背景資訊即可作業", explanation: "這與教材強調「提供上下文」的重要性完全相反。" },
  ],
  correctAnswer: 1
};
const nlmQ63Options = {
  question: "教材建議在提供上下文時，除了說明「想要什麼」，還可以包含哪些資訊來優化結果？",
  options: [
    { text: "為什麼提出這個要求以及將如何使用這些資訊", explanation: "提供目的和預計用途能幫助 AI 量身打造最適合特定情境與知識水平的回應。" },
    { text: "過去曾經嘗試過失敗的提問紀錄", explanation: "雖然回饋有用，但在初始提問中，說明目的比列出失敗紀錄更具指導意義。" },
    { text: "列出所有不相關的個人愛好以建立連結", explanation: "這會浪費 AI 的上下文窗口，且對任務執行沒有實質幫助。" },
    { text: "要求 AI 預測未來的市場走向", explanation: "這屬於特定的任務類型，而非提供上下文以優化現有任務的通用技巧。" },
  ],
  correctAnswer: 0
};
const nlmQ64Options = {
  question: "關於「n-shot prompting」（少樣本提問），下列敘述何者正確？",
  options: [
    { text: "這是一種限制 AI 只能回答 n 個字的方法", explanation: "這混淆了輸出限制與樣本提供這兩個不同的概念。" },
    { text: "這是指對 AI 連續進行 n 次相同的提問", explanation: "重複提問是為了測試一致性，而非透過範例引導 AI 學習模式。" },
    { text: "透過提供具體的例子讓 AI 模仿所需的風格或格式", explanation: "n 代表例子的數量，透過展示而非僅僅透過說明來引導 AI 產生特定的輸出。" },
    { text: "這是一種強制 AI 在 n 秒內回答的指令", explanation: "AI 的響應速度取決於硬體與模型，而非提問技巧中的樣本數量。" },
  ],
  correctAnswer: 2
};
const nlmQ65Options = {
  question: "在處理複雜任務時，為什麼教材建議將其拆解為較小的步驟？",
  options: [
    { text: "為了節省 AI 的計算資源", explanation: "拆解步驟有時反而會消耗更多資源，其主要目的是確保準確性而非節約。" },
    { text: "確保 AI 遵循你預期的處理邏輯而非自行猜測", explanation: "列出步驟就像給朋友指引，能降低 AI 偏離預期執行路徑的風險。" },
    { text: "因為現代的推理模型無法處理單一的大型任務", explanation: "現代模型其實越來越強大，但拆解步驟對於確保執行品質仍然是有效的專家實踐。" },
    { text: "這樣可以讓輸出的文字量變多", explanation: "輸出的品質比數量更重要，拆解步驟是為了邏輯的嚴密性。" },
  ],
  correctAnswer: 1
};
const nlmQ66Options = {
  question: "教材提到讓 AI 在執行任務前先「思考」的關鍵建議是什麼？",
  options: [
    { text: "讓 AI 在回答之後再解釋其思考過程", explanation: "先做後解釋的效果不如先思考後執行，因為思考能直接影響輸出的品質。" },
    { text: "這只對舊型模型有效，現代模型不需要", explanation: "雖然現代模型具備自動思考能力，但手動引導思考在複雜或專業領域依然極具價值。" },
    { text: "給予 AI 空間在回答「之前」先處理問題", explanation: "在產出最終答案前先進行推導，能顯著提升回應的周全性與邏輯性。" },
    { text: "思考過程應該被完全隱藏，不讓用戶看見", explanation: "教材提到看見思考過程有助於用戶發現 AI 可能在哪裡出錯，進而優化提示詞。" },
  ],
  correctAnswer: 2
};
const nlmQ67Options = {
  question: "當你對如何撰寫或改進提示詞感到不確定時，教材推薦的「秘密武器」是什麼？",
  options: [
    { text: "重新啟動電腦並重試", explanation: "這是技術故障排除的方法，而非提升提問技巧的策略。" },
    { text: "直接要求 AI 幫你撰寫或改進提示詞", explanation: "描述你的困境並委託 AI 協助優化指令，是提升效率最強大的技巧之一。" },
    { text: "去搜尋網路上現成的提示詞模板", explanation: "雖然模板有用，但直接與 AI 互動生成量身打造的提示詞通常更直接有效。" },
    { text: "放棄該任務並改用人工處理", explanation: "提問是迭代的過程，教材鼓勵透過實驗與 AI 協作來克服困難。" },
  ],
  correctAnswer: 1
};
const nlmQ68Options = {
  question: "教材中提到的「Artifacts」（成品/產出物）是什麼？",
  options: [
    { text: "一種專門用來儲存舊提問的資料庫", explanation: "Artifacts 並非儲存工具，而是展示輸出的特定方式。" },
    { text: "Claude 特有的一種呈現互動式內容的方式", explanation: "這是一種獨特的輸出形式，使內容比單純的段落文字更容易理解或消化。" },
    { text: "AI 模型內部的程式碼邏輯結構", explanation: "這是技術底層，而非使用者在互動過程中看到的輸出形式。" },
    { text: "一種防止 AI 產生錯誤資訊的過濾器", explanation: "Artifacts 是一種呈現形式，並非安全或準確性的過濾機制。" },
  ],
  correctAnswer: 1
};
const nlmQ69Options = {
  question: "如果一段對話已經嚴重偏離軌道或修正困難，教材建議的有效做法是什麼？",
  options: [
    { text: "持續在同一個對話中指責 AI 的錯誤", explanation: "這通常無法有效導回正軌，反而可能讓上下文變得混亂。" },
    { text: "完全重啟一個全新的對話", explanation: "有時候從頭開始比試圖修復一個已經出錯的長對話更能獲得好結果。" },
    { text: "等待 24 小時後再繼續嘗試", explanation: "AI 本身沒有時間概念，等待並不會改變模型處理錯誤資訊的方式。" },
    { text: "減少提供給 AI 的背景資訊", explanation: "背景資訊不足通常是出錯的原因，而非解決方法。" },
  ],
  correctAnswer: 1
};
const nlmQ70Options = {
  question: "教材提到的常見提問錯誤中，哪一項最可能導致 AI 的產出不符合預期？",
  options: [
    { text: "假設 AI 能夠讀取你的心思", explanation: "這會導致提問過於模糊，讓 AI 只能猜測你的興趣、知識水平和深度需求。" },
    { text: "在同一個對話中討論多個相關的主題", explanation: "討論「相關」主題通常沒問題，錯誤在於將「多個不相關」的任務混在一起。" },
    { text: "給予 AI 過多的正面回饋", explanation: "正向回饋不屬於教材中列出的導致失敗的「錯誤」，雖然它對邏輯改進幫助有限。" },
    { text: "要求 AI 以特定角色的語氣說話", explanation: "這實際上是教材推薦的有效技巧之一，而非錯誤。" },
  ],
  correctAnswer: 0
};

const nlm07Slides = [
  { src: '/images/ai-fluency/nlm07-slide-01-title.png', caption: '投影片 01' },
  { src: '/images/ai-fluency/nlm07-slide-02-overview.png', caption: '投影片 02' },
  { src: '/images/ai-fluency/nlm07-slide-03-components.png', caption: '投影片 03' },
  { src: '/images/ai-fluency/nlm07-slide-04-framework.png', caption: '投影片 04' },
  { src: '/images/ai-fluency/nlm07-slide-05-dimensions.png', caption: '投影片 05' },
  { src: '/images/ai-fluency/nlm07-slide-06-assessment.png', caption: '投影片 06' },
  { src: '/images/ai-fluency/nlm07-slide-07-evaluation.png', caption: '投影片 07' },
  { src: '/images/ai-fluency/nlm07-slide-08-guidelines.png', caption: '投影片 08' },
  { src: '/images/ai-fluency/nlm07-slide-09-examples.png', caption: '投影片 09' },
  { src: '/images/ai-fluency/nlm07-slide-10-implementation.png', caption: '投影片 10' },
  { src: '/images/ai-fluency/nlm07-slide-11-best-practices.png', caption: '投影片 11' },
  { src: '/images/ai-fluency/nlm07-slide-12-summary.png', caption: '投影片 12' },
]
</script>

# 📓 第 07 課：深度探討二：AI 與人類合作的未來

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 07 課：深度探討二：AI 與人類合作的未來

展望 AI 與人類協作的發展方向，理解人機共進的核心原則與最佳實踐。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm07-summary.mp4"
  poster="/images/ai-fluency/nlm07-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm07-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm07-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm07-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理
本課程涵蓋的核心主題與議題概要。
---
## 📊 簡報概覽

<SlideViewer :slides="nlm07Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ61Options" />

<Quiz :options="nlmQ62Options" />

<Quiz :options="nlmQ63Options" />

<Quiz :options="nlmQ64Options" />

<Quiz :options="nlmQ65Options" />

<Quiz :options="nlmQ66Options" />

<Quiz :options="nlmQ67Options" />

<Quiz :options="nlmQ68Options" />

<Quiz :options="nlmQ69Options" />

<Quiz :options="nlmQ70Options" />
