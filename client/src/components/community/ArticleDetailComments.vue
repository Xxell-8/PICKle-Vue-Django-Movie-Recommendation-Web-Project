<template>
  <li>
    <span class="d-flex gap-2 align-items-baseline">
      <i class="fas fa-pizza-slice"></i>
      <span class="comment-user">{{ comment.user }}</span>
      <span class="comment-content mx-3">{{ comment.content }}</span>
      <i v-if="myComment" @click="onDeleteComment" class="fas fa-times"></i>
    </span>
  </li>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleDetailComments',
  props: {
    comment: {
      type: Object,
    }
  },
  methods: {
    ...mapActions('article', ['getArticleDetail', 'deleteComment']),
    onDeleteComment: async function () {
      // console.log(commentPk)
      const response = await this.deleteComment(this.comment.id)
      if (response === 'DONE') {
        this.getArticleDetail(this.$route.params.id)
      }
    },
  },
  computed: {
    ...mapGetters('auth', ['decodeToken']),
    myComment: function () {
      return this.comment.user === this.decodeToken.username
    }
  }
}
</script>

<style>

</style>