// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css' // 此项引入必须放在router前面，不然可能出现build打包编译后修改element-ui默认样式无效
import router from './router'
import axios from 'axios'
import '../static/css/base.css'

Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.prototype.$axios = axios

/* eslint-disable no-new */
/* eslint-disable no-new */
Vue.prototype.getProjectOptions = function () {
  let proResp = {}
  return this.$axios.get('/apiAutoTest/projectManage/projectList/find').then(response => {
    proResp = response.data
    return proResp
  }).catch(error => {
    console.log('系统错误' + error)
  })
}

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
