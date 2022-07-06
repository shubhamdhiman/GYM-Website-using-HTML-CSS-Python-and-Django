from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    age = models.IntegerField()
    gender=models.CharField(max_length=10, default='M')
    