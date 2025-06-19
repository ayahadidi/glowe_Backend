from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..serializers.wishlist_Item_serializer import wishlist_Item_serializer
from rest_framework import status
from rest_framework.response import Response
from ..models.product_model import Products
from ..models.color_model import Colors


class addTo_WishList(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request,product_id,color_id):

        try:
           product=Products.objects.get(id=product_id)
           color = Colors.objects.get(id=color_id, product=product)
        except (Colors.DoesNotExist, Products.DoesNotExist):
            return Response({"error": "This product isn't available in the selected color."}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = wishlist_Item_serializer(data={
            'product': product_id,
            'ColorName':request.data.get('ColorName',color.ColorName),
            'productColor':request.data.get('productColor',color.code),
            },context={'request': request})

        
        if serializer.is_valid():
            wishlist_item=serializer.save()
            return Response(wishlist_Item_serializer(wishlist_item).data, status=201)
        return Response(serializer.errors, status=400)

        