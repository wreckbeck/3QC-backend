from django.conf import settings
from django.contrib import admin
from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login")
]