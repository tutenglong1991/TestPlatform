<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/apiAutoTest/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>执行日志</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
  </el-container>
</template>

<script>
export default {
  name: 'apiRunLog'
}
</script>

<style scoped>
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;;
  }
</style>
