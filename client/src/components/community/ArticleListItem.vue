<template>
  <div class="col-auto my-2">
    <div class="card" style="width: 18rem;">
      <img :src="'https://image.tmdb.org/t/p/w780/' + article.movie[0].backdrop_path" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ article.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">{{ article.user }}</h6>
        <router-link 
          :to="{ name: 'ArticleDetail', params: {id: article.id} }"
        >Details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: {
      type: Object,
    }
  },
}
</script>

<style scoped>
  .card {
    color: black;
  }
</style>