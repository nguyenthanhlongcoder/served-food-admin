from django.db import models
from django.db.models.fields.related import ForeignKey
class Status(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Table(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    order = models.IntegerField(null=True,blank=True)
    status = ForeignKey(Status, on_delete=models.CASCADE, default=1, related_name='status', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
