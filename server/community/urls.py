from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.curation_list),
    path('<int:curation_pk>', views.curation_detail),
]
