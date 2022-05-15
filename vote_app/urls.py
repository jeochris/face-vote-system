from django.contrib import admin
from django.urls import path, include
from vote_app import views

urlpatterns = [
    path('', views.index),
    path('front/<id>', views.front),
    path('left/<id>', views.left),
    path('right/<id>', views.right)
]
