from rest_framework import serializers
from ..models.wishlist_model import Wishlist
from ..models.wishlist_item_model import wishlist_Item
from .Product_Serializer import productInfo_serializer
class wishlist_Item_serializer(serializers.ModelSerializer):
    product=productInfo_serializer(read_only=True)
    class Meta:
        model = wishlist_Item
        fields = ['id', 'productColor','ColorName','product']

    def create(self, validated_data):
        user = self.context['request'].user  
        wishlist, _ = Wishlist.objects.get_or_create(user=user)

        product_color = validated_data.get('productColor')
        ColorName=validated_data.get('ColorName')
        product=self.context.get('product')


        wishlist_item,_ = wishlist_Item.objects.get_or_create(
            wishlist=wishlist,
            product=product,
            defaults={
                'productColor': product_color,
                'ColorName':ColorName
            }
        )

        return wishlist_item
