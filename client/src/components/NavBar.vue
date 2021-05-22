<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand fw-bold" :to="{ name: 'Home' }">PICKle</router-link>
      <div class="collapse navbar-collapse" id="navbarNav">
        <span v-if="isLogin">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Recommendation' }">Recommend</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'PickyPick' }">Picky Pick</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Search' }">검색</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" @click.native="logout" to="#">로그아웃</router-link>
            </li>
            <span class="navbar-text text-white">Hello, {{ decodeToken.username }}!</span>
          </ul>
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