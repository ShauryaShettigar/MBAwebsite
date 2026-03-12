import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/why-us',
      name: 'why-us',
      component: () => import('../views/WhyUsView.vue'),
    },
    {
      path: '/program',
      name: 'program',
      component: () => import('../views/ProgramView.vue'),
    },
    {
      path: '/learning-model',
      name: 'learning-model',
      component: () => import('../views/LearningModelView.vue'),
    },
    {
      path: '/industry',
      name: 'industry',
      component: () => import('../views/IndustryView.vue'),
    },
    {
      path: '/careers',
      name: 'careers',
      component: () => import('../views/CareersView.vue'),
    },
    {
      path: '/insights',
      name: 'insights',
      component: () => import('../views/InsightsView.vue'),
    },
    {
      path: '/admissions',
      name: 'admissions',
      component: () => import('../views/AdmissionsView.vue'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
    },
  ],
  scrollBehavior(to, _from, savedPosition) {
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0, behavior: 'smooth' }
  },
})

export default router
