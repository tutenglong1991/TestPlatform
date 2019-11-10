<template>
    <div class="createProject-form">
        <el-form ref="fm" :model="userData" label-width="100px" :rules="rules">
            <el-form-item label="用户名" prop="userName">
                <el-input v-model="userData.userName"/>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="userData.password"/>
            </el-form-item>
            <el-form-item label="重新密码" prop="repassword">
                <el-input v-model="userData.repassword"/>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
  name: 'createProject',
  data () {
    return {
      userData: {
        userName: '',
        password: '',
        repassword: ''
      },
      rules: {
        userName: { required: true, message: '请输入用户名', trigger: 'blur' },
        password: { required: true, message: '请输入密码', trigger: 'blur' },
        repassword: {
          validator: (rule, value, callback) => {
            if (value !== this.userData.password) {
              return callback(new Error('两次输入密码不一致'))
            }
            callback()
          },
          trigger: 'blur'
        }
      }
    }
  },
  methods: {
    validate (cb) {
      return this.$refs.fm.validate(cb)
    },
    clearValidate () {
      this.$refs.fm.resetFields()
      this.$refs.fm.clearValidate()
    }
  }
}
</script>
