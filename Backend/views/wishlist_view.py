from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models.product_model import Products
from ..models.wishlist_model import Wishlist
from ..serializers.wishlist_serializer import wishlistSerializer
from rest_framework import status
from rest_framework.response import Response



class addTo_WishList(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, productID):
        user=request.user

        try:
            product=Products.objects.get(id=productID)
        except Products.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        

        Wishlist_entry, added = Wishlist.objects.get_or_create(user=user, product=product)
        if not added:    #موجوده اصلا
            return Response({"message": "Product already in wishlist."}, status=status.HTTP_200_OK)

        serializer = wishlistSerializer(Wishlist_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


