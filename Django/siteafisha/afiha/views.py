from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.db.models import Count, Q
from django.views.generic import TemplateView, DetailView, ListView

from .utils import DataMixin

from .models import News, Posts, Event
from .serializers import PostsSerializer

class Index(DataMixin, TemplateView):
    template_name = "afiha/index.html"
    title_page = "Сайт концертно-экскурсионных программ"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            context,
            posts=Event.published.all()
            .select_related("post")
            .order_by("event_time", "-pk")[:2],
            slider=Posts.objects.annotate(
                future_event_count=Count(
                    "event", filter=Q(event__event_time__gt=timezone.now())
                )
            )
            .filter(future_event_count__gt=0)
            .order_by("-future_event_count")[:4],
            news=News.objects.all(),
        )


class Contact(DataMixin, TemplateView):
    template_name = "afiha/contact.html"
    title_page = "Сайт концертно-экскурсионных программ"

class Poster(DataMixin, DetailView):
    model = Posts
    template_name = "afiha/program.html"
    context_object_name = "post"
    pk_url_kwarg = "poster_id"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


class Search(DataMixin, ListView):
    model = Event
    template_name = "afiha/search.html"
    context_object_name = "posts"
    title_page = "Афиша"

    def get_queryset(self) -> QuerySet[Any]:
        day = self.request.GET.get("date")
        month = self.request.GET.get("month")
        year = self.request.GET.get("year")

        if day and (len(day) > 2 or not day.isdigit()):
            day = None
        if month and (len(month) > 2 or not month.isdigit()):
            month = None
        if year and (not year.isdigit() or len(year) != 4 or int(year) > 2024):
            year = None

        if day and month and year:
            return (
                Event.future.future_events()
                .select_related("post")
                .filter(
                    event_time__day=day, event_time__month=month, event_time__year=year
                )
            )
        else:
            return Event.future.future_events().select_related("post")


def news(request, news_id):
    return HttpResponse(f"Новости: {news_id}")
