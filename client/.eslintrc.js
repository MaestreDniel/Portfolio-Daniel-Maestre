module.exports = {
  extends: [
    'plugin:vue/vue3-recommended',
  ],
  rules: {
    "vue/max-attributes-per-line": ["warn", {
      "singleline": {
        "max": 3
      },      
      "multiline": {
        "max": 1
      }
    }]
  }
}