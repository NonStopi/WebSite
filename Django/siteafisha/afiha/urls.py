from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('poster/<int:poster_id>/', views.poster),
    path('poster/<slug:poster_name>/', views.poster_name),
    re_path(r"^poster/(?P<date>\d{2}/\d{2}/\d{4})/$", views.poster_date)
]