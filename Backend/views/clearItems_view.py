from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.cart_model import Cart
from ..models.wishlist_model import Wishlist


parameters=openapi.Parameter(
    'obj',openapi.IN_QUERY,
    description="Delete wishlist or cart",
    type=openapi.TYPE_STRING,
    enum=['cart','wishlist'],
    required=True
)

class Clear(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[parameters])
    def delete(self,request,cart_or_wishlist_id):
        obj = request.query_params.get('obj')
        
        if obj not in ['cart', 'wishlist']:
            return Response({"error": "obj must be cart or wishlist"}, status=400)
        
        if obj=='cart':
            try:
                cart=Cart.objects.get(id=cart_or_wishlist_id,user=request.user)
                cart.delete()
                return Response({"message": f"Cart {cart_or_wishlist_id} and its items deleted."}, status=status.HTTP_200_OK) 
            except Cart.DoesNotExist:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        elif obj=='wishlist':
            try:
                wishlist=Wishlist.objects.get(id=cart_or_wishlist_id,user=request.user)
                wishlist.delete()
                return Response({"message": f"Wishlist {cart_or_wishlist_id} and its items deleted."}, status=status.HTTP_200_OK)
            except Wishlist.DoesNotExist:
                return Response({"error": "Wishlist not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Invalid type. Must be 'cart' or 'wishlist'."}, status=status.HTTP_400_BAD_REQUEST)