---
title: 'NLM 延伸：AI 委派實戰藍圖（The AI Delegation Playbook）'
description: 'Google NotebookLM 根據第 05 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ41Options = {
  question: "根據教材，在選擇用於本課程練習的專案時，下列哪項不是該專案應具備的特徵？",
  options: [
    { text: "規模大到需要多種類型的任務", explanation: "教材明確指出專案應具有足夠的實質性，以涉及多種任務類型。" },
    { text: "大約需要 1 小時的工作量即可完成", explanation: "專案應具備可管理性，使其能在約一小時內完成。" },
    { text: "必須是關於新興技術的研究", explanation: "雖然研究新興技術是建議之一，但並非所有專案都必須以此為主題，學生也可以選擇溝通、創意或學習類專案。" },
    { text: "是你真正感興趣創建或完成的事情", explanation: "個人興趣是選擇專案的重要標準之一，以確保學習過程的投入感。" },
  ],
  correctAnswer: 2
};
const nlmQ42Options = {
  question: "教材中建議「專案規劃與委派」步驟預計需要花費多少時間？",
  options: [
    { text: "10 分鐘", explanation: "這可能不足以進行深入的對話與任務分解。" },
    { text: "20 分鐘", explanation: "教材中明確標註此部分的預估時間為 20 分鐘。" },
    { text: "60 分鐘", explanation: "這通常是完成整個專案所需的時間，而非僅是規劃與委派階段。" },
    { text: "120 分鐘", explanation: "對於一個中等規模的練習專案來說，兩小時的規劃時間過長。" },
  ],
  correctAnswer: 1
};
const nlmQ43Options = {
  question: "下列哪一個選項被歸類為教材中的「研究型專案」範例？",
  options: [
    { text: "為你想要掌握的主題創建一套學習材料", explanation: "這被歸類在「學習型專案」中。" },
    { text: "撰寫一系列向大眾解釋複雜話題的文章", explanation: "這屬於「溝通型專案」的範例。" },
    { text: "比較多種產品、服務或方法並提出建議", explanation: "分析與比較不同選項以產出建議是典型的研究任務。" },
    { text: "為特定產品或服務開發概念", explanation: "這屬於「創意型專案」範例。" },
  ],
  correctAnswer: 2
};
const nlmQ44Options = {
  question: "在第二步「專案願景與目標」中，與 Claude 對話的主要目的是什麼？",
  options: [
    { text: "讓 Claude 幫你決定最終要選擇哪一個專案", explanation: "第一步才是選擇專案，第二步是針對已選定的想法進行深化。" },
    { text: "透過提問與討論來建立對專案最終成果的清晰願景", explanation: "這一步驟強調互動，直到使用者對成功指標與專案價值有明確藍圖。" },
    { text: "直接要求 Claude 生成專案的完整內容", explanation: "這一步是關於規劃與願景設定，而非立即執行最終產出。" },
    { text: "評估 Claude 的語言處理速度", explanation: "這不是教學課程中關於委派的核心目的。" },
  ],
  correctAnswer: 1
};
const nlmQ45Options = {
  question: "在第三步的委派分析中，討論各項任務時應該考慮哪一個層面？",
  options: [
    { text: "哪一部分可以很好地利用 AI 的能力", explanation: "這是委派分析的核心，旨在識別適合 AI 執行的部分。" },
    { text: "如何完全排除人類的參與", explanation: "教材強調識別「人類獨特優勢」，暗示了人機協作的重要性而非完全排除。" },
    { text: "哪一項任務產生的成本最低", explanation: "教材中更關注於技能、知識與協作影響力，而非成本分析。" },
    { text: "如何縮短 Claude 的回應時間", explanation: "教學重點在於委派決策的品質，而非技術性能的優化。" },
  ],
  correctAnswer: 0
};
const nlmQ46Options = {
  question: "在進行委派分析的對話時，教材建議採取什麼樣的溝通方式？",
  options: [
    { text: "僅向 AI 發送單向的指令陳述", explanation: "教材明確指出應避免僅僅交換陳述，而應進行真誠的對話。" },
    { text: "挑戰假設、尋求澄清並對意料之外的見解保持開放", explanation: "這種動態且雙向的溝通有助於挖掘更深層的任務分配見解。" },
    { text: "嚴格遵循預設的腳本，不要與 AI 多聊", explanation: "教材鼓勵開放式的討論與挑戰假設，而非僵化的腳本。" },
    { text: "在對話前就必須先確定所有答案", explanation: "對話的過程本身就是為了產生這些決策與洞察。" },
  ],
  correctAnswer: 1
};
const nlmQ47Options = {
  question: "完成專案計畫後，為什麼需要將其儲存？",
  options: [
    { text: "為了向 Anthropic 公司提交作業", explanation: "教材並未提到需要向該公司提交此計畫。" },
    { text: "為了在後續課程中練習描述、辨識與勤勉等技能", explanation: "該計畫將作為未來實踐 AI 流暢度架構其他核心能力的基礎。" },
    { text: "因為計畫會在一小時後自動失效", explanation: "這是針對工作量的建議，而非文件的效期。" },
    { text: "為了作為法律證據證明版權所有", explanation: "這與課程的學習目標無關。" },
  ],
  correctAnswer: 1
};
const nlmQ48Options = {
  question: "根據「接下來是什麼」章節，緊接在「委派 (Delegation)」之後的第二個核心能力是什麼？",
  options: [
    { text: "辨識 (Discernment)", explanation: "雖然這是架構的一部分，但它不是緊接在委派之後的下一個主題。" },
    { text: "描述 (Description)", explanation: "下一課將探討如何有效地與 AI 系統溝通，即「描述」能力。" },
    { text: "勤勉 (Diligence)", explanation: "這通常是流程中較後期的環節。" },
    { text: "判斷 (Decision)", explanation: "「描述」才是下一個正式介紹的核心能力名稱。" },
  ],
  correctAnswer: 1
};
const nlmQ49Options = {
  question: "如果在嘗試存取課程網站時遇到 CloudFront 403 錯誤，通常意味著什麼？",
  options: [
    { text: "使用者的電腦感染了病毒", explanation: "403 錯誤主要與伺服器端的存取限制或配置有關，而非單機病毒。" },
    { text: "請求被封鎖，可能由於流量過大或配置錯誤", explanation: "403 ERROR 訊息中明確提到無法連接伺服器，可能因流量或配置問題導致請求被擋。" },
    { text: "課程已經永久刪除", explanation: "403 錯誤通常是存取受限，不代表內容已被永久刪除。" },
    { text: "使用者的網路速度太慢", explanation: "雖然這可能導致超時，但 403 錯誤更傾向於權限或伺服器端的拒絕請求。" },
  ],
  correctAnswer: 1
};
const nlmQ50Options = {
  question: "在 AI 流暢度架構中，「描述 (Description)」這項能力主要涵蓋哪些內容？",
  options: [
    { text: "選擇合適的 AI 工具", explanation: "這通常屬於委派或辨識的範疇。" },
    { text: "定義需求、引導 AI 的處理方式並指定互動模式", explanation: "這是下一課將探討的核心，即如何精確地傳達預期目標與操作指導。" },
    { text: "驗證 AI 產出結果的準確性", explanation: "這更多是關於勤勉 (Diligence) 的範疇。" },
    { text: "計算 AI 運算的電力消耗", explanation: "這不在課程提到的核心流暢度能力之內。" },
  ],
  correctAnswer: 1
};

const nlm05Slides = [
  { src: '/images/ai-fluency/nlm05-slide-01-title.png', caption: '投影片 01' },
  { src: '/images/ai-fluency/nlm05-slide-02-theory-vs-practice.png', caption: '投影片 02' },
  { src: '/images/ai-fluency/nlm05-slide-03-task-selection.png', caption: '投影片 03' },
  { src: '/images/ai-fluency/nlm05-slide-04-archetype-matrix.png', caption: '投影片 04' },
  { src: '/images/ai-fluency/nlm05-slide-05-vision-alignment.png', caption: '投影片 05' },
  { src: '/images/ai-fluency/nlm05-slide-06-delegation-lens.png', caption: '投影片 06' },
  { src: '/images/ai-fluency/nlm05-slide-07-diagnostic-dimensions.png', caption: '投影片 07' },
  { src: '/images/ai-fluency/nlm05-slide-08-decision-matrix.png', caption: '投影片 08' },
  { src: '/images/ai-fluency/nlm05-slide-09-practice-guidelines.png', caption: '投影片 09' },
  { src: '/images/ai-fluency/nlm05-slide-10-plan-canvas.png', caption: '投影片 10' },
]
</script>

# 📓 第 05 課：AI 委派實戰藍圖（The AI Delegation Playbook）

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 05 課：AI 委派實戰藍圖（The AI Delegation Playbook）

把委派原則帶入真實工作情境，在實踐中深入理解如何有效運用 AI 進行任務委派。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm05-summary.mp4"
  poster="/images/ai-fluency/nlm05-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm05-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm05-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm05-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理
本課程涵蓋的核心主題與議題概要。
---
## 📊 簡報概覽

<SlideViewer :slides="nlm05Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ41Options" />

<Quiz :options="nlmQ42Options" />

<Quiz :options="nlmQ43Options" />

<Quiz :options="nlmQ44Options" />

<Quiz :options="nlmQ45Options" />

<Quiz :options="nlmQ46Options" />

<Quiz :options="nlmQ47Options" />

<Quiz :options="nlmQ48Options" />

<Quiz :options="nlmQ49Options" />

<Quiz :options="nlmQ50Options" />
