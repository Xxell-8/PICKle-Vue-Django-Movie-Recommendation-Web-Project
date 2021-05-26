import api from '@/api'
import router from '@/router'
import jwt_decode from "jwt-decode"

const state = {
  isLogin: false,
  userToken: null,
  register: null,
  myProfile: null,
  userProfile: null,
}

const actions = {
  async login({ commit, dispatch }, userData) {
    const response = await api.login(userData)
    if (response.status === 200) {
      commit('SET_ISLOGIN', true)
      commit('SET_TOKEN', response.data.token)
      dispatch('getMyProfile')
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
  async follow({ state, dispatch }, userInfo) {
    const userId = userInfo.id
    const username = userInfo.username
    const response = await api.follow(userId, state.userToken)
    if (response.status === 200) {
      dispatch('getMyProfile')
      dispatch('resetProfile', username)
    }
  },
  async getMyProfile({ commit, getters }) {
    const response = await api.getUserInfo(getters.decodeToken.username)
    if (response.status === 200) {
      commit('SET_MY_PROFILE', response.data)
    }
  },
  async getUserProfile({ commit }, username) {
    const response = await api.getUserInfo(username)
    if (response.status === 200) {
      commit('SET_USER_PROFILE', response.data)
      router.push({ name: 'UserProfile', params: { username: username }})
    }
  },
  async resetProfile({ commit }, username) {
    const response = await api.getUserInfo(username)
    if (response.status === 200) {
      commit('SET_USER_PROFILE', response.data)
    }
  },
  async pickMovie ({ state, dispatch }, moviePk) {
    const response = await api.pickMovie(moviePk, state.userToken)
    if (response.status === 200) {
      dispatch('getMyProfile')
    }
  },
  async wishMovie ({ state, dispatch }, moviePk) {
    const response = await api.wishMovie(moviePk, state.userToken)
    if (response.status === 200) {
      dispatch('getMyProfile')
    }
  },
  async watchMovie ({ state, dispatch }, moviePk) {
    const response = await api.watchMovie(moviePk, state.userToken)
    if (response.status === 200) {
      dispatch('getMyProfile')
    }
  },
  async dislikeMovie ({ state, dispatch }, moviePk) {
    const response = await api.dislikeMovie(moviePk, state.userToken)
    if (response.status === 200) {
      dispatch('getMyProfile')
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
  SET_MY_PROFILE(state, payload) {
    state.myProfile = payload
  },
  SET_USER_PROFILE(state, payload) {
    state.userProfile = payload
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