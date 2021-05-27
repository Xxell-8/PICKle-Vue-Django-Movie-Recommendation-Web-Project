<template>
  <div class="modal fade" :id="'detailModal-' + movie.id" tabindex="-1" aria-labelledby="detailModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div 
          class="backdrop"
          :style="{ backgroundImage: `linear-gradient(rgba(30, 31, 38, 0.2), rgba(30, 31, 38, 1)), url('https://image.tmdb.org/t/p/w780/${movie.backdrop_path}')`}"
        >
          <div class="d-flex align-items-baseline gap-3 movie-header">
            <h1 class="movie-title">{{ movie.title }}</h1>
            <span
              v-for="(genre, idx) in movie.genres"
              :key="idx" 
              class="badge">{{ genre }}</span>
          </div>
        </div>
        <div class="modal-body d-flex flex-column gap-3">
          <div class="movie-rate d-flex align-items-baseline gap-3">
            <span :class="{orange : isPicked}"><i @click="onPick" class="clickable fas fa-heartbeat fs-3 me-2"></i>{{ pickCnt }}</span>
            <span :class="{orange : isWished}"><i @click="onWish" class="clickable fas fa-star fs-3 me-2"></i>{{ movie.wish_count }}</span>
            <span :class="{orange : isWatched}"><i @click="onWatch" class="clickable fas fa-eye fs-3 me-2"></i>{{ movie.watch_count }}</span>
            <span :class="{orange : isDisliked}"><i @click="onDislike" class="clickable fas fa-ban fs-3 me-2"></i>{{ movie.dislike_count }}</span>
          </div>
          <p>{{ movie.overview }}</p>
        </div>
        <hr class="mx-4">
        <div class="movie-provider mb-4 d-flex gap-4 justify-content-center">
          <img v-if="movie.netflix" src="../../assets/netflix-logo.svg" alt="netflix">
          <img v-if="movie.watcha" src="../../assets/watcha-logo.svg" alt="watcha">
          <img v-if="movie.wavve" src="../../assets/wavve-logo.svg" alt="wavve">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      pickCnt: '',
      wishCnt: '',
      watchCnt: '',
      dislikeCnt: '',
    }
  },
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions('auth', ['pickMovie', 'wishMovie', 'watchMovie', 'dislikeMovie']),
    onPick: async function () {
      const isPick = this.myProfile.pick_movies.some((pickedMovie) => {
        return pickedMovie.id === this.movie.id
      })
      const response = await this.pickMovie(this.movie.id)
      if (response === 'DONE') {
          if (isPick) {
            this.pickCnt -= 1
          } else {
            this.pickCnt += 1
          }
      }
    },
    onWish: async function () {
      const isWish = this.myProfile.wish_movies.some((wishedMovie) => {
        return wishedMovie.id === this.movie.id
      })
      const response = await this.wishMovie(this.movie.id)
      if (response === 'DONE') {
          if (isWish) {
            this.wishCnt -= 1
          } else {
            this.wishCnt += 1
          }
      }
    },
    onWatch: async function () {
      const isWatch = this.myProfile.watch_movies.some((watchedMovie) => {
        return watchedMovie.id === this.movie.id
      })
      const response = await this.watchMovie(this.movie.id)
      if (response === 'DONE') {
          if (isWatch) {
            this.watchCnt -= 1
          } else {
            this.watchCnt += 1
          }
      }
    },
    onDislike: async function () {
      const isDislike = this.myProfile.dislike_movies.some((dislikedMovie) => {
        return dislikedMovie.id === this.movie.id
      })
      const response = await this.dislikeMovie(this.movie.id)
      if (response === 'DONE') {
          if (isDislike) {
            this.dislikeCnt -= 1
          } else {
            this.dislikeCnt += 1
          }
      }
    },
  },
  computed: {
    ...mapState('auth', ['myProfile']),
    isPicked: function () {
      return this.myProfile.pick_movies.some((pickedMovie) => {
        return pickedMovie.id === this.movie.id
      })
    },
    isWished: function () {
      return this.myProfile.wish_movies.some((wishedMovie) => {
        return wishedMovie.id === this.movie.id
      })
    },
    isWatched: function () {
      return this.myProfile.watch_movies.some((watchedMovie) => {
        return watchedMovie.id === this.movie.id
      })
    },
    isDisliked: function () {
      return this.myProfile.dislike_movies.some((dislikedMovie) => {
        return dislikedMovie.id === this.movie.id
      })
    },
    pickCount: function () {
      return this.movie.pick_count
    },
    wishCount: function () {
      return this.movie.wish_count
    },
    watchCount: function () {
      return this.movie.watch_count
    },
    dislikeCount: function () {
      return this.movie.dislike_count
    },
  },
  filters: {
    moment: function (date) {
      return moment(date).format('YYYY. MM. DD.');
    }
  },
  mounted: function () {
    this.pickCnt = this.pickCount
    this.wishCnt = this.wishCount
    this.watchCnt = this.watchCount
    this.dislikeCnt = this.dislikeCount
  }
}
</script>

<style scoped>
  .modal-content {
    border-radius: 0;
    background-color: #1E1F26;
    background-clip: border-box;
    border: 0.2rem solid #F47B0F;
    border-radius: 0;
    border-top: none;
    outline: 0;
  }

  .modal-header {
  border-radius: 0;
  border: none;
  background-color: #F47B0F;
  height: 1rem;
  }

  .modal-body {
    text-align: start;
    padding: 0 2rem;
    font-weight: 300;
  }

  .backdrop {
    position: relative;
    height: 250px;
    background-size: cover;
  }

  .movie-header {
    position: absolute;
    bottom: 10px;
    left: 20px;
  }
  .movie-title {
    font-weight: 700;
    font-size: 2rem;
  }

  .badge {
    border-radius: 0;
    background-color: #441DB2;
  }

  .movie-provider img {
    height: 2rem;
  }

  .orange {
    color: #F47B0F;
  }

  .clickable {
    cursor: pointer;
  }
</style>