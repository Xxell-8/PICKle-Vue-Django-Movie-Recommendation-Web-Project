from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.curation_list),
    path('<int:curation_pk>', views.curation_detail),
    # path('comments/', views.comment_list),
    path('<int:curation_pk>/comments/', views.comment_create),
    path('<int:curation_pk>/comments/<int:comment_pk>/', views.comment_detail),
    
]
