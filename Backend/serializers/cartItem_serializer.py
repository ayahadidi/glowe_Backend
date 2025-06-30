from rest_framework import serializers
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from .Product_Serializer import productInfo_serializer


class CartItem_Serializer(serializers.ModelSerializer):
    product=productInfo_serializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'productColor', 'cartItemQuantity', 'cartItemPrice','color_name','product','cart']

        extra_kwargs = {
            'cart': {'write_only': True},
        }

 
    