from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..Models.product_model import Products
from ..serializers.Product_Serializer import productInfo_serializer


class productInfo_view(APIView):
    def get(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Products, id=product_id)  
        serializer = productInfo_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)



    