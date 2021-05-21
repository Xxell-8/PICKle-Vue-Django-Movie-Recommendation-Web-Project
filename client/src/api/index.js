import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const YOUTUBE_API_URL = process.env.VUE_APP_YOUTUBE_API_URL
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  // auth
  login(userData) {
    return axios.post(`${SERVER_URL}/accounts/api-token-auth/`, userData)
  },
  signup(userData) {
    return axios.post(`${SERVER_URL}/accounts/signup/`, userData)
  },
  getVideo(movieTitle) {
    return axios({
      url: YOUTUBE_API_URL,
      method: 'get',
      params: {
        key: YOUTUBE_API_KEY,
        part: 'snippet',
        type: 'video',
        q: movieTitle + 'trailer'
      }
    })
  }
}