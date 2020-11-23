<template>
    <div class="v-document">
        <div class="top-page-control">
            <div class="page-control" v-show="!typeLink">
                <button class="prev-button no-outline" @click="onPrevPage()"></button>
                <!--
                <p class="page-control-text">{{pageNum}}/{{pageMax}}</p>
                <p class="page-control-text">{{scale*100}}%</p>
                -->
                <input type="number" value="1" min="1" max="10000" v-model.lazy.number="pageNum" v-on:change="changePage(pageNum)">
                <p class="page-control-text get-rid-of-margins">/{{pageMax}}</p>
                <input type="number" value="1" min="1" max="10000" v-model.lazy.number="scale" v-on:change="changeScale(scale)">
                <p class="page-control-text get-rid-of-margins">%</p>

                <button class="next-button no-outline" @click="onNextPage()"></button>
            </div>
            <div class="rating">
                <p class="page-control-text">{{rating}}</p>
                <button class="comments-icon no-outline" @click="dropdownComments()"></button>
                <div class="dropdown-comments" v-show="dropdown">
                    <div class="comments">
                        <div v-for="comment in comments" :key="comment.id" class="comment">
                            <div class="comment-avatar">
                                <img src="../../assets/profile.png" alt="" class="avatar">
                            </div>
                            <div class="comment-block">
                                <p class="list-item-text-search-bold">{{comment.user.first_name + " "+ comment.user.last_name}}</p>
                                <p class="list-item-text-search">{{comment.content}}</p>
                                <p class="comments-reply list-item-text-search-bold">Reply</p>
                            </div>
                        </div>
                    </div>
                    <div class="comments-add-block">
                        <textarea rows="5" placeholder="Add a comment" class="comments-add" v-model="message"></textarea>
                        <button class="comments-add-button" @click="createMessage()"></button>
                    </div>
                </div>
            </div>
        </div>
        <div class="pdf-document" v-show="!typeLink">
            <canvas id="the-canvas"></canvas>
        </div>
        <div v-show="typeLink" class="pdf-document">
            <a class="link-to-see" :href="doc.link">{{doc.link}}</a>
        </div>
        <div class="document-title-block">
            <p class="document-title">{{doc.title}}</p>
        </div>
    </div>
</template>

<script>
    import * as pdfjsLib from 'pdfjs-dist';
    import {mapState} from 'vuex';
    export default {
        name: "v-content",
        data: function(){
            return {
                message: "",
                dropdown: false,
                scale: 100,
                pdf: undefined,
                pages: [],
                pageRendering: false,
                pageNumPending: null,
                pageMax: 1,
                pageNum: 1
            }
        },
        computed:{
            ...mapState({doc:'currentDoc', comm: 'currentComments'}),
            typeLink:function(){
                if(this.doc.type === 'link')return true;
                return false;
            },
            url() {
                if(this.doc.type === 'link')return "";
                return ('http://127.0.0.1:8000' + this.doc.file)  || "";
            },
            comments() {
                return this.doc.comments || [];
            },
            rating() {
                return this.doc.rating || undefined;
            }
        },
        watch: {
            url:function(new_val){
                this.$store.dispatch('getComments', this.doc.id);
                this.pageNum = this.doc.pageNum || 1;
                if(new_val !=="")this.fetchPDF(new_val);
            }
        },
        methods: {
            createMessage(){
                let data = {
                    content: this.message,
                    id: this.doc.id
                };
                this.$store.dispatch('createComment', data);
                this.$store.dispatch('getComments', this.doc.id);
            },
            dropdownComments(){
                if(!this.dropdown)document.querySelector(".rating").style.borderBottomLeftRadius = 0;
                else document.querySelector(".rating").style.borderBottomLeftRadius = "2vh";
                this.dropdown = !this.dropdown;
            },
            changeScale(scale){
                this.renderPage(this.pageNum);
            },
            changePage(pageNum){
                this.renderPage(this.pageNum);
            },
            fetchPDF(new_url) {
                pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.js`;//change location
                pdfjsLib.getDocument(new_url).promise.then((pdf) => {
                    if(this.pdf)this.pdf.destroy();
                    this.pdf = pdf;
                    this.pageMax = this.pdf.numPages;
                    this.renderPage(this.pageNum);
                });

            },
            renderPage(i) {
                this.pageRendering = true;
                let canvas = document.getElementById('the-canvas');
                let context = canvas.getContext('2d');
                this.pdf.getPage(i).then((page) => {
                    let viewport = page.getViewport({scale: this.scale/100});
                    canvas.height = viewport.height;
                    canvas.width = viewport.width;
                    let renderTask = page.render({
                        canvasContext: context,
                        viewport: viewport,
                    });
                    renderTask.promise.then(() => {
                        this.pageRendering = false;
                        if (this.pageNumPending !== null) {
                            this.renderPage(this.pageNumPending);
                            this.pageNumPending = null;
                        }
                    });
                });
            },
            queueRenderPage(num) {
                if (this.pageRendering) this.pageNumPending = num;
                else this.renderPage(num);
            },
            onPrevPage() {
                if (this.pageNum <= 1) return;
                this.$store.state.currentDoc.pageNum--;
                this.pageNum--;
                this.queueRenderPage(this.pageNum);
            },
            onNextPage(){
                if (this.pageNum >= this.pageMax)return;
                this.$store.state.currentDoc.pageNum++;
                this.pageNum++;
                this.queueRenderPage(this.pageNum);
            }
        },
    }
</script>

<style scoped>
    .link-to-see {
        font-size: 16px;
    }
    .document-title-block {
        padding: 0;
        position: absolute;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0;
        background: #9d9d9d;
    }
    .document-title{
        color: white;
        margin: 0;
    }

    .comments-add-button {
        position: absolute;
        top: 1vh;
        margin: 0 0 0 1vh;
		outline: none;
        width: 3.5vh;
        height: 3.5vh;
        border: none;
        background-color: #5b5b5b;
        background-size: 100%;
        -webkit-mask-position-x: 50%;
        -webkit-mask-position-y: 50%;
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/arrow-right-circle-fill.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/arrow-right-circle-fill.svg") no-repeat 100%;
    }
    .comments-add {
        width: 100%;
        height: 100%;
        border: none;
        outline: none;
        background: white;
        color: black;
    }
    .comments-add-block {
        width: calc(90% - 3vh);
        background-color: #ffffff;
        height: 10vh;
        margin: 1.5vh;
    }
    .comment-avatar {
        width: 15%;
        position: absolute;
        top: 0;
        left: 0;
        padding: 2vh;
    }
    .comment-block {
        position: absolute;
        top: 0;
        left: 15%;
        width: 85%;
    }
    .comments-reply {
        cursor: pointer;
    }
    .comment {
        border-bottom: 1px solid #9b9b9b;
        width: auto;
        height: 23vh;
        display: block;
        position: relative;
    }
    .comments {
        height: 65vh;
        overflow: auto;
        background-color: #ffffff;
        margin: 1.5vh;
    }
    .v-document {
        display: block;
        margin: 0;
        width: 100%;
        height: 100%;
        background-color: #ffffff;
    }
    .pdf-document {
        background-color: rgba(256,256,256,1);
        position: fixed;
        overflow: auto;
        width: 90%;
        padding: 5%;
        height: calc(90% - 6vh);
    }

    .top-page-control {
        position: relative;
        top: 0;
        height: 6vh;
        width: 100%;
        display: block;
        margin: 0;
        background-color: rgba(256,256,256,0);
    }
    .page-control {
        position: relative;
        margin-left: 30%;
        background-color: #ffa854;
        height: inherit;
        display: inline-flex;
        justify-content: center;
        width: 20%;
        border: none;
        padding-left: 1vh;
        padding-right: 1vh;
        border-bottom-left-radius: 2vh;
        border-bottom-right-radius: 2vh;
    }
    .rating {
        position: absolute;
        left: 60%;
        margin-left: 0;
        margin-right: auto;
        background-color: #ffa854;
        height: inherit;
        display: inline-flex;
        justify-content: space-between;
        width: 40%;
        border: none;
        padding-left: 1vh;
        padding-right: 1vh;
        border-bottom-left-radius: 2vh;
        /*
        left: 80%;
        display: inline;
        width: 20%;
        */
    }
    .prev-button, .next-button {
        position: relative;
        left: 0;
        top: 1vh;
        width: 4vh;
        height: 4vh;
        border: none;
        background-color: #ffffff;
        background-size: 100%;
    }
    .prev-button {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/chevron-left.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/chevron-left.svg") no-repeat 100%;
        -webkit-mask-position-x: 50%;
        -webkit-mask-position-y: 50%;
        left: 0.3vh;
    }
    .next-button {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/chevron-right.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/chevron-right.svg") no-repeat 100%;
        -webkit-mask-position-x: 50%;
        -webkit-mask-position-y: 50%;
    }
    .page-control-text {
        color: #ffffff;
        position: relative;
        top: 25%;
        font-size: 17px;
    }
    .btn-comments {
        position: relative;
        top: 1vh;
        width: 4vh;
        height: 4vh;
        background: rgba(256,256,256,0);
        border: 2px solid #ffffff;
        border-radius: 50%;
    }
    .dropdown-comments {
        background-color: #f4f4f4;
        width: 70vh;
        height: 80vh;
        position: absolute;
        top: 6vh;
        left: 0;
        z-index: 1;
    }
</style>