from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('create/', views.create_blog, name="create_blog")
]
