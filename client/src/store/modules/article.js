import api from '@/api'
import router from '@/router'

const state = {
  selectedMovies: [],
  articles: [],
  article: [],
  updateInfo: [],
  updateMovies: [],
}

const actions = {
  selectMovie({ state, commit }, movieInfo) {
    if (state.selectedMovies.length < 5) {
      commit('SET_SELECTED_MOVIE', movieInfo)
    } else {
      alert('영화는 5개까지만 추가할 수 있어요!')
    }
  },
  unselectMovie({ commit }, movieInfo) {
    // console.log(movieInfo)
    commit('DELETE_SELECTED_MOVIE', movieInfo.id)
  },
  backToCommunity({ commit }) {
    commit('RESET_SELECTED_MOVIE')
    router.push({ name: 'PickyPick' })
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
  async deleteArticle({ rootState }, articleId) {
    const userToken = rootState.auth.userToken
    const response = await api.deleteArticle(articleId, userToken)
    if (response.status === 204) {
      router.push({ name: 'PickyPick' })
    }
  },
  async updateArticle({ rootState }, articleInfo) {
    const userToken = rootState.auth.userToken
    const articleId = articleInfo.id
    const response = await api.updateArticle(articleId, userToken, articleInfo)
    if (response.status === 200) {
      router.push({ name: 'ArticleDetail', params: { id: articleId } })
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
  async getUpdateData({ commit, rootState }, articleId) {
    const userToken = rootState.auth.userToken
    const response = await api.getArticleDetail(articleId, userToken)
    if (response.status === 200) {
      // console.log(response)
      commit('SET_UPDATE_INFO', response.data)
      commit('SET_UPDATE_MOVIE', response.data.movie)
      router.push({ name: 'UpdateArticle' })
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
  },
  async deleteComment({ rootState }, commentPk) {
    const userToken = rootState.auth.userToken
    const response = await api.deleteComment(userToken, commentPk)
    if (response.status === 204) {
      return 'DONE'
    }
  },
  async likeArticle({ rootState }, articleId) {
    const userToken = rootState.auth.userToken
    const response = await api.likeArticle(articleId, userToken)
    if (response.status === 200) {
      return 'DONE'
    }
  },
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
  SET_UPDATE_MOVIE(state, payload) {
    state.selectedMovies = payload
  },
  DELETE_SELECTED_MOVIE(state, payload) {
    state.selectedMovies = state.selectedMovies.filter((movie) => {
      return !(movie.id === payload)
    })
  },
  RESET_SELECTED_MOVIE(state) {
    state.selectedMovies = []
  },
  SET_UPDATE_INFO(state, payload) {
    state.updateInfo = payload
  }
}

const getters = {
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