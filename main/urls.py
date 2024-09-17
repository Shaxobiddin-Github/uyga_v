
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="home"),
    path('about',about,name="about"),
    path('blog_details',blog_details,name="blog_details"),
    path('blog',blog,name="blog"),
    path('categori',categori,name="categori"),
    path('contact',contact,name="contact"),
    path('elements',elements,name="elements"),
    path('latest_news',latest_news,name="latest_news"),
    path('main',main,name="main"),
    path('detail/<int:pk>/', detail, name='detail'),
]
