import api from '@/api'
// import router from '@/router'

const state = {
  movies: []
}

const actions = {
  async getMovies({ commit }) {
    const response = await api.getMovies()
    if (response.status === 200) {
      console.log(response)
      commit('SET_MOVIES', response.data)
    }
  }
}

const mutations = {
  SET_MOVIES(state, payload) {
    state.movies = payload
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