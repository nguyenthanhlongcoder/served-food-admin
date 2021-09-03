from django.shortcuts import render
from rest_framework import generics
from fcm_devices import models
from fcm_devices import serializers
from django_filters.rest_framework.backends import DjangoFilterBackend

class FCMDeviceList(generics.ListCreateAPIView):
    queryset = models.FCMDevice.objects.all()
    serializer_class = serializers.FCMDeviceSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_active','user','device_id']

class FCMDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FCMDevice.objects.all()
    serializer_class = serializers.FCMDeviceSerializer
