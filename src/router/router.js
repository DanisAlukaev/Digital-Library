        name: "v-home",
        path: "/",
        component: vHome
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
        name: "account",
        path: "/account"
    }
];
let router = new Router({
    routes: routes
});
=======
import Vue from 'vue';
import Router from 'vue-router';
import vHome from '../components/v-home';
Vue.use(Router);
let routes = [{
        name: "v-home",
        path: "/",
        component: vHome
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
        name: "account",
        path: "/account"
    }
];
let router = new Router({
    routes: routes
});
>>>>>>> 12a1064cbd807b204040ef4fa2924d85e177381e
export default router;
