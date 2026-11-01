from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Category,Product
from.serializers import CategorySerialize,ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CategoryApiView(viewsets.ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerialize
    #   filter_backends = [DjangoFilterBackend]
    #   filterset_fields = ['category'] 

class ProductApiView(viewsets.ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend]
      filterset_fields = ['category'] 





