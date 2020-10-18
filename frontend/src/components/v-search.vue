<template>
    <div>
        <div class="search-top">
            <div class="form-search">
                <div class="search-block">
                    <button class="search-icon"></button>
                    <label for="input-search" class="label-search"></label>
                    <input type="text" required id="input-search">
                </div>
                <button class="upload-icon"></button>
            </div>
            <div class="search-pathname">
                <p class="pathname">Home</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-search",
        methods:{
            search(){
                return true;
            }
        }
    }
</script>

<style scoped>
</style>