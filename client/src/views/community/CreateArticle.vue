<template>
  <div class="article-form">
    <div class="mb-3">
      <input class="form-control" type="text" placeholder="Title" v-model="articleInfo.title" required>
    </div>
    <div class="mb-3">
      <input class="form-control" type="text" placeholder="Content" v-model="articleInfo.content">
    </div>
    <button class="btn btn-primary add-btn" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">+</button>
    <div class="row gap-3 justify-content-center">
      <PickedMovieItem
        v-for="(movie, idx) in selectedMoviePosters"
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
          <div class="form col-12">
            <span><i class="col-2 far fa-hand-point-right fs-3"></i></span>
            <input 
              :value="data"
              @input="insertData"
              class="col-10"
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
    <button @click="newArticle">만들기</button>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import SearchResultItem from '@/components/community/SearchResultItem'
import PickedMovieItem from '@/components/community/PickedMovieItem'

export default {
  name: 'CreateArticle',
  components: {
    SearchResultItem,
    PickedMovieItem,
  },
  data: function () {
    return {
      articleInfo: {
        title: null,
        content: null,
        movie: [],
      },
      data: '',
    }
  },
  methods: {
    insertData: function (event) {
      this.data = event.target.value
      this.$store.dispatch('movie/searchData', this.data)
    },
    newArticle: function () {
      this.articleInfo.movie = this.selectedMovieIds
      this.$store.dispatch('article/createArticle', this.articleInfo)
    }

  },
  computed: {
    ...mapState('movie', ['searchResult']),
    ...mapState('article', ['selectedMovies']),
    ...mapState('auth', ['userToken']),
    ...mapGetters('article', ['selectedMoviePosters', 'selectedMovieIds'])
  }
}
</script>

<style scoped>
  .article-form {
    margin: 2rem 5rem;
  }
  .movie-search {
    background-color: rgba(58, 24, 151, 0.8)
  }
  input{
    padding:0;
    border-radius: 0;
    border: none;
    font-size: 18px;
    color: #1E1F26;
    /* background:none; */
    letter-spacing: 1px;
    word-spacing: 10px;
    padding: 0;
    line-height: 25px;
    outline: none;
  }
  .add-btn {
    border-radius: 100%;
    width: 3rem;
    height: 3rem;
  }
  .form {
    padding: 10px 2px;
    border: 0.25rem solid #F47B0F;
    background-color: #fff;
  }

  .form i {
    color: #F47B0F;
  }
</style>