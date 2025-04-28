from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('add', views.Add, name="Addd"),
    path('view', views.FetchAll, name="Fetch"),
    path('edit/<int:uid>', views.Update, name="Update"),
    path('harddelete/<int:uid>', views.HardDelete, name="HardDelete"),
    path('softdelete/<int:uid>', views.SoftDelete, name="SoftDelete")
]