from rest_framework import generics 
from ..models.wishlist_model import Wishlist
from rest_framework.permissions import IsAuthenticated
from ..serializers.wishlist_serializer import wishlistSerializer

class wishlist_ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = wishlistSerializer

    def get_queryset(self):
        user = self.request.user
        return Wishlist.objects.filter(user=user)
