from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=20)
    employees=models.IntegerField()

    def __str__(self):
        return self.name

class Mobile(models.Model):
    color=models.CharField(max_length=20)
    price=models.FloatField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name="mob")


    def __str__(self):
        return self.company
