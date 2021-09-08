from django.db.models import fields
from django.shortcuts import render
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics
from products import models
from products import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters

class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
        
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_active','id', 'category','label']

    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
class ProductVariationOptionList(generics.ListCreateAPIView):
    queryset = models.ProductVariationOption.objects.all()
    serializer_class = serializers.ProductVariationOptionSerializer
    
class ProductVariationOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductVariationOption.objects.all()
    serializer_class = serializers.ProductVariationOptionSerializer

class VariationList(generics.ListCreateAPIView):
    queryset = models.Variation.objects.all()
    serializer_class = serializers.VariationSerializer

class VariationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Variation.objects.all()
    serializer_class = serializers.VariationSerializer

class LabelList(generics.ListCreateAPIView):
    queryset = models.Label.objects.all()
    serializer_class = serializers.LabelSerializer
    
class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Label.objects.all()
    serializer_class = serializers.LabelSerializer