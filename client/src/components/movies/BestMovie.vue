<template>
  <div class="mx-5">
    <div class="row gap-3 justify-content-center">
      <MovieItem
        v-for="(movie, idx) in bestMovies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieItem from '@/components/movies/MovieItem'

export default {
  name: 'BestMovie',
  components: {
    MovieItem,
  },
  methods: {
    ...mapActions('movie', ['getBestMovies'])
  },
  computed: {
    ...mapState('movie', ['bestMovies'])
  },
  mounted: function () {
    this.getBestMovies()
  }
}
</script>

<style scoped>
  .chapter-title {
      font-weight: 900;
      font-size: 3rem;
      color: #fff;
      text-shadow: -3px -1px #F47B0F, 4px 1px #441DB2;
  }
  hr {
    width: 10rem;
    margin: 1rem auto;
    background-color: #fff;
    border-top: 0.2rem solid #bbb
  }
</style>