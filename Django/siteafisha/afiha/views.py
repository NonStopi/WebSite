from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu = [
    'Афиша',
    'Заказ билетов',
    'Контакты',
    'История дворца',
    'Галерия',
    'Планы Залов',
]

menu = [
    {}
]

data_db = [
    {'id': 1, 'date_day': '6', 'date_month': 'Мая', 'url_img': '', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': True},
    {'id': 2, 'date_day': '30', 'date_month': 'Сентября', 'url_img': '', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре..', 'is_published': True},
    {'id': 3, 'date_day': '6', 'date_month': 'Мая', 'url_img': '', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': False},
]

def index(request):
    data = {
        'title' : 'Сайт концертно-экскурсионных программ',
        'posts' : data_db,
        }
    return render(request, 'afiha/index.html', context=data)

def contact(request):
    data = {'title': 'Контакты'}
    return render(request, 'afiha/contact.html', context=data)

def poster(request, poster_id):
    return HttpResponse(f"<h1>постер №: {poster_id}</h1>")

def poster_name(request, poster_name):
    return HttpResponse(f"<h1>постер name: {poster_name}</h1>")

def search_date(request):
    date=request.GET.get("date", "01")
    if len(date)>2:
        date = "01"

    month=request.GET.get("month", "01")
    if len(month)>2:
        month = "01"

    year=request.GET.get("year", "2000")
    year = int(year)
    if year > 2023:
        print(year)
        return redirect("home", permanent=True)
    if len(str(year))!=4:
        year = "2000"

    return HttpResponse(f"<h1>архив даты: {date}.{month}.{year}</h1>")
