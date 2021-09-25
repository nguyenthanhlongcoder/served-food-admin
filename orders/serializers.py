from django.db.models import fields
from rest_framework import serializers
from orders import models
from tables.serializers import TableSerializer
from users.serializers import UserSerializer
from products.serializers import ExtraSerializer, ProductVariationOptionSerializer, ProductSerializer, VariationOptionSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    product_variation_option = ProductVariationOptionSerializer(many=False)
    user = UserSerializer(many=False)
    order_item_variation_options = VariationOptionSerializer(many=True)
    product = ProductSerializer(many=False)
    extras = ExtraSerializer(many=True)
    class Meta:
        model = models.OrderItem
        fields = ['id','order','user','product','product_variation_option','order_item_variation_options','extras','quantity','note','order_item_price','order_item_price_record','order_product_total_price_record','order_extra_total_price_record','is_active','created_at', 'updated_at']
    
class OrderSerializer(serializers.ModelSerializer):
    # table = TableSerializer(many=False)
    # user = UserSerializer(many=False)
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = models.Order
        fields = ['id','table','status','order_items' ,'order_total_price','order_total_price_record','created_at', 'updated_at']
        
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['id','order','user','product','product_variation_option','order_item_variation_options','extras','quantity','note','order_item_price','order_item_price_record','order_product_total_price_record','order_extra_total_price_record','is_active','created_at', 'updated_at']

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id','table','status','order_items' ,'created_at', 'updated_at']