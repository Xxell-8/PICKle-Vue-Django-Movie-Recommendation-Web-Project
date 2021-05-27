<template>
  <div id="app">
    <NavBar/>
    <router-view style="margin-top: 5rem;"/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: 'App',
  components: {
    NavBar,
  },
}
</script>


<style>
#app {
  font-family: 'Noto Sans KR', 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
}
</style>
