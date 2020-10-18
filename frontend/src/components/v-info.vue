<template>
    <div>
        <!--
        <div class = "top-block">
            <div class="information"></div>

            <div class="top-block-tabs">
                <p class="tab">Answers</p>
            </div>

        </div>
        -->
        <div class="info-top">
            <div class="info-block">
                <p>Something</p>
            </div>
            <div class="info-tabs">
                <!--
                <p class="tab">Answers</p>
                -->
                <ul class="nav nav-tabs">
                    <li class=""><a data-toggle="tab" href="#home">View results <span class="badge badge-danger " title="new/processing">18/2</span> </a></li>
                    <li class="disabled"><a data-toggle="tab" href="#hist">History</a></li>
                    <li class="disabled"><a data-toggle="tab" href="#stat">Statistics</a></li>
                    <li class="disabled"><a data-toggle="tab" href="#profile">Profile</a></li>

                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-info"
    }
</script>

<style scoped>
</style>