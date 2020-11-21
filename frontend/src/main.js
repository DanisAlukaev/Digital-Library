import Vue from 'vue';
import App from './App.vue';
import router from './router/router';
import store from './vuex/store';
import './styles.css';
import './styles2.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css'
//import {BootstrapVue} from 'bootstrap-vue';

Vue.config.productionTip = false;
//Vue.use(BootstrapVue);

new Vue({
  render: h => h(App),
    store,
    router,
}).$mount('#app');
