<template>
    <div class="col-auto my-2" >
      <div class="card h-100">
        <img
          :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" 
          :alt="movie.title"
        >
        <div class="content">
          <div class="inner-content">
            <button
              class="btn btn-primary btn-sm"
              @click="unselectMovie(movie)"
            >DELETE</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {
    ...mapActions('article', ['unselectMovie'])
  },
}
</script>

<style scoped>
  .card {
    background: linear-gradient(180deg, #441DB2 0%, #0d0425 100%);
    border: 0;
    border-radius: 0;
    width: 8rem;
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
  .btn {
    border-radius: 0;
  }
  .btn-primary {
    color: #fff;
    background-color: #F47B0F;
    border: none;
    outline: none;
  }
  .btn-primary:hover {
    color: #fff;
    background-color: #F47B0F;
    border: none;
  }
</style>