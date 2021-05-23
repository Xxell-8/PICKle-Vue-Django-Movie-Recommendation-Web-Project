<template>
  <div class="article-form">
    <div class="mb-3">
      <input class="form-control" type="text" placeholder="Title" v-model="articleInfo.title" required>
    </div>
    <div class="mb-3">
      <input class="form-control" type="text" placeholder="Content" v-model="articleInfo.content">
    </div>
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Toggle right offcanvas</button>
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
      <div class="offcanvas-header">
        <h5 id="offcanvasRightLabel">Offcanvas right</h5>
        <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        ...
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreateArticle',
  data: function () {
    return {
      articleInfo: {
        title: null,
        content: null,
        movies: []
      }
    }
  },
  methods: {

  }
}
</script>

<style>
  .article-form {
    margin: 2rem 5rem;
  }
</style>