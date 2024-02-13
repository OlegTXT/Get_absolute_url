from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

