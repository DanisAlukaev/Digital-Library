import Vue from 'vue';
import Vuex from 'vuex';
import globalAxios from 'axios';
import axios from './axios-auth';
import router from "../router/router";
Vue.use(Vuex);
let store = new Vuex.Store({
    state:{
        user: null,
        idToken: null,
        userId: null,
        currentDoc: {},
        documents:[
            {name:"DL",
            type: "document",
            comments: [
                {text: "What is 2+2?", sender: "12k club member"},
                {text: "You should know it from the school. If the question was what is pi, some people would argue that it is 4 or 3, but to answer your question it is obviously 4.", sender: "Professor Gorodetskiy"},
                {text: "2+2=pi", sender: "36k club member"},
                {text: "22", sender: "JavaScript"}],
            url: 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf',
            rating: 3.5,
            pageNum: 1,
            active: 0},
            {name:"FSE", type: "document",
                url: "https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf",
                active: 0},
            {name:"DE", type: "document", active: 0, url:"./"}],
        openedDocuments: [],

    },
    mutations:{
        clearAuthData(state){
            state.idToken = null;
            state.userId = null;
        },
        authUser(state, authData){
            state.idToken = authData.token;
            state.userId = authData.userId;
        },
        openDocument(state, doc){
            if(state.openedDocuments.length === 0)doc.active = 1;
            else doc.active = 0;
            state.openedDocuments.push(doc);
        },
        closeDocument(state, name){
            state.openedDocuments = state.openedDocuments.filter((tab, i)=>{
                if(name===tab.name && tab.active === 1 && state.openedDocuments.length>0)state.openedDocuments[0].active = 1;
                if(i === 0 && name===tab.name && tab.active && state.openedDocuments.length>1)state.openedDocuments[1].active = 1;
                return name!==tab.name;});
        },
        updatePage(state, {doc, page}){
            doc.pageNum = page;
        },
        activateTab(state, name){
            state.openedDocuments.map((tab)=>{tab.name === name ? tab.active = 1 : tab.active = 0;});
        },
        getDocument(state){
            for (let i = 0; i < state.openedDocuments.length; i++) {
                if (state.openedDocuments[i].active === 1){
                    state.currentDoc = state.openedDocuments[i];
                    break;
                }
            }
        },

        storeUser(state, user){
            state.user = user;
        }
    },
    actions:{
        setLogoutTimer({commit}, expirationTime){
            setTimeout(()=>{
                commit('clearAuthData');
            }, expirationTime*1000);
        },
        logout({commit}){
            commit('clearAuthData');
            localStorage.removeItem('expirationDate');
            localStorage.removeItem('userId');
            localStorage.removeItem('token');
        },
        tryAutoLogin({commit}){
            const token = localStorage.getItem('token');
            if(!token)return;
            const expirationDate = localStorage.getItem('expirationDate');
            const now = new Date();
            if(now >= expirationDate)return;
            const userId = localStorage.getItem('userId');
            commit('authUser', {
                token: token,
                userId: userId
            });
        },
        storeUser({commit, state}, userData){
            if(!state.idToken)return;
            axios.post('/users.json' + '?auth=' + state.idToken, userData)//todo change url, if baseURL is different use globalAxios instead
                .then()
                .catch(err=>console.log(err));
        },
        fetchUser({commit, state}){
            if(!state.idToken)return;
            axios.get('/users.json' + '?auth=' + state.idToken)//todo change url, if baseURL is different use globalAxios instead
                .then(res=>{
                    const data = res.data;
                    let users = [];
                    for(let key in data){
                        const user = data[key];
                        user.id = key;
                        users.push(user);
                    }
                    commit('storeUser', users[0]);
                })
                .catch(err=>console.log(err));
        },
        signup({commit, dispatch}, authData){//registration
            axios.post('',{//todo change url
                email: authData.email,
                password: authData.password//todo change fields
            }).then(res=>{
                commit('authUser', {
                    token: res.data.idToken,
                    userId: res.data.userId//todo check what django send to us and change it
                });
                const now = new Date();
                const expirationDate = new Date(now.getTime() + res.data.expiresIn * 1000);
                localStorage.setItem('token', res.data.idToken);
                localStorage.setItem('userId', res.data.userId);
                localStorage.setItem('expirationDate', expirationDate);
                dispatch('storeUser', authData);
                dispatch('setLogoutTimer', res.data.expiresIn);//todo check expiresIn, if it not exist we need to calculate it
            }).then(()=>{router.replace('/home')}).catch(error=>console.log(error));//todo do something if error occured
        },
        login({commit, dispatch}, authData){//login
            axios.post('',{//todo same as signup
                email: authData.email,
                password: authData.password,
            }).then(res=>{
                commit('authUser', {
                    token: res.data.idToken,
                    userId: res.data.userId
                });
                const now = new Date();
                const expirationDate = new Date(now.getTime() + res.data.expiresIn * 1000);
                localStorage.setItem('token', res.data.idToken);
                localStorage.setItem('userId', res.data.userId);
                localStorage.setItem('expirationDate', expirationDate);
                dispatch('setLogoutTimer', res.data.expiresIn);
            }).then(()=>{router.replace('/home')}).catch(error=>console.log(error));
        },
        getDocument({commit}){
            commit('getDocument');
        },
        activateTab({commit}, name){
            commit('activateTab', name);

            commit('getDocument');
        },
        closeDocument({commit}, name){
            commit('closeDocument', name);

            commit('getDocument');
        },
        openDocument({commit}, doc){
            commit('openDocument', doc);

            commit('getDocument');
        },
        updatePage({commit}, {doc, page}){
            commit('updatePage', {doc, page});
        }
    },
    getters: {
        user(state){
            return state.user;
        },
        isAuthenticated(state){
            return state.idToken !== null;
        }
    }
});
export default store;