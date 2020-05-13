<template>
  <el-container>
    <el-header style="height:15px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>接口自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/apiAutoTest/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>接口详情</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <h1>由【XXX】创建，【XXX】最后修改于【XXXX年-XX月-XX日 XX时-XX分】
        <a href="http://127.0.0.1:8080/#/apiAutoTest/apiDetail/" style="color:#04aa51">查看修改记录</a>
      </h1>
      <el-form :model="apidata" ref="submitForm1" :rules="rules" label-width="80px" class="demo-dynamic" style="width:85%">
        <el-row>
          <el-col :span='6'>
            <el-form-item label="接口名称" prop="apiName">
              <el-input v-model="apidata.apiName" autocomplete="off" placeholder="请输入接口名称"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="接口地址" prop="apiPath">
             <el-input v-model="apidata.apiPath" autocomplete="off" placeholder="请输入接口地址"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="域名/ip" prop="apiDomain">
              <el-input v-model="apidata.apiDomain" autocomplete="off" placeholder="请选择域名/ip"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="网络协议" prop="netProtocol">
              <el-select v-model="apidata.netProtocol" clearable autocomplete="off" placeholder="请选择网络协议">
                <el-option
                  v-for="h in apiDataSelection.netProtocol"
                  :key="h.value"
                  :label="h.label"
                  :value="h.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span='6'>
            <el-form-item label="请求方式" prop="reqMethods">
              <el-select v-model="apidata.reqMethods" clearable autocomplete="off" placeholder="请选择请求方式">
                <el-option
                  v-for="m in apiDataSelection.reqMethods"
                  :key="m.value"
                  :label="m.label"
                  :value="m.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="请求头" prop="reqUa">
              <el-input v-model="apidata.reqUa" autocomplete="off" placeholder="设置请求头不设置即为默认值">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="所属项目" prop="ownPro">
              <el-select v-model="apidata.ownPro" clearable autocomplete="off" placeholder="请选择所属项目">
                <el-option
                  v-for="item in apiDataSelection.projectOptions"
                  :key="item.id"
                  :label="item.projectName"
                  :value="item.id">
                  <span style="float: left">{{ item.projectName }}</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">{{ item.id }}</span>
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span='6'>
            <el-form-item label="所属模块" prop="apiModule">
              <el-input v-model="apidata.apiModule" autocomplete="off" placeholder="请选择接口分组"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-link :underline="false" v-model="apidata" type="success">URL：{{ (this.apiDataSelection.netProtocol[this.apidata.netProtocol]).label + '://' + this.apidata.apiDomain + this.apidata.apiPath }}</el-link>
      </el-form>
      <el-row style="margin-left: 12px">
        <el-button v-if="apidata.parameters.length===0" @click="addParam" type="primary" icon="el-icon-plus" size="small">新增参数</el-button>
        <el-button @click="addParam" type="primary" size="small" disabled>格式化请求入参</el-button>
        <el-button @click="runSingleApi('submitForm1', 'submitForm2')" type="primary" size="small">运行接口</el-button>
        <el-button type="primary" @click="editApi('submitForm1', 'submitForm2')" size="small">保存</el-button>
      </el-row>
      <el-input class='create-text' type="textarea" :rows="10" placeholder="请求参数..." v-model="reqTextarea" style="margin-left:12px; width:45%;">
      </el-input>
      <el-input class='create-text' type="textarea" :rows="10" placeholder="返回参数..." v-model="respTextarea" style="margin-left:12px; width:45%;">
      </el-input>
      <el-form :model="apidata" ref="submitForm2" label-width="0px">
        <el-row :gutter="20" style="font-family: 'Avenir', Helvetica, Arial, sans-serif; font-size: 14px; color: #606266">
          <el-col :span="4" :push="1"><span>参数名称</span></el-col>
          <el-col :span="3"><span>参数值</span></el-col>
          <el-col :span="2" :push="1"><span>是否必选</span></el-col>
          <el-col :span="4" :push="2"><span>类型</span></el-col>
          <el-col :span="4" :push="2"><span>注释</span></el-col>
        </el-row>
        <el-row :gutter="20" v-for="(kv, index) in apidata.parameters" :key="kv.key" style="margin-left: 2px;">
          <el-col :span="3">
            <el-form-item
              :prop="'parameters.' + index + '.paramName'"
              :rules="[{ required: true, message: '参数名不能为空', trigger: 'blur' }]"
            >
              <el-input v-model="kv.paramName" placeholder="请输入参数名" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="4">
            <el-form-item prop="paramValue">
              <el-input v-model="kv.paramValue" placeholder="请输入参数值" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="3" class="params_options">
            <el-form-item
              :prop="'parameters.' + index + '.isForce'"
              :rules="[{ required: true, message: '参数是否必选不能为空', trigger: 'change' }]"
            >
              <el-select v-model="kv.isForce" clearable autocomplete="off" placeholder="请选择是否必选">
                <el-option
                  v-for="op in apiDataSelection.isForce"
                  :key="op.value"
                  :label="op.label"
                  :value="op.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="3" class="params_options">
            <el-form-item
              :prop="'parameters.' + index + '.paramType'"
              :rules="[{ required: true, message: '参数类型不能为空', trigger: 'change' }]"
            >
              <el-select v-model="kv.paramType" clearable autocomplete="off" placeholder="请选择参数类型">
                <el-option
                  v-for="op in apiDataSelection.paramType"
                  :key="op.value"
                  :label="op.label"
                  :value="op.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="5" prop="paramRemark">
            <el-form-item>
              <el-input v-model="kv.paramRemark" placeholder="请输入参数备注信息" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6" style="margin-top:5px">
            <el-button @click="addParam" type="primary" icon="el-icon-plus" size="small">新增参数</el-button>
            <el-button type="danger" @click.prevent="removeParam(kv)" icon="el-icon-minus" size="small">删除参数</el-button>
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
      apiDataSelection: {
        netProtocol: [{
          value: 0,
          label: 'http'
        },
        {
          value: 1,
          label: 'https'
        }],
        reqMethods: [{
          value: 0,
          label: 'get'
        },
        {
          value: 1,
          label: 'post'
        }],
        isForce: [
          {label: 'Y', value: 'Y'},
          {label: 'N', value: 'N'}
        ],
        paramType: [
          {label: 'String', value: 'String'},
          {label: 'Int', value: 'Int'},
          {label: 'float', value: 'float'},
          {label: 'boolean', value: 'boolean'},
          {label: 'Array', value: 'Array'},
          {label: 'Object', value: 'Object'}],
        projectOptions: []
      },
      apidata: {
        parameters: [],
        apiName: null,
        apiPath: null,
        apiDomain: null,
        netProtocol: null,
        reqMethods: null,
        reqUa: '{"Accept-Encoding": "utf-8","User-Agent": "hemeilong","Content-Type": "application/x-www-form-urlencoded"}',
        apiModule: null,
        ownPro: null,
        runStatus: 0
      },
      reqTextarea: '',
      respTextarea: '',
      rules: {
        apiName: [{ required: true, message: '接口名称不能为空', trigger: 'blur', color: 'green' }],
        apiPath: [{ required: true, message: '接口地址不能为空', trigger: 'blur' }],
        apiDomain: [{ required: true, message: '接口域名或ip不能为空', trigger: 'blur' }],
        netProtocol: [{ required: true, message: '网络协议不能为空', trigger: 'change' }],
        reqMethods: [{ required: true, message: '请求方式不能为空', trigger: 'change' }],
        apiModule: [{ required: true, message: '所属模块不能为空', trigger: 'blur' }],
        ownPro: [{ required: true, message: '所属项目不能为空', trigger: 'change' }]
      },
      isParamsCheckedPass: false
    }
  },
  methods: {
    editApi (formName1, formName2) { // 第一个参数是接口必要信息表单，第二个参数是接口对应参数的表单
      this.validParams(formName2)
      this.$refs[formName1].validate((valid) => {
        if (valid && this.isParamsCheckedPass) {
          let param = JSON.stringify(this.apidata)
          return this.$axios.post('/apiAutoTest/apiInfo/editApi', param).then(response => {
            if (response.status === 200 && response.data.code === 200) {
              console.log('发送Ajax请求,请求成功', response.data)
              this.$message({
                message: '接口修改成功',
                type: 'success',
                color: 'green'
              })
              // this.$router.push('/apiAutoTest/apiList')
            } else {
              this.$message({
                showClose: true,
                message: '接口修改失败',
                type: 'error'
              })
            }
          }).catch(response => {
            console.log('发送Ajax请求,' +
            '请求失败', response)
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    runSingleApi (formName1, formName2) {
      this.validParams(formName2)
      this.$refs[formName1].validate((valid) => {
        if (valid && this.isParamsCheckedPass) {
          let param = JSON.stringify(this.apidata)
          return this.$axios.post('/apiAutoTest/apiInfo/runSingleApi', param).then(response => {
            console.log(response.data)
            if (response.status === 200 && response.data.code === 200) {
              console.log('发送Ajax请求,请求成功', response.data)
              this.$message({
                message: '接口执行成功',
                type: 'success',
                color: 'green'
              })
              this.respTextarea = response.data['data']['runResp']
              console.log(response.data['data']['runResp'])
              this.reqTextarea = response.data['data']['runParam']
            } else {
              this.$message({
                showClose: true,
                message: '接口执行失败',
                type: 'error'
              })
            }
          }).catch(response => {
            console.log('发送Ajax请求,' +
            '请求失败', response)
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    validParams (formName) {
      if (this.apidata.parameters.length !== 0) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.isParamsCheckedPass = true
            console.log(this.apidata.parameters)
          } else {
            console.log('error submit!!')
            console.log(this.apidata.parameters)
            this.isParamsCheckedPass = false
          }
        })
      } else { // 若无参数则不需要校验参数必填项
        this.isParamsCheckedPass = true
      }
    },
    getApiParameter () {
      let apiObj = {'id': this.$route.params.id}
      this.apidata['id'] = this.$route.params.id // 给apidata加上接口id，便于后面编辑传给后端
      return this.$axios.get('/apiAutoTest/apiInfo/parameterOfApi', { params: apiObj }).then(response => {
        if (response.status === 200 && response.data.code === 200) {
          console.log('发送Ajax请求,请求成功', response.data)
          this.apidata.parameters = response.data['data']
          // this.queryProject('searchForm')保存成功后回到列表页
        } else {
          this.$message({
            showClose: true,
            message: '获取接口参数失败',
            type: 'error'
          })
        }
      }).catch(response => {
        console.log('发送Ajax请求,' +
        '请求失败', response)
      })
    },
    resetParm (index) {
      let resetParameter = this.apidata.parameters[index]
      for (let k in resetParameter) {
        this.apidata.parameters[index][k] = ''
      }
    },
    addParam () {
      this.apidata.parameters.push({
        id: null,
        paramName: '',
        paramValue: '',
        isForce: '',
        paramType: '',
        paramRemark: '',
        ownApi_id: this.$route.params.id
      })
    },
    removeParam (item) {
      let index = this.apidata.parameters.indexOf(item)
      if (index !== -1) {
        this.apidata.parameters.splice(index, 1)
      }
    },
    fallbackEditDate () {
      console.log(this.$route.params)
      this.apidata.apiName = this.$route.params.apiName
      this.apidata.apiPath = this.$route.params.apiPath
      this.apidata.apiDomain = this.$route.params.apiDomain
      if (this.$route.params.netProtocol === 'http') {
        this.apidata.netProtocol = 0
      } else if (this.$route.params.netProtocol === 'https') {
        this.apidata.netProtocol = 1
      }
      if (this.$route.params.reqMethods === 'get') {
        this.apidata.reqMethods = 0
      } else if (this.$route.params.reqMethods === 'post') {
        this.apidata.reqMethods = 1
      }
      if (this.$route.params.runStatus === '未执行') {
        this.apidata.runStatus = 0
      } else if (this.$route.params.runStatus === '成功') {
        this.apidata.runStatus = 1
      } else if (this.$route.params.runStatus === '失败') {
        this.apidata.runStatus = 2
      }
      this.apidata.reqUa = this.$route.params.reqUa
      this.apidata.apiModule = this.$route.params.apiModule
    }
  },
  created () {
    this.fallbackEditDate()
  },
  mounted () {
    // 获取项目共筛选
    this.getProjectOptions().then(response => {
      this.apiDataSelection.projectOptions = response.data
      for (let index in this.apiDataSelection.projectOptions) {
        if (this.apiDataSelection.projectOptions[index]['projectName'] === this.$route.params.ownPro) {
          this.apidata.ownPro = this.apiDataSelection.projectOptions[index]['id']
        }
      }
    })
    this.getApiParameter()
  }
}
</script>

<style scoped>
  h1 {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-size: 14px;
    margin-bottom: 10px;
    color: #606266;
    line-height: 40px;
    margin-left: 12px;
  }
  .el-form.demo-dynamic {
    border-bottom: 1px solid #c0c4cc;
  }
  .el-link {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-size: 14px;
    color: #606266;
    line-height: 10px;
    margin-left: 12px;
    margin-bottom: 10px;
  }
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
  .params_options>>>.el-select .el-input__inner {
    height: 32px;
    margin-top: 4px;
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
  .el-button--primary {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .el-button--primary:hover {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .el-button--primary:focus {
    color: #FFF;
    background-color: #04aa51;
    border-color: #04aa51;
  }
  .el-select .el-input__inner:hover {
    border-color: #04aa51;
  }
  .el-select .el-input__inner:focus {
    border-color: #04aa51;
  }
  .el-select .el-input.is-focus .el-input__inner {
    border-color: #04aa51;
  }
  .el-input__inner:hover {
    border-color: #04aa51;
  }
  .el-input.is-active .el-input__inner, .el-input__inner:focus {
    border-color: #04aa51;
  }
</style>
