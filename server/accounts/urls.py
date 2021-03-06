from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('userinfo/', views.update_info),
    path('api-token-auth/', obtain_jwt_token),
    path('<username>/', views.profile),
    path('<int:user_pk>/follow/', views.follow),
]
