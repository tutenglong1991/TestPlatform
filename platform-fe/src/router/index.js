import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import Login from '@/components/Login'
import apiAutotest from '@/components/apiAutotest'
import projectManage from '@/components/projectManage'

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
        component: apiAutotest,
        children: [{
          path: '/home/apitest/projectList',
          name: 'projectManage',
<<<<<<< HEAD
          component: projectManage,
          test: ''
=======
          component: projectManage
>>>>>>> 702cfa7486449bf4cd33f5c297ba2108cc3fc252
        }]
      }]
    }
  ]
})
