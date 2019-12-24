<template>
  <el-container style="height:100%; width:100%">
    <el-container>
      <router-view></router-view>
    </el-container>
    <el-footer>© 2019 - 2020 XXXX-XXXX研发中心. All Rights Reserved.</el-footer>
  </el-container>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
    }
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
.el-footer {
  background-color: #161616;
  color: #ffffff;
  text-align: center;
  line-height: 60px;
  font-size: 14px;
}
</style>
