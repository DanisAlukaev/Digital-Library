<template>
  <div id="app">
    {{ uploads }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: () => ({
    uploads: []
  }),
  components: {
  },
  mounted () {
    axios.post('http://localhost:8000/api/uploads/', {
            title: 'Test Uploading',
            description: 'Vue.js integration test'
        });
    axios.get('http://localhost:8000/api/uploads/').then((response) => {this.uploads = response.data})
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
  margin-top: 60px;
}
</style>
