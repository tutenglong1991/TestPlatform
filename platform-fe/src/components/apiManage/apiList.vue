<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/apiAutoTest/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>接口列表</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div class="searchApi">
        <el-form ref="searchForm" :model="searchParams" label-width="75px" style="display:flex; justify-content: left;">
          <el-form-item class="ownPro" label="所属项目" prop="ownPro">
            <el-cascader v-model="searchParams.ownPro"
              placeholder="请选择或输入接口所属项目"
              :options="multipleSelection.ownPro"
              :props="{ label: 'projectName', value: 'id' }"
              filterable
              clearable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="所属模块" prop="apiModule" style="margin-left:30px">
            <el-cascader v-model="searchParams.apiModule"
              placeholder="请选择接口所属模块"
              :options="multipleSelection.apiModule"
              filterable
              clearable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="名称/地址" prop="apiName" style="margin-left:30px">
            <el-select :filterable=true v-model="searchParams.apiName" clearable placeholder="请选择接口">
              <el-option
                v-for="n in multipleSelection.apiName"
                :key="n.apiName"
                :label="n.apiPath"
                :value="n.apiName">
                <span style="float: left; margin-right: 20px">{{ n.apiName }}</span>
                <span style="float: right; color: #8492a6; font-size: 13px">{{ n.apiPath }}</span>
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="执行状态" prop="runStatus" style="margin-left:30px">
            <el-select class="runStatus" v-model="searchParams.runStatus" clearable placeholder="请选择接口执行状态">
              <el-option
                v-for="status in multipleSelection.runStatus"
                :key="status.value"
                :label="status.label"
                :value="status.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button @click="searchApi" class="searchApiBtn" type="primary">搜索</el-button>
            <el-button class="addApiBtn" size="mini" @click="goToAddPage">添加</el-button>
            <el-button class="addApiBtn" size="mini" @click="toggleSelection(multipleSelection)">执行</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="apiTableList">
        <el-table
          ref="multipleTable"
          tooltip-effect="dark"
          @selection-change="handleSelectionChange"
          :data="apiTableData"
          style="width: 100%">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column label="所属项目" width="160">
            <template slot-scope="scope">
              <span>{{ scope.row.ownPro }}</span>
            </template>
          </el-table-column>
          <el-table-column label="所属模块" width="130">
            <template slot-scope="scope">
              <span>{{ scope.row.apiModule }}</span>
            </template>
          </el-table-column>
          <el-table-column label="名称" width="140">
            <template slot-scope="scope">
              <span>{{ scope.row.apiName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="域名/IP" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.apiDomain }}</span>
            </template>
          </el-table-column>
          <el-table-column label="地址" width="200">
            <template slot-scope="scope">
              <span>{{ scope.row.apiPath }}</span>
            </template>
          </el-table-column>
          <el-table-column label="网络协议" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.netProtocol }}</span>
            </template>
          </el-table-column>
          <el-table-column label="请求方式" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.reqMethods }}</span>
            </template>
          </el-table-column>
          <el-table-column label="执行状态" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.runStatus }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="goToDetailPage" size="mini" >详情
              </el-button>
              <el-button size="mini">执行日志
              </el-button>
              <el-button size="mini" >关联用例
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
export default {
  name: 'apiList',
  data () {
    return {
      multipleSelection: {
        ownPro: [],
        apiModule: [],
        apiName: [],
        runStatus: [{
          value: 0,
          label: '未执行'
        },
        {
          value: 1,
          label: '成功'
        },
        {
          value: 2,
          label: '失败'
        }]
      },
      apiTableData: [],
      searchParams: {
        ownPro: [],
        apiModule: [],
        apiName: [],
        runStatus: ''
      }
    }
  },
  methods: {
    searchApi () {
      // let param = JSON.stringify(this.searchParams)
      let finalParams = {}
      for (let obj in this.searchParams) {
        if (obj === 'ownPro' || obj === 'apiModule') {
          finalParams[obj] = this.searchParams[obj][0]
        } else {
          if (this.searchParams[obj] === '') {
            continue
          } else {
            finalParams[obj] = this.searchParams[obj]
          }
        }
      }
      return this.$axios.get('/apiAutoTest/apiInfo/apiList', { params: finalParams }).then(response => {
        if (response.status === 200 && response.data.code === 200) {
          console.log('发送Ajax请求,请求成功', response.data)
          this.apiTableData = response.data['data']
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
    // 获取接口和模块供搜索下拉选项
    getApisAndModules () {
      return this.$axios.get('/apiAutoTest/apiInfo/options-apiModule').then(response => {
        let apiObj = response.data['data']
        for (let i in apiObj) {
          this.multipleSelection.apiModule.push({label: apiObj[i]['apiModule'], value: apiObj[i]['apiModule']})
          this.multipleSelection.apiName.push({apiName: apiObj[i]['apiName'], apiPath: apiObj[i]['apiPath']})
        }
      }).catch(error => {
        console.log('系统错误' + error)
      })
    },
    goToAddPage () {
      this.$router.push('/apiAutoTest/apiAddPage')
    },
    goToDetailPage () {
      this.$router.push('/apiAutoTest/apiDetail')
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          console.log(row)
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      console.log(val)
      this.multipleSelection = val
    }
  },
  mounted () {
    // 获取项目共筛选
    this.getProjectOptions().then(response => {
      for (let i in response.data) {
        this.multipleSelection.ownPro.push(response.data[i])
      }
    })
    this.getApisAndModules()
    this.searchApi()
  }
}
</script>

<style scoped>
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;
  }
  .el-form-item.ownPro>>>.el-form-item__label {  /* 首个搜索项对齐*/
    text-align: left !important;
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
  .el-select.runStatus>>>.el-input__inner {
    color: #606266;
    font-size: 14px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 100px;
  }
  .el-select.runStatus>>>.el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-select.runStatus>>>.el-input__inner:hover {
    border-color: #04aa51;
  }
  .searchBtn {
    margin-left: 100px;
  }
  .searchApi>.el-button:focus, .el-button:hover {
    color: #ffffff;
    border-color: #04aa51;
    background-color: #04aa51;
  }
  .el-button--primary {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .apiTableList {
    margin-top: 30px;
  }
  .apiTableList>>>.el-table th {
    background-color: #f4f5f975;
  }
  .apiTableList>>>.el-table tr {
    background-color: #f4f5f975;
  }
  .searchApi>>>.el-button.addApiBtn.el-button--default.el-button--mini {
    padding: 14px 22px;
  }
</style>
