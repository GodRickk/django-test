from django.contrib import admin
from django.urls import include, path, re_path
from random_number_app import views




random_number_app_urlpatterns = [
    path('', views.index, name='index'),
    path('', views.random_number_app, name='random_number_app')
]