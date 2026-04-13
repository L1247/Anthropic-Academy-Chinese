---
title: 'NLM 延伸：什麼是生成式 AI？'
description: 'Google NotebookLM 根據第 03 課影片自動生成的延伸學習素材：影片摘要、簡報重點、測驗'
---

<script setup>
const nlmQ21Options = ["生成式 AI 專注於分析與分類既有數據，而傳統 AI 則創造新內容。", "生成式 AI 能夠創造出原本不存在的新內容，而不僅僅是分析數據。", "傳統 AI 需要大量計算能力，而生成式 AI 可以在個人電腦上輕鬆運行。", "生成式 AI 僅限於處理結構化數據，傳統 AI 則處理人類語言。"]
const nlmQ22Options = ["模型在實體伺服器中所佔據的物理空間大小。", "模型所包含的參數（Parameters）數量達到數十億計。", "模型只能處理長篇大論的文章，無法處理簡短的對話。", "模型在互聯網上佔用的下載頻寬。"]
const nlmQ23Options = ["卷積神經網絡（CNN）的發明。", "分散式運算集群的全面普及。", "轉換器架構（Transformer Architecture）。", "圖形處理器（GPU）的首次應用。"]
const nlmQ24Options = ["當模型變大時，它們會變得越來越慢且難以預測。", "模型性能會隨數據量增加而呈線性下降。", "隨著規模增長，模型會展現出未經刻意編寫的「湧現能力」（Emergent Capabilities）。", "只要有足夠的數據，小型模型的表現就能超越大型模型。"]
const nlmQ25Options = ["讓模型閱讀整個互聯網以建立基礎的語言地圖。", "教導模型遵循指令、提供有用的回應並避免有害內容。", "減少模型運行所需的 GPU 數量以節省成本。", "將模型的所有記憶永久儲存到外部數據庫中。"]
const nlmQ26Options = ["它是 AI 能夠連接到互聯網的總時長限制。", "它是 AI 的永久記憶庫，儲存了所有歷史訓練數據。", "它是 AI 在單次互動中能同時考慮的資訊量上限。", "它是限制用戶每天可以發送給 AI 的訊息次數。"]
const nlmQ27Options = ["因為它們是基於統計模式生成文本，而非直接檢索事實庫。", "因為它們被編程為必須對用戶撒謊以保護開發者隱私。", "因為它們的硬件溫度過高導致計算錯誤。", "因為它們試圖透過提供錯誤資訊來節省計算成本。"]
const nlmQ28Options = ["該模型將在 2024 年 11 月之後停止運作。", "模型沒有關於 2024 年 11 月之後發生的世界大事的內在知識。", "用戶無法在 2024 年 11 月之後向模型詢問任何問題。", "模型會自動刪除所有在 2024 年 11 月之前學到的過時知識。"]
const nlmQ29Options = ["模型對於同樣的輸入，每次都會給出完全一模一樣的回應。", "模型在生成文本時是基於機率做決定，因此即使輸入相同，回應也可能略有不同。", "這種不確定性是由於網絡連線不穩定造成的。", "非確定性意味著模型無法處理任何邏輯問題。"]
const nlmQ30Options = ["增加模型的參數數量到 $10^{15}$ 以上。", "檢索增強生成（Retrieval Augmented Generation, RAG）。", "重新進行為期數年的完整預訓練過程。", "強制要求模型放棄使用任何機率性預測。"]

const nlm03Slides = [
  { src: '/images/ai-fluency/nlm03-slide-01-cover.png', caption: '封面：生成式 AI 的底層邏輯與應用邊界——AI 素養核心指南：從技術原理到人機協作' },
  { src: '/images/ai-fluency/nlm03-slide-02-analysis-to-creation.png', caption: '從分析到創造：AI 典範的根本轉移——傳統 AI 判斷「這是什麼」，生成式 AI 生成「接下來該出現什麼」，核心差異在於創造全新內容而非分類既有數據' },
  { src: '/images/ai-fluency/nlm03-slide-03-llm-engine.png', caption: '驅動生成的核心引擎：大型語言模型（LLMs）——包含數十億「參數」，運作本質是根據統計機率「預測」最合理的下一個字詞，而非從資料庫中「搜尋」現成答案' },
  { src: '/images/ai-fluency/nlm03-slide-04-three-catalysts.png', caption: '完美風暴：造就現代 AI 的三大技術催化劑——① 2017 年 Transformer 架構突破、② 數據大爆發（網路、書籍、程式碼）、③ 算力躍升（GPU / TPU），三者協同觸發「湧現能力」' },
  { src: '/images/ai-fluency/nlm03-slide-05-pretraining.png', caption: '黑盒子解密（一）：預訓練構建語言地圖——訓練目標是「預測下一個字」，學習成果是建立一張涵蓋語言、知識與概念間深層統計關係的語言地圖；此時為「生肉預測機」' },
  { src: '/images/ai-fluency/nlm03-slide-06-fine-tuning-alignment.png', caption: '黑盒子解密（二）：微調與價值觀對齊——透過人類反饋（RLHF）讓模型遵守 3H 原則：Helpful（有用）、Honest（誠實）、Harmless（無害），從「統計預測機」蛻變為「能對話的專業助手」' },
  { src: '/images/ai-fluency/nlm03-slide-07-ai-superpowers.png', caption: '超越人類的超能力：生成式 AI 的核心優勢——任務切換的敏捷性（Versatility）、情境學習（In-context Learning）、對話記憶維持、工具擴充能力，四大能力造就「全能的新同事」' },
  { src: '/images/ai-fluency/nlm03-slide-08-context-window.png', caption: '互動的物理界限：上下文視窗（Context Window）——AI 的「工作記憶」有上限；超出範圍時採先進先出機制，最早輸入的資訊將被「擠出」遺忘，影響長對話的連貫性' },
  { src: '/images/ai-fluency/nlm03-slide-09-knowledge-cutoff.png', caption: '認知盲區：知識截止日與幻覺——限制一：訓練完成當刻即「封存」，不知截止日後的事；限制二：AI 幻覺（Hallucination）——基於機率而非事實庫，可能生成聽起來合理但實際錯誤的內容' },
  { src: '/images/ai-fluency/nlm03-slide-10-temperature.png', caption: '隨機性與一致性：溫度的奧秘——Temperature 控制輸出隨機程度：低溫→高一致性（適合分析、程式碼）；高溫→高多樣性（適合腦力激盪、創意寫作）' },
  { src: '/images/ai-fluency/nlm03-slide-11-rag-reasoning.png', caption: '突破邊界：技術的演進與未來（RAG 與推理）——痛點解法一：RAG 讓模型連結外部即時或私有知識庫；痛點解法二：進階推理模型（Extended Thinking）在生成前進行逐步推理，大幅提升複雜問題的解題能力' },
  { src: '/images/ai-fluency/nlm03-slide-12-human-ai-symbiosis.png', caption: '最終總結：人機共生的最佳解——AI 的絕對優勢（速度規模、模式辨識、廣博知識）與人類的不可取代（批判性思考、創意與意圖、道德判斷），最高效的應用來自善用雙方的互補優勢' },
]
</script>

# 📓 第 03 課：什麼是生成式 AI？

<Badge type="tip" text="NotebookLM 生成" /> <Badge type="info" text="影片摘要 + 簡報 + 測驗" />

> 以下內容由 Google NotebookLM 根據課程影片自動生成，作為延伸濃縮學習素材。  
> 📖 回到主課程：[AI 素養：框架與基礎](/ai-fluency/framework-foundations)

## 📋 課程概覽

### 第 03 課：深度探討一：什麼是生成式 AI？

不需要技術背景的生成式 AI 原理介紹，帶你建立判斷 AI 能力邊界所需的心智模型。課程從「AI 典範轉移」出發，深入解析大型語言模型（LLMs）的核心引擎、訓練過程的兩大階段，以及影響模型行為的關鍵機制（上下文視窗、知識截止日、幻覺、溫度）。掌握這些概念，是你在後續課程中做出明智委派決策的知識基礎——你不需要成為工程師，但需要知道這台機器是怎麼「想」的。

---

## 🎬 影片摘要

::: info 🎬 NotebookLM 影片摘要：揭開生成式 AI 的神秘面紗
由 Google NotebookLM 根據課程影片自動生成的繁體中文動態摘要。
:::

<NlmVideo
  src="/videos/ai-fluency/nlm03-summary.mp4"
  poster="/images/ai-fluency/nlm03-video-poster.png"
  zh-vtt="/videos/ai-fluency/nlm03-summary.zh-Hant.vtt"
  en-vtt="/videos/ai-fluency/nlm03-summary.en.vtt"
  bi-vtt="/videos/ai-fluency/nlm03-summary.bilingual.vtt"
  default-mode="zh"
/>

### 📝 影片重點整理

**第一章：從分析到創造——AI 典範的根本轉移**

傳統 AI（分析型）的核心是「判斷這是什麼」——垃圾郵件過濾、推薦系統屬於此類；生成式 AI 的核心是「創造前所未有的全新內容」——撰寫報告、生成程式碼、回答問題。這不只是技術升級，而是 AI 能力質的飛躍。

**第二章：驅動一切的核心引擎——大型語言模型（LLMs）**

「L」代表 Large（大型）——數十億個「參數」，如同大腦中的神經突觸連結；「LM」代表 Language Model（語言模型）——透過大量學習，專門用來預測與生成符合人類語言的系統。

> 「它並非從資料庫中『搜尋』現成答案，而是根據統計機率，逐字『生成』最合理的下一個字詞。」

**第三章：完美風暴——造就現代 AI 的三大催化劑**

現代生成式 AI 的崛起並非偶然，而是三個要素同步成熟的結果：  
① **演算法突破（2017 年 Transformer 架構）**——能高效處理長序列文本，並維持詞彙間的上下文關聯；  
② **數據大爆發**——網路、書籍、程式碼提供模型學習的龐大原始資料；  
③ **算力躍升（GPU / TPU）**——讓處理海量數據和超大規模模型成為可能。  
三者協同，觸發了「規模定律（Scaling Laws）」——模型規模越大，會自動湧現出開發者未刻意設計的新能力。

**第四章：黑盒子解密——訓練的兩大階段**

| 階段 | 目標 | 結果 |
|------|------|------|
| **預訓練（Pre-training）** | 預測下一個字，建立語言地圖 | 擁有廣博知識的「生肉預測機」 |
| **微調（Fine-tuning / RLHF）** | 透過人類反饋對齊 3H 原則 | 有用、誠實、無害的「對話助手」 |

微調的核心是**人類反饋強化學習（RLHF）**，讓模型學會遵守指令、拒絕有害請求，從統計預測機蛻變為你日常使用的智慧助手。

**第五章：四大超能力——你的 AI 同事擅長什麼**

生成式 AI 在以下四個面向遠超人類：  
任務切換的敏捷性（Versatility）——在寫作、翻譯、推理之間無縫切換；  
情境學習（In-context Learning）——在提示詞中給少量指令或範例，模型立刻適應全新任務；  
對話記憶維持——在整個對話中保持上下文連貫；  
工具擴充能力——許多模型能連接外部工具，大幅擴展其能力邊界。

**第六章：三大認知限制——使用 AI 必須知道的邊界**

| 限制 | 機制 | 實務影響 |
|------|------|----------|
| **上下文視窗（Context Window）** | 工作記憶有上限，超出則遺忘最早內容 | 長對話需留意資訊截斷 |
| **知識截止日（Knowledge Cutoff）** | 訓練完成後「封存」，不知截止日後的事 | 詢問近期事件需提供最新資料 |
| **AI 幻覺（Hallucination）** | 基於機率生成，可能產生「合理但錯誤」的內容 | 重要事實務必交叉驗證 |

**第七章：溫度與 RAG——調控 AI 行為的關鍵旋鈕**

**溫度（Temperature）** 控制輸出的隨機程度：低溫適合需要準確一致的任務（數據分析、程式碼），高溫適合需要多元發散的任務（腦力激盪、創意寫作）。

**RAG（檢索增強生成）** 是突破知識截止日與私有數據限制的關鍵技術——讓模型在生成前，先從外部知識庫「檢索」相關資訊，大幅降低幻覺、提升準確度。這是企業 AI 應用的核心架構。

**影片結語金句**：
> 「最高效的應用，來自善用雙方的互補優勢。AI 的速度與規模，加上人類的判斷與責任感。」

## 📊 簡報概覽

::: tip 📊 簡報：Generative AI Decoded（由 NotebookLM 生成）
共 12 張投影片，使用左右按鈕或縮圖列切換；點擊主圖或全螢幕鈕可放大檢視。
:::

<SlideViewer :slides="nlm03Slides" />

## 🧪 延伸測驗

::: info 📌 關於這份測驗
以下 10 道題目由 **Google NotebookLM** 根據「深度探討一：什麼是生成式 AI？」課程影片自動生成，涵蓋生成式 AI 原理、LLM 架構、訓練流程及關鍵限制。
:::

### 測驗 3-1

<Quiz
  question="根據教材內容，生成式人工智慧（Generative AI）與傳統人工智慧的主要區別是什麼？"
  :options="nlmQ21Options"
  :answer="1"
  explanation="生成式 AI 的核心特徵在於其「生成」能力，能基於學習到的模式產出全新的文本、代碼或其他資訊。傳統 AI 才是專注於分類與模式識別的系統。"
/>

### 測驗 3-2

<Quiz
  question="在大型語言模型（LLM）中，「大型」一詞主要是指什麼？"
  :options="nlmQ22Options"
  :answer="1"
  explanation="參數是模型處理資訊的數學值，類似於大腦中的突觸連結，其數量之多是 LLM 強大能力的來源。"
/>

### 測驗 3-3

<Quiz
  question="2017 年出現的哪項技術突破，被認為是現代 generative AI 發展的遊戲規則改變者？"
  :options="nlmQ23Options"
  :answer="2"
  explanation="轉換器架構擅長處理文本序列，並能在長篇內容中保持詞彙間的關係，是現代 LLM 的基礎。"
/>

### 測驗 3-4

<Quiz
  question="關於「規模定律」（Scaling Laws），研究人員發現了什麼令人驚訝的現象？"
  :options="nlmQ24Options"
  :answer="2"
  explanation="這指的是模型在成長到一定規模後，會自動發展出如邏輯推理等開發者並未直接教導的能力。"
/>

### 測驗 3-5

<Quiz
  question="在 AI 訓練過程中，「微調」（Fine-tuning）階段的主要目的是什麼？"
  :options="nlmQ25Options"
  :answer="1"
  explanation="微調階段透過人類回饋與強化學習，將預訓練得到的知識轉化為安全且實用的互動能力。"
/>

### 測驗 3-6

<Quiz
  question="什麼是「脈絡視窗」（Context Window），它對 AI 的運作有何限制？"
  :options="nlmQ26Options"
  :answer="2"
  explanation="如果對話或文件超出了這個範圍，AI 將無法「記住」或處理最早輸入的資訊。"
/>

### 測驗 3-7

<Quiz
  question="為什麼 LLM 有時會產生「幻覺」（Hallucination）？"
  :options="nlmQ27Options"
  :answer="0"
  explanation="模型是在預測機率最高的下一個詞，這可能導致產生聽起來很合理但實際上錯誤的內容。"
/>

### 測驗 3-8

<Quiz
  question="若一個模型的「知識截止日期」（Knowledge Cutoff）是 2024 年 11 月，這意味著什麼？"
  :options="nlmQ28Options"
  :answer="1"
  explanation="就像一個在那天之後就斷開了與互聯網所有聯繫的人，模型無法知道未包含在其訓練集中的新資訊。"
/>

### 測驗 3-9

<Quiz
  question="關於 LLM 的「非確定性」（Non-deterministic）特徵，以下敘述何者正確？"
  :options="nlmQ29Options"
  :answer="1"
  explanation="這種變異性源於模型預測下一個詞的機率性質，這對創意工作有益，但在追求一致性時需要注意。"
/>

### 測驗 3-10

<Quiz
  question="為了克服 LLM 無法存取公司內部私有數據或最新資訊的限制，目前研究人員主要採用哪種技術？"
  :options="nlmQ30Options"
  :answer="1"
  explanation="RAG 允許模型連接到外部知識源或檢索特定數據，從而擴展其處理即時或私有資訊的能力。"
/>

---

*本頁測驗由 Google NotebookLM 根據 [The AI Fluency Framework](https://aifluencyframework.org/) 課程影片自動生成（Rick Dakan & Joseph Feller，與 Anthropic 合作開發）。原課程素材以 CC BY-NC-SA 4.0 授權發佈。*
