<template>
  <el-container>
    <el-header>
      <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" background-color="#161616" text-color="#a9a9a9" active-text-color="#ffffff" router>
        <el-submenu index="/apiAuto">
          <template slot="title">接口自动化</template>
          <el-menu-item index="/apiAuto/apiFunc">功能自动化</el-menu-item>
          <el-menu-item index="/apiAuto/apiPerf">性能自动化</el-menu-item>
        </el-submenu>
        <el-menu-item index='/uiAuto'>UI自动化</el-menu-item>
        <el-menu-item index='/dataReport'>数据采集</el-menu-item>
        <el-submenu index="/testTools">
          <template slot="title">测试工具集</template>
          <el-menu-item index="/testTools/querySkuTable">分表查询</el-menu-item>
          <el-menu-item index="/testTools/createAccount">商城测试账号创建</el-menu-item>
        </el-submenu>
        <el-menu-item class="sign_out" index='/'>
          <el-button class="login_sign_out">Sign Out</el-button>
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-container>
      <el-aside style="width: 200px; height: 100%">
        <el-menu style="height: 100%"
                 active-text-color="#04aa51"
                 :default-active="$router.path"
                 class="el-menu-vertical-demo"
                 @open="handleOpen"
                 @close="handleClose"
                 router>
          <el-submenu index="/apiAutoTest/projectManage">
            <template slot="title">
              <i class="el-icon-user-solid"></i>
              <span>项目管理</span>
            </template>
            <el-menu-item index="/apiAutoTest/projectList">项目列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/projectMembers">成员管理</el-menu-item>
          </el-submenu>
          <el-submenu index="/apiAutoTest/apiManage">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>接口管理</span>
            </template>
            <el-menu-item index="/apiAutoTest/apiList">接口列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/apiDetail">接口详情</el-menu-item>
            <el-menu-item index="/apiAutoTest/apiGroup">接口分组</el-menu-item>
            <el-menu-item index="/apiAutoTest/apiRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/apiAutoTest/caseManage">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>用例管理</span>
            </template>
            <el-menu-item index="/apiAutoTest/caseList">用例列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/caseDetail">用例详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/apiAutoTest/taskManage">
            <template slot="title">
              <i class="el-icon-bell"></i>
              <span>任务管理</span>
            </template>
            <el-menu-item index="/apiAutoTest/taskList">任务列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/taskRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/apiAutoTest/programManage">
            <template slot="title">
              <i class="el-icon-notebook-1"></i>
              <span>测试方案</span>
            </template>
            <el-menu-item index="/apiAutoTest/programList">方案列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/programDetail">方案详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/apiAutoTest/reportManage">
            <template slot="title">
              <i class="el-icon-s-data"></i>
              <span>测试报告</span>
            </template>
            <el-menu-item index="/apiAutoTest/reportList">报告列表</el-menu-item>
            <el-menu-item index="/apiAutoTest/reportDetail">报告详情</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'apiAutoTest',
  data () {
    return {
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  },
  mounted () {
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
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
