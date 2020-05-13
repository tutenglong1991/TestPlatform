import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import mainHeader from '@/components/mainHeader'
import projectManage from '@/components/projectManage/projectManage'
import projectMembers from '@/components/projectManage/projectMembers'
import apiList from '@/components/apiManage/apiList'
import apiAddPage from '@/components/apiManage/apiAddPage'
import commonConfig from '@/components/apiManage/commonConfig'
import updateRecord from '@/components/apiManage/updateRecord'
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
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/apiAuto/apiFunc',
      name: 'mainHeader',
      component: mainHeader,
      children: [{
        path: '/mainHeader/projectList',
        name: 'projectManage',
        component: projectManage
      },
      {
        path: '/mainHeader/projectMembers',
        name: 'projectMembers',
        component: projectMembers
      },
      {
        path: '/mainHeader/apiList',
        name: 'apiList',
        component: apiList
      },
      {
        path: '/mainHeader/apiAddPage',
        name: 'apiAddPage',
        component: apiAddPage
      },
      {
        path: '/mainHeader/updateRecord',
        name: 'updateRecord',
        component: updateRecord
      },
      {
        path: '/mainHeader/commonConfig',
        name: 'commonConfig',
        component: commonConfig
      },
      {
        path: '/mainHeader/apiDetail',
        name: 'apiDetail',
        component: () => import('@/components/apiManage/apiDetail.vue')
      },
      {
        path: '/mainHeader/apiRunLog',
        name: 'apiRunLog',
        component: apiRunLog
      },
      {
        path: '/mainHeader/caseList',
        name: 'caseList',
        component: caseList
      },
      {
        path: '/mainHeader/caseDetail',
        name: 'caseDetail',
        component: caseDetail
      },
      {
        path: '/mainHeader/taskList',
        name: 'taskList',
        component: taskList
      },
      {
        path: '/mainHeader/taskRunLog',
        name: 'taskRunLog',
        component: taskRunLog
      },
      {
        path: '/mainHeader/programDetail',
        name: 'programDetail',
        component: programDetail
      },
      {
        path: '/mainHeader/programList',
        name: 'programList',
        component: programList
      },
      {
        path: '/mainHeader/reportList',
        name: 'reportList',
        component: reportList
      },
      {
        path: '/mainHeader/reportDetail',
        name: 'reportDetail',
        component: reportDetail
      }]
    }]
})
