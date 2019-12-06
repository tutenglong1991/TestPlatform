import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import apiAutoTest from '@/components/apiAutoTest'
import projectManage from '@/components/projectManage/projectManage'
import projectMembers from '@/components/projectManage/projectMembers'
import apiList from '@/components/apiManage/apiList'
import apiAddPage from '@/components/apiManage/apiAddPage'
import apiGroup from '@/components/apiManage/apiGroup'
import apiDetail from '@/components/apiManage/apiDetail'
import apiRunLog from '@/components/apiManage/apiRunLog'
import caseList from '@/components/caseManage/caseList'
import caseDetail from '@/components/caseManage/caseDetail'
import taskList from '@/components/taskManage/taskList'
import taskRunLog from '@/components/taskManage/taskRunLog'
import programList from '@/components/programManage/programList'
import programDetail from '@/components/programManage/programDetail'
import reportList from '@/components/reportManage/reportList'
import reportDetail from '@/components/reportManage/reportDetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/apiAuto/apiFunc',
      name: 'apiAutoTest',
      component: apiAutoTest,
      children: [{
        path: '/apiAutoTest/projectList',
        name: 'projectManage',
        component: projectManage
      },
      {
        path: '/apiAutoTest/projectMembers',
        name: 'projectMembers',
        component: projectMembers
      },
      {
        path: '/apiAutoTest/apiList',
        name: 'apiList',
        component: apiList
      },
      {
        path: '/apiAutoTest/apiAddPage',
        name: 'apiAddPage',
        component: apiAddPage
      },
      {
        path: '/apiAutoTest/apiGroup',
        name: 'apiGroup',
        component: apiGroup
      },
      {
        path: '/apiAutoTest/apiDetail',
        name: 'apiDetail',
        component: apiDetail
      },
      {
        path: '/apiAutoTest/apiRunLog',
        name: 'apiRunLog',
        component: apiRunLog
      },
      {
        path: '/apiAutoTest/caseList',
        name: 'caseList',
        component: caseList
      },
      {
        path: '/apiAutoTest/caseDetail',
        name: 'caseDetail',
        component: caseDetail
      },
      {
        path: '/apiAutoTest/taskList',
        name: 'taskList',
        component: taskList
      },
      {
        path: '/apiAutoTest/taskRunLog',
        name: 'taskRunLog',
        component: taskRunLog
      },
      {
        path: '/apiAutoTest/programDetail',
        name: 'programDetail',
        component: programDetail
      },
      {
        path: '/apiAutoTest/programList',
        name: 'programList',
        component: programList
      },
      {
        path: '/apiAutoTest/reportList',
        name: 'reportList',
        component: reportList
      },
      {
        path: '/apiAutoTest/reportDetail',
        name: 'reportDetail',
        component: reportDetail
      }]
    }]
})
