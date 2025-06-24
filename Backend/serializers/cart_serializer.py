from rest_framework import serializers
from ..models.cart_model import Cart
from .cartItem_serializer import CartItem_Serializer

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItem_Serializer(source='cartitem_set', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'total_price', 'total_items', 'user', 'cart_items']