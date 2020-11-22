<template>
    <div class="bg-light">
        <div class="container">
            <div class="py-5 text-center">
                <h2>Welcome to Digital Library!</h2>
            </div>
            <div class="row">
                <div class="col-md-4 order-md-2 mb-4">
                    <p class="lead">Please fill the fields below with your data.</p>
                </div>
                <div class="col-md-4 order-md-2 mb-4">
                    <button class="btn btn-lg btn-primary btn-block" @click="go_to_login()">I'm already registered</button>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4 order-md-2 mb-4">
                    <div class="input-group">
                        <div class="input-group-append">
                        </div>
                    </div>
                </div>

                <div class="col-md-12 order-md-1">
                    <form class="needs-validation" novalidate v-on:submit.prevent>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="firstName">First name</label>
                                <input type="text" class="form-control" id="firstName" placeholder="" required v-model="first_name">
                                <div class="invalid-feedback">
                                    Valid first name is required.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="middleName">Middle name</label>
                                <input type="text" class="form-control" id="middleName" placeholder="" v-model="middle_name">
                                <div class="invalid-feedback">
                                    Valid middle name is required.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="lastName">Last name</label>
                                <input type="text" class="form-control" id="lastName" placeholder="" required v-model="last_name">
                                <div class="invalid-feedback">
                                    Valid last name is required.
                                </div>
                            </div>
                        </div>
                        <!--
                        <div class="mb-3">
                            <label for="username">Username</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text">@</span>
                                </div>
                                <input type="text" class="form-control" id="username" placeholder="Username" required v-model="user_name">
                                <div class="invalid-feedback" style="width: 100%;">
                                    Your username is required.
                                </div>
                            </div>
                        </div>
                        -->
                        <div class="mb-3">
                            <label for="email">Email<span class="text-muted"></span></label>
                            <input type="email" class="form-control" id="email" placeholder="you@innopolis.university" required v-model="email">
                            <div class="invalid-feedback">
                                Please enter a valid email address.
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="password">Password<span class="text-muted"></span></label>
                            <input type="password" class="form-control" id="password" placeholder="" required v-model="password">
                            <div class="invalid-feedback">
                                Please enter your password.
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="password-repeat">Repeat password<span class="text-muted"></span></label>
                            <input type="password" class="form-control" id="password-repeat" placeholder="" required v-model="re_password">
                            <div class="invalid-feedback">
                                Please repeat your password.
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
                                <select class="custom-select d-block w-100" id="course" required v-model="course">
                                    <option value="" disabled>Choose...</option>

                                    <option v-show="degree_bach || degree_mas">1</option>
                                    <option v-show="degree_bach || degree_mas">2</option>
                                    <option v-show="degree_bach && !degree_mas">3</option>
                                    <option v-show="degree_bach && !degree_mas">4</option>
                                    <option v-show="!degree_bach && !degree_mas">I am not a student</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please provide your number of course.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="track">Track</label>
                                <select class="custom-select d-block w-100" id="track" required v-model="track">
                                    <option value="" disabled>Choose...</option>
                                    <option v-show="(degree_bach && course < 3) && !degree_mas">Computer Science</option>
                                    <option v-show="(degree_bach && course > 2) || degree_mas">Robotics</option>
                                    <option v-show="(degree_bach && course > 2) || degree_mas">Data Science</option>
                                    <option v-show="(degree_bach && course > 2) || degree_mas">Software Engineering</option>
                                    <option v-show="(degree_bach && course > 2) || degree_mas">Security and Network Engineering</option>
                                    <option v-show="!degree_bach && !degree_mas">I am not a student</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please provide your track.
                                </div>
                            </div>
                            <hr class="mb-4">

                            <div class="mb-3">
                                <button class="btn btn-lg btn-primary btn-block" @click="onSubmit()">Registrate</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "v-authentication",
        data: function(){
            return {
                first_name: "qwerty",
                last_name: "qwerty",
                middle_name: "qwerty",
                email:"qwe@innopolis.university",
                password:"qwe123rty567",
                re_password:"qwe123rty567",
                track: "Computer Science",
                course: "1",
                degree: "Bachelor",
                degree_mas: "",
                degree_bach: "",
                track_availability: ""
            };
        },
        created() {
            this.$store.dispatch('tryAutoLogin');
        },
        watch: {
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
			}

        },
        methods:{
            go_to_login(){
                this.$router.replace({name: 'login'});
            },
            onSubmit(){
                let form = document.querySelector(".needs-validation");
                if(form.checkValidity() === false) {
                    form.classList.add('was-validated');
                    return;
                }
                if(this.password !== this.re_password)return;//todo write to user that he need to check password
                let deg = ['Bachelor', 'Master', 'I am not a student'].findIndex((element)=>{return this.degree === element});
                let cour = ['1', '2', '3', '4', 'I am not a student'].findIndex((element)=>{return this.course === element}) + 1;
                let tr = ['Computer Science', 'Robotics', 'Data Science', 'Software Engineering', 'Security and Network Engineering', 'I am not a student'].findIndex((element)=>{return this.track === element});
                let authData = {
                    email: this.email,
                    password: this.password,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    re_password: this.re_password,
                    middle_name: this.middle_name,
                    track: tr,
                    course: cour,
                    degree: deg
                };
                console.log(authData);
                this.$store.dispatch("signup", authData);
            }
        }
    }
</script>

<style scoped>
    .container {
        max-width: 960px;
    }

    .lh-condensed {line-height: 1.25;}
</style>