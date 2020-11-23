<template>
    <div class="bg-light">
    <div class="container">
        <div class="py-5 text-center">
            <h2>My Profile</h2>
            <p class="lead">Here you can update or add your personal data.</p>
        </div>

        <div class="row">
            <div class="col-md-4 order-md-2 mb-4">

                <h4 class="d-flex justify-content-between align-items-center mb-3">
                    <span class="text-muted">Profile photo</span>
                </h4>
                <div class="media-right">
                    <img class="media-object" style="width:175px">
                </div>

                <div class="form-group">
                    <label for="file">New photo</label>
                    <input type="file" class="form-control-file" id="file" ref="file" v-on:change="handleFileUpload()">
                </div>

                <h4 class="d-flex justify-content-between align-items-center mb-3">
                    <span class="text-muted">Bookmarks</span>
                </h4>
                <ul class="list-group mb-3">
                    <li class="list-group-item d-flex justify-content-between lh-condensed" v-show="bookmarks.length > 0">
                        <div v-for="bm in bookmarks" :key="bm.uploads">
                            <h6 class="my-0">{{bm.title}}</h6>
                            <small class="text-muted">Tags</small>
                        </div>
                        <!--<button type="button" class="btn btn-link">Open</button>-->
                    </li>
                    <li class="list-group-item d-flex justify-content-between">
                        <button type="button" class="btn btn-link">Show all my bookmarks</button>
                    </li>
                </ul>
                <div class="input-group">
                </div>
            </div>


            <div class="col-md-8 order-md-1">

                <h4 class="d-flex justify-content-between align-items-center mb-3">
                    <span class="text-muted">About me</span>
                </h4>

                <form class="needs-validation" novalidate v-on:submit.prevent>
                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="first-name">First name</label>
                            <input type="text" class="form-control" id="first-name" placeholder="" v-model="first_name">
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="middle-name">Middle name</label>
                            <input type="text" class="form-control" id="middle-name" placeholder="" v-model="middle_name">
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="last-name">Last name</label>
                            <input type="text" class="form-control" id="last-name" placeholder="" v-model="last_name">
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="username">Email</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text">@</span>
                                </div>
                                <input type="text" class="form-control" id="username" placeholder="" v-model="email">
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="password">Password<span class="text-muted"></span></label>
                            <input type="password" class="form-control" id="password" placeholder="" required v-model="password">
                            <div class="invalid-feedback">
                                Please enter your password.
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12 mb-6">
                            <label for="password-repeat">Repeat password<span class="text-muted"></span></label>
                            <input type="password" class="form-control" id="password-repeat" placeholder="" required v-model="re_password">
                            <div class="invalid-feedback">
                                Please repeat your password.
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label for="degree">Degree</label>
                            <select class="custom-select d-block w-100" id="degree" required v-model="degree">
                                <option value="" disabled>Choose...</option>
                                <option>Bachelor</option>
                                <option>Master</option>
                                <option>I am not a student</option>
                            </select>
                            <div class="invalid-feedback">
                                Please select your degree.
                            </div>
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="course">Course</label>
                            <select class="custom-select d-block w-100" id="course" v-model="course">
                                <option value="" disabled>Choose...</option>
                                <option v-show="degree_bach || degree_mas">1</option>
                                <option v-show="degree_bach || degree_mas">2</option>
                                <option v-show="degree_bach && !degree_mas">3</option>
                                <option v-show="degree_bach && !degree_mas">4</option>
                                <option v-show="!degree_bach && !degree_mas">I am not a student</option>
                            </select>
                            <div class="invalid-feedback">
                                Please select your degree.
                            </div>
                        </div>

                        <div class="col-md-4 mb-3">
                            <label for="track">Track</label>
                            <select class="custom-select d-block w-100" id="track" v-model="track">
                                <option value="" disabled>Choose...</option>
                                <option v-show="(degree_bach && course < 3) && !degree_mas">Computer Science</option>
                                <option v-show="(degree_bach && course > 2) || degree_mas">Robotics</option>
                                <option v-show="(degree_bach && course > 2) || degree_mas">Data Science</option>
                                <option v-show="(degree_bach && course > 2) || degree_mas">Software Engineering</option>
                                <option v-show="(degree_bach && course > 2) || degree_mas">Security and Network Engineering</option>
                                <option v-show="!degree_bach && !degree_mas">I am not a student</option>
                            </select>
                            <div class="invalid-feedback">
                                Please select your degree.
                            </div>
                        </div>

                        <hr class="mb-4">
                        <button class="btn btn-primary btn-lg btn-block" type="submit" @click="onSubmit()">Update</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
    </div>
</template>

<script>
    import {mapState} from "vuex";

    export default {
        data: function(){
            return {
                first_name: "",
                last_name: "",
                middle_name: "",
                email: "",
                password: "",
                re_password: "",
                track: "Computer Science",
                course: "1",
                degree: "Bachelor",
                degree_mas: "",
                degree_bach: "",
                track_availability: "",
                file: ""
            };
        },
        name: "profile",
        computed: {
            ...mapState({info:'informationAboutMe', bookmarks: 'bookmarks'}),
        },
        watch:{
            degree:function(){
                this.degree_bach = this.degree === 'Bachelor';
                this.degree_mas = this.degree === 'Master'
            },
            course:function(){
                if(this.degree_mas === true){
                    this.track_availability = true;
                    return;
                }
                if(this.degree_bach === true && this.course > 2){//todo check whether this.course is numerical or string
                    this.track_availability = true;
                    return;
                }
                this.track_availability = false;
            },
            info:function(val){
                document.querySelector('img.media-object').src = val.image;
                //let deg = (['Bachelor', 'Master', 'I am not a student'])[val.degree];
                //let cour = (['1', '2', '3', '4', 'I am not a student'])[val.course-1];
                //let tr = (['Computer Science', 'Robotics', 'Data Science', 'Software Engineering', 'Security and Network Engineering', 'I am not a student'])[val.track];
                //console.log(deg);
                //console.log(cour);
                //console.log(tr);
                this.first_name = val.first_name;
                this.last_name = val.last_name;
                this.middle_name = val.middle_name;
                this.email = val.email;
                //this.track = deg;
                //this.course = cour;
                //this.degree = tr;
            }
        },
        created() {
            this.$store.dispatch('getInfo');
            console.log(this.info);
            this.$store.dispatch('getBookmarks');
        },
        methods: {
            handleFileUpload(){
                this.file = this.$refs.file.files[0];
            },
            onSubmit() {
                let form = document.querySelector(".needs-validation");
                if (form.checkValidity() === false) {
                    form.classList.add('was-validated');
                    return;
                }
                if(this.re_password !== this.password)return;
                let FormData = require('form-data');
                let data = new FormData();
                let deg = ['Bachelor', 'Master', 'I am not a student'].findIndex((element)=>{return this.degree === element});
                let cour = ['1', '2', '3', '4', 'I am not a student'].findIndex((element)=>{return this.course === element}) + 1;
                let tr = ['Computer Science', 'Robotics', 'Data Science', 'Software Engineering', 'Security and Network Engineering', 'I am not a student'].findIndex((element)=>{return this.track === element});
                data.append('first_name', this.first_name);
                data.append('last_name', this.last_name);
                data.append('mid_name', this.middle_name);
                data.append('email', this.email);
                data.append('password', this.password);
                data.append('re_password', this.re_password);
                data.append('degree', deg);
                data.append('image', this.file);
                data.append('course', cour);
                data.append('track', tr);
                this.$store.dispatch('changeInfo', data);
            }
        }
    }
</script>

<style scoped>
    .container {
        max-width: 960px;
    }

    .lh-condensed { line-height: 1.25; }

</style>