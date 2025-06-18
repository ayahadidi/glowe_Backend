from rest_framework import serializers
from ..Models.wishlist_model import Wishlist

class wishlistSerializer(serializers.Serializer):
    class Meta:
        model=Wishlist
        fields=['product_color']