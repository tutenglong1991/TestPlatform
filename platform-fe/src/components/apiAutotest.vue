<template>
  <el-container>
    <el-aside style="width: 200px; height: 100%">
      <el-menu style="height: 100%"
        active-text-color="#04aa51"
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-user-solid"></i>
            <span>项目管理</span>
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">接口管理</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-document"></i>
          <span slot="title">用例管理</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-bell"></i>
          <span slot="title">任务设置</span>
        </el-menu-item>
        <el-menu-item index="5">
          <i class="el-icon-s-data"></i>
          <span slot="title">测试报告</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <div class="open-platform">
        <div class="open-platform-title">
          <h3>GBO选推项目接口测试</h3>
        </div>
        <div class="op-create">
          <el-tabs v-model="activeName"
                   @tab-click="handleClick"
                   type="card">
            <el-tab-pane label="登录接口"
                         name="first">
              <login></login>
            </el-tab-pane>
            <el-tab-pane label="作品列表"
                         name="second">
              <appList></appList>
            </el-tab-pane>
            <el-tab-pane label="作品设置"
                         name="third">
              <setting></setting>
            </el-tab-pane>
            <el-tab-pane label="创建作品"
                         name="fourth">
              <createApp></createApp>
            </el-tab-pane>
            <el-tab-pane label="修改作品"
                         name="fiveth">
              <editApp></editApp>
            </el-tab-pane>
            <el-tab-pane label="作品信息"
                         name="sixth">
              <getAppInfoByIds></getAppInfoByIds>
            </el-tab-pane>
            <el-tab-pane label="删除作品"
                         name="seventh">
              <deleteApp></deleteApp>
            </el-tab-pane>
            <el-tab-pane label="封禁作品"
                         name="eighth">
              <appBlock></appBlock>
            </el-tab-pane>
            <el-tab-pane label="作品转模板"
                         name="ninth">
              <transToTemplate></transToTemplate>
            </el-tab-pane>
            <el-tab-pane label="模板列表"
                         name="tenth">
              <templateList></templateList>
            </el-tab-pane>
            <el-tab-pane label="模板分类"
                         name="eleventh">
              <templateClass></templateClass>
            </el-tab-pane>
            <el-tab-pane label="渠道列表"
                         name="twelfth">
              <channelList></channelList>
            </el-tab-pane>
            <el-tab-pane label="分发列表"
                         name="thirteenth">
              <listByChannelId></listByChannelId>
            </el-tab-pane>
            <el-tab-pane label="获取客户所打标签"
                         name="fourteen">
              <tagList></tagList>
            </el-tab-pane>
            <el-tab-pane label="获取客户列表"
                         name="fifteen">
              <idList></idList>
            </el-tab-pane>
            <el-tab-pane label="获取客户详情"
                         name="sixteen">
              <audienceDetail></audienceDetail>
            </el-tab-pane>
            <el-tab-pane label="获取客户标签库列表"
                         name="seventeen">
              <tagLibList></tagLibList>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'apiAutotest',
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
  .open-platform {
    width: 95%;
    margin: 0px auto;
  }
  .open-platform-title {
    text-align: center;
    margin: 10px 0px;
    font-size: 16px;
  }
  .op-create {
    margin-top: 30px;
  }
</style>
