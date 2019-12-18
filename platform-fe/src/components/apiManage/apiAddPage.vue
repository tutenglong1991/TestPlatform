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
      <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
        <el-form-item label="接口名称" prop="apiName">
          <el-input autocomplete="off" placeholder="请输入接口名称"></el-input>
        </el-form-item>
        <el-form-item label="接口地址" prop="apiPath">
          <el-input autocomplete="off" placeholder="请输入接口地址"></el-input>
        </el-form-item>
        <el-form-item label="域名/ip" prop="apiDomain">
          <el-input autocomplete="off" placeholder="请选择域名/ip"></el-input>
        </el-form-item>
        <el-form-item label="网络协议" prop="netProtocol">
          <el-input autocomplete="off" placeholder="请选择网络协议"></el-input>
        </el-form-item>
        <el-form-item label="请求方式" prop="reqMethods">
          <el-input autocomplete="off" placeholder="请选择请求方式"></el-input>
        </el-form-item>
        <el-form-item label="所属分组" prop="ownGroup">
          <el-input autocomplete="off" placeholder="请选择接口分组"></el-input>
        </el-form-item>
        <el-form-item label="所属项目" prop="ownPro">
          <el-input autocomplete="off" placeholder="请选择所属项目"></el-input>
        </el-form-item>
        <el-row :gutter="20">
          <el-col :span="4"><span>参数名</span></el-col>
          <el-col :span="4"><span>参数值</span></el-col>
          <el-col :span="4"><span>是否必选</span></el-col>
          <el-col :span="4"><span>参数类型</span></el-col>
          <el-col :span="4"><span>备注</span></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="4">
            <el-input placeholder="请输入参数名" size="small" clearable></el-input>
          </el-col>
          <el-col :span="4">
            <el-input placeholder="请输入参数值" size="small" clearable></el-input>
          </el-col>
          <el-col :span="4">
            <el-input placeholder="请输入参数值" size="small" clearable></el-input>
          </el-col>
          <el-col :span="4">
            <el-input placeholder="请输入参数值" size="small" clearable></el-input>
          </el-col>
          <el-col :span="4">
            <el-input placeholder="请输入参数值" size="small" clearable></el-input>
          </el-col>
        </el-row>
        <el-form-item
          prop="email"
          :rules="[
            { required: true, message: '请输入邮箱地址', trigger: 'blur' },
            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
          ]">
          <el-input v-model="dynamicValidateForm.email"></el-input>
        </el-form-item>
        <el-form-item
          v-for="(domain, index) in dynamicValidateForm.domains"
          :label="'域名' + index"
          :key="domain.key"
          :prop="'domains.' + index + '.value'"
          :rules="{
            required: true, message: '域名不能为空', trigger: 'blur'
          }">
          <el-input v-model="domain.value"></el-input><el-button @click.prevent="removeDomain(domain)">删除</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('dynamicValidateForm')">保存</el-button>
          <el-button @click="addDomain">新增参数</el-button>
          <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</template>
<script>
export default {
  name: 'apiAddPage',
  data () {
    return {
      dynamicValidateForm: {
        domains: [{
          value: '',
          paramType: '',
          paramRemark: ''
        }],
        email: ''
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
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeDomain (item) {
      var index = this.dynamicValidateForm.domains.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.domains.splice(index, 1)
      }
    },
    addDomain () {
      this.dynamicValidateForm.domains.push({
        value: '',
        key: Date.now()
      })
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
