<template>
    <div class="v-document">
        <div class="top-page-control">
            <div class="page-control">
                <button class="prev-button no-outline" @click="onPrevPage()"></button>
                <p class="page-control-text">{{pageNum}}/{{pageMax}}</p>
                <p class="page-control-text">{{scale*100}}%</p>
                <button class="next-button no-outline" @click="onNextPage()"></button>
            </div>
            <div class="rating">
                <p class="page-control-text">{{rating}}</p>
                <button class="comments-icon no-outline" @click="dropdownComments()"></button>
                <div class="dropdown-comments" v-show="dropdown">
                    <div class="comments">
                        <div v-for="comment in comments" :key="comment.text" class="comment">
                            <div class="comment-avatar">
                                <img src="../../assets/profile.png" alt="" class="avatar">
                            </div>
                            <div class="comment-block">
                                <p class="list-item-text-search-bold">{{comment.sender}}</p>
                                <p class="list-item-text-search">{{comment.text}}</p>
                                <p class="comments-reply list-item-text-search-bold">Reply</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <div class="pdf-document">
            <canvas id="the-canvas"></canvas>
        </div>
    </div>
</template>

<script>
    import * as pdfjsLib from 'pdfjs-dist';
    export default {
        name: "v-content",
        components: {
        },
        data: function(){
            return {
                comments: [{text: "What is 2+2?", sender: "12k club member"},
                    {text: "You should know it from the school. If the question was what is pi, some people would argue that it is 4 or 3, but to answer your question it is obviously 4.", sender: "Professor Gorodetskiy"},
                    {text: "2+2=pi", sender: "36k club member"},
                    {text: "22", sender: "JavaScript"}],
                dropdown: false,
                rating: 3.5,
                pdf: undefined,
                pages: [],
                pageRendering: false,
                pageNumPending: null,
                pageNum: 1,
                pageMax: undefined,
                url: 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf',
                scale: 1
            }
        },
        methods: {
            dropdownComments(){
                this.dropdown = !this.dropdown;
            },
            changeScale(scale){
                this.renderPage(this.pageNum);
            },
            changePage(pageNum){
                this.renderPage(this.pageNum);
            },
            fetchPDF() {
                pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjsLib.version}/pdf.worker.js`;
                pdfjsLib.getDocument(this.url).promise.then((pdf) => {
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
                    let viewport = page.getViewport({scale: this.scale});
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
                this.pageNum--;
                this.queueRenderPage(this.pageNum);
            },
            onNextPage(){
                if (this.pageNum >= this.pageMax)return;
                this.pageNum++;
                this.queueRenderPage(this.pageNum);
            }
        },
        created() {
            this.fetchPDF();
        }
    }
</script>

<style scoped>
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
        height: 80vh;
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
        overflow: scroll;
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
        top: 1vh;
        width: 4vh;
        height: 4vh;
        border: none;
        background-color: #ffffff;
        background-size: 100%;
        -webkit-mask-position-x: 50%;
        -webkit-mask-position-y: 50%;
    }
    .prev-button {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/chevron-left.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/chevron-left.svg") no-repeat 100%;
    }
    .next-button {
        -webkit-mask: url("../../../node_modules/bootstrap-icons/icons/chevron-right.svg") no-repeat 100%;
        mask: url("../../../node_modules/bootstrap-icons/icons/chevron-right.svg") no-repeat 100%;
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