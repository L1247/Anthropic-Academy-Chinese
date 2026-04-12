<template>
  <div ref="badgeEl" class="role-badge typewriter-badge">
    <span>{{ displayText }}</span><span
      class="typewriter-cursor"
      :class="{ 'typewriter-cursor--done': isDone }"
    >|</span>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  text: {
    type: String,
    default: '✨ 推薦所有人從這裡開始'
  },
  delay: {
    type: Number,
    default: 300
  },
  speed: {
    type: Number,
    default: 90
  }
})

const badgeEl = ref<HTMLElement | null>(null)
const displayText = ref('')
const isDone = ref(false)

let intervalId: ReturnType<typeof setInterval> | null = null
let timeoutId: ReturnType<typeof setTimeout> | null = null
let observer: IntersectionObserver | null = null

const chars = [...props.text]

function reset() {
  if (intervalId) { clearInterval(intervalId); intervalId = null }
  if (timeoutId) { clearTimeout(timeoutId); timeoutId = null }
  displayText.value = ''
  isDone.value = false
}

function play() {
  reset()
  let i = 0
  timeoutId = setTimeout(() => {
    intervalId = setInterval(() => {
      if (i < chars.length) {
        displayText.value += chars[i]
        i++
      } else {
        clearInterval(intervalId!)
        intervalId = null
        isDone.value = true
      }
    }, props.speed)
  }, props.delay)
}

onMounted(() => {
  if (!badgeEl.value) return

  observer = new IntersectionObserver(
    (entries) => {
      const entry = entries[0]
      if (entry.isIntersecting) {
        play()
      } else {
        // 離開視窗後重置，下次捲回來重新播放
        reset()
      }
    },
    { threshold: 0.5 }
  )

  observer.observe(badgeEl.value)
})

onUnmounted(() => {
  reset()
  observer?.disconnect()
})
</script>
