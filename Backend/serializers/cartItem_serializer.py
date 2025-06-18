from rest_framework import serializers
from ..models.cart_item_model import CartItem

class CartItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_color', 'cartItemQuantity', 'cartItemPrice']

    def create(self, validated_data):
        product_color = validated_data.get('product_color')
        quantity = validated_data.get('cartItemQuantity', 0)
        price = validated_data.get('cartItemPrice', 0)

        # Try to get the existing cart item
        cart_item, created = CartItem.objects.get_or_create(
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
