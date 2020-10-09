<template>
    <div>
        <div class = "information">
            <p class = "text">Information about particular item</p>
        </div>
        <div class = "rating">
            <p class = "text">Rating box</p>
        </div>

    </div>
</template>

<script>
    export default {
        name: "v-info"
    }
</script>

<style scoped>
    .information, .rating {
        display: inline-flex;
        background-color: #88B77B;
        height: 10vh;
        border: 3px solid #222222;
        border-radius: 2vh;
    }
    .information {
        width: 40%;
    }
    .rating {
        position: relative;
        top: 0;
        width: 60%;
    }
</style>