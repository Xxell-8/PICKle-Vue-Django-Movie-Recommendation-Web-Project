<template>
  <div class="col-auto my-2">
    <div class="card h-100">
      <div
        class="backdrop"
        :style="{ backgroundImage: `linear-gradient(rgba(30, 31, 38, 0.2), rgba(30, 31, 38, 1)), url('https://image.tmdb.org/t/p/w780/${article.movie[0].backdrop_path}')`}"
      >
      </div>
      <div class="article-info d-flex flex-column">
        <router-link
          class="article-title text-start"
          :to="{ name: 'ArticleDetail', params: {id: article.id} }"
        >{{ article.title }}</router-link>
        <p class="pub-date text-start">{{ article.created_at|moment }}</p>
      </div>
      <span class="like-icon">
        <i class="fas fa-heart me-1"></i>
        <span>{{ article.like_count }}</span>
      </span>
    </div>
    <div class="card-body">
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ArticleListItem',
  props: {
    article: {
      type: Object,
    }
  },
  filters: {
    moment: function (date) {
      return moment(date).fromNow()
    }
  }
}
</script>

<style scoped>
  .card {
    width: 12rem;
    border-radius: 0;
    color: white;
    box-shadow: 15px 15px 25px black;
    border: 0;
    background-color: #1E1F26;
    overflow: hidden;
    position: relative;
  }
  .card-body {
    height: 2rem;
    padding: 0.2rem 1rem 0.5rem;
  }
  .backdrop {
    position: relative;
    height: 10rem;
    background-size: cover;
  }
  .article-info {
    position: absolute;
    bottom: 15px;
    left: 15px;
  }
  .article-title {
    color: white;
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 2px;
  }
  .pub-date {
    margin: 0;
    font-weight: 300;
    font-size: 0.8rem;
  }
  .like-icon {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: rgba(244, 123, 15, 0.8);
    padding: 0 5px;
    border-radius: 0.25rem;
  }
</style>