from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path(r'', include('djoser.urls')),
     path(r'', include('djoser.urls.jwt')),

]