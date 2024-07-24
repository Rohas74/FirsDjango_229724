from django.db import models

# Create your models here.

class Color(models.Model):
   name = models.CharField(max_length=32, unique=True)

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    caption = models.CharField(max_length=50, blank=True)
    colors = models.ManyToManyField(to=Color)

