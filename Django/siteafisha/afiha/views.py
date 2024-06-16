from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Старница приложения")

def contact(request):
    return HttpResponse("<h1>контакты</h1>")