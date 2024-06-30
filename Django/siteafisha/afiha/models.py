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
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(blank=True)
    url_img = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("poster_id", kwargs={"poster_id": self.pk})
    

class Event(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.PROTECT)
    event_time = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()
    future = EventManager()

    class Meta:
        ordering = ['-event_time']
        indexes = [
            models.Index(fields=['-event_time'])
        ]

    def __str__(self):
        return str(self.event_time)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url_img = models.TextField(blank=True)
    time_creats = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
