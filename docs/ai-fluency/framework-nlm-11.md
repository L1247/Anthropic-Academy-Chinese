---
title: 'NLM 延伸：課程總結'
description: 'Google NotebookLM 根據第 11 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ101Options = {
  question: "在 AI 流力框架（AI Fluency Framework）中，「委派」（Delegation）的核心決策基礎是什麼？",
  options: [
    { text: "使用者的專業知識與判斷力", explanation: "委派的本質是根據人類的理解力來分配工作，因此個人專業判斷是有效分工的基石。" },
    { text: "AI 系統的自動化處理速度", explanation: "雖然速度是優勢，但委派更強調人類判斷何時以及如何分配任務，而非單純追求速度。" },
    { text: "演算法的獨立決策邏輯", explanation: "委派應由人類主導任務分配，過度依賴 AI 獨立決策會忽略了人類在判斷問題適配性上的角色。" },
    { text: "硬體計算能力的上限", explanation: "硬體限制與任務的邏輯分配（誰做什麼）較無直接關聯，委派關注的是人機協作的策略。" },
  ],
  correctAnswer: 0
};
const nlmQ102Options = {
  question: "「描述」（Description）能力中的「產品、過程與表現」（Product, Process, and Performance）主要目的是什麼？",
  options: [
    { text: "引導 AI 產生所需產出並成為有效的協作對手", explanation: "透過清晰定義這三個維度，我們能更精確地溝通需求，使 AI 從單純的工具轉化為有意義的夥伴。" },
    { text: "用來評估 AI 模型的市場競爭力指標", explanation: "這三個 P 是指溝通的方法論，而非用於比較不同廠商 AI 模型的性能指標。" },
    { text: "作為 AI 訓練階段的數據標註標準", explanation: "這是使用者與 AI 互動時的溝通技巧，並非開發者在模型訓練過程中所使用的標註工具。" },
    { text: "僅用於自動化流程的效能監控", explanation: "描述能力適用於所有互動模式，包括增強與代理，不侷限於效能監控。" },
  ],
  correctAnswer: 0
};
const nlmQ103Options = {
  question: "根據課程內容，哪一種互動模式是指 AI 被配置為「代表你獨立行動」？",
  options: [
    { text: "代理 (Agency)", explanation: "代理模式涉及 AI 獲得一定的自主權來執行任務，而不僅僅是作為輔助工具。" },
    { text: "增強 (Augmentation)", explanation: "增強模式強調的是人類與 AI 作為思考夥伴進行協作，而非獨立行動。" },
    { text: "自動化 (Automation)", explanation: "自動化通常是指 AI 遵循特定指令執行重複性任務，並不具備獨立代理的性質。" },
    { text: "辨析 (Discernment)", explanation: "辨析是 AI 流力的核心能力之一，而非指人機互動的運作模式。" },
  ],
  correctAnswer: 0
};
const nlmQ104Options = {
  question: "在「辨析」（Discernment）的實踐中，為什麼對 AI 產出進行批判性評估是不可或缺的責任？",
  options: [
    { text: "因為它能防範 AI 的局限性並實現單方無法達到的結果", explanation: "人類的辨析能力可以補足 AI 可能出現的錯誤或偏差，進而提升最終產出的品質。" },
    { text: "為了減少與 AI 進行對話的次數以節省資源", explanation: "辨析通常需要更多的反覆審核，而不是為了減少互動。" },
    { text: "確保 AI 系統不會消耗過多的處理能力", explanation: "辨析關注的是「內容」的品質與適當性，而非計算資源的配置。" },
    { text: "這是為了符合 AI 軟體授權合約的法律要求", explanation: "雖然法律合規很重要，但課程強調辨析是為了產出品質與責任，而非單純的合約義務。" },
  ],
  correctAnswer: 0
};
const nlmQ105Options = {
  question: "關於「勤勉」（Diligence）能力的描述，下列哪一項行為最符合其原則？",
  options: [
    { text: "對 AI 在工作中所扮演的角色保持透明度", explanation: "透明化 AI 的參與能建立信任，這正是勤勉能力中「負責任互動」的核心概念。" },
    { text: "盡可能將所有決策權轉交給 AI 以提高效率", explanation: "勤勉強調人類對最終產出負責，而非放棄決策權。" },
    { text: "隱藏 AI 的使用跡象以展現個人的卓越能力", explanation: "這違反了勤勉中關於「創作透明度」的道德與誠信原則。" },
    { text: "僅選擇市場上價格最昂貴的 AI 系統", explanation: "勤勉涉及的是「周全的選擇」而非單看價格，且重點在於使用過程的倫理。" },
  ],
  correctAnswer: 0
};
const nlmQ106Options = {
  question: "在「描述」（Description）的過程中，什麼樣的互動形式被認為比「繁瑣的提示詞」更有效？",
  options: [
    { text: "提供上下文與回饋的深思熟慮對話", explanation: "透過迭代的對話與反饋，能比單次複雜指令更精確地校準 AI 的表現。" },
    { text: "使用預先設定好的固定指令模板", explanation: "模板雖然方便，但缺乏課程中強調的針對具體情境的雙向互動精神。" },
    { text: "完全依賴 AI 自行推斷隱含的意圖", explanation: "這忽略了描述能力中「清晰闡述需求」的主動性要求。" },
    { text: "限制溝通字數以保持指令的簡潔性", explanation: "有效的描述需要充足的上下文，過度簡化可能會導致資訊遺失。" },
  ],
  correctAnswer: 0
};
const nlmQ107Options = {
  question: "課程中提到 AI 是「強大的系統」，但「並非靈丹妙藥」。這句話旨在提醒學習者什麼？",
  options: [
    { text: "AI 的效用與安全性取決於人類的使用方式", explanation: "這強調了人的能動性（Agency），即技術必須由有素養的人類來正確引導。" },
    { text: "AI 目前的技術水平尚不足以處理複雜任務", explanation: "課程承認系統很強大，但強調的是使用者的責任，而非全盤否定技術能力。" },
    { text: "人類應該完全停止開發生成式 AI 系統", explanation: "課程目標是培養流力以利協作，而非反對技術發展。" },
    { text: "只有頂尖工程師才能駕馭這些系統", explanation: "AI 流力框架是設計給廣泛大眾使用的，旨在提升每個人的協作能力。" },
  ],
  correctAnswer: 0
};
const nlmQ108Options = {
  question: "當我們與 AI 進行「增強」（Augmentation）互動時，其主要的目標是什麼？",
  options: [
    { text: "與 AI 作為思考夥伴協作，產生超越單方的成果", explanation: "增強模式專注於人機智慧的結合，藉此創造出 1 + 1 > 2 的效果。" },
    { text: "由 AI 全權處理所有重複性的數據錄入工作", explanation: "這更接近「自動化」（Automation）的定義，而非深層的智慧協作。" },
    { text: "取代人類在創意流程中的所有思考環節", explanation: "增強強調的是「夥伴關係」，而非由 AI 取代人類的思考角色。" },
    { text: "自動生成最終產品而不需要人類進行後續審核", explanation: "這忽略了「辨析」的重要性，且增強模式本質上需要人類的參與。" },
  ],
  correctAnswer: 0
};
const nlmQ109Options = {
  question: "AI 流力框架（Four Ds）如何因應未來 AI 技術的不斷演進？",
  options: [
    { text: "該框架旨在廣泛適用於各類生成式 AI 並保持長期相關性", explanation: "透過建立核心能力而非操作指南，這套框架能適應技術的快速變革。" },
    { text: "一旦新型模型推出，該框架就必須完全更換", explanation: "框架的設計初衷是作為基礎，具有跨技術的適應能力。" },
    { text: "該框架僅適用於目前主流的文本生成模型", explanation: "框架涵蓋的是通用的協作能力，不限於特定的媒介或模型類型。" },
    { text: "它要求使用者必須學習編寫底層程式碼才能維持流力", explanation: "AI 流力關注的是互動與決策，而非開發層面的技術細節。" },
  ],
  correctAnswer: 0
};
const nlmQ110Options = {
  question: "課程總結建議，提升 AI 流力的最佳途徑為何？",
  options: [
    { text: "透過實踐、練習並持續應用所學的能力", explanation: "流力並非一蹴而就，而是透過不斷的委派、描述、辨析與勤勉實踐積累而成。" },
    { text: "大量閱讀技術文件而不進行實際操作", explanation: "理論知識固然重要，但流力的發展更依賴於實際的互動經驗。" },
    { text: "尋找可以一勞永逸解決所有問題的單一指令", explanation: "AI 並非銀彈，且流力強調的是靈活的協作過程而非單一的解決方案。" },
    { text: "完全模仿其他專業人士的對話風格", explanation: "雖然參考他人有幫助，但建立自己的專業判斷與委派邏輯才是流力的核心。" },
  ],
  correctAnswer: 0
};

const nlm11Slides = [
  { src: '/images/ai-fluency/nlm11-slide-01-title.png', caption: '投影片 01' },
  { src: '/images/ai-fluency/nlm11-slide-02-overview.png', caption: '投影片 02' },
  { src: '/images/ai-fluency/nlm11-slide-03-framework.png', caption: '投影片 03' },
  { src: '/images/ai-fluency/nlm11-slide-04-dimensions.png', caption: '投影片 04' },
  { src: '/images/ai-fluency/nlm11-slide-05-assessment.png', caption: '投影片 05' },
  { src: '/images/ai-fluency/nlm11-slide-06-evaluation.png', caption: '投影片 06' },
  { src: '/images/ai-fluency/nlm11-slide-07-guidelines.png', caption: '投影片 07' },
  { src: '/images/ai-fluency/nlm11-slide-08-implementation.png', caption: '投影片 08' },
  { src: '/images/ai-fluency/nlm11-slide-09-summary.png', caption: '投影片 09' },
]
</script>

# 📓 第 11 課：課程總結

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 11 課：實踐工作場景 4：學習與個人成長

探討 AI 在學習、技能發展與個人成長中的角色，開啟自我改進的新可能。

---
## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm11-summary.mp4"
  poster="/images/ai-fluency/nlm11-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm11-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm11-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm11-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理

**第一章：4D 框架全景回顧——從知識到智慧**

課程總結影片以全景視角重新審視 4D 框架：委派（以你的專業判斷分配工作）、描述（用產品、過程、績效三個維度精確溝通）、辨識（批判性評估 AI 產出以防範侷限）、盡責（透明且負責任地使用 AI）。四個能力構成一個完整的人機協作系統。

**第二章：三種互動模式——根據任務性質選擇協作方式**

影片重申三種人機互動模式的差異：  
**自動化（Automation）**——AI 執行重複性、規則明確的任務；  
**增強（Augmentation）**——人類與 AI 作為思考夥伴協作，創造超越單方的成果；  
**代理（Agency）**——AI 被配置為代表你獨立行動，處理需要一定自主權的任務。  
選對模式，是 AI 流暢度的重要判斷能力。

**第三章：AI 是強大系統，但不是靈丹妙藥**

影片反覆強調一個核心觀點：AI 的效用與安全性取決於人類的使用方式。技術很強大，但沒有具備 AI 流暢度的人類主導，強大的系統也可能帶來問題。這不是反對技術，而是肯定「人的能動性（Agency）」的不可替代。

**第四章：4D 框架的持久性——適應未來 AI 的演進**

影片闡明框架的設計邏輯：4D 並非針對特定工具的操作手冊，而是廣泛適用於各類生成式 AI、能長期保持相關性的核心能力框架。隨著 AI 技術快速迭代，框架本身不需更換，你積累的能力不會過時。

**第五章：提升 AI 流暢度的最佳途徑——實踐**

總結課程最重要的一課：AI 流暢度不是讀完就能擁有的知識，而是透過不斷的委派、描述、辨識與盡責實踐積累而成的能力。與深思熟慮的對話，永遠優於繁瑣但缺乏脈絡的提示詞。

**影片結語金句**：
> 「AI 是強大的系統，但並非靈丹妙藥。它的效用，由使用它的人決定。」

---
## 📊 簡報概覽

<SlideViewer :slides="nlm11Slides" />
---
## 🧪 延伸測驗

::: tip 🧪 互動學習
透過以下測驗檢測你對課程內容的理解程度。
:::

<Quiz :options="nlmQ101Options" />

<Quiz :options="nlmQ102Options" />

<Quiz :options="nlmQ103Options" />

<Quiz :options="nlmQ104Options" />

<Quiz :options="nlmQ105Options" />

<Quiz :options="nlmQ106Options" />

<Quiz :options="nlmQ107Options" />

<Quiz :options="nlmQ108Options" />

<Quiz :options="nlmQ109Options" />

<Quiz :options="nlmQ110Options" />
