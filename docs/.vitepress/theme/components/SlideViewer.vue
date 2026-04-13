<template>
  <div
    ref="viewerEl"
    class="slide-viewer"
    tabindex="0"
    @keydown="onKey"
  >
    <!-- 工具列：上一頁、頁碼、下一頁、全螢幕 -->
    <div class="slide-viewer-toolbar">
      <button
        class="slide-viewer-btn"
        @click="prev"
        :disabled="current === 0"
        aria-label="上一頁"
      >◀</button>
      <span class="slide-viewer-counter">{{ current + 1 }} / {{ slides.length }}</span>
      <button
        class="slide-viewer-btn"
        @click="next"
        :disabled="current === slides.length - 1"
        aria-label="下一頁"
      >▶</button>
      <button
        class="slide-viewer-btn slide-viewer-fs"
        @click="toggleFullscreen"
        :aria-label="isFullscreen ? '退出全螢幕' : '全螢幕'"
        :title="isFullscreen ? '退出全螢幕（Esc）' : '全螢幕'"
      >{{ isFullscreen ? '✕' : '⛶' }}</button>
    </div>

    <!-- 主圖區 -->
    <div class="slide-viewer-stage" @click="toggleFullscreen">
      <img
        v-for="(s, i) in slides"
        :key="i"
        :src="s.src"
        :alt="s.caption"
        class="slide-viewer-image"
        :class="{ active: i === current }"
        loading="lazy"
        draggable="false"
      />
    </div>

    <!-- 說明文字 -->
    <div class="slide-viewer-caption">{{ slides[current].caption }}</div>

    <!-- 縮圖列 -->
    <div class="slide-viewer-thumbs" ref="thumbsEl">
      <button
        v-for="(s, i) in slides"
        :key="i"
        class="slide-viewer-thumb"
        :class="{ active: i === current }"
        @click="goTo(i)"
        :aria-label="`第 ${i + 1} 頁`"
        :title="s.caption"
      >
        <img :src="s.src" :alt="`縮圖 ${i + 1}`" loading="lazy" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'

interface Slide {
  src: string
  caption: string
}

const props = defineProps<{
  slides: Slide[]
  title?: string
}>()

const current = ref(0)
const viewerEl = ref<HTMLElement>()
const thumbsEl = ref<HTMLElement>()
const isFullscreen = ref(false)

function prev() {
  if (current.value > 0) current.value--
}

function next() {
  if (current.value < props.slides.length - 1) current.value++
}

function goTo(i: number) {
  current.value = i
}

// 切換頁面時把對應縮圖捲入視野
watch(current, async (i) => {
  await nextTick()
  const thumbs = thumbsEl.value
  if (!thumbs) return
  const thumb = thumbs.children[i] as HTMLElement | undefined
  if (thumb) thumb.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' })
})

async function toggleFullscreen() {
  if (!viewerEl.value) return
  if (!document.fullscreenElement) {
    await viewerEl.value.requestFullscreen()
  } else {
    await document.exitFullscreen()
  }
}

function onFullscreenChange() {
  isFullscreen.value = !!document.fullscreenElement
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'ArrowLeft') { e.preventDefault(); prev() }
  else if (e.key === 'ArrowRight') { e.preventDefault(); next() }
  else if (e.key === 'Escape' && isFullscreen.value) document.exitFullscreen()
}

onMounted(() => {
  document.addEventListener('fullscreenchange', onFullscreenChange)
})

onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', onFullscreenChange)
})
</script>

<style scoped>
.slide-viewer {
  max-width: 960px;
  margin: 24px auto;
  padding: 16px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  outline: none;
}
:global(.dark) .slide-viewer {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

/* 全螢幕模式 */
.slide-viewer:fullscreen {
  max-width: 100vw;
  height: 100vh;
  border-radius: 0;
  background: #000;
  display: flex;
  flex-direction: column;
  padding: 12px;
  box-shadow: none;
}
.slide-viewer:fullscreen .slide-viewer-stage {
  flex: 1;
  background: #000;
  min-height: unset;
}
.slide-viewer:fullscreen .slide-viewer-image.active {
  max-height: calc(100vh - 180px);
}

/* 工具列 */
.slide-viewer-toolbar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 12px;
}
.slide-viewer-btn {
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 6px 12px;
  cursor: pointer;
  font-size: 14px;
  color: var(--vp-c-text-1);
  transition: background 0.15s;
  line-height: 1;
}
.slide-viewer-btn:hover:not(:disabled) {
  background: var(--vp-c-brand-soft);
}
.slide-viewer-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}
.slide-viewer-counter {
  font-variant-numeric: tabular-nums;
  color: var(--vp-c-text-2);
  font-size: 14px;
  min-width: 64px;
  text-align: center;
}
.slide-viewer-fs {
  margin-left: auto;
  font-size: 16px;
  padding: 4px 10px;
}

/* 主圖區 */
.slide-viewer-stage {
  background: var(--vp-c-bg);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  overflow: hidden;
  cursor: pointer;
}
.slide-viewer-image {
  display: none;
  max-width: 100%;
  max-height: 68vh;
  object-fit: contain;
  user-select: none;
}
.slide-viewer-image.active {
  display: block;
}

/* 說明文字 */
.slide-viewer-caption {
  margin-top: 12px;
  padding: 12px 16px;
  background: var(--vp-c-bg);
  border-left: 4px solid var(--vp-c-brand-1);
  border-radius: 6px;
  color: var(--vp-c-text-1);
  font-size: 14px;
  line-height: 1.65;
}

/* 縮圖列 */
.slide-viewer-thumbs {
  display: flex;
  gap: 6px;
  margin-top: 12px;
  overflow-x: auto;
  padding-bottom: 4px;
  scrollbar-width: thin;
}
.slide-viewer-thumb {
  flex: 0 0 76px;
  height: 48px;
  padding: 0;
  border: 2px solid transparent;
  border-radius: 4px;
  cursor: pointer;
  background: var(--vp-c-bg);
  overflow: hidden;
  transition: border-color 0.15s;
}
.slide-viewer-thumb.active {
  border-color: var(--vp-c-brand-1);
}
.slide-viewer-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
</style>
