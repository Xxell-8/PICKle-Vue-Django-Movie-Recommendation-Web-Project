import api from '@/api'
import router from '@/router'
import jwt_decode from "jwt-decode"

const state = {
  isLogin: false,
  userToken: null,
  register: null,
}

const actions = {
  async login({ commit }, userData) {
    const response = await api.login(userData)
    if (response.status === 200) {
      commit('SET_ISLOGIN', true)
      commit('SET_TOKEN', response.data.token)
      router.push({ name: 'Home' })
    }
  },
  logout({ commit }) {
    commit('SET_ISLOGIN', false)
    commit('SET_TOKEN', null)
    router.push({ name: 'Login' })
  },
  async signup({ commit }, userData) {
    const response = await api.signup(userData)
    if (response.status === 201) {
      commit('SET_REGISTER', true)
      router.push({ name: 'Login'})
    }
  }
}

const mutations = {
  SET_ISLOGIN(state, payload) {
    state.isLogin = payload
  }, 
  SET_TOKEN(state, payload) {
    state.userToken = payload
  },
  SET_REGISTER(state, payload) {
    state.register = payload
  },
}

const getters = {
  decodeToken: function (state) {
    return jwt_decode(state.userToken)
  }
}


export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
}