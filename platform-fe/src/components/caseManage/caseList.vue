<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/apiAutoTest/apiList'}">用例管理</el-breadcrumb-item>
        <el-breadcrumb-item>用例列表</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div class="searchCase">
        <el-form ref="searchForm" :model="caseSearchParam" label-width="70px" style="display:flex; justify-content: left;">
          <el-form-item prop="api_module" class="choose_module_dem" style="margin-left: -20px">
            <span class="case_module_dem">所属服务/接口/方法名</span>
            <el-cascader v-model="caseSearchParam.api_module" style="margin-left: 10px; width: 350px;"
               placeholder="请选择所属服务及接口及方法"
               :options="caseSearchOptions.api_module"
               :props="props"
               collapse-tags
               clearable>
              <template slot-scope="{ node, data }">
                <span>{{ data.label }}</span>
                <span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
              </template>
            </el-cascader>
          </el-form-item>
          <el-form-item label="用例名称" prop="caseName" style="width: 200px; margin-left: 15px;">
            <el-input class="select_caseName" v-model="caseSearchParam.caseName" placeholder="请输入用例名称" clearable></el-input>
          </el-form-item>
          <el-form-item label="用例级别" prop="caseLevel" style="margin-left:35px">
            <el-select class="caseLevel" v-model="caseSearchParam.caseLevel" clearable placeholder="选择用例级别">
              <el-option
                v-for="lev in caseSearchOptions.caseLevel"
                :key="lev.value"
                :label="lev.label"
                :value="lev.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="执行状态" prop="runStatus" style="margin-left: 15px">
            <el-select class="runStatus" v-model="caseSearchParam.runStatus" clearable placeholder="选择执行状态">
              <el-option
                v-for="status in caseSearchOptions.runStatus"
                :key="status.value"
                :label="status.label"
                :value="status.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button @click="searchCase" class="searchCaseBtn" type="primary">搜索</el-button>
            <el-button @click="onCreateCase" class="addCaseBtn">添加</el-button>
          </el-form-item>
        </el-form>
      </div>
      <el-row>
        <el-button class="addTaskBtn" type="primary" @click="createAutoTask">创建任务</el-button>
        <el-button class="manualRunBtn" @click="manualRunCase(multipleSelection)">手动执行</el-button>
      </el-row>
      <div class="caseTableList">
        <el-table
          ref="multipleTable"
          tooltip-effect="dark"
          @selection-change="handleSelectionChange"
          :data="caseTableData"
          style="width: 100%">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column label="用例ID" width="70">
            <template slot-scope="scope">
              <span>{{ scope.row.caseId }}</span>
            </template>
          </el-table-column>
          <el-table-column label="用例名称" width="220">
            <template slot-scope="scope">
              <span>{{ scope.row.caseName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="用例级别" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.caseLevel }}</span>
            </template>
          </el-table-column>
          <el-table-column label="执行状态" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.caseRunStatus }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属模块" width="130">
            <template slot-scope="scope">
              <span>{{ scope.row.caseModule }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属接口" width="160">
            <template slot-scope="scope">
              <span style="text-align: center;">{{ scope.row.caseApiName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="备注" width="235">
            <template slot-scope="scope">
              <span>{{ scope.row.caseRemark }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="goToDetailPage(scope.row)" size="mini" >编辑
              </el-button>
              <el-button size="mini">执行明细
              </el-button>
              <el-button size="mini">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import ConfirmMixin from '../../assets/confirm_mixin'
import createCase from './createCase.vue'
// import editProject from './editProject.vue'
export default {
  mixins: [ConfirmMixin],
  name: 'caseList',
  data () {
    return {
      props: { multiple: true },
      caseSearchOptions: {
        api_module: [],
        caseName: '',
        runStatus: [{
          value: 0,
          label: 'Na(未执行)'
        },
        {
          value: 1,
          label: 'Pass(通过)'
        },
        {
          value: 2,
          label: 'Fail(失败)'
        }],
        caseLevel: [{
          value: 0,
          label: 'P'
        },
        {
          value: 1,
          label: 'P0'
        },
        {
          value: 2,
          label: 'P1'
        }]
      },
      caseSearchParam: { // 搜索前端展示参数
        api_module: [],
        caseName: '',
        caseLevel: '',
        runStatus: ''
      },
      caseTableData: [{
        'caseId': 1,
        'caseName': '获取选品数据列表',
        'caseLevel': 'P',
        'caseRunStatus': '通过',
        'caseModule': '选品工具',
        'caseApiName': '获取选品数据列表',
        'caseRemark': ''
      },
      {
        'caseId': 2,
        'caseName': '获取选品数据列表',
        'caseLevel': 'P',
        'caseRunStatus': '通过',
        'caseModule': '选品工具',
        'caseApiName': '获取选品数据列表',
        'caseRemark': ''
      },
      {
        'caseId': 3,
        'caseName': '获取选品数据列表',
        'caseLevel': 'P',
        'caseRunStatus': '通过',
        'caseModule': '选品工具',
        'caseApiName': '获取选品数据列表',
        'caseApiId': 3,
        'caseRemark': ''
      }],
      addCaseParams: {}
    }
  },
  methods: {
    handleSelectionChange (val) {
      console.log(val)
      this.multipleSelection = val
    },
    manualRunCase (rows) {
      console.log(rows)
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
        let param = JSON.stringify({'runningCase': rows})
        return this.$axios.post('/apiAutoTest/caseInfo/manualRunCase', param).then(response => {
          if (response.status === 200 && response.data.code === 200) {
            console.log('发送Ajax请求,请求成功', response.data)
            this.$message({
              message: '接口执行成功',
              type: 'success',
              color: 'green'
            })
            console.log(response.data['data']['runResp'])
          } else {
            this.$message({
              showClose: true,
              message: '接口执行失败',
              type: 'error'
            })
          }
        }).catch(response => {
          console.log('发送Ajax请求,' +
            '请求失败', response)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    getProRelatedModule (value) {
      return this.$axios.get('/apiAutoTest/caseInfo/options-apiModule', { params: {'selected_pro': value[0]} }).then(response => {
        this.caseSearchOptions.api_module = response.data['data']
      }).catch(error => {
        console.log('系统错误' + error)
      })
    },
    searchCase () {
      let finalParams = {}
      for (let obj in this.caseSearchParam) {
        if (obj === 'casePro' || obj === 'api_module') {
          finalParams[obj] = this.caseSearchParam[obj][0]
        } else {
          if (this.caseSearchParam[obj] === '') {
            continue
          } else {
            finalParams[obj] = this.caseSearchParam[obj]
          }
        }
      }
      return this.$axios.get('/apiAutoTest/caseInfo/caseList', { params: finalParams }).then(response => {
        console.log(finalParams)
        if (response.status === 200 && response.data.code === 200) {
          console.log('发送Ajax请求,请求成功', response.data)
          this.caseTableData = response.data['data']
          this.$message({
            message: '接口查询成功',
            type: 'success',
            color: 'green'
          })
        } else {
          this.$message({
            showClose: true,
            message: '接口查询失败',
            type: 'error'
          })
        }
      }).catch(response => {
        console.log('发送Ajax请求,' +
            '请求失败', response)
      })
    },
    onCreateCase () { // 创建项目方法
      this.confirmBox({
        title: '添加用例',
        customClass: 'createCase_confirmBox',
        closeOnClickModal: false, // 是否可通过点击遮罩关闭 MessageBox
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: '确定',
        component: createCase,
        componentName: 'createCase',
        confirmData: this.caseSearchOptions,
        confirmValidate: (action, formParms, done) => {
          if (action === 'cancel') {
            formParms.clearValidate() // 清空输入项
            return done() // done用于关闭 MessageBox 实例
          }
          formParms.validate(valid => {
            if (!valid) return
            this.addCaseParams = {...formParms.addCaseForm}
            formParms.clearValidate() // 清空输入项
            done()
            let param = JSON.stringify(this.addCaseParams)
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
    createAutoTask () {
      console.log('未完待续')
    }
  },
  mounted () {
    // 获取项目共筛选
    this.getProjectOptions().then(response => {
      for (let i in response.data) {
        this.caseSearchOptions.casePro.push(response.data[i])
      }
    })
    this.getProRelatedModule({})
  }
}
</script>

<style scoped>
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;
  }
  .el-cascader .el-input .el-input__inner {
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  .el-cascader .el-input .el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-cascader .el-input .el-input__inner:hover {
    border-color: #04aa51;
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
  .el-select.runStatus>>>.el-input__inner {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 140px;
  }
  .el-select.caseLevel>>>.el-input__inner {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 140px;
  }
  .case_module_dem {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    margin-left: -50px;
  }
  .searchCase>.el-button:focus, .el-button:hover {
    color: #ffffff;
    border-color: #04aa51;
    background-color: #04aa51;
  }
  .el-button--primary {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .select_caseName.el-input--suffix>>>.el-input__inner {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 150px;
  }
  .select_caseName.el-input>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .select_caseName.el-input>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .searchCaseBtn {
    margin-left: -30px;
  }
  .caseTableList {
    margin-top: 30px;
    border-top: 1px solid #c0c4ccb8;
  }
  .caseTableList>>>.el-table th {
    background-color: #f4f5f975;
  }
  .caseTableList>>>.el-table tr {
    background-color: #f4f5f975;
  }
</style>
