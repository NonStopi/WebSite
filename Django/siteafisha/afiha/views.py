import time, datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string

from .models import Posts

menu = [
    {'title': 'Афиша', 'url_name': 'search'},
    {'title':'Заказ билетов', 'url_name': 'contact'},
    {'title':'Контакты', 'url_name': 'contact'},
    {'title':'История дворца', 'url_name': 'contact'},
    {'title':'Галерия', 'url_name': 'contact'},
    {'title':'Планы залов', 'url_name': 'contact'},
]

news_db = [
    {'id': 1, 'url_image':'static/afiha/img/main_afisha.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 2, 'url_image':'static/afiha/img/poster__image1.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 3, 'url_image':'static/afiha/img/thumb-slider__image.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},
    {'id': 4, 'url_image':'static/afiha/img/thumb-slider__image2.png', 'title_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, voluptatem.', 'des_news': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, asperiores distinctio. Nobis, ratione, nulla cupiditate optio aspernatur nisi ab accusantium deserunt perspiciatis consequuntur delectus itaque repellendus quod animi tempore nihil?'},

]


def index(request):
    post = Posts.published.all().order_by("-pk")[:2]
    slider = Posts.objects.all().order_by("-pk")[:4]
    data = {
        'title' : 'Сайт концертно-экскурсионных программ',
        'menu': menu,
        'posts' : post,
        'slider': slider,
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
    post = get_object_or_404(Posts, pk=poster_id)
    data = {
        'menu': menu,
        'post' : post,
        'title' : post.title,
    }
    return render(request, 'afiha/program.html',context=data)

def search(request):

    posts = Posts.objects.all()

    day=request.GET.get("date")
    month=request.GET.get("month")
    year=request.GET.get("year")

    if day and (len(day) > 2 or not day.isdigit()):
        date = "01"
    if month and (len(month) > 2 or not month.isdigit()):
        month = "01"
    if year and (not year.isdigit() or len(year) != 4 or int(year) > 2024):
        year = "2000"

    if day and month and year:
        posts = posts.filter(
            time_creat__day=day,
            time_creat__month=month,
            time_creat__year=year
        )

    search_info = {
        'date': day,
        'month': month,
        'year': year,
    }

    data = {
        'menu': menu,
        'title' : 'Афиша',
        'posts' : posts,
        'search_info': search_info,
    }

    print(f"Debug: date={day}, month={month}, year={year}")

    return render(request, 'afiha/search.html',context=data)

def news(request, news_id):
    return HttpResponse(f'Новости: {news_id}')
