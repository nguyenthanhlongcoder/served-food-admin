from django.contrib import admin
from django.contrib import admin
from send_messages import models
class SendMessageAdmin(admin.ModelAdmin):
    list_display = ['id','name','is_active', 'date_created']
    search_fields = ['name']
    

admin.site.register(models.SendMessage, SendMessageAdmin)

