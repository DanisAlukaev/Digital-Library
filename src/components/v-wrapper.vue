<template>
 <div class="v-wrapper">
  <v-header />
  <router-view></router-view>
  <v-footer />
 </div>
</template>

<script>
    import vHeader from "./layout/v-header";
    import vFooter from "./layout/v-footer";
    export default {
        name: "v-wrapper",
     components: {
      vFooter,vHeader
     }
    }
</script>

<style scoped>

</style>