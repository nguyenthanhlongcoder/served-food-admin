from django.db.models import fields
from rest_framework import serializers
from promotions import models
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields='__all__'
        
class PromotionSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False, read_only=False)
    class Meta:
        model = models.Promotion
        fields=['id','name','description','image','start_at', 'end_at','status','created_at','updated_at']