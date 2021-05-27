<template>
  <div class="mx-5">
    <h1 class="chapter-title">PICK TODAY's Keyword</h1>
    <button 
      v-if="pickTheme" 
      @click="resetCard"
      class="btn btn-outline-warning my-3"
    >다시뽑기</button>
    <div v-else>
      <p>오늘의 추천 키워드를 선택해주세요</p>
      <hr>
    </div>
    <div v-if="pickTheme" class="row gap-3 justify-content-center">
      <MovieItem
        v-for="(movie, idx) in recommendMovies"
        :key="idx"
        :movie="movie"
      />
    </div>
    <div v-else class="row gap-3 justify-content-center">
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img @click="randomPick" src="../../assets/recommend/random.svg" alt="random">
        </div>
      </div>
      <div v-if="hasGenre" class="col-auto my-2" >
        <div class="card h-100">
          <img @click="genrePick" src="../../assets/recommend/genre.svg" alt="genre">
        </div>
      </div>
      <div v-if="hasFollow" class="col-auto my-2" >
        <div class="card h-100">
          <img @click="followPick" src="../../assets/recommend/follow.svg" alt="follow">
        </div>
      </div>
      <div class="col-auto my-2" >
        <div class="card h-100">
          <img @click="moodPick" src="../../assets/recommend/weather.svg" alt="weather">
        </div>
      </div>
      <div v-if="hasPickedMovie" class="col-auto my-2" >
        <div class="card h-100">
          <img @click="similarPick" src="../../assets/recommend/similar.svg" alt="similar">
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
    followPick: async function () {
      const response = await this.$store.dispatch('movie/getFollowingsMovies')
      if (response === 'DONE') {
        this.pickTheme = true
      }
    },
    moodPick: async function () {
      const response = await this.$store.dispatch('movie/getMoodMovies')
      if (response === 'DONE') {
        this.pickTheme = true
      }
    },
    similarPick: async function () {
      const response = await this.$store.dispatch('movie/getSimilarMovies')
      if (response === 'DONE') {
        this.pickTheme = true
      }
    },
    resetCard: function () {
      this.pickTheme = false
    }
  },
  computed: {
    ...mapState('movie', ['recommendMovies']),
    ...mapState('auth', ['myProfile']),
    hasGenre: function () {
      if (this.myProfile.genres.length) {
        return true
      }
      return false
    },
    hasFollow: function () {
      if (this.myProfile.followings.length) {
        return true
      }
      return false
    },
    hasPickedMovie: function () {
      if (this.myProfile.pick_movies.length) {
        return true
      }
      return false
    }

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
  .btn-outline-warning {
    color: #F47B0F;
    border: 2px solid #F47B0F;
  }
  .btn-outline-warning:hover {
    color: #fff;
    background-color: #441DB2;
    border: 2px solid #F47B0F;
  }
</style>