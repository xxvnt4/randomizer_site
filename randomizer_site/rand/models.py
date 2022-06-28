from django.db import models
from datetime import datetime


class Learning(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=datetime.now())
    date_watched = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def __str__(self):
        if self.subtitle:
            return f'{self.title} / {self.subtitle}'
        return f'{self.title}'