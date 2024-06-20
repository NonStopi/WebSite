from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('poster/<int:poster_id>/', views.poster, name="poster_id"),
    path('poster/<slug:poster_name>/', views.poster_name, name="poster_name"),
    path("search/", views.search_date, name="search"),
]