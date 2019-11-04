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
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

router.beforeEach((to, form, next) => {
  if (to.meta.is_login) {
    if (localStorage.getItem('user')) {
      next()
    } else {
      next(
        {
          path: '/'
        }
      )
    }
  } else {
    next()
  }
})
