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
        <el-form ref="searchForm" :model="searchParams" :rules="rules" label-width="75px" style="display:flex; justify-content: left;">
          <el-form-item class="ownPro" label="所属项目" prop="ownPro">
            <el-cascader
              placeholder="请选择或输入接口所属项目"
              :options="searchParams.ownPro"
              filterable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="所属分组" prop="apiGroup" style="margin-left:30px">
            <el-cascader
              placeholder="请选择或输入接口所属分组"
              :options="searchParams.apiGroup"
              filterable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="名称/地址" prop="apiName" style="margin-left:30px">
            <el-cascader
              placeholder="请选择或输入接口所属项目"
              :options="searchParams.projects"
              filterable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="执行状态" prop="runStatus" style="margin-left:30px">
            <el-select class="runStatus" v-model="searchParams.runStatus" clearable placeholder="请选择">
              <el-option
                v-for="status in searchParams.runStatus"
                :key="status.value"
                :label="status.label"
                :value="status.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button class="searchBtn" type="primary">搜索</el-button>
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
          <el-table-column label="所属分组" width="130">
            <template slot-scope="scope">
              <span>{{ scope.row.ownGroup }}</span>
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
              <span>{{ scope.row.reqMethod }}</span>
            </template>
          </el-table-column>
          <el-table-column label="执行状态" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.runState }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini">执行日志
              </el-button>
              <el-button size="mini" >详情
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
      searchParams: {
        ownPro: [],
        apiGroup: [],
        apiName: [],
        runStatus: []
      },
      rules: {
        selectedParamsKey: [{require: true, message: '请选择任一种搜索方式', trigger: 'blur'}],
        selectedParamsValue: [{require: false, trigger: 'blur'}],
        creator: [{require: false, trigger: 'blur'}],
        status: [{require: false, trigger: 'blur'}]
      },
      apiTableData: [{
        'ownPro': '选推服务',
        'ownGroup': '选品服务',
        'apiName': '获取汇率',
        'apiDomain': 'www.trader-gb.com',
        'apiPath': 'cockpit/public/site-currency-list',
        'netProtocol': 'http',
        'reqMethod': 'get',
        'runState': '成功'
      },
      {
        'ownPro': '选推服务',
        'ownGroup': '选品服务',
        'apiName': '获取ips数据',
        'apiDomain': 'www.trader-gb.com',
        'apiPath': 'cockpit/public/main-data',
        'netProtocol': 'http',
        'reqMethod': 'get',
        'runState': '失败'
      }],
      multipleSelection: []
    }
  },
  methods: {
    getSearchParams () {

    },
    goToAddPage () {
      this.$router.push('/apiAutoTest/apiAddPage')
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
