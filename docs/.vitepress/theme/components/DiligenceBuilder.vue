<script setup>
import { ref, computed } from 'vue'

const allTools = ['Claude', 'ChatGPT', 'Copilot', 'Gemini', '其他']
const allPurposes = ['發想靈感', '草稿撰寫', '翻譯潤稿', '程式碼', '校對修改', '資料研究']
const reviewOptions = [
  { value: 'thorough', label: '逐字校對，並核實所有事實陳述' },
  { value: 'partial', label: '整體結構調整，對關鍵段落事實核對' },
  { value: 'light', label: '閱讀全文，依主觀判斷修改' },
  { value: 'none', label: '主要採用 AI 輸出，僅調整格式' }
]

const selectedTools = ref([])
const selectedPurposes = ref([])
const selectedReview = ref('')
const factsVerified = ref(null)
const extraNote = ref('')
const copied = ref(false)

function toggleTool(t) {
  const idx = selectedTools.value.indexOf(t)
  if (idx === -1) selectedTools.value.push(t)
  else selectedTools.value.splice(idx, 1)
}

function togglePurpose(p) {
  const idx = selectedPurposes.value.indexOf(p)
  if (idx === -1) selectedPurposes.value.push(p)
  else selectedPurposes.value.splice(idx, 1)
}

const statement = computed(() => {
  const tools = selectedTools.value.length
    ? selectedTools.value.join('、')
    : '（尚未選擇 AI 工具）'

  const purposes = selectedPurposes.value.length
    ? selectedPurposes.value.join('、')
    : '（尚未選擇用途）'

  const reviewLabel = reviewOptions.find(o => o.value === selectedReview.value)?.label
    || '（尚未選擇審核方式）'

  const verifyLine = factsVerified.value === true
    ? '我已對文中的關鍵事實與數據進行了獨立驗證。'
    : factsVerified.value === false
    ? '本內容未進行獨立事實查核，讀者應自行驗證重要資訊。'
    : '（尚未說明事實驗證狀況）'

  const noteLine = extraNote.value.trim()
    ? `\n補充說明：${extraNote.value.trim()}`
    : ''

  return `關於 AI 使用的聲明：

本內容在「${purposes}」過程中使用了 ${tools}。

我對 AI 生成的內容進行了以下處理：${reviewLabel}。

${verifyLine}${noteLine}

最終提交的內容反映我的理解與判斷，我對其正確性負全責。`
})

const isReady = computed(() =>
  selectedTools.value.length > 0 &&
  selectedPurposes.value.length > 0 &&
  selectedReview.value !== '' &&
  factsVerified.value !== null
)

async function copyStatement() {
  if (typeof window === 'undefined') return
  try {
    await navigator.clipboard.writeText(statement.value)
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  } catch {
    // fallback: select text
  }
}
</script>

<template>
  <div class="practice-card diligence-builder">
    <p class="builder-intro">
      填寫下方表單，系統將即時產生一份符合格式的盡責聲明。完成後可複製使用。
    </p>

    <!-- 1. AI 工具 -->
    <div class="form-section">
      <label class="form-label">1️⃣ 使用的 AI 工具（可複選）</label>
      <div class="chip-group">
        <button
          v-for="t in allTools"
          :key="t"
          class="chip"
          :class="{ active: selectedTools.includes(t) }"
          @click="toggleTool(t)"
        >
          {{ t }}
        </button>
      </div>
    </div>

    <!-- 2. 用途 -->
    <div class="form-section">
      <label class="form-label">2️⃣ AI 的用途（可複選）</label>
      <div class="chip-group">
        <button
          v-for="p in allPurposes"
          :key="p"
          class="chip"
          :class="{ active: selectedPurposes.includes(p) }"
          @click="togglePurpose(p)"
        >
          {{ p }}
        </button>
      </div>
    </div>

    <!-- 3. 審核方式 -->
    <div class="form-section">
      <label class="form-label">3️⃣ 人類審核方式（單選）</label>
      <div class="radio-group">
        <label
          v-for="opt in reviewOptions"
          :key="opt.value"
          class="radio-option"
          :class="{ active: selectedReview === opt.value }"
        >
          <input
            type="radio"
            :value="opt.value"
            v-model="selectedReview"
            style="display:none"
          />
          <span class="radio-marker">{{ selectedReview === opt.value ? '◉' : '○' }}</span>
          {{ opt.label }}
        </label>
      </div>
    </div>

    <!-- 4. 事實驗證 -->
    <div class="form-section">
      <label class="form-label">4️⃣ 是否已驗證關鍵事實與數據？</label>
      <div class="yn-buttons">
        <button
          class="yn-btn yes-btn"
          :class="{ active: factsVerified === true }"
          @click="factsVerified = true"
        >
          是，已驗證
        </button>
        <button
          class="yn-btn no-btn"
          :class="{ active: factsVerified === false }"
          @click="factsVerified = false"
        >
          否，未特別驗證
        </button>
      </div>
    </div>

    <!-- 5. 補充說明 -->
    <div class="form-section">
      <label class="form-label">5️⃣ 補充說明（選填）</label>
      <textarea
        v-model="extraNote"
        class="prompt-textarea"
        placeholder="例如：AI 負責初稿，我重寫了所有結論段落；或說明特殊使用情境…"
        rows="2"
      />
    </div>

    <!-- 預覽 -->
    <div class="statement-preview-section">
      <h4>📄 你的盡責聲明預覽：</h4>
      <pre class="statement-preview" :class="{ ready: isReady }">{{ statement }}</pre>
      <button
        class="practice-btn"
        :disabled="!isReady"
        @click="copyStatement"
      >
        {{ copied ? '✅ 已複製！' : '📋 複製到剪貼簿' }}
      </button>
      <p v-if="!isReady" class="not-ready-hint">請填寫所有必填欄位（1–4），聲明才算完整。</p>
    </div>
  </div>
</template>
