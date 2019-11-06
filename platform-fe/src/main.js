// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import '../static/css/base.css'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$axios = axios

/* eslint-disable no-new */
/* eslint-disable no-new */
if (navigator.userAgent.indexOf('Trident') > -1) {
  alert('请使用chrome访问本站点！')
} else {
  new Vue({
    el: '#app',
    components: {
      App
    },
    template: '<App/>',
    router: router
  })
}

// router.beforeEach((to, form, next) => {
//   if (to.meta.is_login) {
//     if (localStorage.getItem('user')) {
//       next()
//     } else {
//       next(
//         {
//           path: '/'
//         }
//       )
//     }
//   } else {
//     next()
//   }
// })
