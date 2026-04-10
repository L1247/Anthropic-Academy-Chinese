<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  scenario: { type: String, required: true }
})

// 委派四問設定：favorsDelegation=true 代表「回答 Yes 有利於委派」
const questions = [
  {
    id: 'clarity',
    text: '這個任務明確嗎？',
    hint: '任務越清晰，AI 越容易執行到位。',
    favorsDelegation: true,
    yesExplain: '任務目標清楚，AI 有足夠的方向執行。',
    noExplain: '任務不夠明確時，建議先細化需求或在提示中詳細說明，再考慮委派。'
  },
  {
    id: 'severity',
    text: '如果 AI 出錯，後果會嚴重嗎？',
    hint: '高風險任務（涉及健康、財務、法律、重要關係）需要更多人類把關。',
    favorsDelegation: false,
    yesExplain: '後果嚴重代表需要額外的人類審核與監督，不宜完全依賴 AI 輸出。',
    noExplain: '低風險任務出錯影響有限，適合委派給 AI 嘗試。'
  },
  {
    id: 'humanJudgment',
    text: '這個任務需要獨特的人類判斷嗎？（個人關係、價值觀、道德考量等）',
    hint: '涉及情感、倫理或深度個人脈絡的任務，AI 難以完全代替人類判斷。',
    favorsDelegation: false,
    yesExplain: '此任務依賴人類獨特的判斷力，AI 可以協助，但最終決策應由人類主導。',
    noExplain: '不需要特殊人類判斷，AI 可以獨立完成大部分工作。'
  },
  {
    id: 'evaluability',
    text: '你能有效評估 AI 的輸出品質嗎？',
    hint: '若你無法判斷輸出好壞，就難以對結果負責。',
    favorsDelegation: true,
    yesExplain: '你有能力把關品質，委派更安全可靠。',
    noExplain: '如果難以判斷輸出好壞，建議先補充相關知識，或請能評估的人協助審核。'
  }
]

const answers = ref({
  clarity: null,
  severity: null,
  humanJudgment: null,
  evaluability: null
})
const showResult = ref(false)

function answer(id, value) {
  if (showResult.value) return
  answers.value[id] = value
}

const allAnswered = computed(() =>
  Object.values(answers.value).every(v => v !== null)
)

function calculate() {
  if (allAnswered.value) showResult.value = true
}

function reset() {
  answers.value = { clarity: null, severity: null, humanJudgment: null, evaluability: null }
  showResult.value = false
}

// 計算委派分數（滿分 4）
const score = computed(() => {
  let s = 0
  for (const q of questions) {
    const a = answers.value[q.id]
    if (a === null) continue
    if (q.favorsDelegation && a === true) s++
    else if (!q.favorsDelegation && a === false) s++
  }
  return s
})

const recommendation = computed(() => {
  if (score.value === 4) return { level: 'excellent', icon: '✅', text: '非常適合委派', desc: '此任務符合所有委派條件，可以放心交給 AI 執行，但仍建議檢視最終輸出。' }
  if (score.value === 3) return { level: 'good', icon: '✅', text: '適合委派（注意以下提醒）', desc: '整體適合委派，但有一個面向需要格外留意，請參考下方各題的回饋。' }
  if (score.value === 2) return { level: 'caution', icon: '⚠️', text: '謹慎委派', desc: '有多個面向需要特別注意。可以使用 AI 協助，但人類應深度介入審核與修改。' }
  return { level: 'avoid', icon: '❌', text: '不建議委派', desc: '此任務不適合完全委派給 AI。建議由人類主導，AI 只作為輔助參考。' }
})

// 每題的個別回饋
function questionFeedback(q) {
  const a = answers.value[q.id]
  return a === true ? q.yesExplain : q.noExplain
}

// 哪些題回答方向不利於委派
function isWarning(q) {
  const a = answers.value[q.id]
  if (a === null) return false
  return q.favorsDelegation ? a === false : a === true
}
</script>

<template>
  <div class="practice-card delegation-checklist">
    <div class="scenario-box">
      <strong>📋 情境</strong>
      <p>{{ scenario }}</p>
    </div>

    <div class="questions-list">
      <div
        v-for="(q, idx) in questions"
        :key="q.id"
        class="question-item"
        :class="{ answered: answers[q.id] !== null }"
      >
        <p class="question-text">
          <strong>問 {{ idx + 1 }}：</strong>{{ q.text }}
        </p>
        <p class="question-hint">{{ q.hint }}</p>
        <div class="yn-buttons">
          <button
            class="yn-btn"
            :class="{ active: answers[q.id] === true, 'yes-btn': true }"
            :disabled="showResult"
            @click="answer(q.id, true)"
          >
            是
          </button>
          <button
            class="yn-btn"
            :class="{ active: answers[q.id] === false, 'no-btn': true }"
            :disabled="showResult"
            @click="answer(q.id, false)"
          >
            否
          </button>
        </div>
      </div>
    </div>

    <div class="quiz-actions">
      <button
        v-if="!showResult"
        class="practice-btn"
        :disabled="!allAnswered"
        @click="calculate"
      >
        查看建議
      </button>
      <button v-else class="practice-btn secondary" @click="reset">
        重新評估
      </button>
    </div>

    <div v-if="showResult" class="delegation-result">
      <div
        class="result-banner"
        :class="recommendation.level"
      >
        <span class="result-icon">{{ recommendation.icon }}</span>
        <div>
          <strong>{{ recommendation.text }}</strong>
          <p>{{ recommendation.desc }}</p>
        </div>
      </div>

      <div class="per-question-feedback">
        <h4>各題分析：</h4>
        <div
          v-for="(q, idx) in questions"
          :key="q.id"
          class="feedback-item"
          :class="isWarning(q) ? 'warning-item' : 'ok-item'"
        >
          <span class="feedback-icon">{{ isWarning(q) ? '⚠️' : '✅' }}</span>
          <div>
            <strong>問 {{ idx + 1 }}：</strong>你回答「{{ answers[q.id] ? '是' : '否' }}」
            <p>{{ questionFeedback(q) }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
