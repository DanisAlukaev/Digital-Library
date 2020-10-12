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
</style>