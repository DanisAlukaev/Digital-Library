<template>
    <div class='v-header'>
        <header class="site-header">
            <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
                <div class="container">
                    <div class="digital_library-home">
                        <router-link :to="{name: 'home'}">
                            <a class="navbar-brand mr-4">Digital Library</a>
                        </router-link>
                    </div>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarToggle">
                        <div class="navbar-nav navbar_links">
                            <!--
                            <router-link :to="{name: 'home'}" class="navbar_link">
                                <a class="nav-item nav-link">Home</a>
                            </router-link>
                            -->
                            <router-link :to="{name: 'about'}" class="navbar_link">
                                <a class="nav-item nav-link">About</a>
                            </router-link>

                            <router-link :to="{name: 'documentation'}" class="navbar_link">
                                <a class="nav-item nav-link">Documentation</a>
                            </router-link>

                            <router-link :to="{name: 'contacts'}" class="navbar_link">
                                <a class="nav-item nav-link">Contacts</a>
                            </router-link>
                        </div>
                        <div class="navbar-nav profile">
                            <router-link :to="{name: 'profile'}" class="navbar_link">
                                <a class="nav-item nav-link">Profile</a>
                            </router-link>
                            <router-link :to="{name: 'home'}" class="navbar_link">
                                <a class="nav-item nav-link">Logout</a>
                            </router-link>
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
    export default {
        name: 'v-header',
		methods: {}
    }
</script>

<style scoped>
</style>