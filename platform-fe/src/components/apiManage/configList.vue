<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>功能自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/mainHeader/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>配置列表</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div class="templateSearch" style="margin-left: -25px">
        <el-form ref="searchForm" :model="searchParams" label-width="80px" style="display:flex; justify-content: left;">
          <el-row>
            <el-col :span='8'>
              <el-form-item class="templateId" label="模板id" prop="templateId">
                <el-input v-model="searchParams.templateId" autocomplete="off" placeholder="请输入配置模板id"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span='8'>
              <el-form-item class="templateName" label="模板名称" prop="templateName">
                <el-input v-model="searchParams.templateName" autocomplete="off" placeholder="请输入不同环境下接口请求域名"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span='8'>
              <el-form-item label="状态" prop="templateStatus" style="margin-left:-20px; width:250px">
                <el-select class="templateStatus" v-model="searchParams.templateStatus" clearable placeholder="请选择模板状态">
                  <el-option
                    v-for="status in multipleSelection.templateStatus"
                    :key="status.value"
                    :label="status.label"
                    :value="status.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
          <el-form-item style="margin-left: 245px">
            <el-button class="searchTemplateBtn" @click="searchTemplate" type="primary">搜索</el-button>
            <el-button class="addTemplate" @click="addTemplate">添加</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="templateTableList">
        <el-table
          ref="multipleTable"
          tooltip-effect="dark"
          @selection-change="handleSelectionChange"
          :data="templateTableData"
          style="width: 100%">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column label="模板ID" width="150">
            <template slot-scope="scope">
              <span>{{ scope.row.templateId }}</span>
            </template>
          </el-table-column>
          <el-table-column label="模板名称" width="200">
            <template slot-scope="scope">
              <span>{{ scope.row.templateName }}</span>
            </template>
          </el-table-column>
          <el-table-column label="关键信息" width="280">
            <template slot-scope="scope">
              <span>{{ scope.row.templateUrl }}</span>
            </template>
          </el-table-column>
          <el-table-column label="使用中的接口" width="400">
            <template slot-scope="scope">
              <span>{{ scope.row.usedApi }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="goToDetailPage(scope.row)" size="mini" >编辑
              </el-button>
              <el-button @click="changeStatus(scope.row)" size="mini" >禁用
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
/* eslint-disable */
export default {
  name: 'configList',
  data () {
    return {
      multipleSelection: {
        templateStatus: [{
          value: 1,
          label: '启用'
        },
        {
          value: 0,
          label: '禁用'
        },
        {
          value: 2,
          label: '全部'
        }]
      },
      searchParams: {
        templateId: null,
        templateName: null,
        templateStatus: 2
      },
      templateTableData: [
        {
          templateId: 1,
          templateName: "第一套测试环境",
          templateStatus: 1,
          usedApi: "33333,22222,1111",
          templateUrl: "http://10.40.2.62:2087/gateway/"
        },
        {
          templateId: 2,
          templateName: "第二套测试环境",
          templateStatus: 0,
          usedApi: "全部",
          templateUrl: "http://10.40.2.109:2087/gateway"
        },
      ]
    }
  },
  methods: {
    searchTemplate() {
      console.log("搜索");
      return this.$axios.get('/apiAutoTest/apiInfo/apiList', { params: this.searchParams }).then(response => {
        if (response.status === 200 && response.data.code === 200) {
          console.log('发送Ajax请求,请求成功', response.data)
          this.templateTableData = response.data['data']
          this.$message({
            message: '配置模板查询成功',
            type: 'success',
            color: 'green'
          })
        } else {
          this.$message({
            showClose: true,
            message: '配置模板查询失败',
            type: 'error'
          })
        }
      }).catch(response => {
        console.log('发送Ajax请求,' +
            '请求失败', response)
      })
    },
    addTemplate() {
      this.$router.push('/mainHeader/commonConfig')
    },
    changeStatus() {
        console.log("改变")
    },
    delTemplate() {
      console.log("删除");
    },
    handleSelectionChange (val) {
      console.log(val)
      this.multipleSelection = val
    }
  },
  mounted () {
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
  .el-form-item.ownPro>>>.el-form-item__content {
    line-height: 40px;
    position: relative;
    font-size: 14px;
    float: left; /*使所属项目水平对齐*/
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
    width: 180px;
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
    border-top: 1px solid #c0c4ccb8;
  }
  .apiTableList>>>.el-table th {
    background-color: #f4f5f975;
  }
  .apiTableList>>>.el-table tr {
    background-color: #f4f5f975;
  }
  .apiTableList>>>.cell {
    text-align: center;
  }
  .searchApi>>>.el-button.addApiBtn.el-button--default.el-button--mini {
    padding: 14px 22px;
  }
</style>
