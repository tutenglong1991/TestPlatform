<template>
    <div class="createProject-form">
      <el-form :model="ruleForm" status-icon :rules="rules" ref="rfm" label-width="100px" size="small">
        <el-form-item label="项目名称" prop="projectName">
          <el-input v-model="ruleForm.projectName" autocomplete="off" placeholder="请输入项目名称"></el-input>
        </el-form-item>
        <el-form-item label="项目类型" prop="projectType">
          <el-input v-model="ruleForm.projectType" autocomplete="off" placeholder="请选择项目类型"></el-input>
        </el-form-item>
        <el-form-item label="项目编号" prop="code">
          <el-input v-model.number="ruleForm.code" placeholder="请输入项目编号"></el-input>
        </el-form-item>
        <el-form-item label="所属部门" prop="dept">
          <el-input v-model="ruleForm.dept" placeholder="请输入部门"></el-input>
        </el-form-item>
        <el-form-item label="IT部产品线" prop="productLine">
          <el-input v-model="ruleForm.productLine" placeholder="请输入IT部产品线"></el-input>
        </el-form-item>
        <el-form-item label="项目周期" prop="projectCycle">
            <div class="block">
              <el-date-picker
                v-model="ruleForm.projectCycle"
                type="datetimerange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                value-format='yyyy-MM-dd HH:mm:ss'>
              </el-date-picker>
            </div>
        </el-form-item>
      </el-form>
    </div>
</template>
<script>
export default {
  name: 'createProject',
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
        if (this.ruleForm.checkPass !== '') {
          this.$refs.rfm.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      ruleForm: {
        projectName: '',
        projectType: '',
        code: '',
        dept: '',
        productLine: '',
        projectCycle: ''
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
    // submitForm (formName) {
    //   this.$refs[formName].validate((valid) => {
    //     if (valid) {
    //     } else {
    //       console.log('error submit!!')
    //       return false
    //     }
    //   })
    // },
    validate (cb) {
      return this.$refs.rfm.validate(cb)
    },
    clearValidate () {
      this.$refs.rfm.resetFields()
      this.$refs.rfm.clearValidate()
    }
    // resetForm (formName) {
    //   this.$refs[formName].resetFields()
    // }
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
