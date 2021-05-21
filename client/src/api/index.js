import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  // auth
  login(userData) {
    return axios.post(`${SERVER_URL}/accounts/api-token-auth/`, userData)
  },
  signup(userData) {
    return axios.post(`${SERVER_URL}/accounts/signup/`, userData)
  },
}