import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import Login from '@/components/Login'
import apiAutotest from '@/components/apiAutotest'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'HomePage',
      component: HomePage,
      children: [{
        path: '/home/apitest',
        name: 'apiAutotest',
        component: apiAutotest
      }],
      meta: {
        is_login: false
      }
    },
    {
      path: '/home/apitest',
      name: 'apiAutotest',
      component: apiAutotest
    }
  ]
})
