<template>
  <center>
    <div style="position: absolute;right: 7%;bottom: 10%;">
      <el-tooltip class="item" effect="dark" content="返回顶层" placement="left-start">
        <el-button size="medium" @click="goTop()" icon="el-icon-arrow-up" circle></el-button>
      </el-tooltip>
      <br><br>
      <el-tooltip class="item" effect="dark" content="刷新" placement="left-start">
        <el-button size="medium" @click="goTop()" icon="el-icon-refresh-right" circle></el-button>
      </el-tooltip>
      <br><br>
    </div>
    <div class="footer" style="margin-top: 90px;margin-bottom: 0px">
    </div>
  </center>
</template>
<script>
  export default {
    data() {
      return {
        collapse: false,
        fullscreen: false,
        name: 'admin',
        message: 2
      }
    },
    methods:{
      //前往页面头部
      goTop() {
        location.reload();
      },
      //前往客服
      // gokefu() {
      //   location.reload();//刷新页面
      // },
    }
  }
</script>
<style scoped>
  .footer {
    width: 100%;
    height: 160px;
  }
</style>
