<template>
  <el-container>
    <el-header>
      <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" background-color="#161616" text-color="#a9a9a9" active-text-color="#ffffff" router>
        <el-submenu index="/apiAuto">
          <template slot="title">功能自动化</template>
          <el-menu-item index="/apiAuto/apiFunc">功能自动化</el-menu-item>
        </el-submenu>
        <el-menu-item index='/performanceAuto'>性能自动化</el-menu-item>
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
                 :unique-opened="true"
                 class="el-menu-vertical-demo"
                 @open="handleOpen"
                 @close="handleClose"
                 router>
          <el-submenu index="/mainHeader/projectManage">
            <template slot="title">
              <i class="el-icon-user-solid"></i>
              <span>项目管理</span>
            </template>
            <el-menu-item index="/mainHeader/projectList">项目列表</el-menu-item>
            <el-menu-item index="/mainHeader/projectMembers">成员管理</el-menu-item>
          </el-submenu>
          <el-submenu index="/mainHeader/apiManage">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>接口管理</span>
            </template>
            <el-menu-item index="/mainHeader/configList">配置列表</el-menu-item>
            <el-menu-item index="/mainHeader/apiList">接口列表</el-menu-item>
            <el-menu-item index="/mainHeader/apiDetail">修改记录</el-menu-item>
            <el-menu-item index="/mainHeader/apiRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/mainHeader/caseManage">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>用例管理</span>
            </template>
            <el-menu-item index="/mainHeader/caseList">用例列表</el-menu-item>
            <el-menu-item index="/mainHeader/caseDetail">用例详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/mainHeader/taskManage">
            <template slot="title">
              <i class="el-icon-bell"></i>
              <span>任务管理</span>
            </template>
            <el-menu-item index="/mainHeader/taskList">任务列表</el-menu-item>
            <el-menu-item index="/mainHeader/taskRunLog">执行日志</el-menu-item>
          </el-submenu>
          <el-submenu index="/mainHeader/programManage">
            <template slot="title">
              <i class="el-icon-notebook-1"></i>
              <span>测试方案</span>
            </template>
            <el-menu-item index="/mainHeader/programList">方案列表</el-menu-item>
            <el-menu-item index="/mainHeader/programDetail">方案详情</el-menu-item>
          </el-submenu>
          <el-submenu index="/mainHeader/reportManage">
            <template slot="title">
              <i class="el-icon-s-data"></i>
              <span>测试报告</span>
            </template>
            <el-menu-item index="/mainHeader/reportList">报告列表</el-menu-item>
            <el-menu-item index="/mainHeader/reportDetail">报告详情</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main class="father-main" style="height: 800px">
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
