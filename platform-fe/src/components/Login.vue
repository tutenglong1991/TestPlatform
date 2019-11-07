<template>
  <div id="login" style="height:100%; width:100%">
    <el-container style="height:100%; width:100%">
      <el-header>
        <el-menu background-color="#161616" text-color="#ffffff" active-text-color="#ffffff">
          <el-menu-item class="platform_name">接口测试平台</el-menu-item>
          <el-menu-item class="login_btn" index='/'>
            <el-button class="login_sign_in" @click="go_to_login">Sign In</el-button>
            <el-button class="login_sign_out">Sign Out</el-button>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <div v-if="is_sign_in" class="login_message">
          <div style="margin-top: 55px">
            <el-input class="login_infos" placeholder="请输入账号" v-model="login_params.account">
            </el-input>
          </div>
          <div style="margin-top: 25px;">
            <el-input class="login_infos" placeholder="请输入密码" v-model="login_params.password">
            </el-input>
          </div>
          <el-row class="commit_login">
            <el-button>取消</el-button>
            <el-button :plain="true" type="primary" @click="login">确定</el-button>
          </el-row>
        </div>
      </el-main>
      <el-footer>© 2019 - 2020 环球易购-电子产品研发中心. All Rights Reserved.</el-footer>
    </el-container>
  </div>
</template>

<script>
import JSON from 'JSON'
export default {
  name: 'Login',
  data () {
    return {
      login_params: {
        account: 'hemeilong',
        password: '12345678'
      },
      is_sign_in: true
    }
  },
  methods: {
    go_to_login () {
      this.is_sign_in = true
    },
    login () {
      const self = this
      let param = JSON.stringify(this.login_params)
      return this.$axios.post('/login', param).then(response => {
        if (response.status === 200 && response.data.code === 200) {
          console.log('get发送Ajax请求,请求成功', response.data.message)
          this.$message({
            message: response.data.message,
            type: 'success'
          })
          self.$router.push('/home/apitest')
        } else {
          this.$message({
            showClose: true,
            message: response.data.message,
            type: 'error',
            color: 'green'
          })
        }
      }).catch(response => {
        console.log('get发送Ajax请求,' +
            '请求失败', response)
      })
    }
  },
  mounted () {
  }
}
</script>

<style scoped>
  .el-container {
    background-color: #161616;
  }
  .el-header {
    color: #ffffff;
    line-height: 60px;
    font-size: 14px;
    display: block;
    text-align: center;
  }
  .el-menu {
    border-right: solid 1px #161616;
  }
  .el-header.el-menu {
    list-style: none;
    position: relative;
    margin: 0;
    padding-left: 0;
  }
  .platform_name{
    float: left;
    margin-left: 20px;
    font-size: 17px;
    font-weight: bolder;
  }
  .login_btn{
    float: right;
  }
  .login_btn>>>.el-button {
    margin: auto;
    font-size: 17px;
    color: #ffffff;
    border-color: #161616
  }
  .login_sign_in.el-button {
    background: #04aa51;
    font-weight: bold;
  }
  .login_sign_in.el-button:hover {
    background: #0faa22;
  }
  .login_sign_out.el-button:hover {
    color: #04aa51;
    background: #161616;
  }
  /*图片居中处理*/
  /*#login {*/
  /*  background: url("../assets/login_bg.jpg");*/
  /*  background: #f4f4f4;*/
  /*  background-size: cover;*/
  /*  position: relative;*/
  /*}*/
  .login_message {
    background-color: #2e3033;
    height: 350px;
    width: 450px;
    /*以下三项为居中设置*/
    margin: auto;
    position: absolute;
    top: 0; left: 0; bottom: 0; right: 0;
    border-top: 8px solid #5c6067;
    border-left:1px solid #303133;
    border-right:1px solid #303133;
    border-bottom: 1px solid #303133;
    border-radius: 6px;
  }
  .login_infos {
    width: 65%;
    border-radius: 4px;
  }
  .login_infos>>>.el-input__inner {
    background-color: #fff0;
    border-color: #ffffff;
    color: #ffffff;
  }
  .login_infos>>>.el-input__inner::-webkit-input-placeholder {
    color: #ffffff;
    font-size: 9px;
  }
  .el-button {
    margin-top: 85px;
    color: #ffffff;
    background-color: #ffffff00;
    border-color: #ffffff
  }
  .el-button--primary:focus, .el-button--primary:hover {
    background: #04aa51;
    border-color: #04aa51;
  }
  .el-main {
    background: #161616;
  }
  .el-footer {
    width: 100%;
    color: #ffffff;
    line-height: 60px;
    font-size: 14px;
    display: block;
    text-align: center;
    margin: auto;
    border-top: 1px solid grey;
  }
</style>
