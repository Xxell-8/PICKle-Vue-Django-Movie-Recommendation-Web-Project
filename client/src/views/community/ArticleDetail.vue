<template>
  <div class="container">
    <h1 class="movie-title">{{ article.title }}</h1>
    <div class="d-flex flex-column gap-3">
      <p class="mb-0">{{ article.user }}</p>
      <p class="mb-0">작성일 | {{ article.created_at|moment }}</p>
      <p>{{ article.content }}</p>
    </div>
    <div class="row gap-3 justify-content-center">
      <MovieItem
        v-for="(movie, idx) in article.movie"
        :key="idx"
        :movie="movie"
      />
    </div>
    <div class="comment-form">
      <input type="text" placeholder="댓글" @input="insertData" :value="commentInput">
      <button @click="onCommentInput">ADD</button>
    </div>
    <ul class="comment-list">
      <li
        v-for="(comment, idx) in article.comment_set"
        :key="idx"
      >
        <span>{{ comment.user }}</span> | 
        <span>{{ comment.content }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import moment from 'moment'
import { mapActions, mapState } from 'vuex'
import MovieItem from '@/components/movies/MovieItem'

export default {
  name: 'ArticleDetail',
  components: {
    MovieItem,
  },
  data: function () {
    return {
      commentInput: null,
    }
  },
  methods: {
    ...mapActions('article', ['getArticleDetail', 'addComment']),
    onCommentInput: async function () {
      const response = await this.addComment(this.commentInput)
      if (response === 'DONE') {
        this.commentInput = ''
        this.getArticleDetail(this.$route.params.id)
      }
    },
    insertData: function (event) {
      this.commentInput = event.target.value
    }
  },
  filters: {
    moment: function (date) {
      return moment(date).format('YYYY년 MM월 DD일');
    }
  },
  computed: {
    ...mapState('article', ['article'])
  },
  created: async function () {
    this.getArticleDetail(this.$route.params.id)
  },
}
</script>

<style>

</style>