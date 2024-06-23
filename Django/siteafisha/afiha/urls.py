from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('poster/<int:poster_id>/', views.poster, name="poster_id"),
    path("search/", views.search, name="search"),
    path('news/<int:news_id>', views.news, name='news_id'),
]