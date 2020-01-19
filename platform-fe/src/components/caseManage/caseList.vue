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
          <el-form-item class="ownPro" label="所属项目" prop="ownPro">
            <el-cascader v-model="caseSearchParam.ownPro" style="width: 160px;"
               placeholder="选择用例所属项目"
               :options="caseSearchOptions.ownPro"
               :props="{ label: 'projectName', value: 'id' }"
               filterable
               clearable>
            </el-cascader>
          </el-form-item>
          <el-form-item prop="selectedParamsValue" class="choose_module_dem">
            <span class="case_module_dem">所属模块或接口</span>
            <el-cascader v-model="caseSearchParam.paramsSelectionKey" style="margin-left: 10px; width: 190px;"
               placeholder="请选择所属模块和接口"
               :options="caseSearchOptions.module_name"
               :props="props"
               collapse-tags
               clearable>
            </el-cascader>
          </el-form-item>
          <el-form-item label="用例名称" prop="caseName" style="width: 200px; margin-left: 15px;">
            <el-input class="select_caseName" v-model="finalSearchParams.creator" placeholder="请输入用例名称" clearable></el-input>
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
            <el-button @click="searchApi" class="searchApiBtn" type="primary">搜索</el-button>
            <el-button class="addApiBtn" @click="goToAddPage">添加</el-button>
            <el-button class="addApiBtn" @click="toggleSelection(multipleSelection)">执行</el-button>
          </el-form-item>
        </el-form>
      </div>
<!--      <div class="apiTableList">-->
<!--        <el-table-->
<!--          ref="multipleTable"-->
<!--          tooltip-effect="dark"-->
<!--          @selection-change="handleSelectionChange"-->
<!--          :data="apiTableData"-->
<!--          style="width: 100%">-->
<!--          <el-table-column-->
<!--            type="selection"-->
<!--            width="55">-->
<!--          </el-table-column>-->
<!--          <el-table-column label="所属项目" width="160">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.ownPro }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="所属模块" width="130">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.apiModule }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="名称" width="140">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.apiName }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="域名/IP" width="180">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.apiDomain }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="地址" width="200">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.apiPath }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="网络协议" width="100">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.netProtocol }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="请求方式" width="100">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.reqMethods }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="执行状态" width="100">-->
<!--            <template slot-scope="scope">-->
<!--              <span>{{ scope.row.runStatus }}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button @click="goToDetailPage(scope.row)" size="mini" >编辑-->
<!--              </el-button>-->
<!--              <el-button size="mini">执行日志-->
<!--              </el-button>-->
<!--              <el-button size="mini" >关联用例-->
<!--              </el-button>-->
<!--              <el-button size="mini">删除-->
<!--              </el-button>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </div>-->
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'caseList',
  data () {
    return {
      props: { multiple: true },
      caseSearchOptions: {
        ownPro: [],
        module_name: [{
          value: 'zhinan',
          label: '指南',
          children: [{
            value: 'shejiyuanze',
            label: '设计原则'
          },
          {
            value: 'cexiangdaohang',
            label: '侧向导航'
          }
          ]
        },
        {
          value: 'daohang',
          label: '导航',
          children: [{
            value: 'cexiangdaohang',
            label: '侧向导航'
          }]
        }],
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
        },
        {
          value: 3,
          label: 'P2'
        },
        {
          value: 4,
          label: 'P3'
        }]
      },
      defaultSelectedParamsLabel: '所属模块',
      finalSearchParams: {
        selectedParamsKey: '',
        selectedParamsValue: ''
      },
      caseSearchParam: { // 搜索前端展示参数
        ownPro: [],
        paramsSelectionKey: [],
        paramsSelectionValue: [{'ownModule': [], 'ownApi': []}],
        caseLevel: '',
        select_caseName: '',
        runStatus: ''
      }
    }
  },
  methods: {
    getChangedParam (selectedTtem) { // 在查询条件选择组件变更后更新查询条件的key和value，value为当前输入框输入的值
      this.finalSearchParams['selectedParamsKey'] = selectedTtem
      this.finalSearchParams.selectedParamsValue = this.finalSearchParams.selectedParamsValue[selectedTtem] // 切换后清空搜索条件
    },
    onSelectInputChange (inputValue) { // 在输入框变更时，更新查询条件组件当前选择条件对应的value
      this.finalSearchParams['selectedParamsValue'] = inputValue
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
  .searchApiBtn {
    margin-left: -30px;
  }
</style>
