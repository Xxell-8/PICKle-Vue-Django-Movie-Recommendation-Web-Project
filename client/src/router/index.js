import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'
import MyProfile from '@/views/accounts/MyProfile'
import UserProfile from '@/views/accounts/UserProfile'

import PickyPick from '@/views/community/PickyPick'
import ArticleDetail from '@/views/community/ArticleDetail'
import CreateArticle from '@/views/community/CreateArticle'
import UpdateArticle from '@/views/community/UpdateArticle'

import Home from '@/views/movies/Home'
import Search from '@/views/movies/Search'
import Recommendation from '@/views/movies/Recommendation'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Home',
    component: Home
  },
  {
    path: '/movies/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/movies/recommendation',
    name: 'Recommendation',
    component: Recommendation
  },
  {
    path: '/community/pickypick',
    name: 'PickyPick',
    component: PickyPick
  },
  {
    path: '/community/create',
    name: 'CreateArticle',
    component: CreateArticle
  },
  {
    path: '/community/update',
    name: 'UpdateArticle',
    component: UpdateArticle
  },
  {
    path: '/community/article/:id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/profile/',
    name: 'MyProfile',
    component: MyProfile
  },
  {
    path: '/accounts/profile/:username',
    name: 'UserProfile',
    component: UserProfile
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
