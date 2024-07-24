from django.db import models

# Create your models here.


class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    caption = models.CharField(max_length=50, blank=True)
    #colors = model.