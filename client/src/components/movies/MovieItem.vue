<template>
  <div class="col-auto my-2" >
    <MovieDetail :movie="movie"/>
    <div class="card h-100">
      <img
        :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" 
        :alt="movie.title"
      >
      <div class="content">
        <div class="inner-content">
          <p class="title">{{ movie.title }}</p>
          <hr>
          <p class="overview">{{ movie.overview|shorten }}</p>
          <button
            class="btn btn-primary btn-sm"
            data-bs-toggle="modal"
            :data-bs-target="'#detailModal-' + movie.id">Details</button>
          <ul v-if="isLogin" class="icons">
            <li :class="{orange : isPicked}"><i @click="pickMovie(movie.id)" class="fas fa-heartbeat fs-4"></i></li>
            <li :class="{orange : isWished}"><i @click="wishMovie(movie.id)" class="fas fa-star fs-4"></i></li>
            <li :class="{orange : isWatched}"><i @click="watchMovie(movie.id)" class="fas fa-eye fs-4"></i></li>
            <li :class="{orange : isDisliked}"><i @click="dislikeMovie(movie.id)" class="fas fa-times-circle fs-4"></i></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import MovieDetail from '@/components/movies/MovieDetail'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieItem',
  components: {
    MovieDetail,
  },
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions('auth', ['pickMovie', 'wishMovie', 'watchMovie', 'dislikeMovie'])
  },
  computed: {
    ...mapState('auth', ['isLogin', 'myProfile']),
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
  },
  filters: {
    shorten: function(rawText) {
      return _.truncate(rawText, {
        'length': 70,
      })
    }
  }
}
</script>

<style scoped>
  .card {
    background: linear-gradient(180deg, #441DB2 0%, #0d0425 100%);
    border: 0;
    border-radius: 0;
    width: 13rem;
    overflow: hidden;
    box-shadow: 15px 15px 25px black;
  }
  .card:before,
  .card:after,
  .card .content:before,
  .card .content:after {
    content: "";
    width: 50%;
    height: 4px;
    transform: scaleX(0);
    position: absolute;
    top: 15px;
    left: 15px;
    z-index: 1;
    transition: all 600ms ease;
  }
  .card:after{
      top: auto;
      bottom: 15px;
      left: auto;
      right: 15px;
  }
  .card .content:before,
  .card .content:after{
      width: 4px;
      height: 50%;
      transform: scaleY(0);
  }
  .card .content:after{
      left: auto;
      right: 15px;
      top: auto;
      bottom: 15px;
  }
  .card:hover:before,
  .card:hover:after,
  .card:hover .content:before,
  .card:hover .content:after{
      transform: scale(1);
  }

  .card img {
    width: 100%;
    height: auto;
    transform: scale3d(1.1, 1.1, 1);
    transition: all 0.25s linear;
  }

  .card:hover img {
    opacity: 0.15;
    transform: scale(1.25);
  }

  .card .inner-content {
    width: 80%;
    opacity: 0;
    transform: translateX(-50%) translateY(-50%);
    position: absolute;
    top: 70%;
    left: 50%;
    transition: all 600ms ease;
  }

  .card:hover .inner-content {
    opacity: 1;
    top: 50%
  }
  .title {
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 0;
  }
  .overview {
    font-weight: 200;
    font-size: 0.8rem;
  }
  .btn {
    border-radius: 0;
    margin-bottom: 1rem;
  }
  .btn-primary {
  color: #fff;
  background-color: #F47B0F;
  border: none;
  }
  .btn-primary:hover {
    color: #fff;
    background-color: #F47B0F;
    border: none;
  }
  .icons {
    padding: 0;
    margin: 0;
    list-style: none;
  }
  .icons li {
    display: inline-block;
    margin: 0 0.4rem;
  }

  .orange {
    color: #F47B0F;
  }
</style>