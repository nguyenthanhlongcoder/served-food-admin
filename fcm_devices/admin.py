
from django.contrib import admin
from fcm_devices import models

class FCMDeviceAdmin(admin.ModelAdmin):
    list_display = ['name','user', 'is_active', 'type']
    search_fields = ['name']

admin.site.register(models.FCMDevice, FCMDeviceAdmin)