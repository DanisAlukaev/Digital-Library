<template>
    <div>
        <div class="list-wrapper">
            <div class="list-item" @click="openItem()" v-for="doc in documents" :key="doc.name">
                <div class="list-item-icon" :class="{
                    'list-item-icon-document': doc.type ==='document',
                    'list-item-icon-video': doc.type ==='video',
                    'list-item-icon-link': doc.type ==='link',
                    'list-item-icon-folder': doc.type ==='folder',
                    'list-item-icon-image': doc.type ==='image'}"></div>
                <p class="list-item-text">{{doc.name}}</p>
            </div>
    </div>
    </div>
</template>

<script>
    export default {
        name: "v-list",
        methods: {
            openItem(){
            }
        },
        data:function () {
            return {
                documents:[{name:"ProbStat", type: "document"}, {name:"FSE", type: "document"}, {name:"DE", type: "document"}]
            }
        }
    }
</script>

<style scoped>
    .list-item-icon {
        position: absolute;
        margin: 0;
        top: 1vh;
        width: 2vh;
        height: 2vh;
        border: none;
        background-color: #5b5b5b;
        background-size: 100%;
        -webkit-mask-position-x: 50%;
        -webkit-mask-position-y: 50%;
    }
    .list-item-icon-document {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/file-earmark-text.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/file-earmark-text.svg") no-repeat 100%;
    }
    .list-item-icon-link {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/link-45deg.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/link-45deg.svg") no-repeat 100%;
    }
    .list-item-icon-video {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/camera-reels-fill.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/camera-reels-fill.svg") no-repeat 100%;
    }
    .list-item-icon-image {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/card-image.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/card-image.svg") no-repeat 100%;
    }
    .list-item-icon-folder {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/folder2.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/folder2.svg") no-repeat 100%;
    }
</style>