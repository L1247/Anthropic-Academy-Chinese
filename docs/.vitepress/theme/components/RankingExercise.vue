<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items:        { type: Array, required: true },  // Array<String>，初始（已打亂）顯示順序
  correctOrder: { type: Array, required: true },  // Array<Number>，正確順序中各項目在 items 的索引
  explanation:  { type: String, required: true }
})

// 初始打亂（使用 props.items 的原始順序，由頁面傳入時就已打亂）
const order = ref([...props.items.keys()])  // [0,1,2,...] 代表 items[index]
const submitted = ref(false)

function moveUp(pos) {
  if (pos === 0 || submitted.value) return
  const a = order.value[pos - 1]
  order.value[pos - 1] = order.value[pos]
  order.value[pos] = a
}

function moveDown(pos) {
  if (pos === order.value.length - 1 || submitted.value) return
  const a = order.value[pos + 1]
  order.value[pos + 1] = order.value[pos]
  order.value[pos] = a
}

function submit() {
  submitted.value = true
}

function reset() {
  order.value   = [...props.items.keys()]
  submitted.value = false
}

// 檢查每個位置是否正確
function isPositionCorrect(pos) {
  return order.value[pos] === props.correctOrder[pos]
}

const allCorrect = computed(() =>
  submitted.value && props.correctOrder.every((_, i) => isPositionCorrect(i))
)

const correctScore = computed(() =>
  props.correctOrder.filter((_, i) => isPositionCorrect(i)).length
)
</script>

<template>
  <div class="practice-card">
    <p class="quiz-hint" v-if="!submitted">
      使用「↑ 上移」和「↓ 下移」按鈕，調整到你認為正確的順序後點「確認順序」。
    </p>

    <div class="ranking-list">
      <div
        v-for="(itemIdx, pos) in order"
        :key="pos"
        class="ranking-item"
        :class="{
          'rank-correct': submitted && isPositionCorrect(pos),
          'rank-wrong':   submitted && !isPositionCorrect(pos)
        }"
      >
        <span class="rank-pos">{{ pos + 1 }}</span>
        <span class="rank-text">{{ items[itemIdx] }}</span>
        <div v-if="!submitted" class="rank-controls">
          <button
            class="rank-btn"
            :disabled="pos === 0"
            @click="moveUp(pos)"
          >↑ 上移</button>
          <button
            class="rank-btn"
            :disabled="pos === order.length - 1"
            @click="moveDown(pos)"
          >↓ 下移</button>
        </div>
        <span v-else class="rank-status">
          {{ isPositionCorrect(pos) ? '✅' : '❌' }}
        </span>
      </div>
    </div>

    <div class="quiz-actions">
      <button v-if="!submitted" class="practice-btn" @click="submit">
        確認順序
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
      <strong>
        {{ allCorrect
          ? '✅ 順序完全正確！'
          : `💭 答對 ${correctScore} / ${items.length} 個位置…` }}
      </strong>

      <div v-if="!allCorrect" class="correct-order-list">
        <p><strong>正確順序：</strong></p>
        <div
          v-for="(idx, pos) in correctOrder"
          :key="pos"
          class="pair-row"
        >
          <span class="rank-pos">{{ pos + 1 }}</span>
          <span>{{ items[idx] }}</span>
        </div>
      </div>

      <p>{{ explanation }}</p>
    </div>
  </div>
</template>
