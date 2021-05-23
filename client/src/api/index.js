import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const YOUTUBE_API_URL = process.env.VUE_APP_YOUTUBE_API_URL
// const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  // auth
  login(userData) {
    return axios.post(`${SERVER_URL}/accounts/api-token-auth/`, userData)
  },
  signup(userData) {
    return axios.post(`${SERVER_URL}/accounts/signup/`, userData)
  },

  // movie
  getMovies() {
    return axios.get(`${SERVER_URL}/movies/`)
  },
  getBestMovies() {
    return axios.get(`${SERVER_URL}/movies/pickle-best/`)
  },
  getGenreList() {
    return axios.get(`${SERVER_URL}/movies/genre/`)
  },
  searchData(inputText) {
    return axios.get(`${SERVER_URL}/movies/search?q=${inputText}`)
  },
  pickMovie(moviePk, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/movies/${moviePk}/pick/`,
      headers: {
        Authorization: `JWT ${token}`
      }
    })
  },
  wishMovie(moviePk, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/movies/${moviePk}/wish/`,
      headers: {
        Authorization: `JWT ${token}`
      }
    })
  },
  watchMovie(moviePk, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/movies/${moviePk}/watch/`,
      headers: {
        Authorization: `JWT ${token}`
      }
    })
  },
  dislikeMovie(moviePk, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/movies/${moviePk}/dislike/`,
      headers: {
        Authorization: `JWT ${token}`
      }
    })
  },
  


  // getVideo(movieTitle) {
  //   return axios({
  //     url: YOUTUBE_API_URL,
  //     method: 'get',
  //     params: {
  //       key: YOUTUBE_API_KEY,
  //       part: 'snippet',
  //       type: 'video',
  //       q: movieTitle + 'trailer'
  //     }
  //   })
  // }
}