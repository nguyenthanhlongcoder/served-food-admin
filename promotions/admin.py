from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from promotions import models

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    
class PromotionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="50"/>'.format(obj.image.url))
    
    image_tag.short_description = 'Image'
    list_display = ['name', 'description','image_tag', 'status', 'start_at', 'end_at']
    search_fields = ['name']
    
admin.site.register(models.Status, StatusAdmin)
admin.site.register(models.Promotion, PromotionAdmin)

