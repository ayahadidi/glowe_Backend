from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.cart_model import Cart
from ..models.cart_item_model import CartItem
from ..models.wishlist_model import Wishlist
from ..models.wishlist_item_model import wishlist_Item
from ..utils.cart import get_or_create_guest_cart, get_or_create_guest_wishlist

parameters = openapi.Parameter(
    'obj', openapi.IN_QUERY,
    description="Delete wishlist or cart",
    type=openapi.TYPE_STRING,
    enum=['cart', 'wishlist'],
    required=True
)

class delete_cart_item(APIView):
    @swagger_auto_schema(manual_parameters=[parameters])
    def delete(self, request, item_id):
        obj = request.query_params.get('obj')

        if obj not in ['cart', 'wishlist']:
            return Response({"error": "obj must be 'cart' or 'wishlist'"}, status=400)

        if obj == 'cart':
            # Get cart depending on user auth status
            if request.user.is_authenticated:
                try:
                    cart = Cart.objects.get(user=request.user, type=1)
                except Cart.DoesNotExist:
                    return Response({"error": "Cart not found."}, status=404)
            else:
                cart = get_or_create_guest_cart(request)

            try:
                cart_item = CartItem.objects.get(id=item_id, cart=cart)
            except CartItem.DoesNotExist:
                return Response({"error": "Cart item not found or doesn't belong to this cart."}, status=404)

            if cart.total_items == cart_item.cartItemQuantity:
                cart_item.delete()
                cart.delete()
            else:
                cart.total_items -= cart_item.cartItemQuantity
                cart.total_price -= cart_item.cartItemPrice
                cart.save()
                cart_item.delete()

            return Response({"message": f"Cart item {item_id} successfully removed."}, status=200)

        elif obj == 'wishlist':
            # Get wishlist depending on user auth status
            if request.user.is_authenticated:
                try:
                    wishlist = Wishlist.objects.get(user=request.user)
                except Wishlist.DoesNotExist:
                    return Response({"error": "Wishlist not found."}, status=404)
            else:
                wishlist = get_or_create_guest_wishlist(request)

            try:
                wishlist_item = wishlist_Item.objects.get(id=item_id, wishlist=wishlist)
            except wishlist_Item.DoesNotExist:
                return Response({"error": "Wishlist item not found or doesn't belong to this wishlist."}, status=404)

            wishlist_item.delete()
            return Response({"message": f"Wishlist item {item_id} successfully removed."}, status=200)

        return Response({"error": "Invalid obj type. Must be 'cart' or 'wishlist'."}, status=400)
