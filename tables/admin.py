from django.contrib import admin
from tables import models

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    
class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status']
    search_fields = ['name']
    
admin.site.register(models.Status, StatusAdmin)
admin.site.register(models.Table, TableAdmin)

