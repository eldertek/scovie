const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: 'Scovie',
    themeColor: '#ffc107',
    workboxOptions: {
      skipWaiting: true,
      clientsClaim: true
    }
  }
})