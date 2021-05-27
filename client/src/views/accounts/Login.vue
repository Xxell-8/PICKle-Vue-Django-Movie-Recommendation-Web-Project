<template>
  <div class="login">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-6 justify-content-center py-5">
          <div class="login-wrap">
            <div class="offset-3 col-6 mb-2">
              <img class="logo-img img-fluid" src="../../assets/logo.svg" alt="logo">
            </div>
            <h2 class="text-center">WELCOME</h2>
            <p>Hello, Stranger! This is PICKle.</p>
            <div class="mb-2">
              <input class="form-control" type="text" placeholder="Username" v-model="loginInfo.username" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="password" placeholder="Password" v-model="loginInfo.password" required>
            </div>
            <div>
              <button @click="login(loginInfo)" class="btn btn-outline-primary">Login</button>
            </div>
            <hr>
            <div>
              <span>PICKLE에 가입해보세요 ▸ </span>
              <a class="signup-link" @click="moveToSignup" href="#">Signup</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: 'Login', 
  data: function () {
    return {
      loginInfo: {
        username: null,
        password: null,
      },
    }
  }, 
  methods: {
    ...mapActions('auth', ['login']),
    moveToSignup: function () {
      this.$router.push({ name: 'Signup' })
    }
  }
}
</script>
  
<style scoped>
  .login-wrap {
    background: #1E1F26;
    padding: 50px;
  }

  .form-control {
    color: #fff;
    background: #292A33;
    box-shadow: none;
    border-radius: 0;
    border: none;
    border-bottom: 1px solid #F47B0F;
  }

  .btn-outline-primary {
    color: #F47B0F;
    border: 2px solid #F47B0F;
  }
  .btn-outline-primary:hover {
    color: #fff;
    background-color: #441DB2;
    border: 2px solid #F47B0F;
  }
  .signup-link {
    color: #F47B0F;
  }
  
</style>