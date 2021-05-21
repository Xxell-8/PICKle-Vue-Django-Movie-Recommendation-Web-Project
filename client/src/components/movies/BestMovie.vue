<template>
  <div>
    <h1>PICKle's BEST</h1>
    <BestMovieItem/>
  </div>
</template>

<script>
import BestMovieItem from '@/components/movies/BestMovieItem'

export default {
  name: 'BestMovie',
  components: {
    BestMovieItem,
  }
}
</script>

<style>

</style>