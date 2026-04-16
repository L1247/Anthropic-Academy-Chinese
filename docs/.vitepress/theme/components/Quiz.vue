<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  question: { type: String, default: '' },
  options: { type: [Array, Object], required: true },
  answer: { type: [Number, Array], default: null },
  explanation: { type: String, default: '' },
  multi: { type: Boolean, default: false }
})

// Support both formats:
// 1. Legacy: <Quiz question="..." :options="[str]" :answer="0" explanation="..." />
// 2. Config object: <Quiz :options="{ question, options: [{text, explanation}], correctAnswer }" />
const isConfigObject = computed(() => !Array.isArray(props.options))

const resolvedQuestion = computed(() =>
  isConfigObject.value ? props.options.question : props.question
)

const resolvedOptions = computed(() => {
  const raw = isConfigObject.value ? props.options.options : props.options
  return raw.map(o => (typeof o === 'string' ? o : o.text))
})

const resolvedAnswer = computed(() =>
  isConfigObject.value ? props.options.correctAnswer : props.answer
)

const resolvedExplanation = computed(() => {
  if (isConfigObject.value) {
    const opts = props.options.options
    const ans = props.options.correctAnswer
    if (Array.isArray(ans)) {
      return opts[ans[0]]?.explanation ?? ''
    }
    return opts[ans]?.explanation ?? ''
  }
  return props.explanation
})

const selected = ref(props.multi ? [] : null)
const submitted = ref(false)

function toggleOption(i) {
  if (submitted.value) return
  if (props.multi) {
    const idx = selected.value.indexOf(i)
    if (idx === -1) selected.value.push(i)
    else selected.value.splice(idx, 1)
  } else {
    selected.value = i
  }
}

function submit() {
  if (!canSubmit.value) return
  submitted.value = true
}

function reset() {
  selected.value = props.multi ? [] : null
  submitted.value = false
}

function isSelected(i) {
  return props.multi ? selected.value.includes(i) : selected.value === i
}

function isCorrect(i) {
  const ans = resolvedAnswer.value
  return Array.isArray(ans) ? ans.includes(i) : i === ans
}

function optionStatus(i) {
  if (!submitted.value) return isSelected(i) ? 'selected' : ''
  if (isCorrect(i)) return 'correct'
  if (isSelected(i)) return 'wrong'
  return ''
}

const isAllCorrect = computed(() => {
  if (!submitted.value) return false
  if (props.multi) {
    const ans = new Set(Array.isArray(resolvedAnswer.value) ? resolvedAnswer.value : [resolvedAnswer.value])
    const sel = new Set(selected.value)
    return ans.size === sel.size && [...ans].every(x => sel.has(x))
  }
  return selected.value === resolvedAnswer.value
})

const canSubmit = computed(() => {
  return props.multi ? selected.value.length > 0 : selected.value !== null
})
</script>

<template>
  <div class="practice-card">
    <p class="quiz-question">{{ resolvedQuestion }}</p>
    <p v-if="multi" class="quiz-hint">（可複選，選完後再點「檢查答案」）</p>
    <div class="quiz-options">
      <button
        v-for="(opt, i) in resolvedOptions"
        :key="i"
        class="practice-option"
        :class="optionStatus(i)"
        :disabled="submitted"
        @click="toggleOption(i)"
      >
        <span class="opt-marker">
          <template v-if="!submitted">{{ isSelected(i) ? '◉' : '○' }}</template>
          <template v-else-if="isCorrect(i)">✅</template>
          <template v-else-if="isSelected(i) && !isCorrect(i)">❌</template>
          <template v-else>○</template>
        </span>
        {{ opt }}
      </button>
    </div>
    <div class="quiz-actions">
      <button
        v-if="!submitted"
        class="practice-btn"
        :disabled="!canSubmit"
        @click="submit"
      >
        檢查答案
      </button>
      <button v-else class="practice-btn secondary" @click="reset">
        再試一次
      </button>
    </div>
    <div
      v-if="submitted"
      class="practice-feedback"
      :class="isAllCorrect ? 'correct-feedback' : 'wrong-feedback'"
    >
      <strong>{{ isAllCorrect ? '✅ 正確！' : '💭 再想想看…' }}</strong>
      <p>{{ resolvedExplanation }}</p>
    </div>
  </div>
</template>
