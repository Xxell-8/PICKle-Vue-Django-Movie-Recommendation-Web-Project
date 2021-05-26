<template>
  <div>
    <div class="profile-header d-flex align-items-center">
      <div class="col-2">
        <img class="logo" src="../../assets/logo.svg" alt="">
      </div>
      <div class="col-10 d-flex flex-column align-items-start ps-3">
        <div class="d-flex align-items-center gap-3">
          <h1 class="profile-username">{{ myProfile.username }}</h1>
          <span
            v-for="(genre) in myProfile.genres"
            :key="genre.id" 
            class="badge">{{ genre }}</span>
        </div>
        <!-- <button @click="follow()">Follow</button> -->
        <p class="ms-2">{{ myProfile.followers_count }} followers • {{ myProfile.followings_count }} followings</p>
        <p v-if="myProfile.introduce">{{ myProfile.introduce }}</p>
        <div class="movie-rate d-flex align-items-baseline gap-3 ms-2">
          <span><i class="fas fa-heartbeat fs-3 me-2 orange"></i>{{ myProfile.pick_count }}</span>
          <span><i class="fas fa-star fs-3 me-2 orange"></i>{{ myProfile.wish_count }}</span>
          <span><i class="fas fa-eye fs-3 me-2 orange"></i>{{ myProfile.watch_count }}</span>
        </div>
      </div>
    </div>
    <div class="profile-body container my-5">
      <div class="profile-tab">
        <button @click="showPick" :class="[onPick ? 'btn-current': '', 'btn']">PICK</button>
        <button @click="showWish" :class="[onWish ? 'btn-current': '', 'btn', 'btn-center']">WISH</button>
        <button @click="showArticle" :class="[onArticle ? 'btn-current': '', 'btn']">Article</button>
      </div>
      <div v-if="onPick" class="row gap-3 justify-content-center my-5">
        <ProfileMovieItem
          v-for="(movie) in myProfile.pick_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <div v-if="onWish" class="row gap-3 justify-content-center my-5">
        <ProfileMovieItem
          v-for="(movie) in myProfile.wish_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <div v-if="onArticle" class="row gap-3 justify-content-center my-5">
        <ProfileArticleItem
          v-for="(article) in myProfile.article_set"
          :key="article.id"
          :article="article"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ProfileMovieItem from '@/components/auth/ProfileMovieItem'
import ProfileArticleItem from '@/components/auth/ProfileArticleItem'

export default {
  name: 'MyProfile',
  components: {
    ProfileMovieItem,
    ProfileArticleItem,
  },
  data: function () {
    return {
      onPick: true,
      onWish: false,
      onArticle: false,
    }
  },
  methods: {
    showPick: function () {
      this.onPick = true
      this.onWish = false
      this.onArticle = false
    },
    showWish: function () {
      this.onPick = false
      this.onWish = true
      this.onArticle = false
    },
    showArticle: function () {
      this.onPick = false
      this.onWish = false
      this.onArticle = true
    },

  },
  computed: {
    ...mapState('auth', ['myProfile'])
  },
}
</script>

<style scoped>
  .profile-header {
    background-color: #EFEFEF;
    height: 13rem;
    color: #1E1F26;
    padding: 0 5rem;
  }
  .logo {
    width: 100%;
    height: auto;
    max-width: 10rem;
  }
  .profile-username {
    font-weight: 900;
    font-size: 3rem;
  }
  .badge {
    border-radius: 0.5rem;
    background-color: rgba(68, 29, 178, 0.7);
    font-weight: 400;
  }
  .orange {
    color: #441DB2;
  }
  .btn {
    width: 5rem;
    border-radius: 0;
    border: 0;
    background-color: #EFEFEF;
    color: #441DB2;
    font-weight: 700;
    box-shadow: none;
  }
  .btn-center {
    border-left: 2px solid #441DB2;
    border-right: 2px solid #441DB2;
  }
  .btn-current {
    background-color: #441DB2;
    color: #EFEFEF;
  }
</style>