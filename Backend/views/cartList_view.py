#cartList_view
from rest_framework import generics
from ..models.cart_model import Cart
from ..serializers.cart_serializer import CartSerializer
from rest_framework.permissions import IsAuthenticated
from ..utils.cart import get_or_create_guest_cart
from django.shortcuts import get_object_or_404

class cartList_view(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    
    def get_object(self):
        request=self.request

        if request.user.is_authenticated:
            cart = get_object_or_404(Cart, user=request.user, type=1)
        else:
            cart = get_or_create_guest_cart(request)

        

        return cart




