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
            <div class="mb-3">
              <input class="form-control" type="text" placeholder="Username" v-model="userInfo.username" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="password" placeholder="Password" v-model="userInfo.password" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="password" placeholder="Password Confirmation" v-model="userInfo.passwordConfirmation" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="text" placeholder="First Name" v-model="userInfo.first_name" required>
            </div>
            <div class="mb-3">
              <input class="form-control" type="text" placeholder="Last Name" v-model="userInfo.last_name" required>
            </div>
            <div class="mb-3">
              <multiselect 
                v-model="tags"
                label="name"
                track-by="id" 
                :options="genreOptions" 
                :multiple="true" 
                :max="3"
                @select="addGenre"
                @remove="removeGenre"></multiselect>
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
import Multiselect from 'vue-multiselect'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Signup',
  components: {
    Multiselect,
  },
  data: function () {
    return {
      userInfo: {
        username: null,
        password: null,
        passwordConfirmation: null,
        first_name: null,
        last_name: null,
        genres: [],
      },
      tags: [],
    }
  },
  methods: {
    ...mapActions('auth', ['signup']),
    ...mapActions('movie', ['getGenreList']),
    addGenre(event) {
      //console.log(event)
      this.userInfo.genres.push(event.id)
    },
    removeGenre(event) {
      //console.log(event)
      const index = this.userInfo.genres.indexOf(event.id)
      this.userInfo.genres.splice(index, 1)
    },
  },
  computed: {
    ...mapState('movie', ['genreOptions'])
  },
  created: function () {
    this.getGenreList()
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
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