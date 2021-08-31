from django import forms
from django.contrib import admin
from products import models
from django.utils.html import format_html
import json

class ProductVariationOptionInline(admin.TabularInline):
    model = models.ProductVariationOption
    
class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70" height="50"/>'.format(obj.image.url))
    
    image_tag.short_description = 'Image'
    list_display = ['name','description','is_active','category','label','image_tag']
    inlines = [ProductVariationOptionInline]
    search_fields = ['name']


    
class VariationOptionInline(admin.TabularInline):
    model = models.VariationOption
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [VariationOptionInline]
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

    
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation, VariationAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Label, LabelAdmin)
