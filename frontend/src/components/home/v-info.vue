<template>
    <div>
        <div class="info-top">
            <div class="info-tabs">
                <ul class="nav nav-tabs">
                    <li class="disabled" v-for="tab in tabs" :key="tab.course" :class="{'active': tab.active}">
                        <a @click="activate(tab.course)">{{tab.course}}</a>
                        <button class="close-icon" @click="closebutton(tab.course)"></button>
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
    import vDocument from './v-document'
    export default {
        name: "v-info",
        data:function(){return {
            tabs:[{course:'FSE', active: 1},{course:'PS', active: 0},{course:'History', active: 0},{course:'DE', active: 0}]
        }},
        components: {
            vDocument
        },
        methods: {
            closebutton(course){
                this.tabs = this.tabs.filter((tab)=>{
                    if(course===tab.course && tab.active === 1 && this.tabs.length>0)this.tabs[0].active =1;
                    return course!==tab.course;});
            },
            activate(course){
                this.tabs.map((tab)=>{tab.course === course? tab.active = 1 : tab.active=0;})
            }
        }
    }
</script>

<style scoped>
    .document-block {
        height: 96%;
    }
</style>