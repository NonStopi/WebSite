import time, datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string

from .models import News, Posts, Event

menu = [
    {'title': 'Афиша', 'url_name': 'search'},
    {'title':'Заказ билетов', 'url_name': 'contact'},
    {'title':'Контакты', 'url_name': 'contact'},
    {'title':'История дворца', 'url_name': 'contact'},
    {'title':'Галерия', 'url_name': 'contact'},
    {'title':'Планы залов', 'url_name': 'contact'},
]

def index(request):

    post = Event.published.all().select_related('post').order_by("-pk")[:2]
    slider = Posts.objects.all().order_by("-pk")[:4]
    news = News.objects.all()
    data = {
        'title' : 'Сайт концертно-экскурсионных программ',
        'menu': menu,
        'posts' : post,
        'slider': slider,
        'news': news,
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

    posts = Event.future.future_events()

    day=request.GET.get("date")
    month=request.GET.get("month")
    year=request.GET.get("year")

    if day and (len(day) > 2 or not day.isdigit()):
        day = None
    if month and (len(month) > 2 or not month.isdigit()):
        month = None
    if year and (not year.isdigit() or len(year) != 4 or int(year) > 2024):
        year = None

    if day and month and year:
        posts = Event.objects.filter(
            event_time__day=day,
            event_time__month=month,
            event_time__year=year
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
