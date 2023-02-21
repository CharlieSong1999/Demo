import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import './assets/css/reset.less'
import router from './router'
import {createPinia} from 'pinia'

const store = createPinia()
const app = createApp(App).use(ElementPlus).use(router).use(store).mount('#app')

