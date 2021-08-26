from django.shortcuts import render
from rest_framework import generics
from send_messages import models
from send_messages import serializers

class SendMessageList(generics.ListCreateAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer
    
class SendMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SendMessage.objects.all()
    serializer_class = serializers.SendMessageSerializer