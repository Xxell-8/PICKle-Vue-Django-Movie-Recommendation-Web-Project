<template>
  <div>
    <h1 class="chapter-title">PICKy Pick</h1>
    <button class="btn btn-outline-warning my-3" @click="moveToCreate">Create</button>
    <div class="mx-5">
      <ArticleList/>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList'

export default {
  name: 'PickyPick',
  components: {
    ArticleList,
  },
  methods: {
    moveToCreate: function () {
      this.$router.push({ name: 'CreateArticle' })
    }
  }
}
</script>

<style scoped>
  .chapter-title {
      font-weight: 900;
      font-size: 3rem;
      color: #fff;
      text-shadow: -3px -1px #F47B0F, 4px 1px #441DB2;
    }
  .btn-outline-warning {
    color: #F47B0F;
    border: 2px solid #F47B0F;
  }
  .btn-outline-warning:hover {
    color: #fff;
    background-color: #441DB2;
    border: 2px solid #F47B0F;
  }
</style>