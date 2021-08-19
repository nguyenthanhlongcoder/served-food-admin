from django.db import models
from django.db.models.fields import PositiveIntegerField
from tables.models import Table
from django.contrib.auth.models import User
from products.models import Product, ProductVariationOption

class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def order_total_price(self):
        order_items = OrderItem.objects.filter(order = self)
        total_price = 0
        for item in order_items:
            total_price += item.order_item_price
        return total_price
    
    def __str__(self):
        return self.table.name
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product')
    product_variation_option = models.ForeignKey(ProductVariationOption, on_delete=models.CASCADE, related_name='product_variation_option')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _get_order_item_price(self):
        return self.product_variation_option.price * self.quantity
    
    order_item_price = property(_get_order_item_price)
    
    def __str__(self):
        return self.product.name + ' ' + self.product_variation_option.variation_option.name + ' ' + str(self.quantity)
    


