from colorfield.fields import ColorField
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
import FCMManager as fcm
from fcm_devices.models import FCMDevice
class SendMessage(models.Model):
    name = models.TextField(null=True)

    text_color = ColorField(default='#FF0000')
    border_color = ColorField(default='#FF0000')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



@receiver(pre_save, sender=SendMessage)
def on_push(sender, instance, **kwargs):
    tokens = []
    fcm_devices = FCMDevice.objects.all()

    for item in fcm_devices:
        if item.is_active:
            tokens.append(item.registration_token)
    if instance.id is None:
        if instance.is_active == True:
            fcm.sendPush("Quản lý","Thêm thông báo: "+ instance.name, tokens)
    else:
        try:      
            previous = SendMessage.objects.get(id = instance.id)
            if (previous.name != instance.name and instance.is_active == True):          
                fcm.sendPush("Quản lý", 'Thay đổi thông báo từ "' +  previous.name + '" thành "' + instance.name + '"', tokens)
            if (previous.is_active == False and instance.is_active == True):
                fcm.sendPush("Quản lý","Thêm thông báo: "+ instance.name, tokens)

        except:
            pass

@receiver(post_delete, sender=SendMessage)
def on_delete(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        try:
            fcm_devices = FCMDevice.objects.all()
            tokens = []
            for item in fcm_devices:
                if item.is_active:
                    tokens.append(item.registration_token)
            fcm.sendPush("Quản lý", 'Xóa thông báo "' +  instance.name + '"', tokens) 
        except:
            pass

