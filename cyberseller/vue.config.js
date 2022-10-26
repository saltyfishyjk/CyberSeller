const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    open: false, // 自动打开浏览器
    port: 8088,
  },
  //设置是否在开发环境下每次保存代码时都启用 eslint验证
  lintOnSave: false
})
