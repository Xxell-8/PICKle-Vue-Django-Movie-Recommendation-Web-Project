<template>
  <div class="home mt-5">
    <HomeHeader/>
    <BestMovie/>
  </div>
</template>

<script>
import HomeHeader from '@/components/movies/HomeHeader'
import BestMovie from '@/components/movies/BestMovie'

export default {
  name: 'Home',
  components: {
    HomeHeader,
    BestMovie,
  },
}
</script>
