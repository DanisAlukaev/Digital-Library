<template>
    <div>
    </div>
</template>

<script>
    export default {
        name: "v-authentication",
        data: function(){
            return {
                email:"",
                password:"",
                confirmPassword:""
            };
        },
        methods:{
            onSubmit(){
                if(this.password !== this.confirmPassword)return;//todo write to user that he need to check password
                let authData = {
                    email: this.email,
                    password: this.password,
                };
                this.$store.dispatch("signup", authData);
            }
        }
    }
</script>

<style scoped>

</style>