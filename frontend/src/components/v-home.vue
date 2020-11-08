<template>
    <div class="v-home">
        <div class="left-block">
            <v-list class="v-list"></v-list>
        </div>
        <div class="right-block">
            <v-info class="v-info"></v-info>
        </div>
    </div>

</template>

<script>
    import vInfo from './home/v-info';
    import vList from './home/v-list';
    export default {
        name: "v-home",
        components: {
            vInfo,
            vList
        }
    }
</script>
<style scoped>
</style>