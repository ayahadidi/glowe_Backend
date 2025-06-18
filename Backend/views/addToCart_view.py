from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..models.productColor_model import ProductsColors
from ..serializers.cartItem_serializer import CartItem_Serializer

class AddToCartView(APIView):
    permission=[IsAuthenticated]

    def post(self,request,product_color_id):
        try:
            product_color=ProductsColors.objects.get(id=product_color_id)
        except ProductsColors.DoesNotExist:
            return Response({"error": "This product isn't available in the selected color."}, status=status.HTTP_404_NOT_FOUND)
        serializer=CartItem_Serializer(data={'product_color':product_color.id},context={'request':request})
        if serializer.is_valid():
            cart_item=serializer.save()
            return Response(CartItem_Serializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)
