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

month_map = {
    '01': 'Январь',
    '02': 'Февраль',
    '03': 'Март',
    '04': 'Апрель',
    '05': 'Май',
    '06': 'Июнь',
    '07': 'Июль',
    '08': 'Август',
    '09': 'Сентябрь',
    '10': 'Октябрь',
    '11': 'Ноябрь',
    '12': 'Декабрь',
}

poster_db = [
    {'id': 1, 'date_day': '06', 'date_month': '05', 'date_year': '2024', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': True},
    {'id': 2, 'date_day': '30', 'date_month': '09', 'date_year': '2024', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре.Посвящение Фрэнку Синатре..', 'is_published': True},
    {'id': 3, 'date_day': '06', 'date_month': '05', 'date_year': '2024', 'url_img': 'afiha/img/main_afisha.png', 'title_poster': 'Антонио Вивальди. Времена года', 'description_poster': 'Посвящение Фрэнку Синатре.', 'is_published': False},
]

slider_db = [
    {'id': 1, 'url_image':'https://placehold.co/1000x1000/orange/fff/?text=Hello\nWorld','title_slider': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Lorem ipsum dolor sit amet consectetur adipisicing elit.'},
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
    data_db= {
        'post' : poster_db,
    }
    data = {
        'menu': menu,
        'data_post' : data_db,
        'title' : f'Постер {poster_id}',
    }
    return render(request, 'afiha/program.html',context=data)

def search(request):
    date=request.GET.get("date")
    month=request.GET.get("month")
    year=request.GET.get("year")

    if date and (len(date) > 2 or not date.isdigit()):
        date = "01"
    if month and (len(month) > 2 or not month.isdigit()):
        month = "01"
    if year and (not year.isdigit() or len(year) != 4 or int(year) > 2024):
        year = "2000"

    filtered_posts = poster_db

    if date:
        filtered_posts = [post for post in filtered_posts if post['date_day'] == date]
    if month:
        filtered_posts = [post for post in filtered_posts if post['date_month'] == month]
    if year:
        filtered_posts = [post for post in filtered_posts if post['date_year'] == year]

    if month:
        month_text = month_map.get(month, '')
    else:
        month_text = ''


    search_info = {
        'date': date,
        'month': month_text,
        'year': year,
    }

    data = {
        'menu': menu,
        'title' : 'Афиша',
        'posts' : filtered_posts,
        'search_info': search_info,
    }

    print(f"Debug: date={date}, month={month}, year={year}")

    return render(request, 'afiha/search.html',context=data)

def news(request, news_id):
    return HttpResponse(f'Новости: {news_id}')
