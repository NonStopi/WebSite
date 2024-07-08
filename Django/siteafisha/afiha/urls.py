from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('poster/<int:poster_id>/', views.Poster.as_view(), name="poster_id"),
    path("search/", views.Search.as_view(), name="search"),
    path('news/<int:news_id>', views.news, name='news_id'),
]