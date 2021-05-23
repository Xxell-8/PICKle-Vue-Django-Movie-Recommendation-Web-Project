import api from '@/api'
import router from '@/router'
import jwt_decode from "jwt-decode"

const state = {
  isLogin: false,
  userToken: null,
  register: null,
  picked: [],
  wishList: [],
  watching: [],
  dislike: [],
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
  },
  async pickMovie ({ state, commit }, moviePk) {
    const response = await api.pickMovie(moviePk, state.userToken)
    if (response.status === 200) {
      //console.log(response)
      commit('SET_PICK_LIST', moviePk)
    }
  },
  async wishMovie ({ state, commit }, moviePk) {
    const response = await api.wishMovie(moviePk, state.userToken)
    if (response.status === 200) {
      //console.log(response)
      commit('SET_WISH_LIST', moviePk)
    }
  },
  async watchMovie ({ state, commit }, moviePk) {
    const response = await api.watchMovie(moviePk, state.userToken)
    if (response.status === 200) {
      //console.log(response)
      commit('SET_WATCH_LIST', moviePk)
    }
  },
  async dislikeMovie ({ state, commit }, moviePk) {
    const response = await api.dislikeMovie(moviePk, state.userToken)
    if (response.status === 200) {
      //console.log(response)
      commit('SET_DISLIKE_LIST', moviePk)
    }
  },
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
  SET_PICK_LIST(state, moviePk) {
    state.picked.push(moviePk)
  },
  SET_WISH_LIST(state, moviePk) {
    state.wishList.push(moviePk)
  },
  SET_WATCH_LIST(state, moviePk) {
    state.watching.push(moviePk)
  },
  SET_DISLIKE_LIST(state, moviePk) {
    state.dislike.push(moviePk)
  }
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