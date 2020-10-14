<template>
    <div>
        <div class="form-search">
            <label :for="'search-engine'"></label>
            <b-form-input :id="'search-engine'" :type="'search'" :placeholder="'Search'" size="sm" required class="input-search"></b-form-input>
            <b-button pill variant="info" class="search-button" @click="search()" size="sm">Search!</b-button>
        </div>
        <!--
        <form action = "search" method = "post" class="form-search">
            <fieldset class="fieldset-search">
                <input type = "text" name = "SearchRequest" placeholder="Search" required class="input-search"/>
                <input type = "submit">
            </fieldset>
        </form>
        -->
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