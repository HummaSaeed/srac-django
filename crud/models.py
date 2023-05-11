from turtle import distance
from unicodedata import category
from django.db import models
import datetime

class Item(models.Model):
    username=models.CharField(max_length=255, default='')
    name=models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=255, default='')
    modal = models.CharField(max_length=255,default='')
    category = models.CharField(max_length=255, default='')
    year = models.PositiveIntegerField(default=1)
    distance = models.PositiveIntegerField(default=1)
    transmissionType = models.CharField(max_length=255, default='')
    bodyType = models.CharField(max_length=255, default='')
    price = models.CharField(max_length=255, default='')
    condition = models.CharField(max_length=255, default='')
    paymentoption = models.CharField(max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to = "images/",default='')
    def __str__(self) -> str:
        return self.name

