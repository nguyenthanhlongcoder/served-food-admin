from django.db import models
from datetime import datetime
class Status(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Promotion(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')
    start_at = models.DateField()
    end_at = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _set_status(self):
        now = datetime.now()
        if self.start_at > now.date():
            return Status.objects.get(id = 1)
        elif self.start_at <= now.date() and self.end_at >= now.date():
            return Status.objects.get(id = 2)
        elif self.end_at < now.date():
            return Status.objects.get(id = 3)
            
    status = property(_set_status)
    def __str__(self):
        return self.name