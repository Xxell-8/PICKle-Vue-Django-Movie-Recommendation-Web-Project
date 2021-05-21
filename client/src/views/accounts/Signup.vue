<template>
  <div class="singup">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-6 justify-content-center py-5">
          <div class="signup-wrap">
            <div class="offset-3 col-6 mb-2">
              <img class="logo-img img-fluid" src="../../assets/logo.svg" alt="logo">
            </div>
            <h2 class="text-center">Signup</h2>
            <p>PICKle에 가입하고, 다양한 영화 추천 서비스를 즐겨보세요!</p>
            <div class="mb-2">
              <input class="form-control" type="text" placeholder="Username" v-model="userInfo.username" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="password" placeholder="Password" v-model="userInfo.password" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="password" placeholder="Password Confirmation" v-model="userInfo.passwordConfirmation" required>
            </div>
            <div>
              <button @click="signup(userInfo)" class="btn btn-outline-primary">Signup</button>
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
  name: 'Signup',
  data: function () {
    return {
      userInfo: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },
  methods: {
    ...mapActions('auth', ['signup']),
  },
}
</script>

<style scpoped>
  .signup-wrap {
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
</style>