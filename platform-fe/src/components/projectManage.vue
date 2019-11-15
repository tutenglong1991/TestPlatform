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
<!--        <el-input placeholder="请输入内容" @change="onSelectInputChange" v-model="searchParams.selectedParamValue" class="input-with-select">-->
<!--          <el-select @change="getQueryParam" v-model="selectedParams" slot="prepend" clearable placeholder="请选择">-->
<!--            <el-option v-for="item in searchParams.paramsSelection" :key="item.value" :label="item.label" :value="item.value"></el-option>-->
<!--          </el-select>-->
<!--        </el-input>-->
        <el-form ref="form" :model="finalSearchParams" label-width="80px" style="display: contents">
          <el-input placeholder="请输入内容" @change="onSelectInputChange" v-model="searchParams.selectedParamValue" class="input-with-select">
            <el-select @change="getQueryParam" v-model="searchParams.selectedParams" slot="prepend" clearable placeholder="请选择">
              <el-option v-for="item in searchParams.paramsSelection" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </el-input>
          <el-form-item label="项目周期" prop="projectCycle">
            <el-input class="select_projectCycle" v-model="finalSearchParams.projectCycle"></el-input>
          </el-form-item>
          <el-form-item label="创建者" prop="creator" style="margin-left:30px">
            <el-input class="select_projectCreate" v-model="finalSearchParams.creator"></el-input>
          </el-form-item>
          <el-form-item label="项目状态" prop="status" style="margin-left:30px">
            <el-select class="select_projectStatus" @change="getQueryStatus" v-model="searchParams.status" clearable placeholder="请选择">
              <el-option
                v-for="status in searchParams.statusSelection"
                :key="status.value"
                :label="status.label"
                :value="status.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <el-button class="searchBtn" type="primary" @click="submitForm">搜索</el-button>
        <el-button class="addProjectBtn" size="mini" @click="onCreateProject">新增</el-button>
      </div>
      <div class="projectTableList">
        <el-table
          :data="tableData"
          style="width: 100%">
          <el-table-column label="名称" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.projectName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="类型" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.projectType }}</span>
            </template>
          </el-table-column>
          <el-table-column label="项目编号" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.code }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属部门" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.dept }}</span>
            </template>
          </el-table-column>
          <el-table-column label="IT部产品线" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.productLine }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.status }}</span>
            </template>
          </el-table-column>
          <el-table-column
            label="项目周期"
            width="180">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.projectCycle }}</span>
            </template>
          </el-table-column>
<!--          <el-table-column label="创建者" width="180">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.creater }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
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
      searchParams: { // 搜索前端展示参数
        paramsSelection: [{
          value: 'projectName',
          label: '项目名称'
        },
        {
          value: 'projectType',
          label: '类型'
        },
        {
          value: 'productLine',
          label: 'IT部产品线'
        },
        {
          value: 'code',
          label: '项目编号'
        }],
        selectedParams: '项目名称',
        selectedParamValue: '',
        status: '进行中',
        statusSelection: [
          {
            value: '1',
            label: '进行中'
          },
          {
            value: '0',
            label: '结束'
          }]
      },
      finalSearchParams: {
        status: '进行中',
        projectCycle: '',
        creator: ''
      },
      tableData: [],
      addProjectParams: {
      }
    }
  },
  methods: {
    onCreateProject () { // 创建项目方法
      this.confirmBox({
        title: '创建项目',
        customClass: 'createProject_confirmBox',
        closeOnClickModal: false, // 是否可通过点击遮罩关闭 MessageBox
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: '确定',
        component: createProject,
        componentName: 'createProject',
        confirmValidate: (action, formParms, done) => {
          if (action === 'cancel') {
            formParms.clearValidate() // 清空输入项
            return done() // done用于关闭 MessageBox 实例
          }
          formParms.validate(valid => {
            if (!valid) return
            this.addProjectParams = {...formParms.ruleForm}
            console.log(this.addProjectParams)
            formParms.clearValidate() // 清空输入项
            done()
            let param = JSON.stringify(this.addProjectParams)
            return this.$axios.post('/home/apitest/projectList/add', param).then(response => {
              if (response.status === 200) {
                console.log('get发送Ajax请求,请求成功', response.data)
                this.$message({
                  message: '项目创建成功',
                  type: 'success'
                })
              } else {
                this.$message({
                  showClose: true,
                  message: '项目创建失败',
                  type: 'error',
                  color: 'green'
                })
              }
            }).catch(response => {
              console.log('get发送Ajax请求,' +
              '请求失败', response)
            })
          })
        }
      }).catch(() => { })
    },
    getQueryParam (item) { // 在查询条件选择组件变更后更新查询条件的key和value，value为当前输入框输入的值
      let tempSelectParam = {}
      tempSelectParam[item] = this.searchParams.selectedParamValue
      this.finalSearchParams = tempSelectParam
      this.searchParams.selectedParamValue = '' // 切换后清空搜索条件
    },
    onSelectInputChange (input) { // 在输入框变更时，更新查询条件组件当前选择条件对应的value
      for (let k in this.finalSearchParams) {
        this.finalSearchParams[k] = input
      }
    },
    getQueryStatus (status) {
      if (typeof status === 'undefined') {
        this.finalSearchParams['status'] = '' // 若未选择任一种项目状态则后台默认查询全部
      } else {
        this.finalSearchParams['status'] = status
        console.log(this.finalSearchParams)
      }
    },
    queryProject () {
      // let params = JSON.stringify(this.searchParams)
      return this.$axios.get('/home/apitest/projectList/find' + '?projectName=' + 'test', {timeout: 4000}).then(response => {
        if (response.status === 200) {
          console.log('get发送Ajax请求,请求成功', response.data)
          let responseJsonData = response.data
          this.tableData = responseJsonData['pro_data']['data']
          console.log(this.finalSearchParams)
        }
      }).catch(response => {
        console.log('get发送Ajax请求,' +
            '请求失败', response)
      })
    },
    submitForm (finalSearchParams) {
      // if (this.sizeForm['companyId'] === '') {
      //   delete this.sizeForm['companyId']
      // }
      this.$refs[finalSearchParams].validate(valid => {
        if (valid) {
          this.$axios
            .get('/home/apitest/projectList/find', { params: this.finalSearchParams })
            .then(response => {
              this.textarea = response.data.data
              console.log(response.data.data)
            })
            .catch(error => {
              console.log('系统错误' + error)
            })
        } else {
          console.log('error submit!!')
          return false
        }
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
  },
  mounted () {
    this.getQueryParam('projectName')
    this.queryProject()
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
    width: 23%;
    height: 30px;
    margin-right: 40px;
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
  .select_projectCreate.el-input>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .select_projectCreate.el-input>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .select_projectCycle.el-input>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .select_projectCycle.el-input>>>.el-input__inner:hover {
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
