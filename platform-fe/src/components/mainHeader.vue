<template>
  <el-container>
    <el-header>
      <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" background-color="#161616" text-color="#a9a9a9" active-text-color="#ffffff" router>
        <el-menu-item index="/functionAuto/mainHeader/projectManage">功能自动化</el-menu-item>
        <el-submenu index="/performanceAuto/mainHeader">
          <template slot="title">性能自动化</template>
          <el-menu-item index="/performanceAuto/mainHeader/autoPressMonitorJMeter">JMeter客户端</el-menu-item>
          <el-menu-item index="/performanceAuto/mainHeader/autoPressMonitorService">被压测服务端</el-menu-item>
        </el-submenu>
        <el-menu-item index='/continuousIntegration'>持续集成</el-menu-item>
        <el-submenu index="/testTools">
          <template slot="title">测试工具集</template>
          <el-menu-item index="/testTools/querySkuTable">分表查询</el-menu-item>
          <el-menu-item index="/testTools/createAccount">商城测试账号创建</el-menu-item>
        </el-submenu>
        <el-menu-item class="sign_out" index='/login'>
          <el-button class="login_sign_out">Sign Out</el-button>
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-container>
      <el-aside v-if="isUnderFunctionAutoRoute" style="width: 200px; height: 100%">
        <el-menu style="height: 100%"
                  active-text-color="#04aa51"
                  :default-active="$router.path"
                  :unique-opened="true"
                  class="el-menu-vertical-demo"
                  @open="handleOpen"
                  @close="handleClose"
                  router>
          <el-submenu index="/functionAuto/mainHeader/projectManage">
            <template slot="title">
              <i class="el-icon-user-solid"></i>
              <span>项目管理</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/projectManage">项目列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/projectMembers">成员管理</el-menu-item>
          </el-submenu>
          <el-submenu index="/functionAuto/mainHeader/apiManage">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>接口管理</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/configList">配置列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/apiList">接口列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/apiDetail">修改记录</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/apiRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/functionAuto/mainHeader/caseManage">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>用例管理</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/caseList">用例列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/caseDetail">用例详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/functionAuto/mainHeader/taskManage">
            <template slot="title">
              <i class="el-icon-bell"></i>
              <span>任务管理</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/taskList">任务列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/taskRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/functionAuto/mainHeader/programManage">
            <template slot="title">
              <i class="el-icon-notebook-1"></i>
              <span>测试方案</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/programList">方案列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/programDetail">方案详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/functionAuto/mainHeader/reportManage">
            <template slot="title">
              <i class="el-icon-s-data"></i>
              <span>测试报告</span>
            </template>
            <el-menu-item index="/functionAuto/mainHeader/reportList">报告列表</el-menu-item>
            <el-menu-item index="/functionAuto/mainHeader/reportDetail">报告详情</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main class="father-main" style="height: 100%;">
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'mainHeader',
  data () {
    return {
      isUnderFunctionAutoRoute: true
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    getCurrentRoute () {
      let currentRoute = window.document.location.pathname.substr(1).split('/')[0]
      let fatherMain = document.querySelectorAll('.el-main.father-main')
      console.log(fatherMain)
      if (currentRoute === 'functionAuto') {
        this.isUnderFunctionAutoRoute = true
        fatherMain[0].style.padding = '20px'
      } else {
        this.isUnderFunctionAutoRoute = false
        fatherMain[0].style.padding = '0px'
      }
      console.log(fatherMain)
    }
  },
  // 监听路由变化后进行的处理
  watch: {
    '$route': 'getCurrentRoute'
  }
}
</script>

<style scoped>
  .el-header {
    background-color: #161616;
    color: #333;
    text-align: center;
    line-height: 60px;
    font-size: 14px;
  }
  .el-menu-demo>.el-menu-item {
    font-size: 15px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-weight: bolder;
  }
  .el-menu-demo>>>.el-submenu__title {
    font-size: 15px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-weight: bolder;
  }
  .el-menu-demo>>>.sign_out{
    float: right;
  }
  .sign_out>>>.el-button {
    margin: auto;
    font-size: 17px;
    color: #161616;
  }
  .login_sign_out.el-button {
    color: #ffffff;
    font-weight: bold;
    border-color: #161616;
    background: #04aa51;
  }
  .login_sign_out.el-button:hover {
    background: #0faa22;
  }
</style>
