from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..Models.productColor_model import ProductsColors
from ..Models.wishlist_model import Wishlist
from ..serializers.wishlist_serializer import wishlistSerializer
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
        

        Wishlist_entry, added = Wishlist.objects.get_or_create(user=user, product_color=product_color)
        if not added:    #موجوده اصلا
            return Response({"message": "Product with this color is already in your wishlist."}, status=status.HTTP_200_OK)

        serializer = wishlistSerializer(Wishlist_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)