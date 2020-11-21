<template>
 <div class="v-wrapper">
  <v-header />
  <v-home></v-home>
 </div>
</template>

<script>
    import vHeader from "./home/v-header";
    import vHome from './v-home';
    import router from "../router/router";
    export default {
        name: "v-wrapper",
     components: {
      vHeader,
      vHome
     }
    }
</script>

<style scoped>
</style>