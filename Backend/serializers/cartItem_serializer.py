from rest_framework import serializers
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart

class CartItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'productColor', 'cartItemQuantity', 'cartItemPrice','color_name','product']

    def create(self, validated_data):
        user = self.context['request'].user
        cart,_=Cart.objects.get_or_create(user=user)

        Product_Color = validated_data.get('productColor',0)
        quantity = validated_data.get('cartItemQuantity', 0)
        price = validated_data.get('cartItemPrice', 0)
        ColorName=validated_data.get('color_name')
        Product=validated_data.get('product')


        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            Product =Product,
            defaults={
                'cartItemQuantity': quantity,
                'cartItemPrice': price,
                'color_name' : ColorName,
                'productColor':Product_Color,
                
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
