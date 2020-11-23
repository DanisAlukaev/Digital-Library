<template>
    <div class="bg-light">
        <div class="container">
            <div class="py-5 text-center">
                <h2>Contribute to Digital Library</h2>
                <p class="lead">Here you can upload materials to Digital Library. Please fill the fields carefully and submit for consideration.</p>
            </div>

            <div class="row">

                <div class="col-md-4 order-md-2 mb-4">
                    <h4 class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-muted">Your contributions</span>
                    </h4>
                    <ul class="list-group mb-3">
                        <li class="list-group-item d-flex justify-content-between lh-condensed">
                            <div>
                                <h6 class="my-0">Title 1</h6>
                                <small class="text-muted">01.10.2020</small>
                            </div>
                            <span class="text-muted">3 innopoints</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between lh-condensed">
                            <div>
                                <h6 class="my-0">Title 2</h6>
                                <small class="text-muted">15.10.2020</small>
                            </div>
                            <span class="text-muted">2 innopoints</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between lh-condensed">
                            <div>
                                <h6 class="my-0">Title 3</h6>
                                <small class="text-muted">14.11.2020</small>
                            </div>
                            <span class="text-muted">5 innopoints</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Innopoints total </span>
                            <strong>10</strong>
                        </li>
                    </ul>

                    <div class="input-group">
                    </div>

                </div>

                <div class="col-md-8 order-md-1">
                    <h4 class="mb-3">Information about material</h4>
                    <form class="needs-validation" novalidate v-on:submit.prevent>
                        <div class="row">
                            <div class="col-md-12 mb-6">
                                <label for="title">Title</label>
                                <input type="text" class="form-control" id="title" placeholder="" value="" required v-model="title">
                                <div class="invalid-feedback">
                                    Title is required.
                                </div>
                            </div>

                        </div>
                        <!--
                        <div class="form-group">
                            <label for="description">Description</label>
                            <textarea class="form-control" id="description" rows="3" required v-model="description"></textarea>
                            <div class="invalid-feedback">
                                Description is required.
                            </div>
                        </div>
                        -->
                        <label for="type">Type</label>
                        <div class="mb-3">
                            <select class="custom-select d-block w-100" id="type" v-model="type">
                                <option value="" disabled>Choose...</option>
                                <option>Document</option>
                                <option>Image</option>
                                <option>Video</option>
                                <option>Link</option>
                            </select>
                            <div class="invalid-feedback">
                                Please select type of your upload.
                            </div>
                        </div>

                        <div class="form-group" v-show="type!=='Link'">
                            <label for="file">Choose the file</label>
                            <input type="file" class="form-control-file" id="file" ref="file" v-on:change="handleFileUpload()" required>
                            <div class="invalid-feedback">
                                File is required.
                            </div>
                        </div>

                        <div class="form-group" v-show="type==='Link'">
                            <label for="link">Link</label>
                            <input type="text" class="form-control" id="link" placeholder="Link:" value="" required v-model="link">
                            <div class="invalid-feedback">
                                Link is required.
                            </div>
                        </div>

                        <hr class="mb-4">

                        <div class="row">
                            <div class="col-md-6">
                                <h4 class="mb-3">Tags</h4>
                                <div v-for="tag in tags" :key="tag.id" class="custom-control custom-checkbox">
                                    <input class="custom-control-input" :id="`tag-${tag.id}`" type="checkbox" v-bind:value="tag" v-model="tagsUpload">
                                    <label class="custom-control-label" :for="`tag-${tag.id}`">{{tag.name}}</label><br>
                                </div>
                            </div>

                            <div class="col-md-6">
                                <h4 class="mb-3">Thematic page</h4>
                                <div class="btn-group btn-group-vertical" data-toggle="buttons">

                                    <div v-for="th in th_pages" :key="th.id" class="custom-control custom-radio">
                                        <input class="custom-control-input" :id="`th-${th.id}`" type="radio" v-bind:value="th" v-model="thUpload">
                                        <label class="custom-control-label" :for="`th-${th.id}`">{{th.title}}</label><br>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr class="mb-4">
                        <button class="btn btn-primary btn-lg btn-block" type="submit" @click="onSubmit()">Contribute</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex';
    export default {
        name: "v-cont",
        data: function(){
            return {
                file: '',
                type: 'Document',
                link: '',
                title: "DE Holodov",
                //description: "Pdf Lectures of BS19",
                thUpload: [],
                tagsUpload: []
            }
        },
        computed: {
            ...mapState({tags: 'tags', th_pages: 'thematicalPages'}),
        },
        methods: {
            onSubmit(){
                let form = document.querySelector(".needs-validation");
                if(form.checkValidity() === false) {
                    form.classList.add('was-validated');
                    //console.log("onSubmit shouldn't work");
                    //return;
                }
                let FormData = require('form-data');
                let form_data = new FormData();
                form_data.append('title', this.title);
                //form_data.append('description', this.description);
                this.tagsUpload.forEach((tag, i)=>{
                    form_data.append(`tags[${i}]`, tag.id);
                });
                form_data.append('thematic_page', this.thUpload.id);

                let typen = 0;
                if(this.type === 'Image')typen = 1;
                if(this.type === 'Video')typen = 2;
                if(this.type === 'Link')typen = 3;
                form_data.append('type', typen);
                if(typen === 2)form_data.append('link', this.link);
                else form_data.append('file', this.file);
                this.$store.dispatch('submitFile', form_data);
            },
            handleFileUpload(){
                this.file = this.$refs.file.files[0];
            }
        },
        created(){
            this.$store.dispatch('getTags');
            this.$store.dispatch('getThematicalPages');
        }
    }
</script>

<style scoped>
    .container {
        max-width: 960px;
    }

    .lh-condensed { line-height: 1.25; }

</style>