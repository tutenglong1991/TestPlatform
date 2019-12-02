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
        <el-submenu index="/home/apitest/projectManage">
          <template slot="title">
            <i class="el-icon-user-solid"></i>
            <span>项目管理</span>
          </template>
          <el-menu-item index="/home/apitest/projectHomePage">项目首页</el-menu-item>
          <el-menu-item index="/home/apitest/projectMembers">成员管理</el-menu-item>
        </el-submenu>
        <el-submenu index="home/apitest/apiManage">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span>接口管理</span>
          </template>
          <el-menu-item index="home/apitest/apiList">接口列表</el-menu-item>
          <el-menu-item index="home/apitest/apiDetail">接口详情</el-menu-item>
          <el-menu-item index="home/apitest/apiGroup">分组管理</el-menu-item>
        </el-submenu>
        <el-menu-item index="3">
          <i class="el-icon-document"></i>
          <span slot="title">用例管理</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-bell"></i>
          <span slot="title">任务管理</span>
        </el-menu-item>
        <el-menu-item index="5">
          <i class="el-icon-notebook-1"></i>
          <span slot="title">测试方案</span>
        </el-menu-item>
        <el-menu-item index="6">
          <i class="el-icon-s-data"></i>
          <span slot="title">测试报告</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'apiAutotest',
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
