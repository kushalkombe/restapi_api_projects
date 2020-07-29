from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    price=models.FloatField()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=60)
    boook=models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapter")
