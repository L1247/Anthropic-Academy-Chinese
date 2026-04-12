# 🗺️ 學習路線圖

依照你的目標和背景，選擇最適合的學習路線。每條路線都標註了課程順序與前置條件的關係。

## 📋 官方推薦學習路徑

<div class="recommended-paths">
  <div class="paths-grid">
    <div class="path-card path-orange">
      <div class="path-header">
        <span class="path-badge">非工程師路徑</span>
        <p class="path-audience">上班族・創作者・學生</p>
      </div>
      <ol class="path-courses">
        <li>
          <div class="course-info">
            <div class="course-main">Claude 101</div>
            <div class="course-sub">入門必修，了解核心功能</div>
          </div>
        </li>
        <li>
          <div class="course-info">
            <div class="course-main">AI Fluency：基礎概覽</div>
            <div class="course-sub">建立 AI 協作思維</div>
          </div>
        </li>
        <li>
          <div class="course-info">
            <div class="course-main">Claude Cowork 入門</div>
            <div class="course-sub">實際以應用場景延伸學習</div>
          </div>
        </li>
      </ol>
      <div class="path-cta path-cta-orange">✓ 從「會用」升級到「懂用」</div>
    </div>
    <div class="path-card path-blue">
      <div class="path-header">
        <span class="path-badge">開發者路徑</span>
        <p class="path-audience">後端工程師・AI 開發者</p>
      </div>
      <ol class="path-courses">
        <li>
          <div class="course-info">
            <div class="course-main">Claude Code 實戰</div>
            <div class="course-sub">整合環境工具，提升開發效率</div>
          </div>
        </li>
        <li>
          <div class="course-info">
            <div class="course-main">Agent Skills 入門</div>
            <div class="course-sub">建立可重複使用工具鏈</div>
          </div>
        </li>
        <li>
          <div class="course-info">
            <div class="course-main">使用 Claude API 開發</div>
            <div class="course-sub">完整 API 整合知識</div>
          </div>
        </li>
        <li>
          <div class="course-info">
            <div class="course-main">MCP 入門</div>
            <div class="course-sub">擴展外部協議與工具</div>
          </div>
        </li>
      </ol>
      <div class="path-cta path-cta-blue">✓ 具備完整 AI 開發能力</div>
    </div>
  </div>
</div>

::: tip 🔍 圖表操作提示
點擊下方任一流程圖可放大檢視；放大後可 🖱️ 滾輪縮放、拖曳移動，按 ESC 關閉。
:::

## 🧠 路線一：AI 素養（所有人必讀）

::: warning ⚠️ 建議從這裡開始
無論你的背景或目標為何，**AI 素養是所有路線的共同基礎**。建立正確的 AI 觀念與心智模型，能讓你在後續任何路線中事半功倍。
:::

**目標：** 建立對 AI 的正確認知與協作心態，理解 AI 的能力邊界

<div class="route-literacy-chart">

```mermaid
flowchart TD
    A["🧠 AI 素養：框架與基礎<br/>核心必修：4D 框架與 AI 協作心智模型"] --> B
    B["⚡ AI 能力與限制<br/>理解 AI 行為模式、失敗類型與邊界"] --> C
    C{依目標選擇下一步}
    C --> D["🌱 繼續路線二<br/>一般使用者 / 初學者"]
    C --> E["💻 繼續路線三<br/>開發者"]
    C --> F["👩‍🏫 繼續路線四<br/>教育者"]
    C --> G["🎓 繼續路線五<br/>學生"]
```

</div>

**預計時間：** 1.5–2 小時 | **難度：** ⭐ 無前置條件

---

## 🌱 路線二：初學者 / 一般使用者

**目標：** 掌握 AI 基礎知識，能在日常工作中有效使用 Claude

<div class="route-beginner-chart">

```mermaid
flowchart TD
    A["🧠 AI 素養：框架與基礎<br/>（建議先完成路線一）"] --> B
    B["🌱 起點：Claude 101<br/>了解 Claude 的核心功能與工作流程"] --> C
    C["💬 Claude Cowork 入門<br/>學習與 Claude 協作處理真實檔案與任務"]
```

</div>

**預計時間：** 3–5 小時 | **難度：** ⭐ 初學者

---

## 💻 路線三：開發者

**目標：** 將 Claude 整合進應用程式，掌握 API、MCP 和代理架構

<div class="route-dev-chart">

```mermaid
flowchart TD
    A["💬 Claude 101<br/>（選修）了解 Claude 基本功能"] --> B
    B["🔧 使用 Claude API 開發<br/>84 堂課 · 8 小時+<br/>前置：Python、JSON 基礎"] --> C
    C{選擇方向}
    C --> D["🔌 MCP 入門<br/>前置：Python、HTTP 基礎"]
    C --> E["⚡ Claude Code 實戰<br/>前置：終端、Git"]
    C --> F["☁️ 雲端部署"]
    D --> G["🚀 MCP 進階主題<br/>前置：MCP 入門 + async"]
    E --> H["🤖 Agent Skills 入門<br/>前置：Claude Code 經驗"]
    E --> I["👥 子代理入門<br/>前置：Claude Code 經驗"]
    F --> J["Amazon Bedrock<br/>前置：Python、AWS"]
    F --> K["Google Vertex AI<br/>前置：Python、GCP"]
```

</div>

**預計時間：** 15–30 小時 | **難度：** ⭐⭐–⭐⭐⭐ 中-高級

---

## 👩‍🏫 路線四：教育者

**目標：** 將 AI 素養融入教學實踐與機構策略

<div class="route-edu-chart">

```mermaid
flowchart TD
    A["🧠 路線一：AI 素養<br/>（建議先完成路線一再繼續）"] --> B
    B["👩‍🏫 教育者的 AI 素養<br/>課程設計、評量策略、教學整合"] --> C
    C["📖 教授 AI 素養<br/>前置：AI Fluency 基礎課程<br/>教學場景設計、學習成效評估"]
```

</div>

**預計時間：** 4–6 小時 | **難度：** ⭐–⭐⭐ 初-中級

---

## 🎓 路線五：學生

**目標：** 利用 AI 提升學習效率、職涯規劃與學術成就

<div class="route-student-chart">

```mermaid
flowchart TD
    A["🧠 路線一：AI 素養<br/>（建議先完成路線一再繼續）"] --> B
    B["🎓 學生的 AI 素養<br/>學術研究、職涯規劃、學習策略"] --> C
    C["💬 Claude 101<br/>（選修）掌握 Claude 實際操作技巧"]
```

</div>

**預計時間：** 3–4 小時 | **難度：** ⭐ 初學者

---

## 📋 課程前置條件速查表

| 課程 | 必要前置條件 | 建議前置條件 |
|------|------------|------------|
| AI 素養：框架與基礎 | 無 | — |
| AI 能力與限制 | 無 | — |
| 教育者的 AI 素養 | 無 | AI 素養基礎 |
| 學生的 AI 素養 | 無 | AI 素養基礎 |
| 教授 AI 素養 | AI Fluency 基礎課程 | — |
| 非營利組織的 AI 素養 | 無 | AI Fluency 基礎 |
| Claude 101 | 無 | — |
| Claude Code 101 | 基本命令列操作 | — |
| Claude Cowork 入門 | 無 | — |
| 使用 Claude API 開發 | Python、JSON 基礎 | — |
| MCP 入門 | Python、JSON 和 HTTP 基礎 | — |
| MCP 進階主題 | MCP 入門課程、async 程式設計 | — |
| Claude Code 實戰 | 終端操作、Git 基礎 | — |
| Agent Skills 入門 | Claude Code 基本使用經驗 | — |
| 子代理入門 | Claude Code 基本使用經驗 | — |
| Claude × Amazon Bedrock | Python、AWS 基礎 | — |
| Claude × Google Vertex AI | Python、GCP 基礎 | — |
