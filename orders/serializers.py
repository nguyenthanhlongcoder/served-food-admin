from django.db.models import fields
from rest_framework import serializers
from orders import models
from tables.serializers import TableSerializer
from users.serializers import UserSerializer
from products.serializers import ProductVariationOptionSerializer, ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_variation_option = ProductVariationOptionSerializer(many=False)
    user = UserSerializer(many=False)
    product = ProductSerializer(many=False)
    class Meta:
        model = models.OrderItem
        fields = ['id','order','user','product','product_variation_option','quantity','note','order_item_price','created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    # table = TableSerializer(many=False)
    # user = UserSerializer(many=False)
    order_item = OrderItemSerializer(many=True)
    class Meta:
        model = models.Order
        fields = ['id','table','status','order_item' ,'order_total_price','created_at', 'updated_at']
        
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['id','order','user','product','product_variation_option','quantity','note','order_item_price','created_at', 'updated_at']

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id','table','status','order_item' ,'order_total_price','created_at', 'updated_at']