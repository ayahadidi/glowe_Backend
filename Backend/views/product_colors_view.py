# views/product_colors_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Products, Colors
from ..serializers.color_serializer import ColorSerializer

class ProductColorsView(APIView):
    def get(self, request, product_id):
        try:
            product = Products.objects.get(id=product_id)
            colors = Colors.objects.filter(product=product)  # adjust this if your relation is different
            serializer = ColorSerializer(colors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
