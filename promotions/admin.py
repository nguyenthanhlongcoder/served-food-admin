from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from promotions import models

class PromotionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="50"/>'.format(obj.image.url))
    
    image_tag.short_description = 'Image'
    list_display = ['name', 'description','is_active','image_tag', 'status', 'start_at', 'end_at']
    search_fields = ['name']
    
admin.site.register(models.Promotion, PromotionAdmin)

