from fcm_devices.models import FCMDevice
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import gettext_lazy as _
import FCMManager as fcm
    
class Promotion(models.Model):
    class Status(models.TextChoices):
        READY = 'ready', _('Ready')
        IN_PROGESS = 'in_progess', _('In Progess'),
        STOPPED = 'stopped', _('Stopped')
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    status = models.CharField(max_length=100, choices=Status.choices)
    start_at = models.DateField()
    end_at = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _set_status(self):
        now = datetime.now()
        if self.start_at > now.date():
            return self.Status.READY
        elif self.start_at <= now.date() and self.end_at >= now.date():
            return self.Status.IN_PROGESS
        elif self.end_at < now.date():
            return self.Status.STOPPED
            
    status = property(_set_status)
    def __str__(self):
        return self.name

