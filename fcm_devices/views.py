from django.shortcuts import render
from rest_framework import generics
from fcm_devices import models
from fcm_devices import serializers

class FCMDeviceList(generics.ListCreateAPIView):
    queryset = models.FCMDevice.objects.all()
    serializer_class = serializers.FCMDeviceSerializer

class FCMDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FCMDevice.objects.all()
    serializer_class = serializers.FCMDeviceSerializer