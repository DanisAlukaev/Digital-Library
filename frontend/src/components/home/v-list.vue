<template>
    <div>
        <div class="list-wrapper">
            <div class="list-item" @click="openItem(doc)" v-for="doc in documents" :key="doc.title">
                <div class="list-item-icon" :class="{
                    'list-item-icon-document': doc.type ==='document',
                    'list-item-icon-video': doc.type ==='video',
                    'list-item-icon-link': doc.type ==='link',
                    'list-item-icon-folder': doc.type ==='folder',
                    'list-item-icon-image': doc.type ==='image'}"></div>
                <p class="list-item-text">{{doc.title}}</p>
            </div>
    </div>
        <div class="navigation-bottom">
            <router-link :to="{name: 'about_us'}" class="navigation-bottom-link">About us</router-link>
            <router-link :to="{name: 'documentation'}" class="navigation-bottom-link">Documentation</router-link>
            <router-link :to="{name: 'contacts'}" class="navigation-bottom-link">Contacts</router-link>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex';
    export default {
        name: "v-list",
        methods: {
            openItem(doc){
                this.open(doc);
                if(this.openedDocuments.length === 1)this.active(this.openedDocuments[0].title);
            },
            ...mapActions({open:"openDocument", active: "activateTab", getList:"getList"})
        },
        created() {
            this.getList();
        },
        computed: {
            ...mapState([
                'documents',
                'openedDocuments'
            ])
        }
    }
</script>

<style scoped>
    .navigation-bottom-link {
        padding: 0.5vh;
        text-decoration: none;
        color: #5b5b5b;
    }
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
    .navigation-bottom {
        display: block;
        height: 5vh;
        width: 100%;
    }
</style>