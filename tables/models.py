from fcm_devices.models import FCMDevice
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
import FCMManager as fcm
class Table(models.Model):
    name = models.CharField(max_length=100, null=True,unique=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=[('ready','Ready'),('in_user','In User'), ('ordered','Ordered')], default='ready')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
