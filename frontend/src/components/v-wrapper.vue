<template>
 <div class="v-wrapper">
  <v-header />
  <router-view></router-view>
 </div>
</template>

<script>
    import vHeader from "./home/v-header";
    export default {
        name: "v-wrapper",
     components: {
      vHeader
     }
    }
</script>

<style scoped>
</style>