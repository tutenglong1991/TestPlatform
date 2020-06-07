import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import mainHeader from '@/components/mainHeader'
import projectManage from '@/components/projectManage/projectManage'
import projectMembers from '@/components/projectManage/projectMembers'
import apiList from '@/components/apiManage/apiList'
import apiAddPage from '@/components/apiManage/apiAddPage'
import commonConfig from '@/components/apiManage/commonConfig'
import configList from '@/components/apiManage/configList'
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
import autoPressMonitorJMeter from '@/components/performance/autoPressMonitorJMeter'
import autoPressMonitorService from '@/components/performance/autoPressMonitorService'

Vue.use(Router)

export default new Router({
  mode: 'history', // 去除哈希值的#号
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/performanceAuto/mainHeader',
      name: 'mainHeader',
      component: mainHeader,
      children: [{
        path: '/performanceAuto/mainHeader/autoPressMonitorJMeter',
        name: 'autoPressMonitorJMeter',
        component: autoPressMonitorJMeter
      },
      {
        path: '/performanceAuto/mainHeader/autoPressMonitorService',
        name: 'autoPressMonitorService',
        component: autoPressMonitorService
      }]
    },
    {
      path: '/functionAuto/mainHeader',
      name: 'mainHeader',
      component: mainHeader,
      children: [{
        path: '/functionAuto/mainHeader/projectManage',
        name: 'projectManage',
        component: projectManage
      },
      {
        path: '/functionAuto/mainHeader/projectMembers',
        name: 'projectMembers',
        component: projectMembers
      },
      {
        path: '/functionAuto/mainHeader/apiList',
        name: 'apiList',
        component: apiList
      },
      {
        path: '/functionAuto/mainHeader/apiAddPage',
        name: 'apiAddPage',
        component: apiAddPage
      },
      {
        path: '/functionAuto/mainHeader/updateRecord',
        name: 'updateRecord',
        component: updateRecord
      },
      {
        path: '/functionAuto/mainHeader/configList',
        name: 'configList',
        component: configList
      },
      {
        path: '/functionAuto/mainHeader/commonConfig',
        name: 'commonConfig',
        component: commonConfig
      },
      {
        path: '/functionAuto/mainHeader/apiDetail',
        name: 'apiDetail',
        component: () => import('@/components/apiManage/apiDetail.vue')
      },
      {
        path: '/functionAuto/mainHeader/apiRunLog',
        name: 'apiRunLog',
        component: apiRunLog
      },
      {
        path: '/functionAuto/mainHeader/caseList',
        name: 'caseList',
        component: caseList
      },
      {
        path: '/functionAuto/mainHeader/caseDetail',
        name: 'caseDetail',
        component: caseDetail
      },
      {
        path: '/functionAuto/mainHeader/taskList',
        name: 'taskList',
        component: taskList
      },
      {
        path: '/functionAuto/mainHeader/taskRunLog',
        name: 'taskRunLog',
        component: taskRunLog
      },
      {
        path: '/functionAuto/mainHeader/programDetail',
        name: 'programDetail',
        component: programDetail
      },
      {
        path: '/functionAuto/mainHeader/programList',
        name: 'programList',
        component: programList
      },
      {
        path: '/functionAuto/mainHeader/reportList',
        name: 'reportList',
        component: reportList
      },
      {
        path: '/functionAuto/mainHeader/reportDetail',
        name: 'reportDetail',
        component: reportDetail
      }]
    }]
})
