<template>
  <el-container>
    <el-header style="height:35px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/apiAutoTest/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>添加接口</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <div style="width:100%; height:50px">
        <el-form :model="apidata" ref="apidata" label-width="80px" class="demo-dynamic" style="display: flex; justify-content: left;">
          <el-form-item label="接口名称" prop="apiName">
            <el-input v-model="apidata.apiName" autocomplete="off" placeholder="请输入接口名称"></el-input>
          </el-form-item>
          <el-form-item label="接口地址" prop="apiPath">
            <el-input v-model="apidata.apiPath" autocomplete="off" placeholder="请输入接口地址"></el-input>
          </el-form-item>
          <el-form-item label="域名/ip" prop="apiDomain">
            <el-input v-model="apidata.apiDomain" autocomplete="off" placeholder="请选择域名/ip"></el-input>
          </el-form-item>
          <el-form-item label="网络协议" prop="netProtocol">
            <el-input v-model="apidata.netProtocol" autocomplete="off" placeholder="请选择网络协议"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div style="width:100%; height:50px">
        <el-form :model="apidata" ref="apidata" label-width="80px" class="demo-dynamic" style="display: flex; justify-content: left;">
          <el-form-item label="请求方式" prop="reqMethods">
            <el-input v-model="apidata.reqMethods" autocomplete="off" placeholder="请选择请求方式"></el-input>
          </el-form-item>
          <el-form-item label="设置UA" prop="reqUa">
            <el-input v-model="apidata.reqMethods" autocomplete="off" placeholder="请选择请求方式"></el-input>
          </el-form-item>
          <el-form-item label="所属分组" prop="ownGroup">
            <el-input v-model="apidata.ownGroup" autocomplete="off" placeholder="请选择接口分组"></el-input>
          </el-form-item>
          <el-form-item label="所属项目" prop="ownPro">
            <el-input v-model="apidata.ownPro" autocomplete="off" placeholder="请选择所属项目"></el-input>
          </el-form-item>
<!--          <el-form-item style="margin-left:-65px">-->
<!--            <el-button @click="addParam" type="primary" size="small">运行接口</el-button>-->
<!--            <el-button type="primary" @click="submitForm('apidata')" size="small">保存</el-button>-->
<!--          </el-form-item>-->
        </el-form>
      </div>
      <el-row style="margin-left: 12px">
          <el-button @click="addParam" type="primary" size="small">运行接口</el-button>
          <el-button type="primary" @click="submitForm('apidata')" size="small">保存</el-button>
      </el-row>
      <el-form :model="apidata" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
        <el-row :gutter="20" style="font-family: 'Avenir', Helvetica, Arial, sans-serif; font-size: 14px; color: #606266">
          <el-col :span="4" :push="1"><span>参数名称</span></el-col>
          <el-col :span="3"><span>参数值</span></el-col>
          <el-col :span="2"><span>是否必选</span></el-col>
          <el-col :span="4" :push="1"><span>类型</span></el-col>
          <el-col :span="4" :push="1"><span>备注</span></el-col>
        </el-row>
        <el-row :gutter="20" v-for="(kv, index) in apidata.parameters" :key="index" style="margin-left: 2px;">
          <el-col :span="3">
            <el-input v-model="kv.paramName" placeholder="请输入参数名" size="small" clearable></el-input>
          </el-col>
          <el-col :span="3">
            <el-input v-model="kv.paramValue" placeholder="请输入参数值" size="small" clearable></el-input>
          </el-col>
          <el-col :span="3">
            <el-input v-model="kv.isForce" placeholder="请选择是否必选" size="small" clearable></el-input>
          </el-col>
          <el-col :span="3">
            <el-input v-model="kv.paramType" placeholder="请选择参数类型" size="small" clearable></el-input>
          </el-col>
          <el-col :span="5">
            <el-input v-model="kv.paramRemark" placeholder="请输入参数备注信息" size="small" clearable></el-input>
          </el-col>
          <el-col :span="6">
            <el-button @click="addParam" type="primary" icon="el-icon-plus" size="small">新增参数</el-button>
            <el-button v-if="apidata.parameters.length>1" type="danger" @click.prevent="removeParam(kv)" icon="el-icon-minus" size="small">删除参数</el-button>
            <el-button @click="resetParm(index)" size="small">重置</el-button>
          </el-col>
        </el-row>
      </el-form>

    </el-main>
  </el-container>
</template>
<script>
export default {
  name: 'apiAddPage',
  data () {
    return {
      apidata: {
        parameters: [
          {paramName: '', paramValue: '', isForce: '', paramType: '', paramRemark: ''}
        ],
        apiName: '',
        apiPath: '',
        apiDomain: '',
        netProtocol: '',
        reqMethods: '',
        reqUa: '',
        ownGroup: '',
        ownPro: ''
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetParm (index) {
      let resetParameter = this.apidata.parameters[index]
      for (var k in resetParameter) {
        this.apidata.parameters[index][k] = ''
      }
    },
    addParam () {
      this.apidata.parameters.push({
        paramName: '',
        paramValue: '',
        isForce: '',
        paramType: '',
        paramRemark: ''
      })
    },
    removeParam (item) {
      var index = this.apidata.parameters.indexOf(item)
      if (index !== -1) {
        this.apidata.parameters.splice(index, 1)
      }
    }
  }
}
</script>
<style socped>
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;
  }
  .el-row {
    margin: 20px 0px;
    width: 80%;
    &:last-child {
    margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
