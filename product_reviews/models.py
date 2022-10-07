from itertools import product
from unicodedata import name
from django.db import models

# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length=255)
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    product = models.ForeignKey()