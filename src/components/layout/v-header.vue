<template>
    <div class='v-header'>
        <div class="home">
            <router-link :to="{name: 'home'}">
                <p class="nav-bar-item">Home</p>
            </router-link>
        </div>
        <div class="log-in">
            <span>Log-in</span>


        </div>
    </div>
</template>

<script>
    export default {
        name: 'v-header'
    }
</script>

<style scoped>
.home {
    position: fixed;
}
.log-in {
    position: fixed;
    right: 3vh;
    width: 10%;
    }
</style>