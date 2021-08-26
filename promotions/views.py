from django.shortcuts import render
from rest_framework import generics
from promotions import models
from promotions import serializers

class PromotionList(generics.ListCreateAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer
    
class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Promotion.objects.all()
    serializer_class = serializers.PromotionSerializer