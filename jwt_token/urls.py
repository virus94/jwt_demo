from django.urls import path, include

from django.contrib import admin
from .views import *
from rest_framework_jwt.views import *


urlpatterns = [
    path('sign_up/', UserSignUp.as_view(), name="sign_up"),
    path('api-token-auth/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]