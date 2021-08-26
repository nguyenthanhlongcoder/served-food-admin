from django.db.models import fields
from rest_framework import serializers
from send_messages import models
        
class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SendMessage
        fields='__all__'
