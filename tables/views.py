from django.shortcuts import render
from rest_framework import generics
from tables import models
from tables import serializers

class TableList(generics.ListCreateAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer
    
class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer