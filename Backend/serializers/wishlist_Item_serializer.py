from rest_framework import serializers
from ..models.wishlist_item_model import wishlist_Item

class wishlist_Item_serializer(serializers.Serializer):
    class Meta:
        model=wishlist_Item
        fields=['product_color']