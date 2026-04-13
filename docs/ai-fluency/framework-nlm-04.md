---
title: 'NLM 延伸：委派（Delegation）'
description: 'Google NotebookLM 根據第 04 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ31Options = ["決定哪些工作應由自己完成，以及哪些工作可能更適合交給 AI。", "將所有重複且枯燥的任務自動化，以便人類可以完全停止工作。", "開發新的 AI 系統來取代現有的手動工作流程。", "學習如何操作最先進的 AI 模型以提高打字速度。"]
const nlmQ32Options = ["有效（Effective）與高效（Efficient）。", "倫理（Ethical）與安全（Safe）。", "創意（Creative）與精準（Accurate）。", "自動化（Automation）與代理（Agency）。"]
const nlmQ33Options = ["您自己的專業知識以及對所要達成目標的理解。", "掌握最新的提示詞工程（Prompt Engineering）技巧。", "擁有目前市場上最強大的硬體運算資源。", "對 AI 歷史發展的深入研究。"]
const nlmQ34Options = ["清楚定義目標並在引入 AI 之前理解所需工作的能力。", "識別 AI 系統在運算過程中可能出現的錯誤或偏見。", "能夠預測未來 AI 可能帶來的失業風險。", "了解哪些 AI 模型在基準測試中得分最高。"]
const nlmQ35Options = ["無知領域（Areas of ignorance）。", "不確定領域（Areas of uncertainty）。", "判斷領域（Critical judgment areas）。", "耗時領域（Time-consuming areas）。"]
const nlmQ36Options = ["首先是其領域的專家，其次才是 AI 委派者。", "首先是技術通才，其次才是問題解決者。", "首先是 AI 操作員，其次才是團隊領導者。", "首先是自動化工程師，其次才是內容創作者。"]
const nlmQ37Options = ["對可用 AI 系統及其特定能力與限制的運作知識。", "能夠在多個作業系統上安裝 AI 軟體的能力。", "對 AI 公司的市場佔有率和股價的認識。", "僅僅使用一個完美的 AI 系統來解決所有問題。"]
const nlmQ38Options = ["儘可能多地親自動手實驗不同的 AI 系統。", "詳細閱讀所有 AI 模型的使用手冊和更新日誌。", "等待 AI 發展趨於穩定後再開始學習。", "只關注學術期刊上發表的基準測試結果。"]
const nlmQ39Options = ["審慎地在人類與人工智慧之間分配工作，以發揮各自的獨特優勢。", "將所有與他人溝通的職責交給 AI 代理人。", "完全依賴 AI 的自動化流程以消除人類的所有錯誤。", "尋找一個能獨立完成整項專案而不需要人類介入的系統。"]
const nlmQ40Options = ["關鍵判斷領域（Critical judgment areas）。", "簡單但耗時的工作。", "例行性的互動任務。", "需要大量數據處理的工作。"]

const nlm04Slides = [
  { src: '/images/ai-fluency/nlm04-slide-01-cover.png', caption: '封面：AI 協作的藝術：精通「任務委派」——提升 AI 素養的核心框架，從了解問題到策略性分工' },
  { src: '/images/ai-fluency/nlm04-slide-02-ai-fluency-definition.png', caption: '什麼是真正的 AI 素養？——任務委派的核心目的，正是幫助你達成 AI 協作的「效能」與「效率」；AI 素養不只是技術能力，而是如何有效地決定哪些工作該自己做、哪些該交給 AI' },
  { src: '/images/ai-fluency/nlm04-slide-03-expert-first.png', caption: '令人驚訝的事實：委派的核心不在於 AI——最優秀的 AI 協作者，首先是其領域的專家。沒有清晰的目標與專業理解，再先進的 AI 也無法帶你到達目的地（金字塔底座 = 領域專家）' },
  { src: '/images/ai-fluency/nlm04-slide-04-three-pillars.png', caption: '任務委派的三大核心支柱：問題意識（釐清目標與工作本質）→ 平台意識（理解 AI 系統的能力與限制）→ 任務委派（策略性地在人機之間分配工作）。將複雜工作拆解並結合這三大元素，才是真正的協作藝術' },
  { src: '/images/ai-fluency/nlm04-slide-05-problem-awareness.png', caption: '支柱一：問題意識——在引入 AI 之前，請停下來回答：你究竟想完成或解決什麼（願景與目標）？「成功」對你而言是什麼樣子（成功標準）？達成這個目標需要哪種類型的思考與工作模式（思考模式）？' },
  { src: '/images/ai-fluency/nlm04-slide-06-task-diagnosis-matrix.png', caption: '任務診斷矩陣：剖析你的工作本質——四象限：① 耗時但簡單→適合 AI 自動化；② 充滿不確定性→需要 AI 作為思考夥伴；③ 知識盲區→利用 AI 挖掘數據填補資訊缺口；④ 批判性判斷→必須保留給人類親自處理' },
  { src: '/images/ai-fluency/nlm04-slide-07-platform-awareness.png', caption: '支柱二：平台意識——沒有一個完美的系統。AI 領域幾乎每天都在進化，有效的委派不在於尋找單一完美的工具，而在於深刻了解各種可用選項的獨特優勢與局限性' },
  { src: '/images/ai-fluency/nlm04-slide-08-capability-dashboard.png', caption: 'AI 能力權衡儀表板：針對特定任務選擇合適的模型，需要權衡速度 ↔ 深度、準確性 ↔ 創造力。你的專案優先考慮什麼？了解哪些模型在速度上勝出、哪些在深度推理或創意發想上表現更好，是平台意識的核心' },
  { src: '/images/ai-fluency/nlm04-slide-09-hands-on-practice.png', caption: '實踐法則：親自動手——由於技術版圖變動過快，建立平台意識最好的策略就是「親自動手」：① 頻繁地利用不同 AI 系統進行實驗；② 測試它們在不同任務上的極限；③ 基於個人經驗發展屬於自己的深刻見解' },
  { src: '/images/ai-fluency/nlm04-slide-10-task-delegation.png', caption: '支柱三：任務委派——協作的真正藝術。當你清晰定義了「問題」，並深刻理解了「平台」後，真正的藝術才開始：巧妙地在人類與人工智慧之間分配工作，發揮各自無可取代的獨特優勢（人類特有優勢 vs AI 運算優勢）' },
  { src: '/images/ai-fluency/nlm04-slide-11-four-modes-matrix.png', caption: '四大協作模式矩陣：① 完全人類執行（涉及高度同理心與批判性判斷，不應委派給 AI）；② 人機增強（雙方協同工作，AI 提供數據或作為思考夥伴，創造超越單方的價值）；③ AI 代理執行（授權 AI 代理人代表你處理常規性的互動與流程）；④ 完全自動化（完全交由 AI 處理高重複性、耗時但簡單的任務）' },
  { src: '/images/ai-fluency/nlm04-slide-12-decision-tree.png', caption: '委派決策樹：如何分配這項工作？從「這項任務的本質是什麼？」出發——需要批判性判斷→完全人類執行；重複耗時簡單→完全自動化；需代表你進行常規性對外互動→AI 代理執行；需要深度思考且能從多角度受益→人機增強' },
  { src: '/images/ai-fluency/nlm04-slide-13-delegation-ecosystem.png', caption: '完整的委派生態系統：三大支柱缺一不可——只有問題意識+委派，沒有平台意識→工具誤用與挫折；只有平台意識+委派，沒有問題意識→迷失方向；只有問題意識+平台意識，沒有任務委派→效率低落，人類淪為瓶頸' },
  { src: '/images/ai-fluency/nlm04-slide-14-mindset-shift.png', caption: '思維轉變：從被動到主動編排——交出方向盤（盲目信任 AI，完全放棄控制與思考）→ 精心編排（策略性選擇，主動結合人類智慧與 AI 的雙重優勢）。有效的 AI 協作絕不是「把工作丟給 AI 就大功告成」，而是持續的、深思熟慮的選擇' },
  { src: '/images/ai-fluency/nlm04-slide-15-excel-as-collaborator.png', caption: '成為卓越的 AI 協作者：① 成為領域的專家；② 深刻了解你的工具；③ 做出明智的委派。這三步結合，讓你從「了解到精通」，準備好讓你的 AI 協作之路更上一層樓' },
]
</script>

# 📓 第 04 課：委派（Delegation）

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 04 課：委派（Delegation）

4Ds 的第一個 D。學習如何判斷哪些任務適合委派給 AI，掌握問題意識、平台意識、任務委派三大核心支柱。課程的核心洞察是：最優秀的 AI 協作者，首先是領域的專家——委派能力的基石不是 AI 技術，而是你對目標的理解。透過任務診斷矩陣與四大協作模式，學會策略性地在人類智慧與 AI 運算優勢之間分配工作。

---

## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要：人工智慧協作的關鍵：掌握委派的藝術
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm04-summary.mp4"
  poster="/images/ai-fluency/nlm04-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm04-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm04-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm04-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理

**第一章：委派的真正意義——不是放手，是編排**

委派（Delegation）是 4Ds 框架的第一個 D，核心目的是幫助你達成 AI 協作的「效能」與「效率」。它不是把工作扔給 AI 就算了，而是精準地在每個子任務上做出判斷——哪些自己做、哪些讓 AI 做、哪些一起做。

> 「AI 素養不只是技術能力，而是如何有效地決定：哪些工作該自己做，哪些工作該交給 AI。」

**第二章：令人驚訝的事實——基石不是 AI，而是你**

最優秀的 AI 協作者，首先是其領域的專家。沒有清晰的目標與專業理解，再先進的 AI 也無法帶你到達目的地。這打破了「先學 AI 技術」的迷思——**你的領域知識，才是委派能力的金字塔底座**。

**第三章：三大核心支柱——缺一不可的委派生態**

| 支柱 | 核心問題 | 實踐方法 |
|------|---------|----------|
| **問題意識** | 我真正想完成什麼？ | 定義願景、成功標準、所需思考模式 |
| **平台意識** | 哪個工具最適合這個任務？ | 親自動手實驗不同 AI 系統 |
| **任務委派** | 如何在人機之間最佳分工？ | 套用任務診斷矩陣與決策樹 |

**第四章：任務診斷矩陣——四種工作性質的委派策略**

根據工作性質，決定最佳委派模式：  
耗時但簡單→完全自動化（AI 獨立處理）；  
充滿不確定性→人機增強（AI 作為思考夥伴）；  
知識盲區→人機協作（AI 挖掘數據填補空白）；  
批判性判斷→完全人類主導（不委派）。

**第五章：四大協作模式——從自動化到完全人類執行**

完全自動化（Automation）← 適合高重複性簡單任務；  
AI 代理執行（Agency）← 適合需代表你處理的常規對外互動；  
人機增強（Augmentation）← 適合需要深度思考、多角度受益的任務；  
完全人類執行（Human-only）← 涉及高度同理心、批判性判斷，絕不委派。

**第六章：思維轉變——從被動接受到主動編排**

有效的 AI 協作絕不是「把工作丟給 AI 就大功告成」，而是持續的、深思熟慮的選擇。從「交出方向盤」（盲目信任）轉變為「精心編排」（策略性主導），是成為卓越 AI 協作者的關鍵一步。

**影片結語金句**：
> 「成為卓越的 AI 協作者：成為領域的專家、深刻了解你的工具、做出明智的委派。」

## 📊 簡報概覽

::: tip 📊 簡報：Strategic AI Delegation（由 NotebookLM 生成）
共 15 張投影片，使用左右按鈕或縮圖列切換；點擊主圖或全螢幕鈕可放大檢視。
:::

<SlideViewer :slides="nlm04Slides" />

## 🧪 延伸測驗

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「委派（Delegation）」課程影片自動生成，涵蓋三大支柱、任務診斷矩陣與協作模式。
:::

### 測驗 4-1

<Quiz
  question="根據影片內容，「委派」（Delegation）的核心定義是什麼？"
  :options="nlmQ31Options"
  :answer="0"
  explanation="委派的核心在於有意識地判斷每項工作最佳的執行方式，而非把所有工作都推給 AI，或堅持全部自己做。"
/>

### 測驗 4-2

<Quiz
  question="在 AI 流暢度（AI Fluency）的四個維度中，委派主要關注哪兩者？"
  :options="nlmQ32Options"
  :answer="0"
  explanation="委派的核心目的是幫助你達成 AI 協作的「效能」（做到對的事）與「效率」（用對的方式做），這是整個 4D 框架的起點。"
/>

### 測驗 4-3

<Quiz
  question="良好委派的「基石」並非與 AI 技術相關，而是關於什麼？"
  :options="nlmQ33Options"
  :answer="0"
  explanation="最優秀的 AI 協作者首先是領域的專家。沒有清晰的目標與專業理解，即使最先進的 AI 也無法有效輔助你達成目標。"
/>

### 測驗 4-4

<Quiz
  question="什麼是「問題意識」（Problem Awareness）？"
  :options="nlmQ34Options"
  :answer="0"
  explanation="問題意識要求你在引入 AI 之前先停下來，清楚定義你想完成什麼、成功的樣子是什麼，以及需要什麼類型的思考。"
/>

### 測驗 4-5

<Quiz
  question="在評估任務需求時，如果你需要更多數據來輔助決策，這被歸類為哪一類領域？"
  :options="nlmQ35Options"
  :answer="0"
  explanation="「無知領域」代表你目前缺乏足夠資訊，適合借助 AI 挖掘更多數據、填補資訊缺口並獲取洞察，再做決策。"
/>

### 測驗 4-6

<Quiz
  question="有效的 AI 協作者具備什麼樣的身份優先順序？"
  :options="nlmQ36Options"
  :answer="0"
  explanation="這強調委派能力的基石是你的領域知識——先成為領域專家，再去學如何有效委派給 AI，順序不能顛倒。"
/>

### 測驗 4-7

<Quiz
  question="什麼是「平台意識」（Platform Awareness）？"
  :options="nlmQ37Options"
  :answer="0"
  explanation="平台意識要求你深入了解你所使用的 AI 工具的獨特能力與限制，這樣才能為特定任務選擇最合適的工具。"
/>

### 測驗 4-8

<Quiz
  question="建立平台意識的最佳方法是什麼？"
  :options="nlmQ38Options"
  :answer="0"
  explanation="由於 AI 技術版圖變化極快，最好的學習方式是親自動手實驗——頻繁測試不同系統，基於個人經驗發展深刻見解。"
/>

### 測驗 4-9

<Quiz
  question="「任務委派」（Task Delegation）的核心藝術在於什麼？"
  :options="nlmQ39Options"
  :answer="0"
  explanation="真正的委派藝術在於巧妙地在人類與 AI 之間分配工作，讓雙方都能發揮各自無可取代的獨特優勢。"
/>

### 測驗 4-10

<Quiz
  question="根據影片，哪一類工作應保留給人類，而不應委派給 AI？"
  :options="nlmQ40Options"
  :answer="0"
  explanation="涉及高度同理心與批判性判斷的工作，必須保留給人類親自處理，這是 AI 目前無法替代的核心能力區域。"
/>

---

*本頁測驗由 Google NotebookLM 根據 [The AI Fluency Framework](https://aifluencyframework.org/) 課程影片自動生成（Rick Dakan & Joseph Feller，與 Anthropic 合作開發）。原課程素材以 CC BY-NC-SA 4.0 授權發佈。*
