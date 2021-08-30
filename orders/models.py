from fcm_devices.models import FCMDevice
from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from tables.models import Table
from django.contrib.auth.models import User
from products.models import Product, ProductVariationOption
import FCMManager as fcm

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    status = models.CharField(max_length=100, choices=[('serving','Serving'),('paid','Paid'), ('canceled','Canceled')])

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
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _get_order_item_price(self):
        return self.product_variation_option.price * self.quantity
    
    order_item_price = property(_get_order_item_price)
    
    def __str__(self):
        return self.product.name + ' ' + self.product_variation_option.variation_option.name + ' ' + str(self.quantity)


@receiver(post_save, sender=OrderItem)
def on_save(sender, instance, **kwargs):
    try:
        fcm_devices = FCMDevice.objects.all()
        tokens = []
        order_item = OrderItem.objects.get(id = instance.id)
        order = Order.objects.get(id = order_item.order)
        if order is not None:
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush(order_item.user,'Đặt món "'+ instance.product_variation_option + '" cho bàn "' + order.table + '"' , tokens)

    except:
        pass
@receiver(post_delete, sender=OrderItem)
def on_delete(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        try:
            fcm_devices = FCMDevice.objects.all()
            tokens = []
            order_item = OrderItem.objects.get(id = instance.id)
            order = Order.objects.get(id = order_item.order)
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush("Quản lý", 'Hủy món "' +  instance.product_variation_option + '" cho bàn "' + order.table + '"', tokens) 
        except:
            pass

