from django.db import models
from products.models import Product
# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length=255)
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)