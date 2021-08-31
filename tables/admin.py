from django.contrib import admin
from tables import models


    
class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active','is_in_use','status']
    search_fields = ['name']
    
admin.site.register(models.Table, TableAdmin)

