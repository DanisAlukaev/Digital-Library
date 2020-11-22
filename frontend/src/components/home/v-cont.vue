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
                            <span>Innopoints total</span>
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
                        <div class="form-group">
                            <label for="description">Description</label>
                            <textarea class="form-control" id="description" rows="3" required v-model="description"></textarea>
                            <div class="invalid-feedback">
                                Description is required.
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="file">Choose the file</label>
                            <input type="file" class="form-control-file" id="file" ref="file" v-on:change="handleFileUpload()" required>
                            <div class="invalid-feedback">
                                File is required.
                            </div>
                        </div>

                        <hr class="mb-4">

                        <h4 class="mb-3">Choose tags</h4>
                        <!--todo write v-for loop -->
                        <div class="custom-control custom-checkbox" v-for="tag in tags" :key="tag.id">
                            <input type="checkbox" class="custom-control-input" id="tag" v-model="tagsUpload">
                            <label class="custom-control-label" for="tag">{{tag.name}}</label>
                        </div>
                        <!--todo write v-for loop -->

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
                tagsUpload: [],
                file: ''
            }
        },
        computed: {
            ...mapState({tags: 'tags'}),
            title: "C++ lectures",
            description: "Pdf Lectures of BS19"
        },
        methods: {
            onSubmit(){
                let form = document.querySelector(".needs-validation");
                if(form.checkValidity() === false) {
                    form.classList.add('was-validated');
                    return;
                }
                let FormData = require('form-data');
                let form_data = new FormData();
                form_data.append('title', this.title);
                form_data.append('description', this.description);
                form_data.append('file', this.file);
                /*
                let j = 0;
                this.tags.forEach((tag,i)=>{
                    form_data.append(`tags[${j++}]`, `${i}`)
                });
                 */
                this.$store.dispatch('submitFile', form_data);
            },
            handleFileUpload(){
                this.file = this.$refs.file.files[0];
            }
        },
        created(){
            this.$store.dispatch('getTags');
        }
    }
</script>

<style scoped>
    .container {
        max-width: 960px;
    }

    .lh-condensed { line-height: 1.25; }

</style>