from tables.models import Table
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .managers import StaffUserManager


class StaffUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255,null=False, blank=False)
    last_name = models.CharField(max_length=255,null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    contact_phone = PhoneNumberField(null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StaffUserManager()

    def __str__(self):
        return self.email
    
