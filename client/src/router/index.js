import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import('@/views/IndexView.vue')
  },
  {
    path: '/projects/:slug',
    name: 'project.show',
    component: () => import('@/views/ProjectView.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Error404',
    component: () => import('@/views/404.vue')
  } 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
