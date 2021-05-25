<template>
    <div class="col-auto my-2" >
      <div class="card h-100">
        <img
          :src="'https://image.tmdb.org/t/p/w500/' + movie.poster" 
          :alt="movie.title"
        >
      </div>
    </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object,
    }
  },
}
</script>

<style scoped>
  .card {
    border: 0;
    border-radius: 0;
    width: 8rem;
    overflow: hidden;
    box-shadow: 15px 15px 25px black; 
  }
  .card img {
    height: 100%;
    width: auto;
  }
</style>