<template>
  <div class="searchProject" style="margin-top: 15px;">
    <div class="select_projectStatus">
    </div>
    <div class="select_projectCreate">
    </div>
    <div class="select_search_item">
      <el-input placeholder="请输入内容" v-model="input1" class="input-with-select">
        <el-select v-model="select" slot="prepend" placeholder="请选择">
          <el-option label="项目名称" value="1"></el-option>
          <el-option label="类型" value="2"></el-option>
          <el-option label="IT部产品线" value="3"></el-option>
          <el-option label="项目编号" value="4"></el-option>
        </el-select>
      </el-input>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      input1: '',
      input2: '',
      input3: '',
      select: ''
    }
  }
}
</script>
<style>
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
  .searchProject {
    width: 100%;
    height: 30px;
    display: block;
  }
  .select_search_item {
    width: 45%;
    height: 30px;
    background-color: red;
    display: flex
  }
  .select_projectStatus {
    width: 30%;
    height: 30px;
    background-color: green;
    float: left;
    display: flex
  }
  .select_projectCreate {
    width: 30%;
    height: 30px;
    background-color: grey;
    float: left;
    display: flex
  }
</style>
