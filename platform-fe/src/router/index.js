import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import Login from '@/components/Login'
import apiAutotest from '@/components/apiAutotest'
import projectManage from '@/components/projectManage'
import projectMembers from '@/components/projectMembers'
import apiList from '@/components/apiList'
import apiGroup from '@/components/apiGroup'
import apiDetail from '@/components/apiDetail'

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
          path: '/home/apitest/projectHomePage',
          name: 'projectManage',
          component: projectManage
        },
        {
          path: '/home/apitest/projectMembers',
          name: 'projectMembers',
          component: projectMembers
        },
        {
          path: 'home/apitest/apiList',
          name: 'apiList',
          component: apiList
        },
        {
          path: 'home/apitest/apiDetail',
          name: 'apiDetail',
          component: apiDetail
        },
        {
          path: 'home/apitest/apiGroup',
          name: 'apiGroup',
          component: apiGroup
        }
        ]
      }]
    }
  ]
})
