from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..models.product_model import Products
from ..serializers.cartItem_serializer import CartItem_Serializer
from ..models.color_model import Colors

class AddToCartView(APIView):
    permission=[IsAuthenticated]

    def post(self,request,product_id, color_id):
        try:
            product=Products.objects.get(id=product_id)
            color = Colors.objects.get(id=color_id, product=product)
        except (Colors.DoesNotExist, Products.DoesNotExist):
            return Response({"error": "This product isn't available in the selected color."}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer=CartItem_Serializer(data={
            'product':product_id,
            'cartItemQuantity':request.data.get('cartItemQuantity',1),
            'cartItemPrice':request.data.get('cartItemPrice',product.price),
            'productColor':request.data.get('productColor',color.code),
            'color_name':request.data.get('color_name',color.ColorName),

            },context={'request':request})
        
        if serializer.is_valid():
            cart_item=serializer.save()
            return Response(CartItem_Serializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)
