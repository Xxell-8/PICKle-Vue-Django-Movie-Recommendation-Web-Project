import api from '@/api'
// import router from '@/router'

const state = {
  movies: [],
  bestMovies: [],
  genreOptions: [],
  searchResult: null,
  recommendOptions: ['random', 'genre', 'similar', 'series', 'classic'],
  recommendMovies: null,
  picked: false,
  movieDetail: [],
}

const actions = {
  async getMovies({ commit }) {
    const response = await api.getMovies()
    if (response.status === 200) {
      console.log(response)
      commit('SET_MOVIES', response.data)
    }
  },
  async getBestMovies({ commit }) {
    const response = await api.getBestMovies()
    if (response.status === 200) {
      console.log(response)
      commit('SET_BEST_MOVIES', response.data)
    }
  },
  async getGenreList({ commit }) {
    const response = await api.getGenreList()
    if (response.status === 200) {
      commit('SET_GENRE_OPTIONS', response.data)
    }
  },
  async searchData ({ commit }, inputText) {
    if (inputText.length >= 2) {
      const response = await api.searchData(inputText)
      if (response.status === 200) {
        console.log(response)
        commit('SET_SEARCH_RESULTS', response.data)
      }
    }
  },
  async getDetails ({ commit }, movieId) {
    const response = await api.getMovieDetails(movieId)
    if (response.status === 200) {
      commit('SET_DETAIL', response.data)
    }
  },
  async getRandomMovies({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getRandomMovies(userToken)
    if (response.status === 200) {
      commit('SET_RECOMMEND_MOVIES', response.data)
      return 'DONE'
    }
  },
  async getGenreMovies({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getGenreMovies(userToken)
    if (response.status === 200) {
      commit('SET_RECOMMEND_MOVIES', response.data)
      return 'DONE'
    }
  },
  async getFollowingsMovies({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getFollowingsMovies(userToken)
    if (response.status === 200) {
      commit('SET_RECOMMEND_MOVIES', response.data)
      return 'DONE'
    }
  },
  async getSimilarMovies({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getSimilarMovies(userToken)
    if (response.status === 200) {
      commit('SET_RECOMMEND_MOVIES', response.data)
      return 'DONE'
    }
  },
  async getMoodMovies({ commit, rootState }) {
    const userToken = rootState.auth.userToken
    const response = await api.getMoodMovies(userToken)
    if (response.status === 200) {
      commit('SET_RECOMMEND_MOVIES', response.data)
      return 'DONE'
    }
  },
}

const mutations = {
  SET_MOVIES(state, payload) {
    state.movies = payload
  },
  SET_DETAIL(state, payload) {
    state.movieDetail = payload
  },
  SET_BEST_MOVIES(state, payload) {
    state.bestMovies = payload
  },
  SET_GENRE_OPTIONS(state, payload) {
    state.genreOptions = payload
  },
  SET_SEARCH_RESULTS(state, payload) {
    state.searchResult = payload
  },
  RESET_SEARCH_RESULTS(state) {
    state.searchResult = []
  },
  SET_RECOMMEND_MOVIES(state, payload) {
    state.recommendMovies = payload
  }
}

const getters = {
  
}


export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
}