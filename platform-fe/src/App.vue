<template>
  <el-container style="height:100%; width:100%">
    <el-header v-if="login_status">
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
        <el-menu-item class="login_btn" index='/'>
          <el-button class="login_sign_out" @click="sign_out">Sign Out</el-button>
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-container>
      <router-view @transfer-loginStatus="is_login_callback"></router-view>
    </el-container>
    <el-footer>© 2019 - 2020 环球易购-电子产品研发中心. All Rights Reserved.</el-footer>
  </el-container>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      login_status: false
    }
  },
  methods: {
    is_login_callback (status) {
      console.log(status)
      this.login_status = status
    },
    sign_out () {
      this.login_status = false
      this.$router.push('/')
    }
  },
  mounted () {
    this.is_login_callback()
  }
}
</script>

<style scoped>
body {
  height:100%;
  width:100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
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
.login_btn{
  float: right;
}
.login_btn>>>.el-button {
  margin: auto;
  font-size: 17px;
  color: #161616;
}
.login_sign_in.el-button {
  background-color: #161616;
  border-color: #161616;
  color: #ffffff;
}
.login_sign_in.el-button:hover {
  color: #04aa51;
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
.el-footer {
  background-color: #161616;
  color: #ffffff;
  text-align: center;
  line-height: 60px;
  font-size: 14px;
}
/*body > .el-container {*/
/*  margin-bottom: 40px;*/
/*}*/
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}
.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
