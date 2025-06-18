from rest_framework import serializers
from ..serializers.wishlist_Item_serializer import wishlist_Item_serializer
from ..models.wishlist_model import Wishlist

# cartitem_set to handle reverse for a ForeignKey in Djanggo
class wishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields=['id','user']




