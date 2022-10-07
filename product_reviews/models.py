from email.policy import default
from itertools import product
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length=255)
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    product = models.ForeignKey(User, default=None, on_delete=models.PROTECT)