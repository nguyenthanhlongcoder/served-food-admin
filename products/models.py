from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Variation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price_affected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Label(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    light_theme_color = ColorField(default='#FF0000')
    dark_theme_color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')
    label = models.ManyToManyField(Label, related_name='label')
    variation = models.ManyToManyField(Variation, related_name='variation')
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ProductVariationOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,related_name='product_variation_option')
    variation_option = models.ForeignKey(VariationOption, on_delete=models.CASCADE, related_name='variation_option')
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.product.name + ' ' + self.variation_option.name
