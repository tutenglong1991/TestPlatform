<template>
  <div class="createProject-form">
    <el-form :model="addRuleForm" status-icon :rules="rules" ref="add_fm" label-width="100px" size="small">
      <el-form-item label="项目名称" prop="projectName">
        <el-input v-model="addRuleForm.projectName" autocomplete="off" placeholder="请输入项目名称"></el-input>
      </el-form-item>
      <el-form-item label="项目类型" prop="projectType">
        <el-input v-model="addRuleForm.projectType" autocomplete="off" placeholder="请选择项目类型"></el-input>
      </el-form-item>
      <el-form-item label="项目编号" prop="code">
        <el-input v-model.number="addRuleForm.code" placeholder="请输入项目编号"></el-input>
      </el-form-item>
      <el-form-item label="所属部门" prop="dept">
        <el-input v-model="addRuleForm.dept" placeholder="请输入部门"></el-input>
      </el-form-item>
      <el-form-item label="IT部产品线" prop="productLine">
        <el-input v-model="addRuleForm.productLine" placeholder="请输入IT部产品线"></el-input>
      </el-form-item>
      <el-form-item label="项目周期" prop="projectCycle">
          <div class="block">
            <el-date-picker
              v-model="addRuleForm.projectCycle"
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
    let checkAge = (rule, value, callback) => {
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
    let validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.addRuleForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      addRuleForm: {
        projectName: '',
        projectType: '',
        code: '',
        dept: '',
        productLine: '',
        projectCycle: ''
      },
      rules: {
        checkPass: [{ validator: validatePass2, trigger: 'blur' }],
        age: [{ validator: checkAge, trigger: 'blur' }]
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
