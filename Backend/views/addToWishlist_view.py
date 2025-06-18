from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models.productColor_model import ProductsColors
from ..models.wishlist_model import Wishlist
from ..serializers.wishlist_Item_serializer import wishlist_Item_serializer
from rest_framework import status
from rest_framework.response import Response


class addTo_WishList(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request,product_color_id):
        user=request.user

        try:
            product_color=ProductsColors.objects.get(id=product_color_id)
        except ProductsColors.DoesNotExist:
            return Response({"error": "This product isn't available in the selected color."}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = wishlist_Item_serializer(data={'product_color': product_color_id}, context={'request': request})

        
        if serializer.is_valid():
            wishlist_item=serializer.save()
            return Response(wishlist_Item_serializer(wishlist_item).data, status=201)
        return Response(serializer.errors, status=400)

        