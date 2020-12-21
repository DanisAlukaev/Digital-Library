<template>
    <div>
        <div class="info-top">
            <div class="info-tabs">
                <ul class="nav nav-tabs">
                    <li
                            class="disabled"
                            v-for='(tab) in tabs'
                            :key='tab.title'
                            :class="{'active': tab.active}">
                        <a @click="activate(tab.title)">
                            {{tab.title}}
                            <!--{{ getDisplayTitle(tab.title) }}-->
                        </a>
                        <button class="close-icon" @click="closeButton(tab.title)">
                            &times;
                        </button>
                    </li>
                </ul>
            </div>
        </div>
        <div class="document-block">
            <v-document></v-document>
        </div>
    </div>
</template>

<script>
    import vDocument from './v-document';
    import {mapState, mapActions} from 'vuex';
    export default {
        name: "v-info",
        components: {
            vDocument
        },
        computed:{
            ...mapState({
                tabs:'openedDocuments',
            })
        },
        methods: {
            ...mapActions({
                close: 'closeDocument',
                active: 'activateTab',
                open: 'getDocument',
            }),
            closeButton(name) {
                this.close(name);
            },
            activate(name) {
                this.active(name);
            },
            getDisplayTitle(title) {
                let display = title;
                if (display.length > 22) {
                    display = display.slice(0, 19);
                    display += "...";
                }
                return display;
            },
        }
    }
</script>

<style scoped>
    .document-block {
        height: 96%;
    }
    .v-info .nav-header .tab .close {
        padding-left: 5px;
    }
</style>