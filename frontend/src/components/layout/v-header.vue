<template>
    <div class='v-header'>
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