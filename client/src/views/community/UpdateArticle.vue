<template>
  <div class="article-form">
    <h1 class="chapter-title mb-4">Share your PICK</h1>
    <div class="d-flex gap-2 justify-content-end mb-4 me-1">
      <button class="btn btn-outline-warning" @click="updateArticle">Update</button>
      <button class="btn btn-outline-light" @click="backToCommunity">Back</button>
    </div>
    <div class="mb-3">
      <input
        class="form-control"
        type="text"
        v-model="updateInfo.title"
        required
      >
    </div>
    <div class="mb-3">
      <textarea 
        class="form-control content-input" 
        type="text" 
        v-model="updateInfo.content"
      ></textarea>
    </div>
    <p>테마에 맞는 영화를 PICK해주세요↓</p>
    <button class="btn btn-outline-dark mb-3 btn-add" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">PICK</button>
    <div class="row gap-3 justify-content-center">
      <PickedMovieItem
        v-for="(movie, idx) in selectedMovies"
        :key="idx"
        :movie="movie"
      />
    </div>
    <div class="movie-search offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
      <div class="offcanvas-header">
        <h5 id="offcanvasRightLabel">PICK your MOVIE</h5>
        <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <div class="container">
          <div class="form col-12 mb-3">
            <span><i class="col-2 far fa-hand-point-right fs-3"></i></span>
            <input 
              :value="data"
              @input="insertData"
              class="col-10 search-input"
              type="text" 
              placeholder="Search">
          </div>
          <div class="row gap-2 justify-content-center">
            <SearchResultItem
              v-for="(movie, idx) in searchResult"
              :key="idx"
              :movie="movie"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import SearchResultItem from '@/components/community/SearchResultItem'
import PickedMovieItem from '@/components/community/PickedMovieItem'

export default {
  name: 'UpdateArticle',
  components: {
    SearchResultItem,
    PickedMovieItem,
  },
  data: function () {
    return {
      data: '',
    }
  },
  methods: {
    ...mapActions('article', ['backToCommunity']),
    insertData: function (event) {
      this.data = event.target.value
      this.$store.dispatch('movie/searchData', this.data)
    },
    updateArticle: function () {
      this.updateInfo.movie = this.selectedMovieIds
      this.$store.dispatch('article/updateArticle', this.updateInfo)
    },
  },
  computed: {
    ...mapState('movie', ['searchResult']),
    ...mapState('article', ['selectedMovies', 'updateInfo']),
    ...mapState('auth', ['userToken']),
    ...mapGetters('article', ['selectedMovieIds'])
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
  .article-form {
    margin: 2rem 5rem;
  }
  .movie-search {
    background-color: rgba(58, 24, 151, 0.8)
  }
  .form-control {
    color: #fff;
    background: #1E1F26;
    box-shadow: none;
    border-radius: 0;
    border: none;
    border-bottom: 2px solid #F47B0F;
    padding: 0.5rem 1rem;
    font-size: 18px;
    letter-spacing: 1px;
    word-spacing: 2px;
    line-height: 25px;
    outline: none;
  }
  .content-input {
    padding: 1rem;
    font-size: 15px;
    height: 5rem;
    word-wrap: break-word;
  }
  .form {
    padding: 10px 2px;
    border: 0.25rem solid #F47B0F;
    background-color: #fff;
  }
  .form i {
    color: #F47B0F;
  }
  .search-input {
    border: none;
    color: #1E1F26;
    outline: none;
  }
  .btn-outline-warning {
    color: #F47B0F;
    border: 2px solid #F47B0F;
    background-color: #1E1F26;
    outline: none;
  }
  .btn-outline-warning:hover {
    color: #fff;
    background-color: #F47B0F;
    border: 2px solid #F47B0F;
  }
  .btn-outline-dark {
    height: 4rem;
    width: 4rem;
    color: #fff;
    border: 2px solid #441DB2;
    background-color: #1E1F26;
    outline: none;
  }
  .btn-outline-dark:hover {
    color: #fff;
    background-color: #441DB2;
    border: 2px solid #441DB2;
  }
  .btn-add {
    border-radius: 100%;
  }
</style>