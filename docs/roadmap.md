# 🗺️ 學習路線圖

依照你的目標和背景，選擇最適合的學習路線。每條路線都標註了課程順序與前置條件的關係。

## 🌱 路線一：初學者 / 一般使用者

**目標：** 掌握 AI 基礎知識，能在日常工作中有效使用 Claude

```mermaid
flowchart TD
    A["🌱 起點：Claude 101<br/>了解 Claude 的核心功能與工作流程"] --> B
    B["🧠 AI 素養：框架與基礎<br/>建立 AI 協作的心智模型（4D 框架）"] --> C
    C["⚡ AI 能力與限制<br/>理解 AI 的行為模式與失敗類型"] --> D
    D["💬 Claude Cowork 入門<br/>學習與 Claude 協作處理真實檔案與任務"]

    style A fill:#fef3c7,stroke:#d97706
    style B fill:#fef3c7,stroke:#d97706
    style C fill:#fef3c7,stroke:#d97706
    style D fill:#fef3c7,stroke:#d97706
```

**預計時間：** 3–5 小時 | **難度：** ⭐ 初學者

---

## 💻 路線二：開發者

**目標：** 將 Claude 整合進應用程式，掌握 API、MCP 和代理架構

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

    style B fill:#dbeafe,stroke:#3b82f6
    style D fill:#dbeafe,stroke:#3b82f6
    style E fill:#dbeafe,stroke:#3b82f6
    style G fill:#dbeafe,stroke:#3b82f6
    style H fill:#dbeafe,stroke:#3b82f6
    style I fill:#dbeafe,stroke:#3b82f6
```

**預計時間：** 15–30 小時 | **難度：** ⭐⭐–⭐⭐⭐ 中-高級

---

## 👩‍🏫 路線三：教育者

**目標：** 將 AI 素養融入教學實踐與機構策略

```mermaid
flowchart TD
    A["🧠 AI 素養：框架與基礎<br/>必修：4D 框架核心概念"] --> B
    B["⚡ AI 能力與限制<br/>理解 AI 行為與失敗類型"] --> C
    C["👩‍🏫 教育者的 AI 素養<br/>課程設計、評量策略、教學整合"] --> D
    D["📖 教授 AI 素養<br/>前置：AI Fluency 基礎課程<br/>教學場景設計、學習成效評估"]

    style A fill:#f0fdf4,stroke:#22c55e
    style B fill:#f0fdf4,stroke:#22c55e
    style C fill:#f0fdf4,stroke:#22c55e
    style D fill:#f0fdf4,stroke:#22c55e
```

**預計時間：** 4–6 小時 | **難度：** ⭐–⭐⭐ 初-中級

---

## 🎓 路線四：學生

**目標：** 利用 AI 提升學習效率、職涯規劃與學術成就

```mermaid
flowchart TD
    A["🧠 AI 素養：框架與基礎<br/>必修：建立正確的 AI 使用觀念"] --> B
    B["⚡ AI 能力與限制<br/>了解 AI 的邊界，避免過度依賴"] --> C
    C["🎓 學生的 AI 素養<br/>學術研究、職涯規劃、學習策略"] --> D
    D["💬 Claude 101<br/>（選修）掌握 Claude 實際操作技巧"]

    style A fill:#fdf4ff,stroke:#a855f7
    style B fill:#fdf4ff,stroke:#a855f7
    style C fill:#fdf4ff,stroke:#a855f7
    style D fill:#fdf4ff,stroke:#a855f7
```

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
