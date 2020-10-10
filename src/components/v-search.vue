<template>
    <div class = "search-and-filter">
        <form action = "search" method = "post" class="form-search">
            <fieldset class="fieldset-search">
                <input type = "text" name = "SearchRequest" placeholder="Search" required class="input-search"/>
                <input type = "submit">
            </fieldset>
        </form>
    </div>
</template>

<script>
    export default {
        name: "v-search"
    }
</script>

<style scoped>
</style>