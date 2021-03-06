from django.core.checks.messages import Error
from fcm_devices.models import FCMDevice
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from tables.models import Table
from products.models import Extra, Product, ProductVariationOption, VariationOption
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
                if previous.table != instance.table:
                    previous_table = Table.objects.get(id = previous.table.id)
                    previous_table.status = 'ready'
                    previous_table.save()
                    instance_table = Table.objects.get(id = instance.table.id)
                    instance_table.status = 'ordered'
                    instance_table.save()

                    # fcm.sendPush(str(instance.paid_by.first_name + ' ' + instance.paid_by.last_name),'???? chuy???n b??n "'+ str(previous.table) + '" th??nh "'+ str(instance.table) +'"' , tokens)

                if previous.status != instance.status:
                    instance.order_total_price_record = instance.order_total_price
                    order_items = OrderItem.objects.filter(order = instance)
                    table = Table.objects.get(id = instance.table.id)
                    table.status = 'ready'
                    table.save()

                    for order_item in order_items:
                        extras_total_price = 0
                        if order_item.extras.count() != 0:
                            for extra in order_item.extras.all():
                                extras_total_price += extra.price
                        order_item.order_extra_total_price_record = extras_total_price * order_item.quantity
                        order_item.order_product_total_price_record = order_item.product_variation_option.price* order_item.quantity
                        order_item.order_item_price_record = order_item.order_item_price
                        order_item.save()
                    # if instance.status =='paid':
                       
                    #     fcm.sendPush(str(instance.paid_by.first_name + ' ' + instance.paid_by.last_name),'???? thanh to??n b??n "'+ str(previous.table) + '"' , tokens)
                    # elif instance.status == 'cancelled':                      
                    #     fcm.sendPush('Qu???n l??','???? h???y b??n "'+ str(previous.table) + '"' , tokens)

        except NameError:
            pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product')
    product_variation_option = models.ForeignKey(ProductVariationOption, on_delete=models.CASCADE, related_name='product_variation_option')
    order_item_variation_options = models.ManyToManyField(VariationOption, related_name='order_item_variation_options')
    extras = models.ManyToManyField(Extra, related_name='extras',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order_item_price = models.PositiveIntegerField(default=0)
    order_product_total_price_record = models.PositiveIntegerField(default=0)
    order_extra_total_price_record = models.PositiveIntegerField(default=0)
    order_item_price_record = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def _get_order_item_price(self):
        if self.is_active is True:
            extras_total_price = 0
            if self.extras.count() != 0:
                for extra in self.extras.all():
                    extras_total_price += extra.price
            return (self.product_variation_option.price + extras_total_price) * self.quantity
        else:
            return 0
    
    order_item_price = property(_get_order_item_price)
    
    def __str__(self):
        return self.product.name


@receiver(pre_save, sender=OrderItem)
def on_change(sender, instance, **kwargs):
    order = Order.objects.get(id = instance.order.id)
   
    fcm_devices = FCMDevice.objects.all()
    tokens = []
    if order is not None:
        if order.status == 'serving':
            table = Table.objects.get(id = order.table.id)
            table.status = 'ordered'
            table.save()
        for item in fcm_devices:
            if item.is_active:
                tokens.append(item.registration_token)
    if instance.id is None:
        try:
            fcm.sendPush(instance.user.first_name + ' ' + instance.user.last_name,'?????t m??n "'+ str(instance.product_variation_option) + '" cho b??n "' + str(order.table) + '"' , tokens)
        except NameError:    
            logger.error(NameError)
    else:
        previous = OrderItem.objects.get(id = instance.id)
        if previous is not None:
            try:
                if not instance.is_active:
                    extras_total_price = 0
                    if instance.extras.count() != 0:
                        for extra in instance.extras.all():
                            extras_total_price += extra.price
                    
                    
                    instance.order_product_total_price_record = extras_total_price * instance.quantity
                    instance.order_product_total_price_record = instance.product_variation_option.price* instance.quantity
                    instance.order_item_price_record = previous.order_item_price
                    fcm.sendPush("Qu???n l??", 'H???y m??n "' +  str(previous.product_variation_option) + '" cho b??n "' + str(order.table) + '"', tokens) 

            except NameError:
                logger.error(NameError)
       

# @receiver(post_delete, sender=OrderItem)
# def on_delete(sender, instance, **kwargs):
#     if instance.id is None:
#         pass
#     else:
#         try:
#             fcm_devices = FCMDevice.objects.all()
#             tokens = []
#             order = Order.objects.get(id = instance.order.id)
#             order_items = OrderItem.objects.filter(order = order)

#             if (len(order_items) == 0):
#                 table = Table.objects.get(id = order.table.id)
#                 table.status = 'ready'
#                 table.save()
#             for item in fcm_devices:
#                 if item.is_active:
#                     tokens.append(item.registration_token)
#             fcm.sendPush("Qu???n l??", 'H???y m??n "' +  str(instance.product_variation_option) + '" cho b??n "' + str(order.table) + '"', tokens) 
#         except NameError:
#             logger.error(NameError)


