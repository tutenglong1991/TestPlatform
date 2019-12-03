<template>
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
          <el-menu-item index="/apiAutoTest/projectList">项目首页</el-menu-item>
          <el-menu-item index="/apiAutoTest/projectMembers">成员管理</el-menu-item>
        </el-submenu>
        <el-submenu index="/apiAutoTest/apiManage">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span>接口管理</span>
          </template>
          <el-menu-item index="/apiAutoTest/apiList">接口列表</el-menu-item>
          <el-menu-item index="/apiAutoTest/apiDetail">接口详情</el-menu-item>
          <el-menu-item index="/apiAutoTest/apiGroup">分组管理</el-menu-item>
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
</template>

<script>
export default {
  name: 'apiAutoTest',
  data () {
    return {
    }
  },
  components: {
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
  .open-platform {
    width: 95%;
    margin: 0px auto;
  }
  .open-platform-title {
    text-align: center;
    margin: 10px 0px;
    font-size: 16px;
  }
  .op-create {
    margin-top: 30px;
  }
</style>
