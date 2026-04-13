<script setup lang="ts">
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const props = withDefaults(defineProps<{
  src: string
  poster: string
  zhVtt: string
  enVtt?: string
  biVtt?: string
  defaultMode?: 'off' | 'zh' | 'en' | 'bi'
}>(), {
  defaultMode: 'zh'
})

type Mode = 'off' | 'zh' | 'en' | 'bi'

const videoEl = ref<HTMLVideoElement | null>(null)
const wrapperEl = ref<HTMLDivElement | null>(null)

const isPlaying = ref(false)
const currentTime = ref(0)
const duration = ref(0)
const isMuted = ref(false)
const volume = ref(1)
const isFullscreen = ref(false)
const controlsVisible = ref(true)
const currentCueLines = ref<string[]>([])

const subtitleMode = ref<Mode>(props.defaultMode)

let hideTimer: ReturnType<typeof setTimeout> | null = null
let activeTrack: TextTrack | null = null

// ── 字幕循環序列（依 props 動態組成）──────────────────
const cycle = computed<Mode[]>(() => {
  const seq: Mode[] = ['off', 'zh']
  if (props.enVtt) seq.push('en')
  if (props.biVtt) seq.push('bi')
  return seq
})

const ccLabel = computed(() => {
  switch (subtitleMode.value) {
    case 'zh': return '繁中'
    case 'en': return 'EN'
    case 'bi': return '中英'
    default: return '關'
  }
})

const captionsActive = computed(() => subtitleMode.value !== 'off')

// ── cuechange：讀取當前字幕行 ─────────────────────────
function onCueChange(e: Event) {
  const track = e.target as TextTrack
  if (track.activeCues && track.activeCues.length > 0) {
    const cue = track.activeCues[0] as VTTCue
    // 去除 VTT inline 標籤（<c>、<b>、<i> 等），保留純文字
    const plain = cue.text.replace(/<[^>]*>/g, '')
    currentCueLines.value = plain.split('\n').filter(Boolean)
  } else {
    currentCueLines.value = []
  }
}

// ── 字幕模式應用 ───────────────────────────────────────
function applyMode(mode: Mode) {
  const v = videoEl.value
  if (!v) return
  const tracks = v.textTracks

  // 移除舊監聽、全部停用
  if (activeTrack) {
    activeTrack.removeEventListener('cuechange', onCueChange)
    activeTrack = null
  }
  for (let i = 0; i < tracks.length; i++) {
    tracks[i].mode = 'disabled'
  }
  currentCueLines.value = []

  if (mode === 'off') return

  const target = mode === 'zh' ? '繁中' : mode === 'en' ? 'English' : '中英雙語'
  for (let i = 0; i < tracks.length; i++) {
    if (tracks[i].label === target) {
      // 'hidden'：瀏覽器載入並觸發 cuechange，但不顯示原生字幕疊層
      tracks[i].mode = 'hidden'
      tracks[i].addEventListener('cuechange', onCueChange)
      activeTrack = tracks[i]
      break
    }
  }
}

function cycleSubtitle() {
  const seq = cycle.value
  const idx = seq.indexOf(subtitleMode.value)
  subtitleMode.value = seq[(idx + 1) % seq.length]
}

watch(subtitleMode, applyMode, { flush: 'post' })

// ── 播放控制 ───────────────────────────────────────────
function togglePlay() {
  const v = videoEl.value!
  if (v.paused) {
    v.play()
    isPlaying.value = true
  } else {
    v.pause()
    isPlaying.value = false
  }
}

function onTimeUpdate() {
  currentTime.value = videoEl.value!.currentTime
}

function onLoadedMetadata() {
  duration.value = videoEl.value!.duration
  applyMode(subtitleMode.value)
}

function onEnded() {
  isPlaying.value = false
  controlsVisible.value = true
}

function onSeekInput(e: Event) {
  const t = parseFloat((e.target as HTMLInputElement).value)
  videoEl.value!.currentTime = t
  currentTime.value = t
}

// ── 音量控制 ───────────────────────────────────────────
function toggleMute() {
  const v = videoEl.value!
  v.muted = !v.muted
  isMuted.value = v.muted
}

function onVolumeInput(e: Event) {
  const val = parseFloat((e.target as HTMLInputElement).value)
  volume.value = val
  const v = videoEl.value!
  v.volume = val
  v.muted = val === 0
  isMuted.value = v.muted
}

// ── 全螢幕 ─────────────────────────────────────────────
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    wrapperEl.value!.requestFullscreen()
  } else {
    document.exitFullscreen()
  }
}

function onFullscreenChange() {
  isFullscreen.value = !!document.fullscreenElement
}

// ── 控制列自動隱藏 ─────────────────────────────────────
function showControls() {
  controlsVisible.value = true
  if (hideTimer) clearTimeout(hideTimer)
  if (isPlaying.value) {
    hideTimer = setTimeout(() => { controlsVisible.value = false }, 2500)
  }
}

function scheduleHideControls() {
  if (hideTimer) clearTimeout(hideTimer)
  if (isPlaying.value) {
    hideTimer = setTimeout(() => { controlsVisible.value = false }, 800)
  }
}

// ── 工具函式 ───────────────────────────────────────────
function fmtTime(s: number): string {
  if (!s || isNaN(s)) return '0:00'
  const m = Math.floor(s / 60)
  const sec = Math.floor(s % 60)
  return `${m}:${sec.toString().padStart(2, '0')}`
}

// ── 生命週期 ───────────────────────────────────────────
onMounted(() => {
  document.addEventListener('fullscreenchange', onFullscreenChange)
  applyMode(subtitleMode.value)
})

onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', onFullscreenChange)
  if (hideTimer) clearTimeout(hideTimer)
  if (activeTrack) {
    activeTrack.removeEventListener('cuechange', onCueChange)
  }
})
</script>

<template>
  <div
    ref="wrapperEl"
    class="nlm-wrapper"
    :class="{ 'nlm-fullscreen': isFullscreen }"
    @mousemove="showControls"
    @mouseleave="scheduleHideControls"
    @touchstart.passive="showControls"
  >
    <!-- 影片本體（無 controls，字幕由下方自訂區塊顯示） -->
    <video
      ref="videoEl"
      class="nlm-video-el"
      :src="src"
      :poster="poster"
      preload="metadata"
      playsinline
      @timeupdate="onTimeUpdate"
      @loadedmetadata="onLoadedMetadata"
      @ended="onEnded"
      @click="togglePlay"
    >
      <!-- track 以 mode='hidden' 載入，由 cuechange 讀取文字，不渲染原生疊層 -->
      <track v-if="zhVtt" kind="subtitles" srclang="zh-Hant" label="繁中" :src="zhVtt">
      <track v-if="enVtt" kind="subtitles" srclang="en" label="English" :src="enVtt">
      <track v-if="biVtt" kind="subtitles" srclang="zh-Hant" label="中英雙語" :src="biVtt">
    </video>

    <!-- 中央播放圖示（暫停時顯示） -->
    <div v-if="!isPlaying" class="nlm-play-overlay" @click="togglePlay">
      <div class="nlm-play-icon">▶</div>
    </div>

    <!-- 字幕顯示區（影片下方、控制列上方，不遮擋畫面） -->
    <div
      class="nlm-caption-area"
      :class="{ 'captions-active': captionsActive }"
    >
      <div v-if="currentCueLines.length" class="nlm-caption">
        <span
          v-for="(line, i) in currentCueLines"
          :key="i"
          class="nlm-caption-line"
        >{{ line }}</span>
      </div>
    </div>

    <!-- 控制列 -->
    <div
      class="nlm-controls"
      :class="{ 'controls-visible': controlsVisible || !isPlaying }"
    >
      <!-- 進度條 -->
      <div class="nlm-seek-row">
        <input
          type="range"
          class="nlm-seek"
          min="0"
          :max="duration || 100"
          step="0.1"
          :value="currentTime"
          @input="onSeekInput"
        >
      </div>

      <!-- 按鈕列 -->
      <div class="nlm-btn-row">
        <!-- 播放 / 暫停 -->
        <button
          class="nlm-btn"
          :title="isPlaying ? '暫停' : '播放'"
          @click.stop="togglePlay"
        >
          <span class="nlm-btn-icon">{{ isPlaying ? '⏸' : '▶' }}</span>
        </button>

        <!-- 時間顯示 -->
        <span class="nlm-time">{{ fmtTime(currentTime) }} / {{ fmtTime(duration) }}</span>

        <!-- 彈性間距 -->
        <span class="nlm-spacer"></span>

        <!-- 靜音 -->
        <button
          class="nlm-btn"
          :title="isMuted ? '取消靜音' : '靜音'"
          @click.stop="toggleMute"
        >
          <span class="nlm-btn-icon">{{ isMuted ? '🔇' : '🔊' }}</span>
        </button>

        <!-- 音量滑桿 -->
        <input
          type="range"
          class="nlm-vol"
          min="0"
          max="1"
          step="0.05"
          :value="isMuted ? 0 : volume"
          @input="onVolumeInput"
        >

        <!-- 字幕按鈕（獨立，在全螢幕按鈕左邊） -->
        <button
          class="nlm-btn nlm-cc-btn"
          :class="{ 'nlm-cc-on': subtitleMode !== 'off' }"
          :title="'字幕：' + ccLabel + '（點擊切換）'"
          @click.stop="cycleSubtitle"
        >
          <span class="nlm-btn-icon">CC</span>
          <span v-if="subtitleMode !== 'off'" class="nlm-cc-badge">{{ ccLabel }}</span>
        </button>

        <!-- 全螢幕 -->
        <button
          class="nlm-btn nlm-fs-btn"
          :title="isFullscreen ? '退出全螢幕' : '全螢幕'"
          @click.stop="toggleFullscreen"
        >
          <span class="nlm-btn-icon">{{ isFullscreen ? '⊡' : '⛶' }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ── 外層 wrapper ───────────────────────────────────── */
.nlm-wrapper {
  position: relative;
  max-width: 860px;
  margin: 16px auto;
  border-radius: 12px;
  overflow: hidden;
  background: #000;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  user-select: none;
  cursor: default;
}

.dark .nlm-wrapper {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

.nlm-wrapper.nlm-fullscreen {
  max-width: 100%;
  width: 100%;
  height: 100%;
  border-radius: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
}

/* ── 影片本體 ─────────────────────────────────────────── */
.nlm-video-el {
  width: 100%;
  display: block;
  background: #000;
  cursor: pointer;
}

.nlm-fullscreen .nlm-video-el {
  flex: 1;
  min-height: 0;
  object-fit: contain;
}

/* ── 中央播放圖示（暫停時顯示） ─────────────────────── */
.nlm-play-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: transparent;
  /* 不干擾字幕區與控制列點擊 */
  pointer-events: none;
}

.nlm-play-overlay {
  pointer-events: auto;
}

.nlm-play-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.5);
  border: 2px solid rgba(255, 255, 255, 0.65);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #fff;
  padding-left: 4px;
  transition: transform 0.15s, background 0.15s;
}

.nlm-play-overlay:hover .nlm-play-icon {
  transform: scale(1.1);
  background: rgba(0, 0, 0, 0.7);
}

/* ── 字幕顯示區 ──────────────────────────────────────── */
.nlm-caption-area {
  background: var(--vp-c-bg-alt);
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease, padding 0.2s ease;
  padding: 0 16px;
}

.nlm-caption-area.captions-active {
  max-height: 80px;
  padding: 8px 16px;
}

.nlm-caption {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  min-height: 40px;
  justify-content: center;
}

.nlm-caption-line {
  font-size: 14px;
  line-height: 1.5;
  color: var(--vp-c-text-1);
  text-align: center;
  font-family: var(--vp-font-family-base);
}

/* ── 控制列 ───────────────────────────────────────────── */
.nlm-controls {
  background: var(--vp-c-bg-alt);
  padding: 6px 12px 8px;
  border-top: 1px solid var(--vp-c-divider);
  opacity: 0;
  transition: opacity 0.25s;
  pointer-events: none;
}

.nlm-controls.controls-visible {
  opacity: 1;
  pointer-events: auto;
}

/* ── 進度條 ───────────────────────────────────────────── */
.nlm-seek-row {
  display: flex;
  align-items: center;
  margin-bottom: 4px;
}

.nlm-seek {
  width: 100%;
  height: 4px;
  cursor: pointer;
  accent-color: var(--vp-c-brand-1);
  border-radius: 2px;
}

/* ── 按鈕列 ───────────────────────────────────────────── */
.nlm-btn-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nlm-spacer {
  flex: 1;
}

.nlm-time {
  font-size: 12px;
  font-family: var(--vp-font-family-mono);
  color: var(--vp-c-text-2);
  white-space: nowrap;
  min-width: 80px;
}

/* ── 通用按鈕 ─────────────────────────────────────────── */
.nlm-btn {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 4px 7px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 13px;
  line-height: 1;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s, color 0.15s;
  flex-shrink: 0;
}

.nlm-btn:hover {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.nlm-btn-icon {
  font-size: 13px;
  line-height: 1;
}

/* ── 音量滑桿 ─────────────────────────────────────────── */
.nlm-vol {
  width: 70px;
  height: 4px;
  cursor: pointer;
  accent-color: var(--vp-c-brand-1);
  flex-shrink: 0;
}

@media (max-width: 480px) {
  .nlm-vol {
    display: none;
  }
}

/* ── 字幕按鈕 ─────────────────────────────────────────── */
.nlm-cc-btn {
  font-weight: 600;
  letter-spacing: 0.03em;
}

.nlm-cc-btn.nlm-cc-on {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.nlm-cc-badge {
  font-size: 10px;
  font-weight: 700;
  background: var(--vp-c-brand-1);
  color: #fff;
  border-radius: 3px;
  padding: 1px 4px;
  line-height: 1.4;
}

/* ── 全螢幕模式 ───────────────────────────────────────── */
.nlm-fullscreen .nlm-caption-area {
  background: #1a1a1a;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.nlm-fullscreen .nlm-caption-line {
  color: #f0f0f0;
}

.nlm-fullscreen .nlm-controls {
  background: #1a1a1a;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.nlm-fullscreen .nlm-btn {
  border-color: rgba(255, 255, 255, 0.25);
  background: rgba(255, 255, 255, 0.08);
  color: #e0e0e0;
}

.nlm-fullscreen .nlm-btn:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.5);
  color: #fff;
}

.nlm-fullscreen .nlm-time {
  color: rgba(255, 255, 255, 0.7);
}

.nlm-fullscreen .nlm-cc-btn.nlm-cc-on {
  border-color: var(--vp-c-brand-light);
  color: var(--vp-c-brand-light);
  background: rgba(255, 255, 255, 0.12);
}
</style>
