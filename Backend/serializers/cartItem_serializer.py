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

 
    def create(self, validated_data):
        cart = validated_data.pop('cart')  
        product = self.context.get('product')

        Product_Color = validated_data.get('productColor',0)
        quantity = validated_data.get('cartItemQuantity', 0)
        price = validated_data.get('cartItemPrice', 0)
        ColorName=validated_data.get('color_name')

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product =product,
            defaults={
                'cartItemQuantity': quantity,
                'cartItemPrice': price,
                'color_name' : ColorName,
                'productColor':Product_Color,
                
            }
        )


        cart.total_items += 1
        cart.total_price += product.price
        cart.save()
        if not created:
            cart_item.cartItemQuantity += quantity
            cart_item.cartItemPrice += price
            cart_item.save()

        return cart_item
