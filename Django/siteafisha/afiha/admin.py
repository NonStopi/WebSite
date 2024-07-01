from django.contrib import admin
from .models import Posts, Event

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'url_img')
    list_display_links = ('id', 'title')
    list_per_page = 10

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'event_time', 'is_published')
    list_display_links = ('id', 'post')
    ordering = ['-is_published','-event_time']
    list_editable = ('is_published', )
    list_per_page = 10

admin.site.register(Posts, PostsAdmin)
admin.site.register(Event, EventAdmin)
# Register your models here.
