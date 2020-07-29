from django.db import models

# Create your models here.
from django.db.models import Manager
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    # objects = models.Manager()
    def get_absolute_url(self):
        return reverse("app:books", args=[self.id])


class Chapters(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapter_in_book")

    def __str__(self):
        return self.name
