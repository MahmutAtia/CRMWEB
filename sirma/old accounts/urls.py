
from .views import RegisterApi
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

app_name = "accounts"
urlpatterns = [
    path("register/",RegisterApi.as_view() ),
    path("login/", ObtainAuthToken.as_view())
]
