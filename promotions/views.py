from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from promotions import models
from promotions import serializers

class PromotionList(generics.ListCreateAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['status__id']

class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer