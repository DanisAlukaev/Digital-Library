<template>
    <div class='v-header'>
        <header class="site-header">
            <nav class="navbar navbar-expand-md navbar-dark fixed-top">
                <div class="container">
                    <button class="upload-icon"></button>
                    <div class="digital_library-home">
                        <router-link :to="{name: 'home'}">
                            <a class="navbar-brand mr-4 header-font-size no-outline">Digital Library</a>
                        </router-link>
                    </div>
                    <!--
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    -->
                    <div class="collapse navbar-collapse" id="navbarToggle">
                        <div class="form-search">
                            <div class="search-block">
                                <button class="search-icon" @click="search(searchArg)"></button>
                                <label for="input-search" class="label-search"></label>
                                <input type="text" required id="input-search" v-model="searchArg">
                                <!--
                                <div class="dropdown-search">
                                    <div class="list-item-search-last">
                                        <p class="list-item-text-search-bold">Videos:</p>
                                        <p class="list-item-text-search">Whatever</p>
                                        <p class="list-item-text-search">Whatever</p>
                                    </div>
                                </div>
                                -->
                            </div>
                        </div>
                        <div class="navbar-nav profile">
                            <div class="name-profile nav-link header-font-size">
                                {{userName}}
                                <div class="dropdown-profile">
                                    <div class="list-item-profile" v-if="isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'profile'}">My profile</router-link></p>
                                    </div>
                                    <div class="list-item-profile" v-if="!isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'login'}">Sign in</router-link></p>
                                    </div>
                                    <div class="list-item-profile-last" v-if="!isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'registration'}">Sign up</router-link></p>
                                    </div>

                                    <div class="list-item-profile" v-if="isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'contribute'}">Contribute</router-link></p>
                                    </div>
                                    <!--
                                    <div class="list-item" v-if="isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'uploads'}">Uploads</router-link></p>
                                    </div>

                                    <div class="list-item" v-if="isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'users'}">Users</router-link></p>
                                    </div>
                                    -->
                                    <div class="list-item-last" v-if="isAuthenticated">
                                        <a class="list-item-text" @click="logout()">Log out</a>
                                    </div>
                                </div>
                            </div>
                            <img alt="" class="avatar">
                        </div>
                    </div>
                </div>
            </nav>
        </header>
    </div>
</template>

<script>
    import {mapGetters, mapState} from "vuex";
    export default {
        name: 'v-header',
        data: function(){
            return {
                searchArg: '',
                elements: []
            }
        },
        computed: {
            ...mapState({info:'informationAboutMe', documents: 'documents'}),
            ...mapGetters(["isAuthenticated"]),
            userName: function(){
                if(this.info === undefined)return "";
                return this.info.first_name + " " + this.info.last_name || "";
            }
        },
        watch:{
            info:function(val){
                document.querySelector('.avatar').src = val.image;
            }
        },
        activated() {
            this.$store.dispatch('getInfo');
        },
        created() {
            this.$store.dispatch('getInfo');
        },
        methods: {
            logout(){
                this.$store.dispatch('logout');
            },
            search(arg){
                let data = {
                    tags: [],
                    title: arg
                };
                this.$store.dispatch('search', data);
            }
        }
    }
</script>

<style scoped>
    .list-item-profile {
        height: 4vh;
        margin: 0 5% 0 5%;
        cursor: pointer;
        border-bottom: 1px solid #9b9b9b;
    }
    .list-item-profile-last {
        height: 4vh;
        margin: 0 5% 0 5%;
        cursor: pointer;
    }
</style>