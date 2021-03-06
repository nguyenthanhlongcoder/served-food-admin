from django.contrib import admin
from orders.models import Order,OrderItem


class OrderItemInline(admin.TabularInline):
    exclude = ('product_variation_option','order_product_total_price_record','order_extra_total_price_record')

    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['table', 'paid_by', 'status','order_total_price','order_total_price_record']
    search_fields = ['table']
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)

