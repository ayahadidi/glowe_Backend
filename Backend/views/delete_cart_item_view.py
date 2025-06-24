from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from ..models.cart_item_model import CartItem


class delete_cart_item(DestroyAPIView):
    Permission=[IsAuthenticated]
    

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

