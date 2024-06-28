from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)
    
class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url_img = models.TextField(blank=True)
    time_creat = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-time_creat']
        indexes = [
            models.Index(fields=['-time_creat'])
        ]
    def get_absolute_url(self):
        return reverse("poster_id", kwargs={"poster_id": self.pk})
    