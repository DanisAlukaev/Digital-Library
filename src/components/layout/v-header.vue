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
        <b-modal size="lg" id='log_in_form' centered title="Log-in" ok-only button-size="lg">
            <p>enter you login and password</p>
            <p>Write form here!</p>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: 'v-header'
    }
</script>

<style scoped>
</style>