<template>
  <div>
    <h1>큐레이션 페이지</h1>
    <button @click="moveToCreate">Create</button>
    <ArticleList/>
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

<style>

</style>