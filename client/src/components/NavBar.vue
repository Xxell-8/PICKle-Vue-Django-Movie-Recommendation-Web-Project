<template>
  <nav class="fixed-top navbar navbar-expand navbar-dark">
    <router-link class="navbar-brand fw-bold" :to="{ name: 'Pickle' }">PICKle</router-link>
    <div v-if="isLogin" class="navbar-nav d-flex justify-content-between">
      <div class="d-flex gap-1">
        <router-link class="nav-link" :to="{ name: 'Recommendation' }">Recommend</router-link>
        <router-link class="nav-link" :to="{ name: 'PickyPick' }">Picky Pick</router-link>
        <router-link class="nav-link" :to="{ name: 'MyProfile' }">My Pickle</router-link>
        <span v-if="myProfile.is_superuser">
          <a class="nav-link" href="http://localhost:8000/admin/">Admin</a>
        </span>
        <router-link class="nav-link" @click.native="logout" to="#">Logout</router-link>
        <router-link class="nav-link" :to="{ name: 'Search' }"><i class="fas fa-search"></i></router-link>
      </div>
    </div>
    <div v-else class="navbar-nav">
      <router-link class="nav-link" :to="{ name: 'Login' }">Login</router-link>
      <router-link class="nav-link" :to="{ name: 'Signup' }">Signup</router-link>
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
    ...mapState('auth', ['username', 'isLogin', 'myProfile']),
    ...mapGetters('auth', ['decodeToken']),
  }
}
</script>

<style>
  .navbar-dark {
    height: 3rem;
    background-color: rgba(30, 31, 38, 0.9);
    padding: 0.5rem 3rem;
  }
</style>