from colorfield.fields import ColorField
from django.db import models

class SendMessage(models.Model):
    name = models.CharField(max_length=100, null=True)

    text_color = ColorField(default='#FF0000')
    border_color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name