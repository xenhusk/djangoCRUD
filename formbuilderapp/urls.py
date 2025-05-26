from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "formbuilderapp"

urlpatterns = [
    path('', views.user_form, name='user_form'),
]