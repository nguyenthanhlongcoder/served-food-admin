from django.shortcuts import render
from rest_framework import generics
from send_messages import models
from send_messages import serializers
from rest_framework.filters import SearchFilter, OrderingFilter
class SendMessageList(generics.ListCreateAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    
class SendMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer