from django.shortcuts import render
from rest_framework import generics
from tables import models
from tables import serializers
from django_filters.rest_framework.backends import DjangoFilterBackend

class TableList(generics.ListCreateAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_active']
    
class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer