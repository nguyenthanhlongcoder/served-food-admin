from django.contrib import admin

from django.contrib import admin
from orders import models

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['table', 'user', 'status', 'order_total_price']
    search_fields = ['table']
    inlines = [OrderItemInline]
    
admin.site.register(models.Order, OrderAdmin)


