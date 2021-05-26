<template>
  <div>
    <div class="profile-header d-flex align-items-center">
      <div class="col-2">
        <img class="logo" src="../../assets/logo.svg" alt="">
      </div>
      <div class="col-10 d-flex flex-column align-items-start ps-3">
        <div class="d-flex align-items-center gap-3">
          <h1 class="profile-username">{{ userProfile.username }}</h1>
          <span
            v-for="(genre) in userProfile.genres"
            :key="genre.id" 
            class="badge">{{ genre }}</span>
        </div>
        <div class="d-flex gap-3">
          <p class="ms-2">{{ userProfile.followers_count }} followers • {{ userProfile.followings_count }} followings</p>
          <div v-if="isOthers">
            <button 
              v-if="isFollowed" 
              @click="follow(userInfo)"
              class="btn btn-unfollow"
            >UnFollow</button>
            <button 
              v-else 
              @click="follow(userInfo)"
              class="btn btn-follow"
            >Follow</button>
          </div>
        </div>
        <p v-if="userProfile.introduce">{{ userProfile.introduce }}</p>
        <div class="movie-rate d-flex align-items-baseline gap-3 ms-2">
          <span><i class="fas fa-heartbeat fs-3 me-2 orange"></i>{{ userProfile.pick_count }}</span>
          <span><i class="fas fa-star fs-3 me-2 orange"></i>{{ userProfile.wish_count }}</span>
          <span><i class="fas fa-eye fs-3 me-2 orange"></i>{{ userProfile.watch_count }}</span>
        </div>
      </div>
    </div>
    <div class="profile-body container my-5">
      <div class="profile-tab">
        <button @click="showPick" :class="[onPick ? 'btn-current': '', 'btn', 'btn-tab']">PICK</button>
        <button @click="showWish" :class="[onWish ? 'btn-current': '', 'btn', 'btn-tab', 'btn-center']">WISH</button>
        <button @click="showArticle" :class="[onArticle ? 'btn-current': '', 'btn', 'btn-tab']">Article</button>
      </div>
      <div v-if="onPick" class="row gap-3 justify-content-center my-5">
        <ProfileMovieItem
          v-for="(movie) in userProfile.pick_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <div v-if="onWish" class="row gap-3 justify-content-center my-5">
        <ProfileMovieItem
          v-for="(movie) in userProfile.wish_movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <div v-if="onArticle" class="row gap-3 justify-content-center my-5">
        <ProfileArticleItem
          v-for="(article) in userProfile.article_set"
          :key="article.id"
          :article="article"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import ProfileMovieItem from '@/components/auth/ProfileMovieItem'
import ProfileArticleItem from '@/components/auth/ProfileArticleItem'

export default {
  name: 'UserProfile',
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
    ...mapActions('auth', ['follow']),
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
    ...mapState('auth', ['userProfile']),
    ...mapGetters('auth', ['decodeToken']),
    userInfo: function () {
      return {'id': this.userProfile.id, 'username': this.userProfile.username }
    },
    isOthers: function () {
      return this.userProfile.id != this.decodeToken.user_id
    },
    isFollowed: function () {
      return this.userProfile.followers.includes(this.decodeToken.user_id)
    }
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
  .btn-tab {
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
  .btn-follow {
    height: 1.5rem;
    background-color: #F47B0F;
    color: white;
    padding: 0.05rem 0.5rem;
    font-size: 0.875rem;
    border-radius: 0.2rem;
    box-shadow: none;
  }
  .btn-unfollow {
    height: 1.5rem;
    border: 1px solid #F47B0F;
    background-color: none;
    color: #F47B0F;
    padding: 0.05rem 0.5rem;
    font-size: 0.875rem;
    border-radius: 0.2rem;
    box-shadow: none;
  }
</style>