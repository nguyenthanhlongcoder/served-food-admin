from fcm_devices.models import FCMDevice
from django.db import models

import FCMManager as fcm
class Table(models.Model):
    name = models.CharField(max_length=100, null=True,unique=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_in_use = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=[('ready','Ready'), ('ordered','Ordered')], default='ready')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
