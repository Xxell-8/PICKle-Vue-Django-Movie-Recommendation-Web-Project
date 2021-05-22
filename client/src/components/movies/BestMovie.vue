<template>
  <div class="container">
    <h1>PICKle's BEST</h1>
    <button @click="getMovies"></button>
    <div class="row gap-3 justify-content-center">
      <BestMovieItem
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import BestMovieItem from '@/components/movies/BestMovieItem'

export default {
  name: 'BestMovie',
  components: {
    BestMovieItem,
  },
  methods: {
    ...mapActions('movie', ['getMovies'])
  },
  computed: {
    ...mapState('movie', ['movies'])
  }
}
</script>

<style>

</style>