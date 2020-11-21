import Vue from 'vue';
import Vuex from 'vuex';
import globalAxios from 'axios';
import axios from './axios-auth';
import router from "../router/router";

Vue.use(Vuex);
let store = new Vuex.Store({
    state: {
        currentComments: [],
        informationAboutMe: {},
        idToken: null,
        //userId: null,
        currentDoc: {},
        documents: [],
        openedDocuments: [],
        tags: []
    },
    mutations: {
        clearAuthData(state) {
            state.idToken = null;
            //state.userId = null;
        },
        authUser(state, authData) {
            state.idToken = authData.token;
            //state.userId = authData.userId;
        },
        openDocument(state, doc) {
            if (state.openedDocuments.length === 0) doc.active = 1;
            else doc.active = 0;
            state.openedDocuments.push(doc);
        },
        closeDocument(state, name) {
            if (state.openedDocuments.length === 1) return;
            state.openedDocuments = state.openedDocuments.filter((tab, i) => {
                if (name === tab.title && tab.active === 1 && state.openedDocuments.length > 0) state.openedDocuments[0].active = 1;
                if (i === 0 && name === tab.title && tab.active && state.openedDocuments.length > 1) state.openedDocuments[1].active = 1;
                if (name === tab.title) tab.pageNum = 1;

                return name !== tab.title;
            });
        },
        updatePage(state, {doc, page}) {
            doc.pageNum = page;
        },
        activateTab(state, name) {
            state.openedDocuments.forEach((tab) => {
                tab.title === name ? tab.active = 1 : tab.active = 0;
            });
        },
        getDocument(state) {
            state.openedDocuments.forEach((doc) => {
                if (doc.id === state.currentDoc.id) doc.pageNum = state.currentDoc.pageNum;
            });
            for (let i = 0; i < state.openedDocuments.length; i++) {
                if (state.openedDocuments[i].active === 1) {
                    state.currentDoc = state.openedDocuments[i];
                    break;
                }
            }
        },
        getInfo(state, data){
            state.informationAboutMe = data;
        }
    },
    actions: {
        getTags({state}){
            let config = {
                method: 'get',
                url: 'http://127.0.0.1:8000/api/storage/tags/',
                headers: {}
            };

            axios(config)
                .then(function (response) {
                    console.log(JSON.stringify(response.data));
                    state.tags = response.data;
                })
                .catch(function (error) {
                    console.log(error.response.data);
                });

        },
        setLogoutTimer({commit}, expirationTime) {
            setTimeout(() => {
                commit('logout');
            }, expirationTime * 1000);
        },
        getList({state}){
            let config = {
                method: 'get',
                url: 'http://127.0.0.1:8000/api/storage/uploads/',
                headers: {}
            };
            if(state.documents.length === 0)axios(config)
                    .then(function (response) {
                        state.documents = response.data;
                        state.documents.forEach((doc)=>{
                            if(doc.type === 0)doc.type = 'document';
                            if(doc.type === 1)doc.type ='image';
                            if(doc.type === 2)doc.type ='video';
                            if(doc.type === 3)doc.type ='link';
                            if(doc.status === 0)doc.status = 'rejected';
                            if(doc.status === 1)doc.status = 'approved';
                            if(doc.status === 2)doc.status = 'pending';
                            doc.pageNum = 1;
                            doc.active = 0;
                        });
                    })
                    .catch(function (error) {
                        console.log(error.response.data);
                    });
        },
        logout({commit, state}) {
            let flag = true;
            let logout = async()=>{
                let config = {
                    method: 'post',
                    url: '/auth/token/logout/',
                    headers: {
                        'Authorization': 'Token '+ state.idToken
                    }
                };
                await axios(config)
                    .then(function (response) {
                    })
                    .catch(function (error) {
                        console.log(error.response.data);
                        flag = false;
                    });
                commit('clearAuthData');
                localStorage.removeItem('expirationDate');
                //localStorage.removeItem('userId');
                localStorage.removeItem('token');
            };
            (async () => {
                await logout();
                if (flag) router.replace('/login');
            })();
        },
        tryAutoLogin({commit}) {
            const token = localStorage.getItem('token');
            if (!token) return;
            const expirationDate = localStorage.getItem('expirationDate');
            const now = new Date();
            if (now >= expirationDate) return;
            //const userId = localStorage.getItem('userId');
            commit('authUser', {
                token: token,
                //userId: userId
            });
            router.replace('/');
        },
        submitFile({state}, formdata){
            let config = {
                method: 'post',
                url: 'http://127.0.0.1:8000/api/storage/uploads/',
                headers: {
                    'Authorization': 'Token ' + state.idToken
                },
                data : formdata
            };

            axios(config)
                .then(function (response) {
                    console.log(JSON.stringify(response.data));
                })
                .catch(function (error) {
                    console.log(error.response.data);
                });

        },
getComments({state}, id){
    let config = {
        method: 'get',
        url: `http://127.0.0.1:8000/api/storage/uploads/comments/${id}/`,
        headers: {}
    };

    axios(config)
        .then(function (response) {
            state.currentComments = response.data;
            console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
        });
        },
        signup({commit, dispatch}, authData) {//registration
            let flag = true;
            let registration = async () => {
                let FormData = require('form-data');
                let form = new FormData();
                form.append('first_name', authData.first_name);
                form.append('last_name', authData.last_name);
                form.append('email', authData.email);
                form.append('password', authData.password);
                form.append('re_password', authData.re_password);
                form.append('degree', authData.degree);
                form.append('track', authData.track);
                form.append('course', authData.course);
                await axios.post('/auth/users/', form).then(res => {
                    let id  = res.data.id;
                    let config = {
                        method: 'get',
                        url: 'http://127.0.0.1:8000/auth/create_token/?id=' + id,
                        headers: {}
                    };
                    axios(config)
                        .then(function (response) {
                            localStorage.setItem('token', res.data.auth_token);
                            commit('authUser', {
                                token: res.data,
                            });
                            console.log(JSON.stringify(response.data.auth_token));
                        })
                        .catch(function (error) {
                            console.log(error.response.id);
                        });

                    const now = new Date();
                    const expirationDate = new Date(now.getTime() + 60 * 24 * 3600 * 1000);
                    //localStorage.setItem('userId', res.data.id);
                    localStorage.setItem('expirationDate', expirationDate);
                    dispatch('setLogoutTimer', 60 * 24 * 3600);
                })
                    .catch(error => {
                        console.log(error.response.data);
                        flag = false;
                    });
            };
            (async () => {
                await registration();
                if (flag) router.replace('/');
            })();
            //todo do something if error occured
        },
        login({commit, dispatch}, authData) {//login
            let flag = true;
            let login = async () => {
                await axios.post(`/auth/token/login/?email=${authData.email}&password=${authData.password}`, {//todo same as signup
                    email: authData.email,
                    password: authData.password,
                }).then(res => {
                    commit('authUser', {
                        token: res.data.auth_token,
                        //userId: res.data.id
                    });
                    const now = new Date();
                    const expirationDate = new Date(now.getTime() + 60 * 24 * 3600 * 1000);
                    localStorage.setItem('token', res.data.auth_token);
                    //localStorage.setItem('userId', res.data.id);
                    localStorage.setItem('expirationDate', expirationDate);
                    dispatch('setLogoutTimer', 60 * 24 * 3600);
                })
                    .catch(error => {
                        console.log(error.response.data);
                        flag = false;
                    });
            };
            (async () => {
                await login();
                if (flag) router.replace('/');
            })();
        },
        getDocument({commit}) {
            commit('getDocument');
        },
        activateTab({commit}, name) {
            commit('activateTab', name);

            commit('getDocument');
        },
        closeDocument({commit}, name) {
            commit('closeDocument', name);

            commit('getDocument');
        },
        openDocument({commit}, doc) {
            commit('openDocument', doc);

            commit('getDocument');
        },
        updatePage({commit}, {doc, page}) {
            commit('updatePage', {doc, page});
        },
        getInfo({state, commit}){
            let config = {
                method: 'get',
                url: '/auth/users/me/',
                headers: {
                    'Authorization': 'Token ' + state.idToken
                }
            };
            axios(config)
                .then(function (response) {
                    commit('getInfo', response.data);
                })
                .catch(function (error) {
                    console.log(error);
                });

        }
    },
    getters: {
        isAuthenticated(state) {
            return state.idToken !== null;
        }
    }
});
export default store;