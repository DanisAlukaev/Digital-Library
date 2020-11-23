import Vue from 'vue';
import Router from 'vue-router';
import vUploads from '../components/home/v-uploads';
import vUsers from '../components/home/v-users';
import vWrapper from '../components/v-wrapper';
import vAuth from '../components/otherPages/v-authentication';
import vProfile from '../components/otherPages/v-profile';
import store from '../vuex/store';
import vLogin from '../components/otherPages/v-login';
import vCon from '../components/home/v-cont';
Vue.use(Router);
let routes = [{
        name: "home",
        path: "/",
        component: vWrapper,

        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
    }
    },
    {
        name: 'contribute',
        component: vCon,
        path: "/contribute",

        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
        }
    },
    {
        name: 'uploads',
        component: vUploads,
        path: '/uploads',

        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
        }
    },
    {
        name: 'users',
        component: vUsers,
        path: '/Users',

        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
        }
    },
    {
        name: "login",
        path: "/login",
        component: vLogin,
    },
    {
        name: "profile",
        path: "/profile",
        component: vProfile,

        beforeEnter(to, from, next){
            if(store.state.idToken)next();
            else next('./registration');
        }
    },
    {
        name: "documentation",
        path: "/docs"
    },
    {
        name: "about",
        path: "/about"
    },
    {
        name: "contacts",
        path: "/contacts"
    },
    {
        name: "registration",
        path: "/registration",
        component: vAuth,
    },
    {
        name: "catchAll",
        path: "*",
        redirect: {name: 'home'}
    }
];
let router = new Router({
    routes: routes,
    mode: 'history'
});
export default router;
