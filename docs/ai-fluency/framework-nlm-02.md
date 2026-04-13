---
title: 'NLM 延伸：4D 框架詳解'
description: 'Google NotebookLM 根據第 02 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ11Options = ["精通當月最流行的前 10 名最佳 AI 提示詞技巧。", "發展出一套能隨技術變化而調整的實用技能、知識、見解與價值觀。", "成為一名能夠理解大規模語言模型底層架構的技術專家。", "僅僅是獲得使用最新人工智慧系統的權限與管道。"]
const nlmQ12Options = ["需要與 AI 共同腦力激盪以克服創作瓶頸時。", "設定一個願景，讓 AI 獨立決定如何分類與處理大量郵件時。", "對於最終成果已有清晰構想，需要 AI 協助執行具體任務（如摘要文件）。", "當解決方案尚不明確，需要空間進行探索與實驗時。"]
const nlmQ13Options = ["AI 完全獨立於使用者之外工作，不需任何反饋。", "使用者將 AI 視為創意夥伴，透過來回討論來提升自己的思考品質。", "這種模式主要用於處理重複性高且不需人類介入的瑣事。", "它要求使用者像寫腳本一樣給出完全精確的執行步驟。"]
const nlmQ14Options = ["寫出精確每一步指令的「腳本撰寫員」。", "設定整體願景與行為模式的「導演」。", "單純負責將文件輸入給 AI 的「數據錄入員」。", "在 AI 完成每一行草稿後立即修正的「文字校對員」。"]
const nlmQ15Options = ["如何調整 AI 的回覆口吻，使其更符合品牌形象。", "判斷哪些工作應該由自己保留，哪些工作適合交給 AI 處理。", "檢查 AI 提供的數據是否有引用來源或事實性錯誤。", "確保輸入給 AI 的敏感資料都已經過加密處理。"]
const nlmQ16Options = ["僅輸入「幫我寫一個 Logo」而不提供任何其他資訊。", "詳細說明公司的價值觀、目標受眾及希望 AI 採用的溝通風格。", "當 AI 給出回覆後，判斷其推論邏輯是否符合現實。", "決定在整個專案中完全不使用 AI 以保證原創性。"]
const nlmQ17Options = ["使用者在該領域的專業知識與批判性洞察力。", "AI 模型本身的參數大小與計算能力。", "是否使用了最先進的加密技術來保護數據。", "提示詞中是否包含特定的技術關鍵字。"]
const nlmQ18Options = ["將 AI 生成的內容直接發布，不加任何修改以提高效率。", "主動檢查 AI 在招募流程中是否產生了潛在的偏見。", "使用多個不同的 AI 工具來完成同一個簡單任務。", "在對話中要求 AI 不要直接給答案，而是引導自己思考。"]
const nlmQ19Options = ["因為 4D 框架能直接提升 AI 模型運行的物理速度。", "因為這些能力不侷限於特定工具，能隨著技術演進持續適用。", "因為學會 4D 框架後就不再需要進行任何描述或溝通。", "因為 4D 框架是由目前最強大的 AI 系統自動生成的。"]
const nlmQ20Options = ["兩者完全獨立，描述結束後就不再需要辨別。", "它們形成一種反覆迭代的循環：描述需求、評估輸出、進一步細化需求。", "辨別必須先於描述發生，否則無法開始對話。", "只要描述得足夠完美，就不需要進行辨別。"]

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

const nlm02Slides = [
  { src: '/images/ai-fluency/nlm02-slide-01-cover.png', caption: '封面：超越提示詞——掌握自動化、增強與代理模式的 4D 實踐框架' },
  { src: '/images/ai-fluency/nlm02-slide-02-access-friction.png', caption: '「取得」≠「精通」：許多人有 AI 工具，卻仍面臨回覆不準確、無法描述需求、資安隱憂等阻礙' },
  { src: '/images/ai-fluency/nlm02-slide-03-ai-fluency.png', caption: 'AI 流暢度四維度：效能（最大化互動成果）、效率（減少時間浪費）、安全（保護隱私）、倫理（負責任的態度）' },
  { src: '/images/ai-fluency/nlm02-slide-04-paradigm-shift.png', caption: '三個演化階段：工具（被動執行）→ 媒介（思維延伸）→ 協作者/共創夥伴（提供創意與洞察）' },
  { src: '/images/ai-fluency/nlm02-slide-05-interaction-spectrum.png', caption: '互動光譜：自動化（人類主導 AI 執行）→ 增強（人機高頻協同）→ 代理（人類設定願景 AI 自主運行）' },
  { src: '/images/ai-fluency/nlm02-slide-06-automation.png', caption: '自動化：人類角色為「指令下達者」，適用已有明確預期結果的任務；注意目標不清晰時容易遇到瓶頸' },
  { src: '/images/ai-fluency/nlm02-slide-07-augmentation.png', caption: '增強：人類為「協同探索者」，AI 是創意思考與解決問題的夥伴；適用於故事角色發展、攻克難題、複雜研究等' },
  { src: '/images/ai-fluency/nlm02-slide-08-agency.png', caption: '代理：人類從「撰寫精確指令」轉變為「設定願景的導演」；適用於需持續運作或動態應對的情境' },
  { src: '/images/ai-fluency/nlm02-slide-09-decision-matrix.png', caption: '決策矩陣：自動化（低 AI 自主性、標準化）vs 增強（中、具備創意）vs 代理（高、動態自動化流程）' },
  { src: '/images/ai-fluency/nlm02-slide-10-4d-framework.png', caption: '雙層齒輪模型：外圈（委派 + 勤勉）定義邊界與責任；內圈（描述 ↔ 辨別）構成日常高頻微循環' },
  { src: '/images/ai-fluency/nlm02-slide-11-delegation.png', caption: '委派三步驟：釐清目標與問題 → 辨識 AI 能力邊界 → 在你與 AI 之間進行深思熟慮的工作劃分' },
  { src: '/images/ai-fluency/nlm02-slide-12-description-discernment.png', caption: '描述（超越單一提示詞）vs 辨別（注入人類專業判斷）：「這個產出真的能幫助我推進工作嗎？」' },
  { src: '/images/ai-fluency/nlm02-slide-13-diligence.png', caption: '勤勉五支柱：確保公平（防偏見）→ 驗證準確度 → 保護資料 → 維持透明 → 承擔責任' },
  { src: '/images/ai-fluency/nlm02-slide-14-conclusion.png', caption: '全域架構：底層基石（4D 框架）× 三種互動模式 × 頂層目標（AI 流暢度）→「掌握 4D 框架，讓 AI 成為擴展人類潛能的最強媒介」' },
]
</script>

# 📓 第 02 課：4D 框架詳解

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片「The 4D Framework」自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 02 課：AI 素養框架

正式介紹核心架構：4Ds（委派、描述、辨識、盡責）與三種人機互動模式（自動化、擴增、代理）。這是整門課程的概念地圖，後續每一課都在擴展這張地圖。

<details>
<summary>詳細說明：4Ds 與互動模式如何搭配</summary>

4Ds 是你的**能力工具箱**，三種模式是你選擇的**協作情境**，兩者組合形成完整的 AI 素養框架。  
在「自動化」模式下（AI 獨立執行任務），委派和辨識最關鍵——你需要判斷任務是否適合委派，並在事後審核結果；  
在「擴增」模式下（人機共同思考），描述和辨識最常用——你不斷精煉提示，評估每次的輸出；  
在「代理」模式下（AI 自主完成多步驟任務），盡責和委派的策略設計尤為重要——因為錯誤的後果可能已造成影響再才被發現。  
掌握框架後，你就能根據任務性質選擇最合適的協作方式。

</details>

## 📝 重點筆記

### 🧩 什麼是 4D 框架？

4D 框架是 AI 素養的**四大核心能力**，每個 D 代表一種與 AI 協作時必備的行動：

| 能力 | 英文 | 定義 |
|------|------|------|
| **委派** | Delegation | 設定目標，決定是否、何時、以何種方式與 AI 合作 |
| **描述** | Description | 精準描述目標，引導 AI 產出有用的行為與輸出 |
| **辨識** | Discernment | 準確評估 AI 輸出和行為的有用程度 |
| **盡責** | Diligence | 對我們使用 AI 的方式以及 AI 的輸出負起責任 |

```mermaid
flowchart LR
  D1["🎯 委派<br/>Delegation"] --> D2["✍️ 描述<br/>Description"]
  D2 --> D3["🔍 辨識<br/>Discernment"]
  D3 --> D4["🛡️ 盡責<br/>Diligence"]
  D4 -.->|"持續循環"| D1
```

<div class="slide-card">
  <div class="slide-grid-2x2">
    <div class="grid-item" style="background: var(--slide-purple)">
      <div class="grid-icon">🏛️</div>
      <div class="grid-label">有效 Effective</div>
    </div>
    <div class="grid-item" style="background: var(--slide-blue)">
      <div class="grid-icon">⏱️</div>
      <div class="grid-label">高效 Efficient</div>
    </div>
    <div class="grid-item" style="background: var(--slide-green)">
      <div class="grid-icon">⚖️</div>
      <div class="grid-label">倫理 Ethical</div>
    </div>
    <div class="grid-item" style="background: var(--slide-teal)">
      <div class="grid-icon">🛡️</div>
      <div class="grid-label">安全 Safe</div>
    </div>
  </div>
</div>

::: tip 4Ds 與 EEES 的關係
課程的副標題是「有效、高效、合乎倫理且安全地（Effectively, Efficiently, Ethically, and Safely）」——這四個形容詞是**實踐 4Ds 之後所達成的結果**，而不是 4Ds 本身。熟練地委派、描述、辨識與盡責，就能讓你的 AI 使用達到有效、高效、倫理且安全的標準。
:::

### 🔄 三種人機互動模式

4Ds 框架不只適用於一種合作方式，而是橫跨三種人機互動模式：

| 模式 | 英文 | 說明 | 範例 |
|------|------|------|------|
| <span style="white-space:nowrap">**自動化**</span> | Automation | AI 根據人類指令執行特定任務 | 讓 AI 整理電子郵件分類 |
| <span style="white-space:nowrap">**擴增**</span> | Augmentation | 人類與 AI 作為思考夥伴共同協作 | 與 AI 腦力激盪、共同撰寫 |
| <span style="white-space:nowrap">**代理**</span> | Agency | 人類設定目標，AI 獨立執行未來的多步驟任務 | 讓 AI 代理管理行程排程 |

理解你在哪種模式下工作，有助於選擇最合適的 4Ds 應用方式。

```mermaid
flowchart LR
  subgraph 自動化["🤖 自動化 Automation"]
    A1["人類設定指令"] --> A2["AI 獨立執行"]
  end
  subgraph 擴增["🤝 擴增 Augmentation"]
    B1["人類與 AI<br/>共同思考迭代"]
  end
  subgraph 代理["🚀 代理 Agency"]
    C1["人類設定目標"] --> C2["AI 自主執行<br/>多步驟任務"]
  end
  自動化 --- 擴增 --- 代理
```

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

## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要：AI 流暢度——精通與 AI 的協作
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm02-summary.mp4"
  poster="/images/ai-fluency/nlm02-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm02-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm02-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm02-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理

**影片主軸：超越提示詞，建構 AI 時代的核心流暢度**

| 段落 | 核心訊息 |
|------|----------|
| 問題診斷 | 擁有強大的 AI 系統，不代表懂得發揮其最大價值——「取得」≠「精通」 |
| AI 流暢度定義 | 一套持續適應技術變革的綜合素養：效能、效率、安全、倫理 |
| 範式轉移 | 工具（執行指令）→ 媒介（思維延伸）→ 協作者/共創夥伴 |
| 三種互動模式 | 自動化（指令執行）→ 增強（創意協同）→ 代理（願景自主） |
| 4D 框架 | 委派、描述、辨別、勤勉——驅馭 AI 流暢度的核心作業系統 |
| 結語 | 掌握 4D 框架，讓 AI 成為擴展人類潛能的最強媒介 |

**課程核心主張：**
> 「掌握 4D 框架，讓 AI 成為擴展人類潛能的最強媒介。」

**描述—辨別—精煉微循環（影片動畫重點）：**

步驟1 **描述**：提供豐富的背景脈絡，清楚表達需求與期望  
步驟2 **辨別**：評估 AI 產出的事實準確度、邏輯合理性與品牌對齊  
步驟3 **精煉**：根據辨別結果調整與深化請求

這個微循環在每次 AI 互動中反覆進行，不斷優化結果。

## 📊 簡報概覽

::: tip 📊 簡報：超越提示詞——建構 AI 時代的核心流暢度（由 NotebookLM 生成）
共 14 張投影片，使用左右按鈕或縮圖列切換；點擊主圖或全螢幕鈕可放大檢視。
:::

<SlideViewer :slides="nlm02Slides" />

## 🧪 延伸測驗

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「The 4D Framework」課程影片自動生成，深度考驗 AI 流暢度定義、三種互動模式、4D 各能力的精確定義與應用情境。
:::

### 測驗 2-1

<Quiz
  question="根據教材，下列哪一項最能準確描述「AI 流暢度」（AI Fluency）的本質？"
  :options="nlmQ11Options"
  :answer="1"
  hint="請思考 AI 流暢度是關於短暫的技巧還是長久且多面向的能力組合。"
  explanation="流暢度不僅是技術專業，更是結合了有效性、效率、倫理與安全的綜合能力。"
/>

### 測驗 2-2

<Quiz
  question="在 AI 互動的三種模式中，「自動化」（Automation）最適合應用於下列哪種情況？"
  :options="nlmQ12Options"
  :answer="2"
  hint="關鍵在於任務的目標是否已經非常明確且流程是直接執行的。"
  explanation="自動化模式的核心在於使用者定義明確結果，由 AI 執行指令。"
/>

### 測驗 2-3

<Quiz
  question="「增強」（Augmentation）模式與其他互動方式的主要區別為何？"
  :options="nlmQ13Options"
  :answer="1"
  hint="請聯想與朋友共同討論專案並互相激發靈感的過程。"
  explanation="增強模式下 AI 不只是代勞工具，而是幫助使用者「做得更好」的合作者。"
/>

### 測驗 2-4

<Quiz
  question="在「代理」（Agency）模式中，使用者的角色最接近下列何者？"
  :options="nlmQ14Options"
  :answer="1"
  hint="思考在管理團隊時，高階主管如何設定目標而非細微干預。"
  explanation="代理模式強調建立知識背景與規則，讓 AI 能在此框架下獨立代表使用者行動。"
/>

### 測驗 2-5

<Quiz
  question="關於 4D 框架中的「委派」（Delegation），下列哪項是其核心決策點？"
  :options="nlmQ15Options"
  :answer="1"
  hint="這是在開始工作前，針對「誰該做什麼」所做的權衡。"
  explanation="委派的核心在於戰略性地劃分人機分工，並理解 AI 的能力邊界。"
/>

### 測驗 2-6

<Quiz
  question="下列哪種行為體現了 4D 框架中的「描述」（Description）能力？"
  :options="nlmQ16Options"
  :answer="1"
  hint="想像在給予任務說明時，如何確保對方完全理解你的期望與風格。"
  explanation="有效的描述涉及明確表達需求、願景以及 AI 工作所需的完整背景資訊。"
/>

### 測驗 2-7

<Quiz
  question="在 AI 流暢度中，「辨別」（Discernment）主要依賴於什麼？"
  :options="nlmQ17Options"
  :answer="0"
  hint="思考當你收到 AI 的建議時，你需要具備什麼才能知道這個建議是否真的好用。"
  explanation="辨別需要使用者的專業判斷，以區分 AI 輸出的有用部分與需要捨棄的部分。"
/>

### 測驗 2-8

<Quiz
  question="「勤勉」（Diligence）在 4D 框架中強調的責任感，最直接體現在哪一項行為？"
  :options="nlmQ18Options"
  :answer="1"
  hint="這與道德、倫理以及你是否願意為最終產出「掛保證」有關。"
  explanation="勤勉涉及確保公平、驗證準確性、保護隱私以及對 AI 輔助作品的問責。"
/>

### 測驗 2-9

<Quiz
  question="為什麼 4D 框架被認為比學習特定的 AI 工具技巧更具長遠價值？"
  :options="nlmQ19Options"
  :answer="1"
  hint="思考「給魚吃不如教如何釣魚」的道理。"
  explanation="4D 是根本性的協作技能，無論未來 AI 軟體如何變更，其核心原則依然有效。"
/>

### 測驗 2-10

<Quiz
  question="在實際應用中，描述（Description）與辨別（Discernment）通常呈現什麼樣的關係？"
  :options="nlmQ20Options"
  :answer="1"
  hint="思考當你在與某人協作時，如何透過不斷的對話來修正對方的成果。"
  explanation="大多數 AI 互動涉及多次小型的描述與辨別迴圈，以不斷優化結果。"
/>

---

::: tip 🎯 下一步
理論看完了嗎？前往 [4D 互動練習](/ai-fluency/4d-practice) 動手操練四個核心能力。
:::

---

*本頁測驗由 Google NotebookLM 根據 [The AI Fluency Framework](https://aifluencyframework.org/) 課程影片自動生成（Rick Dakan & Joseph Feller，與 Anthropic 合作開發）。原課程素材以 CC BY-NC-SA 4.0 授權發佈。*
