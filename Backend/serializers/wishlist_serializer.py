from rest_framework import serializers
from ..models.wishlist_model import Wishlist

class wishlistSerializer(serializers.Serializer):
    class Meta:
        model=Wishlist
        fields=['image','name','ratings','price']