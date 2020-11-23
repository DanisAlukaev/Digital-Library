<template>
  <div id="app">
      <router-view></router-view>
      <!--<v-wrapper></v-wrapper>-->
  </div>
</template>

<script>
    //import vWrapper from './components/v-wrapper';
export default {
  name: 'App',
  components: {
    //vWrapper
  },
    created() {
      //this.$store.dispatch('fetchUser');
      //this.$store.dispatch('tryAutoLogin');
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    height: 100%;
    width: 100%;
}
</style>
