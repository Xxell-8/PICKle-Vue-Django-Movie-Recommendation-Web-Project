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
  getUserInfo(userId) {
    return axios.get(`${SERVER_URL}/accounts/${userId}/`)
  },

  // movie
  getMovies() {
    return axios.get(`${SERVER_URL}/movies/`)
  },
  getMovieDetails(movieId) {
    return axios.get(`${SERVER_URL}/movies/${movieId}/`)
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
  getRandomMovies() {
    return axios.get(`${SERVER_URL}/movies/recommend/random/`)
  },
  getGenreMovies(token) {
    return axios({
      method: 'get',
      url: `${SERVER_URL}/movies/genre-recommend/`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
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
  
  // article
  getArticles(token) {
    return axios({
      method: 'get',
      url: `${SERVER_URL}/community/`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
  },
  getArticleDetail(articleId, token) {
    return axios({
      method: 'get',
      url: `${SERVER_URL}/community/${articleId}`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
  },
  createArticle(articleInfo, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/community/`,
      headers: {
        Authorization: `JWT ${token}`
      },
      data: articleInfo,
    })
  },
  deleteArticle(articleId, token) {
    return axios({
      method: 'delete',
      url: `${SERVER_URL}/community/${articleId}/`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
  },
  updateArticle(articleId, token, articleInfo) {
    return axios({
      method: 'put',
      url: `${SERVER_URL}/community/${articleId}/`,
      headers: {
        Authorization: `JWT ${token}`
      },
      data: articleInfo
    })
  },
  likeArticle(articleId, token) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/community/${articleId}/like/`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
  },
  addComment(articleId, token, data) {
    return axios({
      method: 'post',
      url: `${SERVER_URL}/community/${articleId}/comments/`,
      headers: {
        Authorization: `JWT ${token}`
      },
      data,
    })
  },
  deleteComment(token, commentPk) {
    return axios({
      method: 'delete',
      url: `${SERVER_URL}/community/comments/${commentPk}`,
      headers: {
        Authorization: `JWT ${token}`
      },
    })
  },



}