from rest_framework import serializers
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from ..models.productColor_model import ProductsColors

class CartItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_color', 'cartItemQuantity', 'cartItemPrice']

    def create(self, validated_data):
        user=self.request.user
        cart,_=Cart.objects.get_or_create(user=user)

        product_color = validated_data.get('product_color')
        quantity = validated_data.get('cartItemQuantity', 0)
        price = validated_data.get('cartItemPrice', 0)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_color=product_color,
            defaults={
                'cartItemQuantity': quantity,
                'cartItemPrice': price
            }
        )

        cart.total_items+=1
        cart.total_price+=cart_item.cartItemPrice
        cart.save()
        if not created:
            cart_item.cartItemQuantity += quantity
            cart_item.cartItemPrice += price
            cart_item.save()

        return cart_item
