<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand fw-bold" :to="{ name: 'Home' }">PICKle</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <span v-if="isLogin">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" :to="{ name: 'Recommendation' }">Recommend</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" :to="{ name: 'PickyPick' }">Picky Pick</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" :to="{ name: 'Search' }">검색</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" @click.native="logout" to="#">로그아웃</router-link>
            </li>
          </ul>
          <span class="nav-link text-white ms-auto">{{ decodeToken.username }}님 환영합니다!</span>
        </span>
        <span v-else>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" :to="{ name: 'Login' }">로그인</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link btn btn-link" :to="{ name: 'Signup' }">회원가입</router-link>
            </li>
          </ul>
        </span>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  methods: {
    ...mapActions('auth', ['logout']),
  },
  computed: {
    ...mapState('auth', ['username', 'isLogin']),
    ...mapGetters('auth', ['decodeToken']),
  }
}
</script>

<style>

</style>