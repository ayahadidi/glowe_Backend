from rest_framework import serializers
from ..models.cart_item_model import CartItem
from ..models.productColor_model import ProductsColors  # adjust import path
from ..models.cart_model import Cart  # adjust import path

class CartItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'Cart', 'product_color', 'cartItemQuantity', 'cartItemPrice']

    def create(self, validated_data):
        cart = validated_data.get('Cart')
        product_color = validated_data.get('product_color')
        quantity = validated_data.get('cartItemQuantity', 0)
        price = validated_data.get('cartItemPrice', 0)

        # Try to get the existing cart item
        cart_item, created = CartItem.objects.get_or_create(
            Cart=cart,
            product_color=product_color,
            defaults={
                'cartItemQuantity': quantity,
                'cartItemPrice': price
            }
        )

        if not created:
            # If the item already exists, increase quantity and double the price
            cart_item.cartItemQuantity += quantity
            cart_item.cartItemPrice *= 2  # Assuming doubling previous price
            cart_item.save()

        return cart_item
