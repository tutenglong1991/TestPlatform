<template>
  <div id="login" style="height:100%; width:100%">
    <div class="login_message">
      <div style="margin-top: 50px">
        <el-input class="login_infos" placeholder="请输入账号" v-model="login_params.account">
        </el-input>
      </div>
      <div style="margin-top: 25px;">
        <el-input class="login_infos" placeholder="请输入密码" v-model="login_params.password">
        </el-input>
      </div>
      <el-row class="commit_login">
        <el-button>取消</el-button>
        <el-button type="primary" @click="login">确定</el-button>
      </el-row>
    </div>
  </div>
</template>

<script>
import JSON from 'JSON'
export default {
  name: 'Login',
  data () {
    return {
      login_params: {
        account: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      let param = JSON.stringify(this.login_params)
      return this.$axios.post('/login', param).then(response => {
        if (response.status === 200) {
          console.log('get发送Ajax请求,请求成功', response.data)
          // this.ResultOptions = response.data.testOptions
          // if (jquery.isEmptyObject(this.ResultOptions)) {
          //     this.isResultOptionsEmpty = 1
          // } else {
          //     this.isResultOptionsEmpty = 0
          // }
        }
      }).catch(response => {
        console.log('get发送Ajax请求,' +
            '请求失败', response)
      })
    }
  },
  mounted () {
    console.log(this.account)
  }
}
</script>

<style scoped>
  #login {
    background: url("../assets/login_bg.jpg");
    background-size: cover;
    position: relative;
  }
  .login_message {
    background-color: #5183c7ba;
    height: 350px;
    width: 450px;
    /*以下三项为居中设置*/
    margin: auto;
    position: absolute;
    top: 0; left: 0; bottom: 0; right: 0;
    border-top: 7px solid #0c5def99;
    border-radius: 6px;
  }
  .login_infos {
    width: 65%;
    border-radius: 4px;
    font-size: inherit;
  }
  .login_infos>>>.el-input__inner {
    background-color: #ffffff8a;
    color: #333333;
  }
  .login_infos>>>.el-input__inner::-webkit-input-placeholder {
    color: #333333;
  }
  .el-button {
    margin-top: 85px;
  }
</style>
