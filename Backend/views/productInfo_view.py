# from rest_framework import generics
# from ..models.product_model import Products
# from ..serializers.Product_Serializer import productInfo_serializer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class productInfo_view(APIView):
#     def get(self, product_id):
#         serializer= productInfo_serializer(Products)
#         return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.product_model import Products
from ..serializers.Product_Serializer import productInfo_serializer


class productInfo_view(APIView):
    def get(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Products, id=product_id)  
        serializer = productInfo_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)



    