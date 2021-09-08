from django.db.models import fields
from rest_framework import serializers
from orders import models
from tables.serializers import TableSerializer
from users.serializers import UserSerializer
from products.serializers import ProductVariationOptionSerializer, ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    # table = TableSerializer(many=False)
    # user = UserSerializer(many=False)
    order_item = OrderItemSerializer(many=True)
    class Meta:
        model = models.Order
        fields = ['id','table','status','order_item' ,'order_total_price','created_at', 'updated_at']
 
        