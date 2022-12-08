const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: 'localhost',
    port: 8088,
      proxy: {
        '/api': {
          target: 'http://43.143.179.158:8080',
          changeOrigin: true,
          pathRewrite: {
            '/api': ''
          }
        }
      }
  },
  //设置是否在开发环境下每次保存代码时都启用 eslint验证
  lintOnSave: false,
  
})
