from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Старница приложения")

def contact(request):
    return HttpResponse("<h1>контакты</h1>")

def poster(request, poster_id):
    return HttpResponse(f"<h1>постер №: {poster_id}</h1>")

def poster_name(request, poster_name):
    return HttpResponse(f"<h1>постер name: {poster_name}</h1>")

def poster_date(request, date):
    return HttpResponse(f"<h1>архив: {date}</h1>")