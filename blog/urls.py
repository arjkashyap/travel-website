from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views. generic import ListView, DetailView
from blog.models import Post

app_name = 'blog'   

urlpatterns = [
    url(r'^$', views.blog, name = 'blog'),
    url(r'^(?P<pk>[0-9]+)/', views.post, name = 'post'),
]
