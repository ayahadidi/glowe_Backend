from rest_framework import serializers
from ..models.cart_model import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','product_color','total_price','total_items']

    def create(self,validated_data):
        request=self.context.get('request')
        product_color=validated_data['product_color']

        cart_item,created=Cart.objects.get_or_create(
            user=request.user,
            product_color=product_color,
        )
        if not created:
            cart_item.total_items+=1
            cart_item.total_price+=product_color.products.price
            cart_item.save()
        return cart_item