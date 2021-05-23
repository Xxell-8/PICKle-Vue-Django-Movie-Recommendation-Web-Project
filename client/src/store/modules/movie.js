import api from '@/api'
// import router from '@/router'

const state = {
  movies: [],
  bestMovies: [],
  genreOptions: [],
  searchResult: null,
  recommendOptions: ['random', 'genre', 'similar', 'series', 'classic'],
  picked: false
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
    if (inputText.length >= 1) {
      const response = await api.searchData(inputText)
      if (response.status === 200) {
        console.log(response)
        commit('SET_SEARCH_RESULTS', response.data)
      }
    } else {
      commit('RESET_SEARCH_RESULTS')
    }
  },
}

const mutations = {
  SET_MOVIES(state, payload) {
    state.movies = payload
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