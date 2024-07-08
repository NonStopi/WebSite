from django.contrib import admin, messages
from .models import Posts, Event, News

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'url_img')
    list_display_links = ('title', )
    list_per_page = 10
    search_fields = ['title']
    fields = ['title', 'url_img', 'content']
    save_on_top = True

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('post', 'event_time', 'is_published')
    list_display_links = ('post', )
    ordering = ['-is_published','-event_time']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['post__title']
    list_filter = ['post__title', 'event_time', 'is_published']
    save_on_top = True

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Event.Status.PUBLISHED)
        self.message_user(request, f'Опубликованно{count} записей')

    @admin.display(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Event.Status.DRAFT)
        self.message_user(request, f'Снято с публикации {count} записей', messages.WARNING)


admin.site.register(News)
