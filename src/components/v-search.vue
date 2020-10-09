<template>
    <div class = "search-and-filter">
        <form action = "search" method = "post">
            <fieldset>
                <input type = "text" name = "SearchRequest" placeholder="Search" required/>
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
.search-and-filter {
    display: flex;
    width: 100%;
    background-color: #68975B;
    border: 3px solid #222222;
    border-radius: 2vh;
}
    form {
        padding: 0 5%;
        border-style: none;
        margin: auto;
    }
    fieldset {
        border-style: none;
    }
    input {
        width: 90%;
        background-color: #ececec;
        border-style: none;
    }
</style>