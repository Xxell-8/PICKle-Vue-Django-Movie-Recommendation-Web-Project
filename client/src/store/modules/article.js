import api from '@/api'
import router from '@/router'

const state = {
  selectedMovies: [],
  articles: [],
  article: [],
}

const actions = {
  selectMovie({ state, commit }, movieInfo) {
    if (state.selectedMovies.length < 5) {
      commit('SET_SELECTED_MOVIE', movieInfo)
    } else {
      alert('영화는 5개까지만 추가할 수 있어요!')
    }
  },
  async createArticle({ commit, rootState }, articleInfo) {
    const userToken = rootState.auth.userToken
    const response = await api.createArticle(articleInfo, userToken)
    if (response.status === 201) {
      console.log(response)
      commit('RESET_SELECTED_MOVIE')
      router.push({ name: 'PickyPick' })
    }
  },
  async getArticles({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getArticles(userToken)
    if (response.status === 200) {
      console.log(response)
      commit('SET_ARTICLES', response.data)
    }
  },
  async getArticleDetail({ commit, rootState }, articleId) {
    const userToken = rootState.auth.userToken
    const response = await api.getArticleDetail(articleId, userToken)
    if (response.status === 200) {
      console.log(response)
      commit('SET_ARTICLE_DETAIL', response.data)
    }
  },
  async addComment({ state, rootState }, commentInput) {
    const userToken = rootState.auth.userToken
    const articleId = state.article.id
    const data = {content: commentInput}
    const response = await api.addComment(articleId, userToken, data)
    if (response.status === 201) {
      return 'DONE'
    }
  }
}

const mutations = {
  SET_ARTICLES(state, payload) {
    state.articles = payload
  },
  SET_ARTICLE_DETAIL(state, payload) {
    state.article = payload
  },
  SET_SELECTED_MOVIE(state, payload) {
    state.selectedMovies.push(payload)
  },
  RESET_SELECTED_MOVIE(state) {
    state.selectedMovies = []
  },
}

const getters = {
  selectedMoviePosters: function (state) {
    return state.selectedMovies.map((movie) => {
      return {poster: movie.poster_path}
    })
  },
  selectedMovieIds: function (state) {
    return state.selectedMovies.map((movie) => {
      return movie.id
    })
  },
}


export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
}