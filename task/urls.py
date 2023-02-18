from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('groups/', views.group, name="groups"),
    path('mark/', views.mark, name='mark'),
]
