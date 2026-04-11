import DefaultTheme from 'vitepress/theme'
import './custom.css'
import Quiz from './components/Quiz.vue'
import DelegationChecklist from './components/DelegationChecklist.vue'
import PromptRewrite from './components/PromptRewrite.vue'
import DiligenceBuilder from './components/DiligenceBuilder.vue'
import MatchingPairs from './components/MatchingPairs.vue'
import RankingExercise from './components/RankingExercise.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
    app.component('DelegationChecklist', DelegationChecklist)
    app.component('PromptRewrite', PromptRewrite)
    app.component('DiligenceBuilder', DiligenceBuilder)
    app.component('MatchingPairs', MatchingPairs)
    app.component('RankingExercise', RankingExercise)
  }
}
