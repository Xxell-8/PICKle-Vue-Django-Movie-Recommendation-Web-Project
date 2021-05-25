<template>
  <div>
    <h1 class="chapter-title">PICK TODAY's Keyword</h1>
    <p>오늘의 추천 키워드를 선택해주세요</p>
    <hr>
    <div v-if="pickTheme" class="row gap-3 justify-content-center">
      <MovieItem
        v-for="(movie, idx) in recommendMovies"
        :key="idx"
        :movie="movie"
      />
      <button @click="resetCard">다시뽑기</button>
    </div>
    <div v-else class="row gap-3 justify-content-center">
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img @click="randomPick" src="../../assets/recommend/random.svg" alt="random">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img @click="genrePick" src="../../assets/recommend/genre.svg" alt="genre">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/similar.svg" alt="similar">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/classic.svg" alt="classic">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img src="../../assets/recommend/series.svg" alt="series">
        </div>
      </div>
    </div>    
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieItem from '@/components/movies/MovieItem'

export default {
  name: 'Recommendation',
  components: {
    MovieItem,
  },
  data: function () {
    return {
      pickTheme: false,
    }
  },
  methods: {
    randomPick: async function () {
      const response = await this.$store.dispatch('movie/getRandomMovies')
      if (response === 'DONE') {
        this.pickTheme = true
      }
    },
    genrePick: async function () {
      const response = await this.$store.dispatch('movie/getGenreMovies')
      if (response === 'DONE') {
        this.pickTheme = true
      }
    },
    resetCard: function () {
      this.pickTheme = false
    }
  },
  computed: {
    ...mapState('movie', ['recommendMovies'])
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
  .card {
    border: 0;
    border-radius: 0;
    width: 13rem;
    overflow: hidden;
    box-shadow: 15px 15px 25px black;
  }
</style>