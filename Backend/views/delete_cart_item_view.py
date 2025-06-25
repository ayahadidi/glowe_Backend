from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart

class delete_cart_item(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self,request,cart_item_id):
        try:
            cart=Cart.objects.get(user=request.user)
            cart_item=CartItem.objects.get(id=cart_item_id)
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
        
        return Response({"message":f"{cart_item_id} successfulty removed from cart"})