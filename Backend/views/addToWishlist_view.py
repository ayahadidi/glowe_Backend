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
        

        Wishlist_entry, added = Wishlist.objects.get_or_create(user=user)
        if not added:    
            return Response({"message": "Product with this color is already in your wishlist."}, status=status.HTTP_200_OK)

        serializer = wishlist_Item_serializer(Wishlist_entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# class AddToWishlistView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, product_color_id):
#         user = request.user

#         try:
#             product_color = ProductsColors.objects.get(id=product_color_id)
#         except ProductsColors.DoesNotExist:
#             return Response({"error": "Product color not found."}, status=404)

#         # Ensure wishlist container exists for user
#         wishlist, created = Wishlist.objects.get_or_create(user=user)

#         # Add product color as item in wishlist
#         wishlist_item, item_created = wishlist_Item_serializer.objects.get_or_create(
#             wishlist=wishlist,
#             product_color=product_color
#         )

#         if not item_created:
#             return Response({"message": "Product is already in your wishlist."}, status=200)

#         serializer = wishlist_Item_serializer(wishlist_item)
#         return Response(serializer.data, status=201)
