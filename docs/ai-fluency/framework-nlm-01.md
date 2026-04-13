---
title: 'NLM 延伸：AI 素養簡介'
description: 'Google NotebookLM 根據第 01 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
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
</script>

# 📓 第 01 課：AI 素養簡介（4Ds 概覽）

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 01 課：AI 素養簡介

課程開場，建立共同語言。介紹「AI 素養」的定義——不是技術技能，而是與 AI 系統有效協作的思維能力。說明為什麼所有人，無論職業背景，都需要培養 AI 素養。一位行銷人員、一位教師、一位工程師，都需要不同但同樣重要的 AI 素養——「會用 AI 工具」和「能有效、負責任地與 AI 協作」是截然不同的能力。

---

## 🎬 影片摘要

::: info 🎬 影片摘要：AI 流暢力框架：與 AI 一起思考
**NotebookLM 影片概覽**（內容萃取自影片畫面，約 6 分 10 秒）

**第一章：AI 時代的挑戰——快速變化的世界**

AI 發展如此迅速，一般人如何跟上腳步？影片開場點出現代人面臨的困境：時間壓力、複雜度爆炸、工具層出不窮，讓人不知從何學起。光靠追逐最新工具或技巧，是行不通的——我們需要的是一套能長期適用的思維框架。

**第二章：什麼是 AI 流暢力？——一種新的互動模式**

過去的方式（舊思維）：人類單向指揮機器，把 AI 當作執行命令的工具。  
新的方式（新思維）：人類與 AI 並肩合作，建立雙向的協作夥伴關係。

> 「AI 流暢力——以**有效、高效、合乎道德且安全**的方式與 AI 系統互動的能力。」

**第三章：4D 框架——AI 流暢力的四大核心職能**

| 核心職能 | 關鍵問題 |
|----------|----------|
| **委派**（Delegation） | 何時該由人類執行，何時該交給 AI？ |
| **描述**（Description） | 我們如何與 AI 系統清晰地溝通？ |
| **排識**（Discernment） | 我們如何評估 AI 提供的內容？ |
| **勤勉**（Diligence） | 我們如何確保互動是負責任的？ |

每一個「D」都有其視覺隱喻：委派是「用天平衡量人機分工」；描述是「人向 AI 清楚表達需求」；排識是「拿放大鏡審視 AI 的產出」；勤勉是「人與 AI 握手，建立負責任的夥伴關係」。

**第四章：超越提示工程的思維——建立宏觀的思維模式**

學習 AI 流暢力的意義，在於掌握四項持久能力：  
方向感——知道何時該用 AI、何時不該用；  
創造力——與 AI 共同發想、解決問題；  
判斷力——評估產出並承擔責任；  
可靠性——與 AI 建立值得信任的合作關係。

**影片結語金句**：
> 「我們希望改變我們**看待** AI 的思維，進而學會如何**與 AI 一起思考**。」
:::

## 📊 簡報概覽

::: tip 📊 簡報：AI 流暢度核心概念（由 NotebookLM 生成）
以下為 NotebookLM 根據課程自動生成的繁體中文簡報關鍵頁面：
:::

<div class="slide-image-gallery">

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-03-gap.png" alt="可能性與直覺之間的巨大落差" loading="lazy" />
  <div class="slide-image-caption">為什麼需要框架？AI 能力與人類直覺之間存在日益擴大的落差。</div>
</div>

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-04-strategy-comparison.png" alt="重新定義我們的 AI 學習策略" loading="lazy" />
  <div class="slide-image-caption">戰術性技能 vs 核心素養：兩種截然不同的學習方向。</div>
</div>

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-05-ai-fluency-definition.png" alt="定義標準：什麼是真正的 AI 流暢度？" loading="lazy" />
  <div class="slide-image-caption">AI 流暢度的四個高標準：有效（Effective）、高效（Efficient）、道德（Ethical）、安全（Safe）。</div>
</div>

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-06-4ds-framework.png" alt="人機協作的四大核心支柱：The 4Ds Framework" loading="lazy" />
  <div class="slide-image-caption">4D 框架總覽：委派、描述、辨別、盡責，四大核心支柱。</div>
</div>

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-11-interaction-loop.png" alt="動態循環：將 4D 轉化為工作流" loading="lazy" />
  <div class="slide-image-caption">4D 不是單向清單，而是持續迭代的互動循環，讓你真正「與 AI 共同思考」。</div>
</div>

<div class="slide-image-item">
  <img src="/images/ai-fluency/slide-12-conclusion.png" alt="掌握適應未來變局的持久能力" loading="lazy" />
  <div class="slide-image-caption">課程結語：準備好迎接的不只是今天的 AI 系統，而是未來無限的變革。</div>
</div>

</div>

## 🧪 延伸測驗

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「The 4Ds of AI Fluency: A Foundation for Human-AI Partnership」課程影片自動生成，涵蓋 4D 框架的核心概念、定義與思維轉變。
:::

### 測驗 1-1

<Quiz
  question="根據課程內容，「AI 流暢力」（AI Fluency）課程的核心焦點主要在於什麼？"
  :options="nlmQ1Options"
  :answer="1"
  explanation="課程強調這門課是關於「我們」以及人類與 AI 之間的合作關係。課程明確提到重點不在 AI 作為一種技術，而是人類如何與其互動。"
/>

### 測驗 1-2

<Quiz
  question="課程中提到的「AI 流暢力」定義為何？"
  :options="nlmQ2Options"
  :answer="1"
  explanation="這是課程中對「AI 流暢力」的明確定義，涵蓋了效率與責任感。流暢力不是技術開發能力，而是廣泛的互動能力——有效、高效、倫理且安全。"
/>

### 測驗 1-3

<Quiz
  question="課程希望幫助學員達成哪種思維轉變？"
  :options="nlmQ3Options"
  :answer="1"
  explanation="這反映了將 AI 從外部工具視為合作夥伴的根本性轉變。「與 AI 一起思考」意味著 AI 是思考過程的參與者，而非被動工具。"
/>

### 測驗 1-4

<Quiz
  question="在 AI 流暢力框架的「4D」核心能力中，「委派」（Delegation）主要處理什麼問題？"
  :options="nlmQ4Options"
  :answer="2"
  explanation="「委派」關乎於人類與 AI 之間的工作權責分配——何時由人做、何時交給 AI、何時人機協作。這是 4D 中決策層面的能力。"
/>

### 測驗 1-5

<Quiz
  question="關於「描述」（Description）這項能力，其核心探討的問題是什麼？"
  :options="nlmQ5Options"
  :answer="0"
  explanation="「描述」的核心在於溝通的清晰度，以便 AI 理解人類的意圖。這是 4D 中資訊輸入階段的能力，涵蓋如何設計有效提示。"
/>

### 測驗 1-6

<Quiz
  question="「辨識」（Discernment）能力在 AI 流暢力框架中扮演什麼角色？"
  :options="nlmQ6Options"
  :answer="2"
  explanation="「辨識」要求使用者批判性地審視 AI 的回答，而非盲目接受。這包含事實查核、邏輯評估、以及持續改善協作品質。"
/>

### 測驗 1-7

<Quiz
  question="「勤勉」（Diligence）能力要求我們在與 AI 互動時確保哪些特質？"
  :options="nlmQ7Options"
  :answer="1"
  explanation="「勤勉」旨在確保 AI 的使用是合乎倫理並對結果負責的。這包含透明揭露 AI 的參與、承擔最終責任、以及防範偏見與錯誤資訊。"
/>

### 測驗 1-8

<Quiz
  question="為什麼課程強調建立「基礎框架」而非僅學習戰術性技能（如特定提示語）？"
  :options="nlmQ8Options"
  :answer="1"
  explanation="AI 領域變化極快，唯有核心能力能幫助使用者應對未來的技術迭代。特定的提示語或設定在模型更新後可能完全失效，但 4D 思維框架具有持久價值。"
/>

### 測驗 1-9

<Quiz
  question="課程提到的「組織採用 AI 但缺乏明確策略」會導致什麼後果？"
  :options="nlmQ9Options"
  :answer="1"
  explanation="缺乏策略與理解會導致工具與人的期待之間產生斷層，使員工對不熟悉的系統感到挫折，反而降低效率與信任感。"
/>

### 測驗 1-10

<Quiz
  question="課程中提到的「信任夥伴」（Trusted Partner）概念，是希望將 AI 視為："
  :options="nlmQ10Options"
  :answer="1"
  explanation="這反映了 AI 在更高階的思維與創新任務中所扮演的角色。信任夥伴不是被動工具，而是能與人類共同解決創意與複雜問題的協作者。"
/>

---

*本頁測驗由 Google NotebookLM 根據 [The AI Fluency Framework](https://aifluencyframework.org/) 課程影片自動生成（Rick Dakan & Joseph Feller，與 Anthropic 合作開發）。原課程素材以 CC BY-NC-SA 4.0 授權發佈。*
