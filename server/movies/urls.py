from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
   path('', views.movie_list),
   path('<int:movie_pk>/', views.movie_detail),
   path('genre/', views.genre_list),
   path('<int:movie_pk>/<options>/', views.rating),
   path('search/', views.movie_search_list),
   path('pickle-best/', views.pick_best),
   path('recommend/random/', views.random_recommend),
   path('recommend/genre/', views.genre_recommend),
   path('recommend/follow/', views.follow_recommend),
   path('recommend/weather/', views.weather_recommend),
   path('recommend/overview/', views.overview_recommend),
]
