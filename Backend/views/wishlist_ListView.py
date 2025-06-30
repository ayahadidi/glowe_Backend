from rest_framework import generics 
from ..models.wishlist_model import Wishlist
from rest_framework.permissions import IsAuthenticated
from ..serializers.wishlist_serializer import wishlistSerializer
from ..utils.cart import get_or_create_guest_wishlist


class wishlist_ListView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = wishlistSerializer

    def get_object(self):
        request=self.request
        if request.user.is_authenticated:
            wishlist, _ = Wishlist.objects.get_or_create(user=request.user, type=1)
        else:
            wishlist = get_or_create_guest_wishlist(request)

        return wishlist

    
    

