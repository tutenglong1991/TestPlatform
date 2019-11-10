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
        <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
          <el-select v-model="select" slot="prepend" placeholder="请选择">
            <el-option label="项目名称" value="1"></el-option>
            <el-option label="类型" value="2"></el-option>
            <el-option label="IT部产品线" value="3"></el-option>
            <el-option label="项目编号" value="4"></el-option>
          </el-select>
        </el-input>
        <el-form class="select_projectStatus" ref="form" :model="form" label-width="80px">
          <el-form-item label="项目状态">
            <el-select class="select_projectStatus" v-model="value" clearable placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <el-form class="select_projectCreate" ref="form" :model="form" label-width="80px">
          <el-form-item label="创建者">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
        </el-form>
        <el-button class="searchBtn" type="primary">搜索</el-button>
        <el-button class="addProjectBtn" size="mini" @click="onCreateProject">新增</el-button>
      </div>
      <div class="projectTableList">
        <el-table
          :data="tableData"
          style="width: 100%">
          <el-table-column label="姓名" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="类型" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.type }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属部门" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.ownDept }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属项目编号" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.ownProjectCode }}</span>
            </template>
          </el-table-column>
          <el-table-column label="IT部产品线" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.itProductLine }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.status }}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="日期"
            width="180">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.createDate }}</span>
            </template>
          </el-table-column>
          <el-table-column label="创建者" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.creater }}</span>
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
                @click="projectDelete(scope.$index, scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-main>
  </el-container>
</template>
<script>
import ConfirmMixin from '../assets/confirm_mixin'
import createProject from './createProject.vue'
export default {
  mixins: [ConfirmMixin],
  data () {
    return {
      input: '',
      select: '',
      form: {
        name: ''
      },
      options: [{
        value: '选项1',
        label: '进行中'
      }, {
        value: '选项2',
        label: '结束'
      }],
      value: '',
      tableData: [{
        name: '选推项目',
        type: 'Epic',
        ownDept: 'IT产品总部',
        ownProjectCode: 'ITPM20190800000075-选推服务',
        itProductLine: 'GB-选推服务',
        status: '进行中',
        createDate: '2016-05-02',
        creater: 'hemeilong'
      },
      {
        name: '选推项目',
        type: 'Epic',
        ownDept: 'IT产品总部',
        ownProjectCode: 'ITPM20190800000075-选推服务',
        itProductLine: 'GB-选推服务',
        status: '进行中',
        createDate: '2019-11-08',
        creater: 'hemeilong'
      },
      {
        name: '选推项目',
        type: 'Epic',
        ownDept: 'IT产品总部',
        ownProjectCode: 'ITPM20190800000075-选推服务',
        itProductLine: 'GB-选推服务',
        status: '结束',
        createDate: '2019-11-08',
        creater: 'hemeilong'
      }]
    }
  },
  methods: {
    onCreateProject () {
      this.confirmBox({
        title: '创建项目',
        customClass: 'createProject_alert',
        showCancelButton: true,
        confirmButtonText: '确定',
        component: createProject,
        componentName: 'createProject',
        confirmValidate: (action, cpt, done) => {
          console.log(action)
          console.log(cpt)
          if (action === 'cancel') {
            cpt.clearValidate()
            return done()
          }
          cpt.validate(valid => {
            if (!valid) return
            console.log('{userData}: ', { ...cpt.userData })
            cpt.clearValidate()
            done()
          })
        }
      }).catch(() => { })
    },
    projectAdd () {
      this.$prompt('请输入邮箱', '提示', {
        title: '创建项目',
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: '邮箱格式不正确'
      }).then(({ value }) => {
        this.$message({
          type: 'success',
          message: '你的邮箱是: ' + value
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        })
      })
    },
    projectEdit () {
      this.$prompt('请输入邮箱', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: '邮箱格式不正确'
      }).then(({ value }) => {
        this.$message({
          type: 'success',
          message: '你的邮箱是: ' + value
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        })
      })
    },
    projectDelete (index, row) {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
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
    display:flex;
    justify-content: left;
    padding-bottom: 40px;
    border-bottom: 1px solid #bbbcbf59;
  }
  .searchProject>.input-with-select {
    width: 25%;
    height: 30px;
    margin-right: 50px;
  }
  .input-with-select>>>.el-input-group__prepend {
    background-color: #fff;
    color: #606266;
    width: 130px;
    font-size: 14px;
  }
  .input-with-select>>>.el-input__inner::-webkit-input-placeholder {
    color: #c3c3c5;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .el-input-group__prepend div.el-select>>>.el-input__inner {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .el-input.is-active >>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-select.select_projectStatus>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-select.select_projectStatus>>>.el-input__inner {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 100px;
  }
  .select_projectCreate {
    width: 15%;
    height: 30px;
    margin-right: 100px;
    margin-left: 20px;
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
