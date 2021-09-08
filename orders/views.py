from django.shortcuts import render
from rest_framework import generics
from orders import models
from orders import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework.backends import DjangoFilterBackend

class OrdertList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['table','status']
    
class OrderCreateList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer
    
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemList(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['order']
    
class OrderItemCreateList(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemCreateSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer