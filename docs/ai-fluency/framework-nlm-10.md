---
title: 'NLM 延伸：盡責（Diligence）'
description: 'Google NotebookLM 根據第 10 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ91Options = {
  question: "在 AI 流利度（AI Fluency）框架中，「盡職」（Diligence）職能與其他三項職能的主要區別在於它更關注什麼？",
  options: [
    { text: "產出的工作效率與產量", explanation: "這通常是其他三項職能（如有效性與效率）的關注點，而非盡職職能的核心。" },
    { text: "倫理與安全方面的考量", explanation: "盡職職能旨在確保 AI 的使用不僅具備生產力，更要符合嚴謹、透明與負責任的倫理標準。" },
    { text: "AI 模型運算的技術複雜度", explanation: "雖然技術理解很重要，但盡職職能更強調互動的責任與影響，而非單純的技術規格。" },
    { text: "自動化流程的執行速度", explanation: "執行速度屬於效率範疇，而盡職職能是在探討即使速度快，是否也符合倫理與安全規範。" },
  ],
  correctAnswer: 1
};
const nlmQ92Options = {
  question: "影片中將與 AI 協作比作「開車」，這主要是為了說明什麼概念？",
  options: [
    { text: "操作 AI 系統需要經過長期的專業執照培訓", explanation: "雖然需要學習，但影片的比喻重點在於行為的社會影響與安全責任，而非執照制度。" },
    { text: "使用 AI 應專注於以最快的速度達成目標", explanation: "這忽略了比喻中提到的交通規則與對他人的影響，這正是盡職職能要補足的部分。" },
    { text: "AI 互動並非存在於真空，需考慮其對外部環境與他人的影響", explanation: "如同開車需注意路況與安全，盡職職能要求我們意識到 AI 協作在社會與專業背景下的廣泛影響。" },
    { text: "AI 系統終將像汽車一樣普及於每個家庭", explanation: "這是對普及率的預測，並未觸及影片中強調的責任感與安全維護的核心主題。" },
  ],
  correctAnswer: 2
};
const nlmQ93Options = {
  question: "當您在思考「誰擁有我現在輸入的數據？」時，您正在實踐哪一種盡職行為？",
  options: [
    { text: "部署盡職（Deployment Diligence）", explanation: "部署盡職主要發生在產出完成後的分享與承擔責任階段，而非輸入階段。" },
    { text: "透明度盡職（Transparency Diligence）", explanation: "這主要涉及對他人告知 AI 的角色，而不是系統本身的數據隱私與選擇考量。" },
    { text: "創作盡職（Creation Diligence）", explanation: "創作盡職涉及對 AI 系統的選擇、數據安全、隱私保護以及與價值觀一致性的批判性思考。" },
    { text: "效率盡職（Efficiency Diligence）", explanation: "AI 流利度框架中的盡職概念並不包含這個特定名稱，且這更偏向生產力而非安全性。" },
  ],
  correctAnswer: 2
};
const nlmQ94Options = {
  question: "在專業環境中，如果您將 AI 協助撰寫的部分告知同事，這符合以下哪項職能？",
  options: [
    { text: "部署盡職（Deployment Diligence）", explanation: "這項職能更多關注於產出的準確性驗證，而非與利害關係人的溝通揭露。" },
    { text: "透明度盡職（Transparency Diligence）", explanation: "透明度盡職強調在互動中保持開放與誠實，讓相關人員了解 AI 在工作中所扮演的角色。" },
    { text: "技術盡職（Technical Diligence）", explanation: "這不是影片中定義的三大盡職類別之一，且揭露行為屬於溝通倫理而非技術操作。" },
    { text: "創作盡職（Creation Diligence）", explanation: "創作盡職關注的是系統的選擇與輸入端的保護，而非後續的角色披露。" },
  ],
  correctAnswer: 1
};
const nlmQ95Options = {
  question: "根據「部署盡職」（Deployment Diligence）的要求，當 AI 生成的內容出現錯誤時，誰應負最終責任？",
  options: [
    { text: "開發該 AI 系統的公司", explanation: "雖然開發者有其義務，但盡職職能強調使用者在分享內容時應承擔的主動責任。" },
    { text: "AI 系統本身，因為它是內容的創作者", explanation: "AI 只是工具，無法承擔法律或專業上的道德責任，責任主體始終是人。" },
    { text: "分享該內容的使用者", explanation: "部署盡職的核心在於，當您將 AI 產出分享給世界時，您必須對其準確性與妥當性負責。" },
    { text: "驗證資料的第三方查核機構", explanation: "第三方機構是輔助工具，但最終決定發布並代表該內容的人才是責任方。" },
  ],
  correctAnswer: 2
};
const nlmQ96Options = {
  question: "為了落實部署盡職，一名記者在使用 AI 輔助撰稿後，應該採取什麼行動？",
  options: [
    { text: "直接發布文章，因為 AI 已經過大數據訓練，事實錯誤率極低", explanation: "這忽略了 AI 可能產生幻覺或偏見的風險，違反了盡職職能中驗證的要求。" },
    { text: "僅檢查文章的錯字，語意部分由 AI 全權負責", explanation: "這不足以達到部署盡職的標準，因為事實查核與偏見審查才是關鍵。" },
    { text: "核實每一個事實與來源，確保符合傳統的新聞專業標準", explanation: "部署盡職要求產出必須達到與人類親自創作時相同的專業標準與準確度。" },
    { text: "在文章末尾標註「由 AI 生成」即可忽略事實核實", explanation: "標註僅屬於透明度盡職，並不能免除使用者對內容準確性的部署責任。" },
  ],
  correctAnswer: 2
};
const nlmQ97Options = {
  question: "在處理敏感的公司資訊前，創作盡職要求我們首先執行哪項動作？",
  options: [
    { text: "測試 AI 系統的回答速度是否夠快", explanation: "這屬於效率考量，並非保護敏感資訊的安全性考量。" },
    { text: "檢查該服務的數據保護政策或組織的共享規定", explanation: "這是確保個人與組織隱私安全、遵循政策的重要步驟，屬於創作盡職的核心。" },
    { text: "詢問 AI 助手它是否會保密", explanation: "AI 的回答不代表實際的數據處理政策或法律保障，必須查閱官方條款或公司規定。" },
    { text: "先將資訊匿名化後再隨意上傳至任何 AI 平台", explanation: "雖然匿名化有幫助，但忽視組織政策與平台條款仍是不夠謹慎的行為。" },
  ],
  correctAnswer: 1
};
const nlmQ98Options = {
  question: "關於透明度盡職，以下哪項描述體現了其對於「信任」的價值？",
  options: [
    { text: "它確保了 AI 生成的內容比人類創作的內容更便宜", explanation: "成本與透明度無直接關係，且這不是盡職職能關注的重點。" },
    { text: "它承認人們有權知道 AI 何時在影響他們的決定或內容創作", explanation: "尊重他人的知情權是建立人際信任與社會負責任協作的基礎。" },
    { text: "它讓使用者可以避免為 AI 的錯誤承擔任何責任", explanation: "揭露 AI 的角色並不能免責；相反地，它是在誠實的基礎上進行負責任的溝通。" },
    { text: "它強制要求在所有微小的 AI 互動中都必須提供極度詳細的技術報告", explanation: "影片提到揭露的細節層次應根據背景與受眾需求而定，而非一成不變的極度詳細。" },
  ],
  correctAnswer: 1
};
const nlmQ99Options = {
  question: "由於 AI 的法律與監管框架仍在不斷演變，盡職職能建議我們應該怎麼做？",
  options: [
    { text: "在法律完全定案前，應停止所有 AI 互動", explanation: "這過於極端且不符合 AI 流利度的目標，重點在於如何安全且有效地「使用」而非「禁用」。" },
    { text: "僅依賴 AI 系統內建的過濾機制來防範法律風險", explanation: "內建機制可能無法覆蓋所有法律或組織政策的變動，主動保持資訊更新是使用者的責任。" },
    { text: "持續關注並了解最新的資訊與規定", explanation: "保持資訊領先是盡職的一部分，因為法律環境的快速變遷會影響 AI 使用的合規性。" },
    { text: "開發自己的專屬 AI 以避開所有現有法律規管", explanation: "開發專屬系統仍需遵守法律，且這對於大多數使用者而言並非實際的盡職做法。" },
  ],
  correctAnswer: 2
};
const nlmQ100Options = {
  question: "下列哪一項不是「盡職」職能旨在實現的目標？",
  options: [
    { text: "確保 AI 的使用是透明且可問責的", explanation: "這是盡職職能的核心目標，旨在建立負責任的協作模式。" },
    { text: "最大化 AI 系統的處理速度以節省人力成本", explanation: "速度與成本節約屬於效率範疇，並非盡職職能（專注倫理與安全）的主要目的。" },
    { text: "使 AI 的使用符合個人與專業價值觀", explanation: "盡職職能強調將 AI 互動與自身及組織的道德標準相對齊。" },
    { text: "確保 AI 協作在社會中是公平、安全且有益的", explanation: "這是盡職職能最終希望透過個人行為引導出的社會影響目標。" },
  ],
  correctAnswer: 1
};

const nlm10Slides = [
  { src: '/images/ai-fluency/nlm10-slide-01-title.png', caption: '投影片 01' },
  { src: '/images/ai-fluency/nlm10-slide-02-overview.png', caption: '投影片 02' },
  { src: '/images/ai-fluency/nlm10-slide-03-components.png', caption: '投影片 03' },
  { src: '/images/ai-fluency/nlm10-slide-04-framework.png', caption: '投影片 04' },
  { src: '/images/ai-fluency/nlm10-slide-05-assessment.png', caption: '投影片 05' },
  { src: '/images/ai-fluency/nlm10-slide-06-evaluation.png', caption: '投影片 06' },
  { src: '/images/ai-fluency/nlm10-slide-07-guidelines.png', caption: '投影片 07' },
  { src: '/images/ai-fluency/nlm10-slide-08-examples.png', caption: '投影片 08' },
  { src: '/images/ai-fluency/nlm10-slide-09-implementation.png', caption: '投影片 09' },
  { src: '/images/ai-fluency/nlm10-slide-10-summary.png', caption: '投影片 10' },
]
</script>

# 📓 第 10 課：盡責（Diligence）

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 10 課：實踐工作場景 3：編碼與技術開發

學習如何善用 AI 輔助程式碼編寫、技術問題排查與開發流程最佳化。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm10-summary.mp4"
  poster="/images/ai-fluency/nlm10-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm10-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm10-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm10-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理

**第一章：盡責的獨特性——4D 框架中的道德守衛**

「盡責（Diligence）」是 4D 框架中最關注「倫理與安全考量」的能力，與其他三個 D 的最大差異在於：它不只問「這樣做有沒有效」，而是問「這樣做有沒有責任感」。它確保 AI 的使用是透明、謹慎且符合個人與社會價值觀的。

**第二章：開車的比喻——AI 互動不存在於真空**

影片用「開車」來比喻 AI 使用：開車需要遵守交通規則、考慮對其他用路人的影響——AI 互動也一樣，並非存在於真空中，而是會對外部環境、同事、受眾和社會產生廣泛影響。這個比喻提醒我們：使用 AI 是一種帶有社會責任的行為。

**第三章：盡責的三個類型**

| 類型 | 核心問題 | 實踐重點 |
|------|---------|---------|
| **創作盡責（Creation）** | 我輸入的數據誰擁有？AI 系統的選擇符合我的價值觀嗎？ | 選擇前先查閱數據保護政策與組織規定 |
| **透明度盡責（Transparency）** | 利害關係人知道 AI 參與了這項工作嗎？ | 尊重他人的知情權，告知 AI 在工作中的角色 |
| **部署盡責（Deployment）** | AI 生成的內容達到你分享標準嗎？錯誤出現時誰負責？ | 分享前核實事實與來源，標準與人類親自撰寫相同 |

**第四章：責任主體永遠是人——AI 無法代替你承擔**

當 AI 生成的內容出現錯誤，責任歸屬於「分享該內容的使用者」，而非開發公司或 AI 本身。部署盡責的核心原則是：你發布的每一份 AI 輔助內容，都必須達到與你親自創作時相同的專業標準。

**第五章：法律持續演進——保持資訊更新是使用者的責任**

AI 的法律與監管框架仍在快速變化中，盡責要求使用者主動持續關注並了解最新規定——不能只依賴 AI 內建的過濾機制，也不能等法律完全定案才採取行動。

**影片結語金句**：
> 「使用 AI 就像開車：你不只要開得快，還要開得安全、對他人負責。盡責，是讓 AI 成為社會正向力量的關鍵。」

---
## 📊 簡報概覽

<SlideViewer :slides="nlm10Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ91Options" />

<Quiz :options="nlmQ92Options" />

<Quiz :options="nlmQ93Options" />

<Quiz :options="nlmQ94Options" />

<Quiz :options="nlmQ95Options" />

<Quiz :options="nlmQ96Options" />

<Quiz :options="nlmQ97Options" />

<Quiz :options="nlmQ98Options" />

<Quiz :options="nlmQ99Options" />

<Quiz :options="nlmQ100Options" />
