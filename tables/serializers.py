from django.db.models import fields
from rest_framework import serializers
from tables import models
        
        
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Table
        fields='__all__'
