<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  originalPrompt: { type: String, required: true },
  requiredKeywords: { type: Array, required: true },
  minLength: { type: Number, default: 60 },
  sampleAnswer: { type: String, required: true }
})

const userInput = ref('')
const checked = ref(false)
const showSample = ref(false)

function check() {
  if (userInput.value.trim().length === 0) return
  checked.value = true
  showSample.value = false
}

function reset() {
  userInput.value = ''
  checked.value = false
  showSample.value = false
}

function hasKeyword(kw) {
  return userInput.value.includes(kw)
}

const hitCount = computed(() =>
  props.requiredKeywords.filter(kw => hasKeyword(kw)).length
)

const lengthOk = computed(() =>
  userInput.value.trim().length >= props.minLength
)

const score = computed(() => {
  let s = hitCount.value
  if (lengthOk.value) s++
  return s
})

const maxScore = computed(() => props.requiredKeywords.length + 1)
</script>

<template>
  <div class="practice-card prompt-rewrite">
    <div class="original-prompt-box">
      <strong>📌 原始提示（模糊版）：</strong>
      <blockquote class="original-prompt">{{ originalPrompt }}</blockquote>
    </div>

    <p class="rewrite-instruction">
      請在下方輸入你的<strong>改寫版提示</strong>，試著讓它更清晰、完整、有效：
    </p>

    <textarea
      v-model="userInput"
      class="prompt-textarea"
      :disabled="checked"
      placeholder="在這裡輸入你改寫後的提示…"
      rows="5"
    />

    <div class="quiz-actions">
      <button
        v-if="!checked"
        class="practice-btn"
        :disabled="userInput.trim().length === 0"
        @click="check"
      >
        檢查我的提示
      </button>
      <button v-else class="practice-btn secondary" @click="reset">
        重新改寫
      </button>
    </div>

    <div v-if="checked" class="rewrite-result">
      <div class="score-banner">
        <strong>你的提示得分：{{ score }} / {{ maxScore }}</strong>
      </div>

      <div class="keyword-checklist">
        <h4>關鍵元素檢核：</h4>
        <ul>
          <li
            v-for="(kw, i) in requiredKeywords"
            :key="i"
            :class="hasKeyword(kw) ? 'kw-hit' : 'kw-miss'"
          >
            <span>{{ hasKeyword(kw) ? '✅' : '❌' }}</span>
            包含「<strong>{{ kw }}</strong>」相關內容
          </li>
          <li :class="lengthOk ? 'kw-hit' : 'kw-miss'">
            <span>{{ lengthOk ? '✅' : '❌' }}</span>
            提示長度達到 {{ minLength }} 字以上
            <span class="char-count">（目前：{{ userInput.trim().length }} 字）</span>
          </li>
        </ul>
      </div>

      <div v-if="score < maxScore" class="rewrite-tip">
        <strong>💡 提示</strong>：沒涵蓋到的元素，試著在你的提示中加入背景說明、具體限制、範例或格式要求。
      </div>

      <button class="sample-toggle-btn" @click="showSample = !showSample">
        {{ showSample ? '▲ 收起參考答案' : '▼ 查看參考答案' }}
      </button>
      <div v-if="showSample" class="sample-answer">
        <strong>參考答案：</strong>
        <blockquote>{{ sampleAnswer }}</blockquote>
        <p class="sample-note">
          ※ 這只是一種可能的寫法，只要你的提示包含足夠的脈絡與限制，都算是好提示。
        </p>
      </div>
    </div>

    <p class="disclaimer-note">
      ⚙️ 此工具為純前端關鍵字偵測，不呼叫任何 AI——是你自我評估的鏡子，不是 AI 評分。
    </p>
  </div>
</template>
