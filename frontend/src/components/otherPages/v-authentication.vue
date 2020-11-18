<template>
    <div class="bg-light">
        <div class="container">
            <div class="py-5 text-center">
                <!--<h2>Welcome to Digital Library!</h2>-->
                <p class="lead">Please fill the fields below with your data.</p>
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
                                <input type="text" class="form-control" id="firstName" placeholder="" required v-model="firstName">
                                <div class="invalid-feedback">
                                    Valid first name is required.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="middleName">Middle name</label>
                                <input type="text" class="form-control" id="middleName" placeholder="" v-model="middleName">
                                <div class="invalid-feedback">
                                    Valid middle name is required.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="lastName">Last name</label>
                                <input type="text" class="form-control" id="lastName" placeholder="" required v-model="lastName">
                                <div class="invalid-feedback">
                                    Valid last name is required.
                                </div>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="username">Username</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text">@</span>
                                </div>
                                <input type="text" class="form-control" id="username" placeholder="Username" required v-model="userName">
                                <div class="invalid-feedback" style="width: 100%;">
                                    Your username is required.
                                </div>
                            </div>
                        </div>

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
                            <input type="password" class="form-control" id="password-repeat" placeholder="" required v-model="confirmPassword">
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
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option>I am not a student</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please provide your number of course.
                                </div>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label for="track">Track</label>
                                <select class="custom-select d-block w-100" id="track" required v-model="track">
                                    <option value="" disabled>Choose...</option>
                                    <option>Computer Science</option>
                                    <option>Robotics</option>
                                    <option>Data Science</option>
                                    <option>Software Engineering</option>
                                    <option>Security and Network Engineering</option>
                                    <option>I am not a student</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please provide your track.
                                </div>
                            </div>
                            <hr class="mb-4">
                            <button class="btn btn-primary btn-lg btn-block" @click="onSubmit()">Registrate</button>
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
                firstName: "",
                lastName: "",
                middleName: "",
                userName: "",
                email:"",
                password:"",
                confirmPassword:"",
                track: "",
                course: "",
                degree: ""
            };
        },
        methods:{
            onSubmit(){
                let form = document.querySelector(".needs-validation");

                if(form.checkValidity() === false) {
                    form.classList.add('was-validated');
                    return;
                }

                if(this.password !== this.confirmPassword)return;//todo write to user that he need to check password
                let authData = {
                    email: this.email,
                    password: this.password,
                    firstName: this.firstName,
                    lastName: this.lastName,
                    middleName: this.middleName,
                    userName: this.userName,
                    track: this.track,
                    course: this.course,
                    degree: this.degree
                };
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