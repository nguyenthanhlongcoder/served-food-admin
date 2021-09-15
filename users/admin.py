from django.contrib import admin
from users.models import CustomUser
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','is_active','is_staff', 'is_superuser','image']
    search_fields = ['email']
    
admin.site.register(CustomUser, UserAdmin)