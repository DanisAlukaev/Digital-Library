<template>
    <div>
        <v-document v-bind="{url, scale}"></v-document>
    </div>
</template>

<script>
    import vDocument from './v-document';
    export default {
        name: "v-content",
        components: {
            vDocument,
        },
        data: function() {
            return {
                url: 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf',//'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf',
                scale: 3
            }
        }
    }
</script>

<style scoped>
    .viewer {
        overflow: scroll;
        width: 100%;
        height: 100%;
    }
</style>