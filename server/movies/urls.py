from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
   path('', views.movie_list),
   path('<int:movie_pk>/', views.movie_detail),
   path('genre/', views.genre_list),
   path('<int:movie_pk>/<options>/', views.rating),
   path('search/', views.movie_search_list),
   path('random/', views.random_movie_list),
   path('pickle-best/', views.pick_best),
   path('weather_recommend/', views.weather_recommend),
#    path('short-movie', views.short_movie_list),
#    path('genre_recommend', views.genre_recommended),
# #    path('recommend', views.recommend),
]
