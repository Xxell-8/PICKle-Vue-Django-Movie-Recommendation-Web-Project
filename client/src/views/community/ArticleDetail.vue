<template>
  <div class="mb-5">
    <div 
      class="backdrop"
      :style="{ backgroundImage: `linear-gradient(rgba(41, 42, 51, 0.2), rgba(41, 42, 51, 1)), url('https://image.tmdb.org/t/p/w780/${article.movie[0].backdrop_path}')`}"
    >
      <div class="d-flex flex-column text-start article-header">
        <h1 class="article-title">{{ article.title }}</h1>
        <p class="m-1 text-muted article-plus">
          <i class="fas fa-pizza-slice me-2"></i>
          <span>{{ article.user }}</span> , {{ article.created_at|moment }}</p>
        <p class="m-1 article-content">{{ article.content }}</p>
      </div>
      <span class="article-like">
        <i v-if="isLiked" @click="onClickLike" class="fas fa-heart fs-2 me-2"></i>
        <i v-else @click="onClickLike" class="far fa-heart fs-2 me-2"></i>
        <span class="article-cnt me-4">{{ article.like_count }}</span>
        <i class="far fa-comment-alt fs-2 me-2"></i>
        <span class="article-cnt">{{ article.comment_count }}</span>
      </span>
    </div>
    <div v-if="isMyArticle" class="user-btn d-flex gap-2 justify-content-end">
      <button class="btn btn-outline-warning" @click="getUpdateData(article.id)">Update</button>
      <button class="btn btn-outline-light" @click="deleteArticle(article.id)">Delete</button>
    </div>
    <div class="row gap-3 justify-content-center mt-5 mx-3">
      <MovieItem
        v-for="(movie, idx) in article.movie"
        :key="idx"
        :movie="movie"
      />
    </div>
    <div class="comment-box mt-5">
      <div class="comment-bar row">
        <div class="comment-form col-11 align-items-baseline">
          <span class="col-1"><i class="fas fa-quote-left"></i></span>
          <input 
            class="col-11"
            type="text" 
            placeholder="댓글" 
            @input="insertData" 
            :value="commentInput"
            @keyup.enter="onCommentInput"
          >
        </div>
        <button class="col-1 btn btn-light" @click="onCommentInput">Add</button>
      </div>
      <ul class="comment-list text-start mt-3 ps-0">
        <ArticleDetailComments
          class="my-2"
          v-for="(comment, idx) in article.comment_set"
          :key="idx"
          :comment="comment"
        />
      </ul>
    </div>
  </div>
</template>

<script>
import moment from 'moment'
import { mapActions, mapState, mapGetters } from 'vuex'
import MovieItem from '@/components/movies/MovieItem'
import ArticleDetailComments from '@/components/community/ArticleDetailComments'

export default {
  name: 'ArticleDetail',
  components: {
    MovieItem,
    ArticleDetailComments,
  },
  data: function () {
    return {
      commentInput: null,
    }
  },
  methods: {
    ...mapActions(
      'article', 
      [
        'getArticleDetail', 'addComment', 
        'likeArticle', 'deleteArticle', 'getUpdateData'
      ]
    ),
    onCommentInput: async function () {
      const response = await this.addComment(this.commentInput)
      if (response === 'DONE') {
        this.commentInput = ''
        this.getArticleDetail(this.$route.params.id)
      }
    },
    insertData: function (event) {
      this.commentInput = event.target.value
    },
    onClickLike: async function () {
      const response = await this.likeArticle(this.article.id)
      if (response === 'DONE') {
        this.getArticleDetail(this.$route.params.id)
      }
    },
    moveToUpdate: function () {
      this.$router.push({ name: 'UpdateArticle' })
    }
  },
  filters: {
    moment: function (date) {
      return moment(date).format('MMMM Do YYYY');
    }
  },
  computed: {
    ...mapState('article', ['article']),
    ...mapGetters('auth', ['decodeToken']),
    isLiked: function () {
      return this.article.liked_user.includes(this.decodeToken.user_id)
    },
    isMyArticle: function () {
      return this.article.user === this.decodeToken.username
    }
  },
  created: async function () {
    this.getArticleDetail(this.$route.params.id)
  },
}
</script>

<style scoped>
  .article-box {
    background-color: #1E1F26;
  }
  .backdrop {
    position: relative;
    height: 18rem;
    background-size: cover;
  }
  .article-like {
    position: absolute;
    top: 14rem;
    right: 5rem;
  }
  .article-cnt {
    font-weight: 500;
    font-size: 1.2rem;
  }
  .article-header {
    position: absolute;
    top: 12rem;
    left: 5rem;
  }
  .article-title {
    color: white;
    font-weight: 700;
    font-size: 2.5rem;
    margin-bottom: 2px;
  }
  .article-content {
    max-width: 50rem;
  }
  .article-plus {
    font-weight: 400;
    font-size: 0.9rem;
  }

  .comment-box{
    max-width: 720px;
    margin: auto;
    padding: 0 50px;
  }

  .comment-form{
    padding: 10px 2px;
    background-color: #1E1F26;
  }
  .comment-form input {
    padding:0;
    border-radius: 0;
    border: none;
    font-size: 15px;
    color: #bbb;
    background:none;
    letter-spacing: 1px;
    word-spacing: 2px;
    padding-left: 20px;
    line-height: 15px;
    outline: none;
  }
  .btn {
    border-radius: 0;
  }
  .comment-list {
    list-style: none;
  }
  .comment-user {
    font-weight: 500;
    min-width: 4rem;
  }
  .comment-content {
    font-weight: 300;
  }
  .user-btn {
    margin-right: 5rem;
  }
  .btn-outline-warning {
    color: #F47B0F;
    border: 2px solid #F47B0F;
    background-color: #1E1F26;
    outline: none;
  }
  .btn-outline-warning:hover {
    color: #fff;
    background-color: #F47B0F;
    border: 2px solid #F47B0F;
  }

</style>