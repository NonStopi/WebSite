import time, datetime
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
    {'title': 'Афиша', 'url_name': 'search'},
    {'title':'Заказ билетов', 'url_name': 'contact'},
    {'title':'Контакты', 'url_name': 'contact'},
    {'title':'История дворца', 'url_name': 'contact'},
    {'title':'Галерия', 'url_name': 'contact'},
    {'title':'Планы залов', 'url_name': 'contact'},
]

poster_db = [
    {'id': 1, 'date_day': '6', 'date_month': 'Мая', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': True},
    {'id': 2, 'date_day': '30', 'date_month': 'Сентября', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре..', 'is_published': True},
    {'id': 3, 'date_day': '6', 'date_month': 'Мая', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': False},
]

slider_db = [
    {'id': 1, 'url_image':'https://placehold.co/1000x1000/orange/fff/?text=Hello\nWorld','title_slider': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'},
    {'id': 2, 'url_image':'https://placehold.co/1000x1000/green/fff/?text=Hello\nWorld','title_slider': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'},
    {'id': 3, 'url_image':'https://placehold.co/1000x1000/black/fff/?text=Hello\nWorld','title_slider': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'},
    {'id': 4, 'url_image':'https://placehold.co/1000x1000/red/fff/?text=Hello\nWorld','title_slider': 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'},
]

news_db = [
    {'id': 1, 'url_image':'static/afiha/img/main_afisha.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 2, 'url_image':'static/afiha/img/poster__image1.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 3, 'url_image':'static/afiha/img/thumb-slider__image.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 4, 'url_image':'static/afiha/img/thumb-slider__image2.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},

]


def index(request):
    data = {
        'title' : 'Сайт концертно-экскурсионных программ',
        'menu': menu,
        'posts' : poster_db,
        'slider': slider_db,
        'news': news_db,
        }
    return render(request, 'afiha/index.html', context=data)

def contact(request):
    data = {
        'title': 'Контакты',
        'menu': menu,
        }
    return render(request, 'afiha/contact.html', context=data)

def poster(request, poster_id):
    return HttpResponse(f"<h1>постер №: {poster_id}</h1>")

def poster_name(request, poster_name):
    return HttpResponse(f"<h1>постер name: {poster_name}</h1>")

def search(request):
    data = {
        'menu': menu,
        'title' : 'Афиша',
        'posts' : poster_db,
    }
    return render(request, 'afiha/search.html',context=data)

def search_date(request):
    date=request.GET.get("date", "01")
    if len(date)>2:
        date = "01"

    month=request.GET.get("month", "01")
    if len(month)>2:
        month = "01"

    year=request.GET.get("year", "2000")
    year = int(year)
    if year > 2024:
        print(year)
        return redirect("home", permanent=True)
    if len(str(year))!=4:
        year = "2000"

    return HttpResponse(f"<h1>архив даты: {date}.{month}.{year}</h1>")

def news(request, news_id):
    return HttpResponse(f'Новости: {news_id}')
