<template>
  <div class="row gap-3 justify-content-center">
    <ArticleListItem
      v-for="(article, idx) in articles"
      :key="idx"
      :article="article"
    />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ArticleListItem from '@/components/community/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  methods: {
    ...mapActions('article', ['getArticles'])
  },
  computed: {
    ...mapState('article', ['articles'])
  },
  created: function () {
    this.getArticles()
  }
}
</script>

<style>

</style>