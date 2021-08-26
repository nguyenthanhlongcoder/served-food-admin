from django.contrib import admin
from django.contrib import admin
from send_messages import models

class SendMessageAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

admin.site.register(models.SendMessage, SendMessageAdmin)

