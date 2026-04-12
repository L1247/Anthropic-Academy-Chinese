import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(defineConfig({
  lang: 'zh-TW',
  title: 'Anthropic Academy 中文指南',
  description: 'Anthropic Academy 17 門免費課程的完整繁體中文學習指南',

  head: [
    ['meta', { property: 'og:title', content: 'Anthropic Academy 中文指南' }],
    ['meta', { property: 'og:description', content: 'Anthropic Academy 17 門免費課程完整繁體中文導覽' }],
    ['meta', { name: 'theme-color', content: '#d97706' }],
  ],

  themeConfig: {
    logo: '📚',
    siteTitle: 'Anthropic Academy 中文指南',

    nav: [
      { text: '🏠 首頁', link: '/' },
      {
        text: '📂 課程分類',
        items: [
          { text: '🧠 AI 素養（6 門）', link: '/ai-fluency/' },
          { text: '💬 Claude 產品（3 門）', link: '/claude-products/' },
          { text: '🛠️ 開發者（8 門）', link: '/developer/' },
        ],
      },
      { text: '🗺️ 學習路線', link: '/roadmap' },
      { text: '🎓 官方證書', link: '/certificates' },
      { text: '📖 參考連結', link: '/references' },
      { text: '📎 額外資源', link: '/resources' },
      {
        text: '🔗 官方課程',
        link: 'https://anthropic.skilljar.com/',
        target: '_blank',
      },
    ],

    sidebar: {
      '/ai-fluency/': [
        {
          text: '🧠 AI 素養課程',
          items: [
            { text: '課程總覽', link: '/ai-fluency/' },
          ],
        },
        {
          text: '📚 基礎課程',
          items: [
            { text: 'AI 素養：框架與基礎', link: '/ai-fluency/framework-foundations' },
            { text: '└ 🎯4D 互動練習', link: '/ai-fluency/4d-practice' },
            { text: 'AI 能力與限制', link: '/ai-fluency/capabilities-limitations' },
            { text: '└ 🎯AI 能力練習', link: '/ai-fluency/capabilities-practice' },
          ],
        },
        {
          text: '🎓 學生族群',
          items: [
            { text: '學生的 AI 素養', link: '/ai-fluency/for-students' },
            { text: '└ 🎯學生練習', link: '/ai-fluency/students-practice' },
          ],
        },
        {
          text: '👩‍💼 非學生族群',
          items: [
            { text: '教育者的 AI 素養', link: '/ai-fluency/for-educators' },
            { text: '└ 🎯教育者練習', link: '/ai-fluency/educators-practice' },
            { text: '教授 AI 素養', link: '/ai-fluency/teaching' },
            { text: '└ 🎯教授 AI 素養練習', link: '/ai-fluency/teaching-practice' },
            { text: '非營利組織的 AI 素養', link: '/ai-fluency/for-nonprofits' },
            { text: '└ 🎯非營利組織練習', link: '/ai-fluency/nonprofits-practice' },
          ],
        },
        {
          text: '📓 NotebookLM 延伸學習',
          collapsed: false,
          items: [
            { text: '第 01 課：AI 素養簡介', link: '/ai-fluency/framework-nlm-01' },
            { text: '第 02 課：4D 框架詳解', link: '/ai-fluency/framework-nlm-02' },
          ],
        },
      ],
      '/claude-products/': [
        {
          text: '💬 Claude 產品課程',
          items: [
            { text: '課程總覽', link: '/claude-products/' },
            { text: 'Claude 101', link: '/claude-products/claude-101' },
            { text: '└ 🎯Claude 101 練習', link: '/claude-products/claude-101-practice' },
            { text: 'Claude Code 101', link: '/claude-products/claude-code-101' },
            { text: '└ 🎯Claude Code 101 練習', link: '/claude-products/claude-code-101-practice' },
            { text: 'Claude Cowork 入門', link: '/claude-products/claude-cowork' },
            { text: '└ 🎯Claude Cowork 練習', link: '/claude-products/claude-cowork-practice' },
          ],
        },
      ],
      '/developer/': [
        {
          text: '🛠️ 開發者課程',
          items: [
            { text: '課程總覽', link: '/developer/' },
          ],
        },
        {
          text: '💻 核心開發',
          items: [
            { text: '使用 Claude API 開發', link: '/developer/building-with-api' },
            { text: 'Claude Code 實戰', link: '/developer/claude-code-in-action' },
          ],
        },
        {
          text: '🔌 MCP 協定',
          items: [
            { text: 'MCP 入門', link: '/developer/mcp-intro' },
            { text: 'MCP 進階主題', link: '/developer/mcp-advanced' },
          ],
        },
        {
          text: '⚡ Claude Code 擴充',
          items: [
            { text: 'Agent Skills 入門', link: '/developer/agent-skills' },
            { text: '子代理入門', link: '/developer/subagents' },
          ],
        },
        {
          text: '☁️ 雲端平台',
          items: [
            { text: 'Claude × Amazon Bedrock', link: '/developer/amazon-bedrock' },
            { text: 'Claude × Google Vertex AI', link: '/developer/google-vertex' },
          ],
        },
      ],
    },

    outline: {
      label: '本頁目錄',
      level: [2, 3],
    },

    docFooter: {
      prev: '上一頁',
      next: '下一頁',
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜尋課程',
            buttonAriaLabel: '搜尋課程',
          },
          modal: {
            noResultsText: '無相關結果',
            resetButtonTitle: '清除搜尋',
            footer: {
              selectText: '選擇',
              navigateText: '切換',
              closeText: '關閉',
            },
          },
        },
      },
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/anthropics/courses' },
    ],

    footer: {
      message: '本網站為非官方中文學習指南，內容整理自 <a href="https://anthropic.skilljar.com/" target="_blank">Anthropic Academy</a>',
      copyright: '© 2026 Anthropic Academy 中文指南 | 版權歸 Anthropic 所有',
    },
  },

  mermaid: {
    theme: 'default',
    themeVariables: {
      fontSize: '13px',
    },
    flowchart: {
      padding: 20,
      rankSpacing: 70,
      htmlLabels: true,
    },
  },

}))
