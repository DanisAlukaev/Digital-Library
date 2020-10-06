import Vue from 'vue';
import App from './App.vue';
import router from './router/router';
import store from './vuex/store';
import './styles.css';

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
    store,
    router
}).$mount('#app');
