<template>
  <div class="createProject-form">
    <el-form :model="addCaseForm" status-icon :rules="rules" ref="add_fm" label-width="100px" size="small">
      <el-form-item label="用例名称" prop="caseName">
        <el-input v-model="addCaseForm.caseName" autocomplete="off" placeholder="请输入项目名称"></el-input>
      </el-form-item>
      <el-form-item label="用例等级" prop="caseLevel">
        <el-input v-model="addCaseForm.caseLevel" autocomplete="off" placeholder="请选择项目类型"></el-input>
      </el-form-item>
      <el-form-item label="所属项目" prop="casePro">
        <el-input v-model="addCaseForm.casePro" placeholder="请输入部门"></el-input>
      </el-form-item>
      <el-form-item label="所属模块" prop="caseModule">
        <el-input v-model="addCaseForm.caseModule" placeholder="请输入IT部产品线"></el-input>
      </el-form-item>
      <el-form-item label="所属接口" prop="caseApiName">
        <el-input v-model="addCaseForm.caseApiName" placeholder="请输入IT部产品线"></el-input>
      </el-form-item>
      <el-form-item label="用例备注" prop="caseRemark">
        <el-input v-model="addCaseForm.caseRemark" placeholder="请输入IT部产品线"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  name: 'createCase',
  data () {
    var checkAge = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('年龄不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字值'))
        } else {
          if (value < 18) {
            callback(new Error('必须年满18岁'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.addCaseForm.checkPass !== '') {
          this.$refs.add_fm.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.addCaseForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      addCaseForm: {
        caseName: '',
        caseLevel: '',
        casePro: '',
        caseModule: '',
        caseApiName: '',
        caseRemark: ''
      },
      rules: {
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        age: [
          { validator: checkAge, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    validate (cb) {
      return this.$refs.add_fm.validate(cb)
    },
    clearValidate () {
      this.$refs.add_fm.resetFields()
      this.$refs.add_fm.clearValidate()
    }
  }
}
</script>
<style socped>
  .el-message-box.createProject_confirmBox {
    width: 550px;
  }
  .createProject-form {
    width: 350px;
    margin-left: 20px;
  }
</style>
