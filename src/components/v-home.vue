<template>
    <div class="v-home">
        <div class="top">
            <v-search class="v-search"></v-search>
            <v-info class="v-info"></v-info>
        </div>
        <div class="center">
            <v-list class="v-list"></v-list>
            <v-content class="v-content"></v-content>
        </div>
    </div>

</template>

<script>
    import vSearch from './v-search';
    import vInfo from './v-info';
    import vContent from './v-content';
    import vList from './v-list';
    export default {
        name: "v-home",
        components: {
            vSearch,
            vInfo,
            vContent,
            vList
        }
    }
</script>

<style scoped>
 .v-search {
     width: 20%;
     position: relative;
     left: 0;
 }
 .v-info {
     display: flex;
     position: relative;
     right: 0;
     width: 80%;
 }
 .v-home {
     display: block;
     position: relative;
     top: calc(3vh + 11px);
 }
 .v-list {
     width: 20%;
     display: flex;
     position: relative;
     top: 0;
     left: 0;
     margin: 0;
     background-color: #88B77B;
     height: calc(84vh - 6px);
 }
 .v-content {
     display: flex;
     width: 80%;
     position: relative;
     left: 0;
     top: 0;
     margin: 0;
 }
 .top, .center {
     display: flex;
 }
 .center {
     position: relative;
     top: 0;
 }
</style>