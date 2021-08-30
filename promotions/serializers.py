from django.db.models import fields
from rest_framework import serializers
from promotions import models
        

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promotion
        fields=['id','name','is_active','description','image','start_at', 'end_at','status','created_at','updated_at']