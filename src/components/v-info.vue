<template>
    <div>
        <div class = "information">
            <p class="title">title</p>
            <p class="size">size</p>
            <p class="uploader">name of uploader</p>
            <p class="tags">tags</p>
            <p class="time">uploading time</p>
            <p class="type">extension</p>
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