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
                                <button class="search-icon"></button>
                                <label for="input-search" class="label-search"></label>
                                <input type="text" required id="input-search">
                                <div class="dropdown-search">
                                    <div class="list-item-search">
                                        <p class="list-item-text-search-bold">Topics:</p>
                                        <p class="list-item-text-search">Probability Theory</p>
                                        <p class="list-item-text-search">Probability and Statistics</p>
                                    </div>
                                    <div class="list-item-search">
                                        <p class="list-item-text-search-bold">Documents:</p>
                                        <p class="list-item-text-search">Probability Theory Textbook by somebody</p>
                                        <p class="list-item-text-search">Probability and Statistics Textbook by somebody</p>
                                    </div>
                                    <div class="list-item-search">
                                        <p class="list-item-text-search-bold">Images:</p>
                                        <p class="list-item-text-search">Whatever</p>
                                        <p class="list-item-text-search">Whatever</p>
                                    </div>
                                    <div class="list-item-search-last">
                                        <p class="list-item-text-search-bold">Videos:</p>
                                        <p class="list-item-text-search">Whatever</p>
                                        <p class="list-item-text-search">Whatever</p>
                                    </div>
                                </div>
                            </div>
                            <!--<button class="upload-icon"></button>-->
                        </div>
                        <div class="navbar-nav profile">
                            <div class="name-profile nav-link header-font-size">
                                {{name}}
                                <div class="dropdown-profile">
                                    <div class="list-item" v-if="isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'profile'}">My account</router-link></p>
                                    </div>
                                    <div class="list-item" v-if="!isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'login'}">Sign in</router-link></p>
                                    </div>
                                    <div class="list-item-last" v-if="!isAuthenticated">
                                        <p class="list-item-text"><router-link :to="{name: 'registration'}">Sign up</router-link></p>
                                    </div>
                                    <div class="list-item-last" v-if="isAuthenticated">
                                        <p class="list-item-text">Log out</p>
                                    </div>
                                </div>
                            </div>
                            <img src="../../assets/profile.png" alt="" class="avatar">
                        </div>
                    </div>
                </div>
            </nav>
        </header>
        <!--
        <div class="home">
            <router-link :to="{name: 'home'}">
                <p class="nav-bar-item">Home</p>
            </router-link>
        </div>
        <div class="log-in">
            <b-button pill variant="info" v-b-modal="'log_in_form'" class="log-in-button">Log-in</b-button>

        </div>
        <b-modal size="lg" id='log_in_form' centered title="Enter your login and password" ok-only button-size="lg" ok-variant="info">
			<template v-slot:modal-footer="{ ok }">
				<b-button size="sm" variant="info" @click="ok()" class="log-in-form-button" pill>Log in</b-button>
			</template>
            <b-form-input :id="'login'" :name="'log-in-input'" :type="'text'" :placeholder="'Login'" size="sm" required class="input-search"></b-form-input>
			<b-form-input :id="'password'" :name="'log-in-input'" :type="'password'" :placeholder="'Password'" size="sm" required class="input-search"></b-form-input>
			<b-form-checkbox :id="'remember'" :name="'log-in-input'" v-model="selected">Remember me</b-form-checkbox>
        </b-modal>
        -->
    </div>
</template>

<script>
    import {mapGetters} from "vuex";
    export default {
        name: 'v-header',
        data: function(){
            return {
                name: 'Miley Cyrus'
            }
        },
        computed: {
            ...mapGetters(["isAuthenticated"])
        },
		methods: {}
    }
</script>

<style scoped>
</style>