<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>项目管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/home/apitest/projectList' }">项目首页</el-breadcrumb-item>
        <el-breadcrumb-item>项目列表</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div class="searchProject">
        <el-form ref="searchForm" :model="finalSearchParams" :rules="rules" label-width="85px" style="display:flex; justify-content: left;">
          <el-form-item prop="selectedParamsValue" class="choose_params">
            <el-input placeholder="请输入内容" @change="onSelectInputChange" v-model="finalSearchParams.selectedParamsValue" clearable  class="input-with-select">
              <el-select @change="getChangedParam" v-model="defaultSelectedParamsLabel" slot="prepend" placeholder="请选择">
                <el-option v-for="item in searchParams.paramsSelection" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-input>
          </el-form-item>
          <el-form-item label="创建者" prop="creator" style="margin-left:30px">
            <el-input class="select_projectCreate" v-model="finalSearchParams.creator" clearable></el-input>
          </el-form-item>
          <el-form-item label="项目状态" prop="status" style="margin-left:30px">
            <el-select class="select_projectStatus" @change="getQueryStatus" v-model="defaultSelectedStatus" clearable placeholder="请选择">
              <el-option
                v-for="status in searchParams.statusSelection"
                :key="status.value"
                :label="status.label"
                :value="status.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button class="searchBtn" type="primary" @click="queryProject('searchForm')">搜索</el-button>
            <el-button class="addProjectBtn" size="mini" @click="onCreateProject">新增</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="projectTableList">
        <el-table
          :data="tableData"
          style="width: 100%">
          <el-table-column label="名称" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.projectName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="类型" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.projectType }}</span>
            </template>
          </el-table-column>
          <el-table-column label="项目编号" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.code }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属部门" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.dept }}</span>
            </template>
          </el-table-column>
          <el-table-column label="IT部产品线" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.productLine }}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="项目周期"
            width="160">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.projectCycle }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.status }}</span>
            </template>
          </el-table-column>
          <el-table-column label="创建人" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.creator }}</span>
            </template>
          </el-table-column>
          <el-table-column label="更新时间" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.update_time }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="projectEdit(scope.$index, scope.row)">编辑
              </el-button>
              <el-button
                size="mini"
                @click="projectDelete(scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-main>
  </el-container>
</template>
<script>
</script>
<style scoped>
  .el-container {
    height: 100%;
  }
  .el-header {
    margin-top: 2px;
  }
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;;
  }
  .searchProject {
    width: 100%;
    height: 40px;
    padding-bottom: 40px;
    border-bottom: 1px solid #bbbcbf59;
  }
  form.el-form.el-form-item.choose_params>>>.el-form-item__content {
    background: #04aa51;
  }
  .input-with-select>>>.el-input-group__prepend {
    background-color: #fff;
    color: #606266;
    width: 100px;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .input-with-select.el-input-group--prepend>>>.el-input__inner {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .input-with-select>>>.el-input__inner::-webkit-input-placeholder {
    color: #c3c3c5;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    border-color: #04aa51;
  }
  .input-with-select>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .el-input-group__prepend div.el-select>>>.el-input__inner {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .el-select.select_projectStatus>>>.el-input__inner {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 100px;
  }
  .el-select.select_projectStatus>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-select.select_projectStatus>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .select_projectCreate.el-input--suffix>>>.el-input__inner {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .select_projectCreate.el-input>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .select_projectCreate.el-input>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .searchBtn {
    margin-left: 100px;
  }
  .searchProject>.el-button:focus, .el-button:hover {
    color: #ffffff;
    border-color: #04aa51;
    background-color: #04aa51;
  }
  .el-button--primary {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .projectTableList {
    margin-top: 30px;
  }
  .projectTableList>>>.el-table th {
    background-color: #f4f5f975;
  }
  .projectTableList>>>.el-table tr {
    background-color: #f4f5f975;
  }
  .searchProject>>>.el-button.addProjectBtn.el-button--default.el-button--mini {
    padding: 14px 22px;
  }
</style>
