from configparser import InterpolationMissingOptionError
from itertools import product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from .serializers import ReviewSerializer
from .models import Review
from product_reviews import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def review_list(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        reviews = Review.objects.filter(product=product)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # if request.method == 'GET':
    #     serializer = ReviewSerializer(review)
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


