<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  leftItems:    { type: Array, required: true },   // [{id, text}]
  rightItems:   { type: Array, required: true },   // [{id, text}]
  correctPairs: { type: Array, required: true },   // [[leftId, rightId], ...]
  explanation:  { type: String, required: true }
})

// 目前選中的左側 id
const selectedLeft  = ref(null)
// 使用者配對結果：{ leftId: rightId }
const pairs         = ref({})
const submitted     = ref(false)

function clickLeft(id) {
  if (submitted.value) return
  selectedLeft.value = selectedLeft.value === id ? null : id
}

function clickRight(id) {
  if (submitted.value || selectedLeft.value === null) return
  // 若右側已被配對，先解除舊配對
  const existingLeft = Object.keys(pairs.value).find(k => pairs.value[k] === id)
  if (existingLeft) delete pairs.value[existingLeft]
  pairs.value[selectedLeft.value] = id
  selectedLeft.value = null
}

function removePair(leftId) {
  if (submitted.value) return
  delete pairs.value[leftId]
}

const allPaired = computed(() =>
  props.leftItems.every(l => pairs.value[l.id] !== undefined)
)

function submit() {
  if (!allPaired.value) return
  submitted.value = true
}

function reset() {
  pairs.value       = {}
  selectedLeft.value = null
  submitted.value   = false
}

// 正確對照表：leftId → rightId
const correctMap = computed(() => {
  const m = {}
  for (const [l, r] of props.correctPairs) m[l] = r
  return m
})

function isPairCorrect(leftId) {
  return pairs.value[leftId] === correctMap.value[leftId]
}

const allCorrect = computed(() =>
  submitted.value && props.leftItems.every(l => isPairCorrect(l.id))
)

function rightTextById(id) {
  return props.rightItems.find(r => r.id === id)?.text ?? ''
}

function leftStatus(id) {
  if (!submitted.value) return selectedLeft.value === id ? 'selected' : ''
  return isPairCorrect(id) ? 'correct' : 'wrong'
}
</script>

<template>
  <div class="practice-card">
    <p class="quiz-hint" v-if="!submitted">
      點選左側項目，再點右側項目完成配對。點擊已配對的左側項目可取消。
    </p>

    <div class="matching-grid">
      <!-- 左側 -->
      <div class="matching-col">
        <div
          v-for="item in leftItems"
          :key="item.id"
          class="matching-item left-item"
          :class="[leftStatus(item.id), { paired: pairs[item.id] !== undefined }]"
          @click="clickLeft(item.id)"
        >
          <span class="match-marker">
            <template v-if="submitted">
              {{ isPairCorrect(item.id) ? '✅' : '❌' }}
            </template>
            <template v-else-if="selectedLeft === item.id">◉</template>
            <template v-else-if="pairs[item.id] !== undefined">✔</template>
            <template v-else>○</template>
          </span>
          {{ item.text }}
        </div>
      </div>

      <!-- 右側 -->
      <div class="matching-col">
        <div
          v-for="item in rightItems"
          :key="item.id"
          class="matching-item right-item"
          :class="{
            highlighted: selectedLeft !== null,
            matched: Object.values(pairs).includes(item.id) && !submitted
          }"
          @click="clickRight(item.id)"
        >
          {{ item.text }}
        </div>
      </div>
    </div>

    <!-- 已配對預覽 -->
    <div v-if="Object.keys(pairs).length > 0 && !submitted" class="pairs-preview">
      <p class="pairs-title">目前配對：</p>
      <div
        v-for="(rightId, leftId) in pairs"
        :key="leftId"
        class="pair-row"
      >
        <span>{{ leftItems.find(l => l.id == leftId)?.text }}</span>
        <span class="pair-arrow">→</span>
        <span>{{ rightTextById(rightId) }}</span>
        <button class="remove-pair" @click="removePair(leftId)">✕</button>
      </div>
    </div>

    <div class="quiz-actions">
      <button
        v-if="!submitted"
        class="practice-btn"
        :disabled="!allPaired"
        @click="submit"
      >
        檢查配對
      </button>
      <button v-else class="practice-btn secondary" @click="reset">
        再試一次
      </button>
    </div>

    <div
      v-if="submitted"
      class="practice-feedback"
      :class="allCorrect ? 'correct-feedback' : 'wrong-feedback'"
    >
      <strong>{{ allCorrect ? '✅ 全部正確！' : '💭 有配對需要修正…' }}</strong>

      <!-- 正確答案對照 -->
      <div v-if="!allCorrect" class="correct-pairs-list">
        <p><strong>正確配對：</strong></p>
        <div
          v-for="[leftId, rightId] in correctPairs"
          :key="leftId"
          class="pair-row correct-pair"
        >
          <span>{{ leftItems.find(l => l.id === leftId)?.text }}</span>
          <span class="pair-arrow">→</span>
          <span>{{ rightTextById(rightId) }}</span>
        </div>
      </div>

      <p>{{ explanation }}</p>
    </div>
  </div>
</template>
