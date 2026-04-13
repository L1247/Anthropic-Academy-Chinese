---
title: 'NLM 延伸：描述（Description）'
description: 'Google NotebookLM 根據第 06 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ51Options = {
  question: "根據影片內容，「AI 流暢度」（AI Fluency）的核心定義是什麼？",
  options: [
    { text: "能夠有效、高效、符合倫理且安全地與 AI 合作。", explanation: "這涵蓋了影片開頭提到的四個關鍵維度，強調了與 AI 互動的全面性要求。" },
    { text: "精通多種程式語言以直接修改 AI 的底層代碼。", explanation: "雖然技術能力有用，但 AI 流暢度更側重於作為使用者與系統的互動與溝通能力。" },
    { text: "擁有編寫極其複雜提示詞以獲取隱藏功能的能力。", explanation: "影片指出描述不僅僅是編寫聰明的提示詞，而是建立一種思維環境。" },
    { text: "自動化所有與 AI 的互動以減少人類的參與。", explanation: "AI 流暢度強調的是「人類與 AI 的互動」，而非單純的自動化。" },
  ],
  correctAnswer: 0
};
const nlmQ52Options = {
  question: "「描述」（Description）能力被視為一種「思維環境」，其主要目的是什麼？",
  options: [
    { text: "在人類的意圖與 AI 的能力之間建立橋樑。", explanation: "這反映了透過清晰溝通來引導 AI 邏輯推理並達成目標的核心觀點。" },
    { text: "取代 AI 的訓練數據以提供最新的資訊。", explanation: "描述是提供背景而非取代 AI 原有的廣泛訓練知識。" },
    { text: "限制 AI 的思考範圍以防止其產生創意。", explanation: "描述是為了引導而非單純限制，且 AI 的探索能力在某些場景下是必要的。" },
    { text: "讓 AI 能夠獨立預測使用者的所有潛在需求。", explanation: "影片強調 AI 無法讀心，因此需要使用者主動進行細節描述。" },
  ],
  correctAnswer: 0
};
const nlmQ53Options = {
  question: "在「產品描述」（Product Description）中，下列哪一項是使用者應該明確告知 AI 的細節？",
  options: [
    { text: "輸出內容的格式、受眾以及適當的風格。", explanation: "這屬於定義最終成果特徵的範疇，確保 AI 不必猜測使用者的具體需求。" },
    { text: "AI 應該使用的特定神經網路層級。", explanation: "這屬於模型底層技術細節，通常不在使用者進行產品描述的範疇內。" },
    { text: "AI 進行邏輯推理時的具體思考步驟。", explanation: "這更接近「過程描述」，而非定義最終產品的樣貌。" },
    { text: "使用者過去與所有 AI 互動的歷史記錄。", explanation: "雖然歷史脈絡有用，但產品描述專注於當前任務的具體要求。" },
  ],
  correctAnswer: 0
};
const nlmQ54Options = {
  question: "「過程描述」（Process Description）的主要作用為何？",
  options: [
    { text: "引導 AI 助手如何處理或著手進行你的請求。", explanation: "這強調了指定工作方法與工作流的重要性，有時這比終點目標更關鍵。" },
    { text: "確保 AI 的回應語氣顯得專業且客觀。", explanation: "語氣和行為風格通常被歸類為「表現描述」而非「過程描述」。" },
    { text: "向 AI 提供任務完成後的評分標準。", explanation: "這屬於回饋機制，過程描述側重於任務執行中的引導。" },
    { text: "決定 AI 是否應該詳細解釋其答案。", explanation: "這涉及到 AI 的行為表現方式，屬於表現描述的範疇。" },
  ],
  correctAnswer: 0
};
const nlmQ55Options = {
  question: "當你給予 AI 範例並說「這就是我會做的方式」時，這屬於哪種描述技術？",
  options: [
    { text: "過程描述（Process Description）", explanation: "透過範例演示（Demonstration）是引導 AI 採用特定工作方式的有效手段。" },
    { text: "產品描述（Product Description）", explanation: "範例雖然展示了成品，但在這裡的主要目的是展示達成成品的「方式」。" },
    { text: "表現描述（Performance Description）", explanation: "表現描述側重於 AI 的行為特質（如：挑戰假設），而非具體操作步驟。" },
    { text: "基礎描述（Foundation Description）", explanation: "影片中並未提及「基礎描述」這一專有名詞。" },
  ],
  correctAnswer: 0
};
const nlmQ56Options = {
  question: "關於「表現描述」（Performance Description），下列哪項描述最為準確？",
  options: [
    { text: "定義 AI 在互動過程中的行為特徵或「人格」。", explanation: "這包含決定 AI 是要挑戰使用者還是順從使用者，以及提供細節的程度。" },
    { text: "優化 AI 運算速度以提高系統效能。", explanation: "這裡的「表現」是指互動行為，而非硬體或演算法的執行效能。" },
    { text: "列出所有 AI 不應該使用的禁語清單。", explanation: "這雖然涉及行為，但表現描述更側重於定義 AI 作為思維夥伴的角色定位。" },
    { text: "僅僅是指規定 AI 回應的字數限制。", explanation: "字數限制通常屬於產品描述中的格式要求，表現描述層次更高。" },
  ],
  correctAnswer: 0
};
const nlmQ57Options = {
  question: "影片中提到，如果不將 AI 視為資料庫或自動販賣機，我們應該如何看待它？",
  options: [
    { text: "會根據情境表現出不同行為的互動系統。", explanation: "影片強調 AI 像人一樣，在不同脈絡下會有不同的表現，需要適當的行為引導。" },
    { text: "一個能隨時讀取使用者心思的數位助理。", explanation: "影片明確反對 AI 能讀心這一觀念，強調溝通的必要性。" },
    { text: "一個儲存了人類所有知識的靜態工具。", explanation: "這與「資料庫」的定義過於接近，忽略了 AI 的動態互動特質。" },
    { text: "一個不需要指令就能自行優化任務的黑盒子。", explanation: "這種看法忽略了人類在「描述」與「引導」中所扮演的關鍵角色。" },
  ],
  correctAnswer: 0
};
const nlmQ58Options = {
  question: "在詢問 AI 時，思考「我現在需要什麼樣的思維夥伴」是屬於哪一個概念的範疇？",
  options: [
    { text: "表現描述（Performance Description）", explanation: "決定 AI 應該探索多種可能性還是鎖定單一答案，是行為特質的選擇。" },
    { text: "產品描述（Product Description）", explanation: "這並非在描述最終產出的外觀，而是在描述 AI 思考的姿態。" },
    { text: "過程描述（Process Description）", explanation: "雖然與過程有關，但重點在於 AI 的角色定位與互動風格。" },
    { text: "環境描述（Context Description）", explanation: "影片中使用的是「表現描述」來涵蓋行為方面的定義。" },
  ],
  correctAnswer: 0
};
const nlmQ59Options = {
  question: "為什麼提供詳細的「過程描述」對 AI 的輸出品質有巨大影響？",
  options: [
    { text: "因為它提供了特定情境下的引導，輔助 AI 原有的廣泛訓練。", explanation: "AI 雖有訓練，但過程描述能讓其應用最適合當前獨特情況的方法論。" },
    { text: "因為 AI 的內部邏輯非常脆弱，必須步步指引才能運作。", explanation: "AI 並非脆弱，而是需要導航來確保其強大能力被應用在正確的方向上。" },
    { text: "因為這能強制 AI 關閉其所有的隨機性。", explanation: "過程描述是引導方向，而非完全消除 AI 的生成能力或多樣性。" },
    { text: "因為這可以讓使用者不必再檢查 AI 的最終產出。", explanation: "無論描述多完美，人類的審核與監督（AI 流暢度的一環）仍然不可或缺。" },
  ],
  correctAnswer: 0
};
const nlmQ60Options = {
  question: "透過發展描述能力，你可以將 AI 從「通用助手」轉化為什麼？",
  options: [
    { text: "精確調校的思維夥伴（Finely tuned thinking partners）", explanation: "這總結了描述能力的終極目標：使 AI 真正滿足使用者的獨特需求。" },
    { text: "完全自動化的決策機器。", explanation: "AI 流暢度強調的是互動與合作，而非將決策權完全移交給機器。" },
    { text: "更快速的資料檢索工具。", explanation: "描述能力超越了檢索，它涉及創造、分析與共同思考。" },
    { text: "不需要任何提示詞的自主智能體。", explanation: "描述本身就是一種提示與溝通的過程，這與自主性並不衝突但強調互動。" },
  ],
  correctAnswer: 0
};

const nlm06Slides = [
  { src: '/images/ai-fluency/nlm06-slide-01-title.png', caption: '投影片 01' },
  { src: '/images/ai-fluency/nlm06-slide-02-concept.png', caption: '投影片 02' },
  { src: '/images/ai-fluency/nlm06-slide-03-framework.png', caption: '投影片 03' },
  { src: '/images/ai-fluency/nlm06-slide-04-dimensions.png', caption: '投影片 04' },
  { src: '/images/ai-fluency/nlm06-slide-05-checklist.png', caption: '投影片 05' },
  { src: '/images/ai-fluency/nlm06-slide-06-assessment.png', caption: '投影片 06' },
  { src: '/images/ai-fluency/nlm06-slide-07-evaluation.png', caption: '投影片 07' },
  { src: '/images/ai-fluency/nlm06-slide-08-guidelines.png', caption: '投影片 08' },
  { src: '/images/ai-fluency/nlm06-slide-09-examples.png', caption: '投影片 09' },
  { src: '/images/ai-fluency/nlm06-slide-10-implementation.png', caption: '投影片 10' },
]
</script>

# 📓 第 06 課：描述（Description）

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 06 課：AI 能力診斷與限制

深入探討 AI 系統的能力邊界與診斷方法，學會精確評估 AI 在不同任務中的實際表現。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm06-summary.mp4"
  poster="/images/ai-fluency/nlm06-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm06-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm06-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm06-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理
本課程涵蓋的核心主題與議題概要。
---
## 📊 簡報概覽

<SlideViewer :slides="nlm06Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ51Options" />

<Quiz :options="nlmQ52Options" />

<Quiz :options="nlmQ53Options" />

<Quiz :options="nlmQ54Options" />

<Quiz :options="nlmQ55Options" />

<Quiz :options="nlmQ56Options" />

<Quiz :options="nlmQ57Options" />

<Quiz :options="nlmQ58Options" />

<Quiz :options="nlmQ59Options" />

<Quiz :options="nlmQ60Options" />
