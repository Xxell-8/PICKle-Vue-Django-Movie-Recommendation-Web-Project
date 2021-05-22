<template>
  <div class="modal fade" :id="'detailModal-' + movie.id" tabindex="-1" aria-labelledby="detailModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="d-flex align-items-baseline gap-3">
            <h2>{{ movie.title }}</h2>
            <span><i class="fas fa-heartbeat fs-3"></i></span>
            <span><i class="fas fa-star-and-crescent fs-3"></i></span>
            <span><i class="fas fa-eye fs-3"></i></span>
            <span><i class="fas fa-times-circle fs-3"></i></span>
          </div>
          <hr>
          <div>
            <p>{{ movie.release_date }} 개봉</p>
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: {
      type: Object,
    }
  },
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
</style>