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
            <span><i class="fas fa-heartbeat fs-3 me-2"></i>{{ movie.pick_count }}</span>
            <span><i class="fas fa-star-and-crescent fs-3 me-2"></i>{{ movie.wish_count }}</span>
            <span><i class="fas fa-eye fs-3 me-2"></i>{{ movie.watch_count }}</span>
            <span><i class="fas fa-times-circle fs-3 me-2"></i>{{ movie.dislike_count }}</span>
          </div>
          <p class="mb-0">감독 | {{ movie.director }}</p>
          <p class="mb-0">개봉일 | {{ movie.release_date | moment }}</p>
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

export default {
  name: 'MovieDetail',
  props: {
    movie: {
      type: Object,
    }
  },
  filters: {
    moment: function (date) {
      return moment(date).format('YYYY년 MM월 DD일');
    }
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

</style>