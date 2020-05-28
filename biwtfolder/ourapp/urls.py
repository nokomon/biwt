from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('music/', views.music, name='music'),
    path('post/', views.createpost, name='createpost'),
    path('newspot/', views.newpost, name='newpost'),
    path('music/<int:post_id>/', views.detail, name='detail'),
]
