from django.db.models import fields
from rest_framework import serializers
from tables import models
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields='__all__'
        
class TableSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False, read_only=False)
    class Meta:
        model = models.Table
        fields=['id','name','description','status','created_at','updated_at']
