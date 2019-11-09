// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// 引入全部mint-ui全部组件
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
import axios from 'axios'
// import VueAxios from 'vue-axios'

Vue.config.productionTip = false

Vue.use(Mint)

// 配置axios
Vue.prototype.$http = axios
// Vue.prototype.$axios = Axios
// 配置公共得url
axios.defaults.baseURI = 'http://json.apiopen.top/'
axios.defaults.withCredentials = true

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
