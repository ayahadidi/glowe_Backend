from rest_framework import serializers
from ..serializers.wishlist_Item_serializer import wishlist_Item_serializer
from ..models.wishlist_model import Wishlist

# cartitem_set to handle reverse for a ForeignKey in Djanggo
class wishlistSerializer(serializers.ModelSerializer):

    wishList_items = wishlist_Item_serializer(source='wishlistitem_set', many=True, read_only=True)

    class Meta:
        model=Wishlist
        fields=['id','user','wishList_items']




