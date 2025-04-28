from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name="bahay"),
    path('register', views.Register, name="rehistro"),
    path('cashin', views.Cashin, name="paload")
]