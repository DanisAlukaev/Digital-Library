<template>
    <div class="v-footer">
        <router-link :to="{name: 'documentation'}">
            <p class="footer-item">Documentation</p>
        </router-link>

        <router-link :to="{name: 'contacts'}">
            <p class="footer-item">Contacts</p>
        </router-link>

        <router-link :to="{name: 'about'}">
            <p class="footer-item">About</p>
        </router-link>
    </div>
</template>

<script>
    export default {
        name: 'v-footer'
    }
</script>

<style scoped>

</style>