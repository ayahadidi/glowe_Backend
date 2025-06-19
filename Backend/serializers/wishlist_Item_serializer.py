from rest_framework import serializers
from ..models.wishlist_model import Wishlist
from ..models.wishlist_item_model import wishlist_Item

class wishlist_Item_serializer(serializers.ModelSerializer):
    class Meta:
        model = wishlist_Item
        fields = ['product_color']

    def create(self, validated_data):
        user = self.context['request'].user  
        wishlist, _ = Wishlist.objects.get_or_create(user=user)

        product_color = validated_data.get['product_color']

        wishlist_item,_ = wishlist_Item.objects.get_or_create(
            wishlist=wishlist,
            product_color=product_color,
            defaults={
                'product_color': product_color,
            }
        )

        return wishlist_item
