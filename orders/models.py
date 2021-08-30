from django.core.checks.messages import Error
from fcm_devices.models import FCMDevice
from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from tables.models import Table
from django.contrib.auth.models import User
from products.models import Product, ProductVariationOption
import FCMManager as fcm
import logging
logger = logging.getLogger(__name__)

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True,null=True)
    status = models.CharField(max_length=100, choices=[('serving','Serving'),('paid','Paid'), ('cancelled','Cancelled')])

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

@receiver(pre_save, sender=Order)
def on_change(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        try:
            fcm_devices = FCMDevice.objects.all()
            tokens = []
            previous = Order.objects.get(id = instance.id)
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            if previous is not None:
                if previous.status != instance.status:
                    if instance.status =='paid':
                        fcm.sendPush(str(instance.paid_by.username),'Đã thanh toán bàn "'+ str(previous.table) + '"' , tokens)
                    elif instance.status == 'cancelled':
                        fcm.sendPush('Quản lý','Đã hủy bàn "'+ str(previous.table) + '"' , tokens)

        except NameError:
            pass

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product')
    product_variation_option = models.ForeignKey(ProductVariationOption, on_delete=models.CASCADE, related_name='product_variation_option')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(null=True, blank=True)
    order_item_price = models.PositiveBigIntegerField(default=0)
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
        order = Order.objects.get(id = order_item.order.id)
        if order is not None:
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush(order_item.user.username,'Đặt món "'+ str(instance.product_variation_option) + '" cho bàn "' + str(order.table) + '"' , tokens)
    except NameError:    
        logger.error(NameError)

@receiver(post_delete, sender=OrderItem)
def on_delete(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        try:
            fcm_devices = FCMDevice.objects.all()
            tokens = []
            order = Order.objects.get(id = instance.order.id)
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush("Quản lý", 'Hủy món "' +  str(instance.product_variation_option) + '" cho bàn "' + str(order.table) + '"', tokens) 
        except NameError:
            logger.error(NameError)

