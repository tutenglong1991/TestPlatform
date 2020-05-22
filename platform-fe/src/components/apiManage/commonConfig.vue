<template>
  <el-container>
    <el-header style="height:15px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item>功能自动化</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/mainHeader/apiList'}">接口管理</el-breadcrumb-item>
        <el-breadcrumb-item>公共配置</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>
    <el-main>
      <el-form :model="commonSet" ref="submitForm1" label-width="80px" class="add_http_default" >
        <el-row>
          <h1>http默认配置</h1>
        </el-row>
        <el-row>
          <el-col :span='8'>
            <el-form-item label="网络协议" prop="netProtocol">
              <el-select v-model="commonSet.httpDefault.netProtocol" clearable autocomplete="off" placeholder="请选择网络协议如http或https">
                <el-option
                  v-for="m in httpDefaultSelection.netProtocol"
                  :key="m.value"
                  :label="m.label"
                  :value="m.value"
                >
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span='8'>
            <el-form-item label="请求方式" prop="reqMethods">
              <el-select v-model="commonSet.httpDefault.reqMethods" clearable autocomplete="off" placeholder="请选择get或post方式">
                <el-option
                  v-for="h in httpDefaultSelection.reqMethods"
                  :key="h.value"
                  :label="h.label"
                  :value="h.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span='8'>
            <el-form-item label="域名或IP" prop="apiDomain" style="width:310px">
              <el-input v-model="commonSet.httpDefault.apiDomain" autocomplete="off" placeholder="请输入不同环境下接口请求域名"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="16" style="border-bottom: 1px solid #c0c4cc;">
          <el-col :span='8'>
            <el-form-item label="请求端口" prop="apiPort" style="width:297px">
              <el-input v-model="commonSet.httpDefault.apiPort" autocomplete="off" placeholder="请输入接口地址"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span='8'>
            <el-form-item label="接口路径" prop="apiPath" style="width:297px">
              <el-input v-model="commonSet.httpDefault.apiPath" autocomplete="off" placeholder="请输入接口地址"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
            <h1>添加请求头配置</h1>
        </el-row>
        <el-row v-for="(kv, index) in commonSet.httpHeaderDefault" :key="kv.key">
          <el-col :span="8">
            <el-form-item label="属性" prop="attrName" style="width:297px">
              <el-input v-model="kv.attrName" placeholder="请输入属性名" autocomplete="off" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="属性值" prop="'attrValue'" style="width:297px">
              <el-input v-model="kv.attrValue" placeholder="请输入属性值" autocomplete="off" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="8" style="margin-top:5px;">
            <el-button @click="add(1)" type="success" icon="el-icon-plus" size="small">添加属性</el-button>
            <el-button v-if="commonSet.httpHeaderDefault.length != 1" type="danger" @click.prevent="remove(kv, 1)" icon="el-icon-minus" size="small">删除属性</el-button>
            <el-button @click="reset(index, 1)" size="small">重置</el-button>
          </el-col>
        </el-row>
      </el-form>
      <el-form :model="commonSet" ref="submitForm2" label-width="80px" class="add_user_variable">
        <el-row>
          <h1>新增自定义变量</h1>
        </el-row>
        <el-row v-for="(kv, index) in commonSet.userDefinedCommonVar" :key="kv.key">
          <el-col :span="8">
            <el-form-item label="变量" prop="varName" style="width:297px">
              <el-input v-model="kv.varName" placeholder="请输入变量名" autocomplete="off" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="变量值" prop="varValue" style="width:297px">
              <el-input v-model="kv.varValue" placeholder="请输入变量值"  autocomplete="off" size="small" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="8" style="margin-top:5px;">
            <el-button @click="add(2)" type="success" icon="el-icon-plus" size="small">添加变量</el-button>
            <el-button v-if="commonSet.userDefinedCommonVar.length != 1" type="danger" @click.prevent="remove(kv, 2)" icon="el-icon-minus" size="small">删除变量</el-button>
            <el-button @click="reset(index, 2)" size="small">重置</el-button>
          </el-col>
        </el-row>
      </el-form>
      <el-form :model="commonSet" ref="submitForm3" class="add_affected_apis">
        <el-row>
          <h1>选择或批量更新需要使用该默认配置的接口</h1>
        </el-row>
        <el-row style="margin-left: -10px">
          <el-form-item prop="api_module" class="choose_apis_apply_configs">
            <el-cascader v-model="commonSet.relApiList" style="margin-left: 10px; width: 350px;"
               placeholder="请选择需要使用该配置的接口，不选择默认全部接口适用"
               :options="apiListSelections"
               :props="props"
               collapse-tags
               clearable>
              <template slot-scope="{ node, data }">
                <span>{{ data.label }}</span>
                <span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
              </template>
            </el-cascader>
          </el-form-item>
        </el-row>
      </el-form>
      <el-row class="confirm_configs">
        <el-button @click="submitConfig" type="success" size="middle">批量更新</el-button>
        <el-button @click="cancelConfig" size="middle">取消</el-button>
      </el-row>
    </el-main>
  </el-container>
</template>
<script>
/* eslint-disable */
export default {
  name: 'commonConfig',
  data () {
    return {
      props: { multiple: true },
      commonSet: {
        httpDefault: {
          netProtocol: null,
          reqMethods: null,
          apiDomain: null,
          apiPort: null,
          apiPath: null
        },
        httpHeaderDefault: [{}],
        userDefinedCommonVar: [{}],
        relApiList: []
      },
      httpDefaultSelection: {
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
        }]
      },
      apiListSelections: [{"value": "\u9009\u54c1\u670d\u52a1", "label": "\u9009\u54c1\u670d\u52a1", "children": [{"value": "\u83b7\u53d6ips\u6570\u636e\u5217\u8868", "label": "\u83b7\u53d6ips\u6570\u636e\u5217\u8868"}, {"value": "\u83b7\u53d6ips\u53d1\u52a8\u673a", "label": "\u83b7\u53d6ips\u53d1\u52a8\u673a"}]}, {"value": "\u9009\u63a8\u4efb\u52a1\u7ba1\u7406", "label": "\u9009\u63a8\u4efb\u52a1\u7ba1\u7406", "children": [{"value": "\u9009\u63a8\u81ea\u8425\u4efb\u52a1\u5217\u8868", "label": "\u9009\u63a8\u81ea\u8425\u4efb\u52a1\u5217\u8868"}]}]
    }
  },
  methods: {
    reset (index, type) {
      if (type === 1) {
        let resetHeaders = this.commonSet.httpHeaderDefault[index]
        for (let k in resetHeaders) {
          this.commonSet.httpHeaderDefault[index][k] = ''
        }
      } else {
        let resetUserVariable = this.commonSet.userDefinedCommonVar[index]
        for (let k in resetUserVariable) {
          this.commonSet.userDefinedCommonVar[index][k] = ''
        }
      }
    },
    add (type) {
      if (type === 1) {
        this.commonSet.httpHeaderDefault.push({
          'attrName': '',
          'attrValue': ''
        })
      } else {
        this.commonSet.userDefinedCommonVar.push({
          'varName': '',
          'varValue': ''
        })
      }
    },
    remove (item, type) {
      if (type === 1) {
        let index = this.commonSet.httpHeaderDefault.indexOf(item)
        if (index !== -1) {
          this.commonSet.httpHeaderDefault.splice(index, 1)
        }
      } else {
        let index = this.commonSet.userDefinedCommonVar.indexOf(item)
        if (index !== -1) {
          this.commonSet.userDefinedCommonVar.splice(index, 1)
        }
      }
    }
  },
  mounted () {
  }
}
</script>
<style socped>
  .el-breadcrumb>>>.el-breadcrumb__inner.is-link:hover {
    color: #04aa51;
  }
  h1 {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-size: 14px;
    margin-bottom: 10px;
    color: #606266;
    line-height: 40px;
    margin-left: 12px;
    font-weight: bold;
  }
  .el-form.add_http_default {
    width: 70%;
    border-bottom: 1px solid #c0c4cc;
  }
  .el-form.add_user_variable {
    width: 70%;
    border-bottom: 1px solid #c0c4cc;
  }
  .el-form.add_affected_apis {
    width: 70%;
    margin-top: 20px;
  }
  .el-row.confirm_configs {
    margin-top: 30px;
  }
  .el-button--success {
    color: #ffffff;
    background: #04aa51;
    border-color: #04aa51;
  }
  .el-button--success:focus, .el-button--success:hover {
    color: #ffffff;
    background: #04aa51;
    border-color: #04aa51;
  }

  .el-col {
    border-radius: 4px;
  }
  .add_user_variable.el-select .el-input__inner {
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
