from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
   path('', views.movie_list),
   path('<int:movie_pk>/', views.movie_detail),
   path('short-movie', views.short_movie_list),
   path('random', views.random_recommended),
   path('genre_recommend', views.genre_recommended),
   path('pick/', views.pick_best),
#    path('search/', views.search),
#    path('recommend', views.recommend),
]
