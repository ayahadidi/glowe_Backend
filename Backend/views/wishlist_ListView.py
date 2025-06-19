from rest_framework import generics
from ..Models.wishlist_model import Wishlist
from rest_framework.permissions import IsAuthenticated
from ..serializers.wishlist_serializer import wishlistSerializer

class wishlist_ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=wishlistSerializer
    def get_queryset(self):
        return Wishlist.objects.all()
    