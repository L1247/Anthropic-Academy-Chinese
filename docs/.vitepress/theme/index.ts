import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'
import Quiz from './components/Quiz.vue'
import DelegationChecklist from './components/DelegationChecklist.vue'
import PromptRewrite from './components/PromptRewrite.vue'
import DiligenceBuilder from './components/DiligenceBuilder.vue'
import MatchingPairs from './components/MatchingPairs.vue'
import RankingExercise from './components/RankingExercise.vue'
import MermaidLightbox from './components/MermaidLightbox.vue'
import HeroCertBadge from './components/HeroCertBadge.vue'
import TypewriterBadge from './components/TypewriterBadge.vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(MermaidLightbox),
      'home-hero-image': () => h(HeroCertBadge),
    })
  },
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('DelegationChecklist', DelegationChecklist)
    app.component('PromptRewrite', PromptRewrite)
    app.component('DiligenceBuilder', DiligenceBuilder)
    app.component('MatchingPairs', MatchingPairs)
    app.component('RankingExercise', RankingExercise)
    app.component('TypewriterBadge', TypewriterBadge)
  }
}
