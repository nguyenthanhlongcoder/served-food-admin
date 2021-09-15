from django.db.models import fields
from rest_framework import serializers
from products import models
from django.db.models.query import QuerySet

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields='__all__'

            
class VariationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VariationOption
        fields='__all__'   
              

class VariationSerializer(serializers.ModelSerializer):
    variation_options = VariationOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Variation
        fields=['id', 'name','description', 'variation_options']  


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Label
        fields='__all__'

class ProductVariationOptionSerializer(serializers.ModelSerializer):
    variation_options = VariationOptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.ProductVariationOption
        fields=['id','price','variation_options','created_at','updated_at']
       
class ProductSerializer(serializers.ModelSerializer):
    product_variation_options = ProductVariationOptionSerializer(many=True, read_only=True)
    labels = LabelSerializer(many=True, read_only=True)
    variations = VariationSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = models.Product
        fields=['id', 'name', 'description','category', 'labels', 'variations','image', 'product_variation_options', 'created_at','updated_at']



  


