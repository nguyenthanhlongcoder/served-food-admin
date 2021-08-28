from django.db import models
from django.contrib.auth.models import User

class FCMDevice(models.Model):
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100, null=True, blank=True)
    registration_token = models.TextField(null=True)
    type = models.CharField(max_length=100, choices=[('ios','ios'),('android','android'), ('web','web')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name