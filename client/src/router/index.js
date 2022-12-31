import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import ProjectView from '../views/ProjectView.vue'
import Error404 from '@/views/404.vue'

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/projects/:slug',
    name: 'project',
    component: ProjectView
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Error404',
    component: Error404,
  } 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})  

// router.onError(window.location = '/');

export default router
