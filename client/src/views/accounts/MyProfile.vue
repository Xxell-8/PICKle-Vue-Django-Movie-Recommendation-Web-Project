<template>
  <div class="mt-5">
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
          <button class="badge edit-btn" type="button" data-bs-toggle="modal" data-bs-target="#updateModal">edit</button>
        </div>

        <!-- Modal -->
        <div class="modal fade" id="updateModal" tabindex="-1" aria-labelledby="updateModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="m-3">
                  <h2 class="modal-title mb-3">회원 정보 수정</h2>
                  <p>좋아하는 장르를 선택해주세요.</p>
                  <multiselect 
                    v-model="tags"
                    label="name"
                    track-by="id" 
                    :options="genreOptions" 
                    :multiple="true" 
                    :max="3"
                    @select="addGenre"
                    @remove="removeGenre"></multiselect>
                </div>
                <div>
                  <p>소개 글을 작성해주세요.</p>
                  <textarea 
                    class="form-control content-input" 
                    type="text"
                    placeholder="다른 사용자를 위해 소개 글을 적어보세요"
                    v-model="userInfo.introduce"></textarea>
                </div>
                <div class="d-flex justify-content-center">
                  <button @click="updateInfo(userInfo)" data-bs-dismiss="modal" class="btn btn-modal mt-3">SUBMIT</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <button @click="follow()">Follow</button> -->
        <p class="ms-2">{{ myProfile.followers_count }} followers • {{ myProfile.followings_count }} followings</p>
        <p v-if="myProfile.introduce" class="ms-2 profile-intro">{{ myProfile.introduce }}</p>
        <div class="movie-rate d-flex align-items-baseline gap-3 ms-2 mt-3">
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
import { mapState, mapActions } from 'vuex'
import Multiselect from 'vue-multiselect'
import ProfileMovieItem from '@/components/auth/ProfileMovieItem'
import ProfileArticleItem from '@/components/auth/ProfileArticleItem'

export default {
  name: 'MyProfile',
  components: {
    Multiselect,
    ProfileMovieItem,
    ProfileArticleItem,
  },
  data: function () {
    return {
      onPick: true,
      onWish: false,
      onArticle: false,
      userInfo: {
        genres: [],
        introduce: '',
      },
      tags: [],
    }
  },
  methods: {
    ...mapActions('auth', ['updateInfo']),
    ...mapActions('movie', ['getGenreList']),
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
    addGenre(event) {
      //console.log(event)
      this.userInfo.genres.push(event.id)
    },
    removeGenre(event) {
      //console.log(event)
      const index = this.userInfo.genres.indexOf(event.id)
      this.userInfo.genres.splice(index, 1)
    },
  },
  computed: {
    ...mapState('auth', ['myProfile']),
    ...mapState('movie', ['genreOptions'])
  },
  created: function () {
    this.getGenreList()
    this.userInfo.introduce = this.myProfile.introduce
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
  .profile-header {
    background-color: #EFEFEF;
    min-height: 13rem;
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
  .profile-header p {
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
  }
  .profile-intro {
    font-size: 0.9rem;
  }
  .badge {
    border-radius: 0.5rem;
    background-color: rgba(68, 29, 178, 0.7);
    font-weight: 400;
  }
  .edit-btn {
    background-color: #EFEFEF;
    border: 0.1rem solid rgba(68, 29, 178, 0.7);
    color: rgba(68, 29, 178, 0.7);
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
  .btn-modal {
    border: 2px solid #441DB2;
    width: auto;
  }
  .btn-modal:hover {
    background-color: #441DB2;
    color: #EFEFEF;
  }
  .modal-content {
    border-radius: 0;
    background-color: #EFEFEF;
    background-clip: border-box;
    border: 0.2rem solid #441DB2;
    border-radius: 0;
    border-top: none;
    outline: 0;
  }
  .modal-header {
  border-radius: 0;
  border: none;
  background-color: #441DB2;
  height: 1rem;
  }

  .modal-body {
    text-align: start;
    padding: 0 2rem;
    font-weight: 300;
    margin: 2rem;
  }
  .modal-title {
    font-weight: 700;
    text-align: center;
    color: #1E1F26;
  }
  textarea {
    border-radius: 0;
    box-shadow: none;
    outline: none;
  }
</style>