from django.db.models import fields
from rest_framework import serializers
from fcm_devices import models

class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FCMDevice
        fields = ('__all__')