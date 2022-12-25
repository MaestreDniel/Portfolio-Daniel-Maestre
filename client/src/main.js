import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import i18n from './locales'
// import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import '@/assets/scss/app.scss'

createApp(App).use(i18n).use(router).mount('#app')
