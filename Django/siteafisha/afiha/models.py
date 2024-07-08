from django.utils import timezone
from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)
    
class EventManager(models.Manager):
    def future_events(self):
        return self.filter(event_time__gt=timezone.now())
    
class Posts(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    url_img = models.ImageField(upload_to='media/', blank=True, verbose_name='Картинка')

    class Meta:
        verbose_name = 'Доступное представление'
        verbose_name_plural = 'Список доступных представлений'

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("poster_id", kwargs={"poster_id": self.pk})
    

class Event(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Законченно'
        PUBLISHED = 1, 'Опубликовано'

    post = models.ForeignKey('Posts', on_delete=models.PROTECT, verbose_name='Название представления')
    event_time = models.DateTimeField(verbose_name='Дата и время представления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.PUBLISHED, verbose_name='Статус')

    objects = models.Manager()
    published = PublishedManager()
    future = EventManager()

    class Meta:
        verbose_name = 'Расписание представлений'
        verbose_name_plural = 'Расписание представлений'
        ordering = ['event_time']
        indexes = [
            models.Index(fields=['event_time'])
        ]

    def __str__(self):
        return str(self.event_time)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url_img = models.ImageField(upload_to='media/', blank=True)
    time_creats = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
