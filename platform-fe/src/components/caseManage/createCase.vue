<template>
  <div class="createProject-form">
    <el-form :model="addCaseForm" status-icon ref="case_add_fm" label-width="150px" size="small">
      <el-form-item label="用例名称" prop="caseName" :rules="{required: true, message: '用例名称不能为空'}">
        <el-input v-model="addCaseForm.caseName" style="width: 300px;" autocomplete="off" clearable placeholder="请输入用例名称"></el-input>
      </el-form-item>
      <el-form-item label="用例等级" prop="caseLevel" :rules="{required: true, message: '用例级别不能为空'}">
        <el-select class="caseLevel" v-model="addCaseForm.caseLevel" style="width: 300px;" clearable placeholder="请选择用例等级">
          <el-option
            v-for="lev in caseAddOptions.caseLevel"
            :key="lev.value"
            :label="lev.label"
            :value="lev.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item
        label="所属项目"
        prop="casePro"
        :rules="{required: true, message: '所属项目不能为空'}">
        <el-select v-model="addCaseForm.casePro" style="width: 300px;"
           placeholder="请选择所属项目"
           @change="getProRelatedModule"
           clearable>
          <el-option
            v-for="pro in caseAddOptions.casePro"
            :key="pro.id"
            :label="pro.projectName"
            :value="pro.id">
            <span style="float: left; margin-right: 20px">{{ pro.projectName }}</span>
            <span style="float: right; color: #8492a6; font-size: 13px">{{ pro.id }}</span>
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="所属模块/接口" prop="caseModule">
        <el-cascader v-model="addCaseForm.caseApi_module" style="width: 300px;"
           placeholder="请选择所属模块和接口"
           :options="caseAddOptions.caseApi_module"
           :props="props"
           collapse-tags
           clearable>
          <template slot-scope="{ node, data }">
            <span>{{ data.label }}</span>
            <span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
          </template>
        </el-cascader>
      </el-form-item>
      <el-form-item label="用例备注" prop="caseRemark">
        <el-input v-model="addCaseForm.caseRemark" style="width: 300px;" placeholder="请输入用例备注"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  name: 'createCase',
  props: ['confirmData'],
  data () {
    return {
      props: { multiple: false },
      addCaseForm: {
        caseName: '',
        caseLevel: '',
        casePro: '',
        caseApi_module: [],
        caseRemark: ''
      },
      caseAddOptions: {
        casePro: [],
        caseApi_module: [],
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
      }
    }
  },
  methods: {
    validate (cb) {
      return this.$refs.case_add_fm.validate(cb)
    },
    clearValidate () {
      this.$refs.case_add_fm.resetFields()
      this.$refs.case_add_fm.clearValidate()
    },
    getProRelatedModule (value) {
      return this.$axios.get('/apiAutoTest/caseInfo/options-apiModule', { params: {'selected_pro': value} }).then(response => {
        this.caseAddOptions.caseApi_module = response.data['data']
      }).catch(error => {
        console.log('系统错误' + error)
      })
    }
  },
  mounted () {
    this.caseAddOptions.casePro = this.confirmData.casePro
  }
}
</script>
<style socped>
  .el-message-box.createCase_confirmBox {
    width: 550px;
  }
  .createProject-form {
    width: 350px;
    margin-left: 20px;
  }
</style>
