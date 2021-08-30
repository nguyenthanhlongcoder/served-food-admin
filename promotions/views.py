from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from promotions import models
from promotions import serializers
from django_filters.rest_framework.backends import DjangoFilterBackend

class PromotionList(generics.ListCreateAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_active']

class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer