from django.core.checks.messages import Error
from fcm_devices.models import FCMDevice
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from tables.models import Table
from products.models import Product, ProductVariationOption
import FCMManager as fcm
import logging
from django.contrib.auth import get_user_model


User = get_user_model()

logger = logging.getLogger(__name__)

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True,null=True)
    status = models.CharField(max_length=100, choices=[('serving','Serving'),('paid','Paid'), ('cancelled','Cancelled')],default='serving')
    order_total_price = models.PositiveIntegerField(default=0)
    order_total_price_record = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def _order_total_price(self):
        order_items = OrderItem.objects.filter(order = self)
        total_price = 0
        for item in order_items:
            total_price += item.order_item_price
        return total_price
        
    order_total_price = property(_order_total_price)
    
   
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
                if item.user == instance.paid_by:
                    pass
                elif item.is_active:
                    tokens.append(item.registration_token)
            if previous is not None:
                if previous.status != instance.status:
                    instance.order_total_price_record = instance.order_total_price
                    if instance.status =='paid':
                       
                        fcm.sendPush(str(instance.paid_by.first_name + ' ' + instance.paid_by.last_name),'Đã thanh toán bàn "'+ str(previous.table) + '"' , tokens)
                    elif instance.status == 'cancelled':                      
                        fcm.sendPush('Quản lý','Đã hủy bàn "'+ str(previous.table) + '"' , tokens)

        except NameError:
            pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product')
    product_variation_option = models.ForeignKey(ProductVariationOption, on_delete=models.CASCADE, related_name='product_variation_option')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order_item_price = models.PositiveIntegerField(default=0)
    order_item_price_record = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _get_order_item_price(self):
        if self.is_active is True:
            return self.product_variation_option.price * self.quantity
        else:
            return 0
    
    order_item_price = property(_get_order_item_price)
    
    def __str__(self):
        return self.product.name


@receiver(pre_save, sender=OrderItem)
def on_change(sender, instance, **kwargs):
    order = Order.objects.get(id = instance.order.id)
    table = Table.objects.get(id = order.table.id)
    table.status = 'ordered'
    table.save()
    fcm_devices = FCMDevice.objects.all()
    tokens = []
    if order is not None:
        for item in fcm_devices:
            if item.is_active:
                tokens.append(item.registration_token)
    if instance.id is None:
        try:
            fcm.sendPush(instance.user.first_name + ' ' + instance.user.last_name,'Đặt món "'+ str(instance.product_variation_option) + '" cho bàn "' + str(order.table) + '"' , tokens)
        except NameError:    
            logger.error(NameError)
    else:
        previous = OrderItem.objects.get(id = instance.id)
        if previous is not None:
            try:
                if not instance.is_active:
                    logger.error(instance.order_item_price)
                    instance.order_item_price_record = previous.order_item_price
                    fcm.sendPush("Quản lý", 'Hủy món "' +  str(previous.product_variation_option) + '" cho bàn "' + str(order.table) + '"', tokens) 

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
            order_items = OrderItem.objects.filter(order = order)

            if (len(order_items) == 0):
                table = Table.objects.get(id = order.table.id)
                table.status = 'ready'
                table.save()
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush("Quản lý", 'Hủy món "' +  str(instance.product_variation_option) + '" cho bàn "' + str(order.table) + '"', tokens) 
        except NameError:
            logger.error(NameError)


