from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.cart_item_model import CartItem
from rest_framework.permissions import IsAuthenticated


class minus_cartItem(APIView):
    permission_classes=[IsAuthenticated]

    def patch(self, request, cartItem_id):
        try:
            cart_item=CartItem.objects.get(id=cartItem_id, cart__user=request.user)
            cart=cart_item.cart

            if cart_item.cartItemQuantity>1:
                unit_price=cart_item.cartItemPrice//cart_item.cartItemQuantity
                cart_item.cartItemQuantity-=1
                cart_item.cartItemPrice-=unit_price
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
                return Response({'message': 'Item removed because quantity was 1.'}, status=status.HTTP_200_OK)
            
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)
            



            