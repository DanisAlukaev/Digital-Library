<template>
    <div class="text-center login-body">
        <form class="form-signin" v-on:submit.prevent>
            <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus v-model="email">

            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" id="inputPassword" class="form-control" placeholder="Password" required v-model="password">

            <button class="btn btn-lg btn-primary btn-block" @click="onSubmit()">Sign in</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: "login",
        data:function(){
            return {
                email:"d.alukaev@innopolis.university",
                password:"4F67rE21h%26l"
            }
        },
        created() {
            this.$store.dispatch('tryAutoLogin');
        },
        methods:{
            onSubmit(){
                let authData = {
                    email: this.email,
                    password: this.password,
                };
                //this.$store.dispatch("testlogin");
                this.$store.dispatch("login", authData);
            }
        }
    }
</script>

<style scoped>
    .login-body {
        height: 95vh;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
    }

    .form-signin {
        width: 100%;
        max-width: 330px;
        padding: 15px;
        margin: auto;
    }
    .form-signin .checkbox {
        font-weight: 400;
    }
    .form-signin .form-control {
        position: relative;
        box-sizing: border-box;
        height: auto;
        padding: 10px;
        font-size: 16px;
    }
    .form-signin .form-control:focus {
        z-index: 2;
    }
    .form-signin input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }
    .form-signin input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>