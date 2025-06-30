from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.wishlist_model import Wishlist
from ..models.wishlist_item_model import wishlist_Item

parameters=openapi.Parameter(
    'obj',openapi.IN_QUERY,
    description="Delete wishlist or cart",
    type=openapi.TYPE_STRING,
    enum=['cart','wishlist'],
    required=True
)
class delete_cart_item(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(manual_parameters=[parameters])

    def delete(self,request,item_id):
        obj = request.query_params.get('obj')
        
        if obj not in ['cart', 'wishlist']:
            return Response({"error": "obj must be cart or wishlist"}, status=400)
        if obj=='cart':
            try:

                cart=Cart.objects.get(user=request.user,type=1)
                cart_item=CartItem.objects.get(id=item_id)
            except CartItem.DoesNotExist:
                return Response({"error": "Cart item not found."})
            
            if cart.total_items==cart_item.cartItemQuantity:
                cart_item.delete()
                cart.delete()
            else:
                cart.total_items-=cart_item.cartItemQuantity
                cart.total_price-=cart_item.cartItemPrice
                cart.save()
                cart_item.delete()
        elif obj=='wishlist':
            try:
                wishlist_item=wishlist_Item.objects.get(id=item_id)
            except wishlist_item.DoesNotExist:
                return Response({"error": "wishlist item not found."})

            wishlist_item.delete()

        return Response({"message":f"{item_id} successfulty removed from cart"})