from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.cart_model import Cart
from ..models.wishlist_model import Wishlist

parameters = openapi.Parameter(
    'obj', openapi.IN_QUERY,
    description="Delete wishlist or cart",
    type=openapi.TYPE_STRING,
    enum=['cart', 'wishlist'],
    required=True
)

class Clear(APIView):
    
    @swagger_auto_schema(manual_parameters=[parameters])
    def delete(self, request, cart_or_wishlist_id):
        obj = request.query_params.get('obj')

        if obj not in ['cart', 'wishlist']:
            return Response({"error": "obj must be 'cart' or 'wishlist'"}, status=400)

        if obj == 'cart':
            if request.user.is_authenticated:
                try:
                    cart = Cart.objects.get(id=cart_or_wishlist_id, user=request.user, type=1)
                except Cart.DoesNotExist:
                    return Response({"error": "Cart not found."}, status=404)
            else:
                session_cart_id = request.session.get('cart_id')
                if not session_cart_id or str(session_cart_id) != str(cart_or_wishlist_id):
                    return Response({"error": "Guest cart not found or does not match session."}, status=404)
                try:
                    cart = Cart.objects.get(id=session_cart_id, user=None)
                except Cart.DoesNotExist:
                    return Response({"error": "Guest cart not found."}, status=404)

                del request.session['cart_id']
                request.session.modified = True

            cart.delete()
            return Response({"message": f"Cart {cart_or_wishlist_id} and its items deleted."}, status=200)

        elif obj == 'wishlist':
            if request.user.is_authenticated:
                try:
                    wishlist = Wishlist.objects.get(id=cart_or_wishlist_id, user=request.user)
                except Wishlist.DoesNotExist:
                    return Response({"error": "Wishlist not found."}, status=404)
            else:
                session_wishlist_id = request.session.get('wishlist_id')
                if session_wishlist_id != cart_or_wishlist_id:
                    return Response({"error": "Guest wishlist not found or does not match session."}, status=404)
                try:
                    wishlist = Wishlist.objects.get(id=session_wishlist_id, user=None)
                except Wishlist.DoesNotExist:
                    return Response({"error": "Guest wishlist not found."}, status=404)

                
                del request.session['wishlist_id']
                request.session.modified = True

            wishlist.delete()
            return Response({"message": f"Wishlist {cart_or_wishlist_id} and its items deleted."}, status=200)

        return Response({"error": "Invalid type. Must be 'cart' or 'wishlist'."}, status=400)
