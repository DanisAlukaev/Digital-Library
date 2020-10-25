<template>
    <div class="v-document">
        <div class="page-control">
            <button @click="onPrevPage" class="prev-button">Previous page</button>
            <button @click="onNextPage" class="next-button">Next page</button>
            <p>{{pageNum}}/{{pageMax}}</p>
            <div class="search-block">
                <input type="text"  required class="input-search" placeholder="Scale" v-model.number.lazy="scale" @change="changeScale(scale)">
            </div>
            <div class="search-block">
                <input type="text" required class="input-search" placeholder="Go to Page" v-model.number.lazy="pageNum" @change="renderPage(pageNum)">
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
        props: {
            url: {
                type: String,
                required: true
            },
            scale: {
                type: Number,
                default: 1
            }
        },
        data: function(){
            return {
                pdf: undefined,
                pages: [],
                pageRendering: false,
                pageNumPending: null,
                pageNum: 1,
                pageMax: 0
            }
        },
        methods: {
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
    .v-document {
        display: block;
        margin: 0;
        width: 100%;
    }
    .pdf-document {
        position: fixed;
        overflow: scroll;
        width: 90%;
        padding: 5%;
        height: 90%;
    }

    .page-control {
        height: 6vh;
        width: 100%;
        display: inline-flex;
        justify-content: center;
        background: rgba(0,0,0,0);
        border-bottom: 2px solid #DDDDDD;
    }
    .prev-button, .next-button {
        width: 15vh;
        height: 6vh;
        border: none;
        background: rgba(0,0,0,0);
    }

</style>