<template>
  <el-container>
    <router-view></router-view>
    <el-container>
      <el-header style="height:35px">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/apiAutoTest/projectList' }">项目管理</el-breadcrumb-item>
          <el-breadcrumb-item>项目列表</el-breadcrumb-item>
        </el-breadcrumb>
      </el-header>
      <el-main>
        <div class="searchProject">
          <el-form ref="searchForm" :model="finalSearchParams" :rules="rules" label-width="75px" style="display:flex; justify-content: left;">
            <el-form-item prop="selectedParamsValue" class="choose_params">
              <el-input placeholder="请输入内容" @change="onSelectInputChange" v-model="finalSearchParams.selectedParamsValue" clearable  class="input-with-select">
                <el-select @change="getChangedParam" v-model="defaultSelectedParamsLabel" slot="prepend" placeholder="请选择">
                  <el-option v-for="item in searchParams.paramsSelection" :key="item.value" :label="item.label" :value="item.value"></el-option>
                </el-select>
              </el-input>
            </el-form-item>
            <el-form-item label="创建者" prop="creator" style="margin-left:30px">
              <el-input class="select_projectCreate" v-model="finalSearchParams.creator" placeholder="请输入项目创建人" clearable></el-input>
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
  </el-container>
</template>
<script>
import ConfirmMixin from '../../assets/confirm_mixin'
import createProject from './createProject.vue'
import editProject from './editProject.vue'
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
      defaultSelectedParamsLabel: '项目名称',
      defaultSelectedStatus: '进行中',
      finalSearchParams: {
        selectedParamsKey: '',
        selectedParamsValue: '',
        creator: '',
        status: ''
      },
      rules: {
        selectedParamsKey: [{require: true, message: '请选择任一种搜索方式', trigger: 'blur'}],
        selectedParamsValue: [{require: false, trigger: 'blur'}],
        creator: [{require: false, trigger: 'blur'}],
        status: [{require: false, trigger: 'blur'}]
      },
      tableData: [],
      addProjectParams: {},
      editProjectParams: {}
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
            this.addProjectParams = {...formParms.addRuleForm}
            let projectStartTime = new Date(this.addProjectParams.projectCycle[0])
            let projectEndTime = new Date(this.addProjectParams.projectCycle[1])
            if (projectStartTime.getTime() >= new Date().getTime()) { // 还需要设置控件开始时间只能选择大于等于当前时间
              this.addProjectParams['status'] = '1' // 进行中
            } else {
              this.addProjectParams['status'] = '2' // 未开始
            }
            if (projectEndTime.getTime() < new Date().getTime()) {
              this.addProjectParams['status'] = '0' // 已结束
            } else {
              this.addProjectParams['status'] = '1' // 进行中
            }
            formParms.clearValidate() // 清空输入项
            done()
            this.addProjectParams['creator'] = 'hemeilong' // 后续需动态获取当前登录的用户名，暂时先写死
            let param = JSON.stringify(this.addProjectParams)
            return this.$axios.post('/apiAutoTest/projectManage/projectList/addPro', param).then(response => {
              if (response.status === 200) {
                console.log('发送Ajax请求,请求成功', response.data)
                this.$message({
                  message: '项目创建成功',
                  type: 'success',
                  color: 'green'
                })
                this.queryProject('searchForm')
              } else {
                this.$message({
                  showClose: true,
                  message: '项目创建失败',
                  type: 'error'
                })
              }
            }).catch(response => {
              console.log('发送Ajax请求,' +
              '请求失败', response)
            })
          })
        }
      }).catch(() => { })
    },
    getChangedParam (selectedTtem) { // 在查询条件选择组件变更后更新查询条件的key和value，value为当前输入框输入的值
      this.finalSearchParams['selectedParamsKey'] = selectedTtem
      this.finalSearchParams.selectedParamsValue = '' // 切换后清空搜索条件
    },
    onSelectInputChange (inputValue) { // 在输入框变更时，更新查询条件组件当前选择条件对应的value
      this.finalSearchParams['selectedParamsValue'] = inputValue
    },
    getQueryStatus (status) {
      if (typeof (status) === 'undefined') {
        this.finalSearchParams['status'] = '' // 若未选择任一种项目状态则后台默认查询全部
      } else {
        this.finalSearchParams['status'] = status
      }
    },
    queryProject (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$axios
            .get('/apiAutoTest/projectManage/projectList/find', { params: this.finalSearchParams })
            .then(response => {
              let responseJsonData = response.data
              this.tableData = responseJsonData['data']['data']
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
    projectEdit (index, row) {
      let tempRow = {}
      for (const i in row) {
        if (i === 'projectCycle') {
          tempRow[i] = [row[i].slice(0, 19), row[i].slice(20)] // 转换字符串为日期格式，便于显示原始数据
        } else {
          tempRow[i] = row[i]
        }
      }
      this.confirmBox({
        title: '编辑项目',
        customClass: 'editProject_confirmBox',
        closeOnClickModal: false, // 是否可通过点击遮罩关闭 MessageBox
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: '确定',
        component: editProject,
        componentName: 'editProject',
        confirmData: tempRow,
        confirmValidate: (action, instance, done) => {
          if (action === 'cancel') {
            return done() // done用于关闭 MessageBox 实例
          }
          instance.validate(valid => {
            if (!valid) return
            this.editProjectParams = {...instance.editRuleForm}
            let projectStartTime = new Date(this.editProjectParams.projectCycle[0])
            let projectEndTime = new Date(this.editProjectParams.projectCycle[1])
            if (projectStartTime.getTime() > new Date().getTime()) { // 还需要设置控件开始时间只能选择大于等于当前时间，且结束时间不能小于开始时间
              this.editProjectParams['status'] = '2' // 未开始
            } else if (projectStartTime.getTime() <= new Date().getTime() && projectEndTime.getTime() > new Date().getTime()) {
              this.editProjectParams['status'] = '1' // 进行中
            }
            if (projectEndTime.getTime() < new Date().getTime()) {
              this.editProjectParams['status'] = '0' // 已结束
            }
            done()
            console.log(new Date())
            this.editProjectParams['update_time'] = new Date().getTime()
            this.editProjectParams['creator'] = 'hemeilong' // 后续需动态获取当前登录的用户名，暂时先写死
            // 去除编辑会自动更新的字段，无需提交
            delete (this.editProjectParams.created_time)
            let param = JSON.stringify(this.editProjectParams)
            return this.$axios.post('/apiAutoTest/projectManage/projectList/editPro', param).then(response => {
              if (response.status === 200) {
                console.log('发送Ajax请求,请求成功', response.data)
                this.$message({
                  message: '项目编辑更新成功',
                  type: 'success'
                })
                this.queryProject('searchForm')
              } else {
                this.$message({
                  showClose: true,
                  message: '项目编辑更新失败',
                  type: 'error',
                  color: 'green'
                })
              }
            }).catch(response => {
              console.log('发送Ajax请求,' +
                '请求失败', response)
            })
          })
        }
      }).catch(() => { })
    },
    projectDelete (row) {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let param = JSON.stringify({'id': row.id})
        return this.$axios.post('/apiAutoTest/projectManage/projectList/delPro', param).then(response => {
          if (response.status === 200) {
            console.log('发送Ajax请求,请求成功', response.data)
            this.$message({
              message: '删除项目成功！',
              type: 'success'
            })
            this.queryProject('searchForm')
          } else {
            this.$message({
              showClose: true,
              message: '删除项目失败',
              type: 'error',
              color: 'green'
            })
          }
        }).catch(response => {
          console.log('发送Ajax请求,' +
            '请求失败', response)
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
    this.getChangedParam('projectName')
    this.getQueryStatus('1')
    this.queryProject('searchForm')
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
    padding-bottom: 40px;
  }
  .el-form-item.choose_params.is-success>>>.el-form-item__content {
    margin-left: 0px !important;
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
  .input-with-select>>>.el-input__inner:focus {
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
    border-top: 1px solid #c0c4ccb8;
  }
  .projectTableList>>>.el-table th {
    background-color: #f4f5f975;
  }
  .projectTableList>>>.el-table tr {
    background-color: #f4f5f975;
  }
  .projectTableList>>>.cell {
    text-align: center;
  }
  .searchProject>>>.el-button.addProjectBtn.el-button--default.el-button--mini {
    padding: 14px 22px;
  }
</style>
