import Vue from 'vue'
import App from './App'
import uploader from 'vue-simple-uploader'
import router from './router'
import ElementUI from 'element-ui'
import store from './store'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/bootstrap.min.css'

var axios = require('axios')
axios.defaults.baseURL = 'http://182.92.236.19:8000/api/'
// axios.defaults.baseURL = 'http://localhost:8443/api/'
Vue.prototype.$axios = axios
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(uploader)
router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      next()
    } else {
      next({
        path: 'login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
}
)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store,
  components: { App },
  template: '<App/>'
})
