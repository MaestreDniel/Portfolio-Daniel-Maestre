const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    historyApiFallback: {
      rewrites: [
        { 
          from: /./, 
          to: '/' 
        },
      ],
    }
  },
  transpileDependencies: true,
  publicPath: '/',
  chainWebpack: config => {   
    config
      .plugin('html')
      .tap(args => {
        args[0].title = "Daniel Maestre";
        return args;
      })
    config
      .plugin('define')
      .tap((definitions) => {
        Object.assign(definitions[0], {
          // Workaround to get rid of vue-i18n warning
          __VUE_I18N_FULL_INSTALL__: JSON.stringify(true),
          __INTLIFY_PROD_DEVTOOLS__: JSON.stringify(false),
          __VUE_I18N_LEGACY_API__: JSON.stringify(false),
        })

      return definitions;
    })
  }
})
