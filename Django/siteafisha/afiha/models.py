from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url_img = models.TextField(blank=True)
    time_creat = models.DateTimeField()
    is_published = models.BooleanField(default=False)