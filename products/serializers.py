from django.db.models import fields
from rest_framework import serializers
from products import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields='__all__'
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields='__all__'
        
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variation
        fields='__all__'
        
class VariationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VariationOption
        fields='__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Label
        fields='__all__'

class ProductVariationOptionSerializer(serializers.ModelSerializer):
    variation_option = VariationOptionSerializer(many=False, read_only=True)
    
    class Meta:
        model = models.ProductVariationOption
        fields=['id','price','variation_option','created_at','updated_at']
       
class ProductSerializer(serializers.ModelSerializer):
    product_variation_option = ProductVariationOptionSerializer(many=True, read_only=True)
    label = LabelSerializer(many=True, read_only=True)
    variation = VariationSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    status = StatusSerializer(many=False, read_only=True)
    class Meta:
        model = models.Product
        fields=['id', 'name', 'description','category','status', 'label', 'variation','image', 'product_variation_option', 'created_at','updated_at']



  


