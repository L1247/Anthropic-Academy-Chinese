<template>
  <Teleport v-if="isMounted" to="body">
    <div v-if="isOpen" class="mermaid-lb-overlay" @wheel.prevent="onWheel">
      <!-- 點擊背景關閉 -->
      <div class="mermaid-lb-bg" @click="close" />

      <!-- SVG 顯示容器，transform-origin: 0 0 配合 translate + scale 實現正確的滑鼠中心縮放 -->
      <div
        ref="contentRef"
        class="mermaid-lb-content"
        :class="{ 'is-dragging': isDragging }"
        :style="panStyle"
        @mousedown="startDrag"
      />

      <button class="mermaid-lb-close" @click.stop="close" aria-label="關閉">✕</button>
      <div class="mermaid-lb-hint">滾輪縮放 · 拖曳移動 · ESC 關閉</div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRoute } from 'vitepress'

// SSR 安全：確保只在 client 端渲染 Teleport
const isMounted = ref(false)

const isOpen = ref(false)
const scale = ref(1)
const translateX = ref(0)
const translateY = ref(0)
const isDragging = ref(false)
const dragStartX = ref(0)
const dragStartY = ref(0)
const contentRef = ref<HTMLElement | null>(null)

// transform-origin: 0 0，所以 translate 是絕對像素偏移
const panStyle = computed(() => ({
  transform: `translate(${translateX.value}px, ${translateY.value}px) scale(${scale.value})`,
}))

async function open(mermaidEl: HTMLElement) {
  const svg = mermaidEl.querySelector('svg')
  if (!svg) return

  // 取得 SVG 的實際渲染尺寸
  const rect = svg.getBoundingClientRect()
  const svgW = rect.width || parseFloat(svg.getAttribute('width') ?? '0') || 800
  const svgH = rect.height || parseFloat(svg.getAttribute('height') ?? '0') || 600

  isOpen.value = true
  scale.value = 1
  isDragging.value = false

  // 初始位置：置中於視窗
  translateX.value = (window.innerWidth - svgW) / 2
  translateY.value = (window.innerHeight - svgH) / 2

  await nextTick()

  const container = contentRef.value
  if (!container) return

  container.innerHTML = ''

  const cloned = svg.cloneNode(true) as SVGElement
  // 保留 viewBox，設定明確尺寸讓 SVG 以自然大小顯示
  cloned.setAttribute('width', String(svgW))
  cloned.setAttribute('height', String(svgH))
  cloned.style.cssText = 'display: block; max-width: none !important;'
  container.appendChild(cloned)
}

function close() {
  isOpen.value = false
  isDragging.value = false
  if (contentRef.value) contentRef.value.innerHTML = ''
  removeWindowListeners()
}

// 滾輪縮放：以滑鼠位置為縮放中心
function onWheel(event: WheelEvent) {
  const oldScale = scale.value
  const factor = event.deltaY < 0 ? 1.1 : 0.9
  const newScale = Math.min(8, Math.max(0.15, oldScale * factor))

  // 保持滑鼠游標下的點不動
  const mx = event.clientX
  const my = event.clientY
  translateX.value = mx - (mx - translateX.value) * (newScale / oldScale)
  translateY.value = my - (my - translateY.value) * (newScale / oldScale)

  scale.value = newScale
}

// 拖曳平移
function startDrag(event: MouseEvent) {
  if (event.button !== 0) return
  event.preventDefault()
  isDragging.value = true
  dragStartX.value = event.clientX - translateX.value
  dragStartY.value = event.clientY - translateY.value
  window.addEventListener('mousemove', onDragMove)
  window.addEventListener('mouseup', stopDrag)
}

function onDragMove(event: MouseEvent) {
  if (!isDragging.value) return
  translateX.value = event.clientX - dragStartX.value
  translateY.value = event.clientY - dragStartY.value
}

function stopDrag() {
  isDragging.value = false
  removeWindowListeners()
}

function removeWindowListeners() {
  window.removeEventListener('mousemove', onDragMove)
  window.removeEventListener('mouseup', stopDrag)
}

function onKeyDown(event: KeyboardEvent) {
  if (event.key === 'Escape' && isOpen.value) close()
}

// MutationObserver：偵測 .mermaid 容器中的 SVG 渲染完成後綁定點擊
let observer: MutationObserver | null = null

/**
 * 修正 Mermaid 節點高度：Mermaid 量測時 VitePress 的 line-height 可能導致
 * 實際渲染高度比量測值高，foreignObject 截斷文字。
 * 用 scrollHeight 取得真實內容高度，同步調整 foreignObject 與背景 rect。
 */
function fixNodeHeights(mermaidEl: HTMLElement) {
  requestAnimationFrame(() => {
    mermaidEl.querySelectorAll<SVGForeignObjectElement>('foreignObject').forEach((fo) => {
      const inner = fo.querySelector<HTMLElement>('.nodeLabel') ?? fo.querySelector<HTMLElement>('div')
      if (!inner) return

      const foH = parseFloat(fo.getAttribute('height') ?? '0')
      if (!foH) return

      // scrollHeight 回傳完整內容高度（不受 overflow 裁切影響）
      const contentH = inner.scrollHeight
      if (contentH <= foH + 2) return // 在容差內，無需調整

      const extra = contentH - foH + 10 // 10px 緩衝
      fo.setAttribute('height', String(foH + extra))

      // 同步擴展背景 rect（維持垂直置中）
      const nodeGroup = fo.closest<SVGGElement>('.node')
      if (!nodeGroup) return
      const rect = nodeGroup.querySelector<SVGRectElement>('rect')
      if (!rect) return
      const rh = parseFloat(rect.getAttribute('height') ?? '0')
      const ry = parseFloat(rect.getAttribute('y') ?? '0')
      rect.setAttribute('height', String(rh + extra))
      rect.setAttribute('y', String(ry - extra / 2))
    })
  })
}

function bindMermaidClicks() {
  document.querySelectorAll<HTMLElement>('.mermaid:not([data-lb-bound])').forEach((el) => {
    // 等 SVG 真正渲染後再綁定
    if (!el.querySelector('svg')) return
    el.setAttribute('data-lb-bound', '1')
    el.addEventListener('click', () => open(el))
    fixNodeHeights(el)
  })
}

const route = useRoute()
let currentPath = ''

onMounted(() => {
  isMounted.value = true
  currentPath = route.path

  // 延遲初始綁定，等 Mermaid 渲染完成
  setTimeout(bindMermaidClicks, 200)

  observer = new MutationObserver(() => {
    bindMermaidClicks()
    // 路由切換時關閉燈箱
    if (route.path !== currentPath) {
      currentPath = route.path
      if (isOpen.value) close()
    }
  })

  observer.observe(document.body, { childList: true, subtree: true })
  window.addEventListener('keydown', onKeyDown)
})

onUnmounted(() => {
  observer?.disconnect()
  window.removeEventListener('keydown', onKeyDown)
  removeWindowListeners()
})
</script>

<style scoped>
.mermaid-lb-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  overflow: hidden;
  user-select: none;
}

/* 半透明背景，點擊可關閉 */
.mermaid-lb-bg {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.82);
  cursor: default;
}

/* SVG 容器：transform-origin 設 0 0，配合 translate + scale 實現正確縮放中心 */
.mermaid-lb-content {
  position: absolute;
  top: 0;
  left: 0;
  transform-origin: 0 0;
  cursor: grab;
  z-index: 1;
}

.mermaid-lb-content.is-dragging {
  cursor: grabbing;
}

/* 確保 SVG 完整顯示 */
.mermaid-lb-content :deep(svg) {
  display: block;
  max-width: none !important;
}

/* 關閉按鈕 */
.mermaid-lb-close {
  position: fixed;
  top: 16px;
  right: 20px;
  z-index: 10000;
  background: rgba(255, 255, 255, 0.92);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  transition: background 0.15s;
}

.mermaid-lb-close:hover {
  background: #fff;
}

/* 底部操作提示 */
.mermaid-lb-hint {
  position: fixed;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: rgba(255, 255, 255, 0.85);
  font-size: 12px;
  padding: 4px 14px;
  border-radius: 20px;
  pointer-events: none;
  z-index: 10000;
  white-space: nowrap;
}
</style>
