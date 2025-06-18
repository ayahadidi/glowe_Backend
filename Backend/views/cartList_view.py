from rest_framework import generics
from ..models.cart_model import Cart
from ..serializers.cart_serializer import CartSerializer
from rest_framework.permissions import IsAuthenticated

class cartList_view(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        return Cart.objects.get(user=self.request.user)
