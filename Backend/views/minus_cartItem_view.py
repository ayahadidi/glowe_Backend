from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from ..utils.cart import get_or_create_guest_cart


from rest_framework.permissions import IsAuthenticated
from ..models.cart_model import Cart
from django.shortcuts import get_object_or_404
class minus_cartItem(APIView):
    def patch(self, request, cartItem_id):
        # Get the correct cart
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user, type=1)
            except Cart.DoesNotExist:
                return Response({'error': 'Cart not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            cart = get_or_create_guest_cart(request)

        try:
            cart_item = CartItem.objects.get(id=cartItem_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found or does not belong to this cart.'}, status=status.HTTP_404_NOT_FOUND)

        if cart_item.cartItemQuantity > 1:
            unit_price = cart_item.cartItemPrice // cart_item.cartItemQuantity
            cart_item.cartItemQuantity -= 1
            cart_item.cartItemPrice -= unit_price
            cart_item.save()

            cart.total_items -= 1
            cart.total_price -= unit_price
            cart.save()

            return Response({'message': 'Item quantity decreased.'}, status=status.HTTP_200_OK)
        else:
            cart.total_items -= 1
            cart.total_price -= cart_item.cartItemPrice
            cart.save()
            cart_item.delete()
            cart.delete()
            return Response({'message': 'Item removed because quantity was 1.'}, status=status.HTTP_200_OK)
