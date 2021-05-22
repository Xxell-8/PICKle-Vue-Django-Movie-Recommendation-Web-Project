from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.curation_list),
    path('<int:curation_pk>', views.curation_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('curation/<int:curation_pk>/comments/', views.comment_create),
]
