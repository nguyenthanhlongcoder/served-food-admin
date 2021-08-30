from django.shortcuts import render
from rest_framework import generics
from send_messages import models
from send_messages import serializers
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class SendMessageList(generics.ListCreateAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filter_fields = ['is_active']
    
class SendMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer