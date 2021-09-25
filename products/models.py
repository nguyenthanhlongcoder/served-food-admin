from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Variation(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)
    price_affected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, related_name='variation_options')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True)
    background_color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True,unique=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    labels = models.ManyToManyField(Label, related_name='labels', null=True, blank=True)
    variations = models.ManyToManyField(Variation, related_name='variations')
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ProductVariationOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,related_name='product_variation_options')
    variation_options = models.ManyToManyField(VariationOption, related_name='variation_options')
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.product.name

class Extra(models.Model):
    name =  models.CharField(max_length=100, null=True,unique=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
