from rest_framework.response import Response
from rest_framework.views import APIView
from Backend.models import Products, ProductsCategories
from ..serializers.ProductSerializer import ProductSerializer

class ProductListByCategory(APIView):
    def get(self, request, category_id=None):
        products_id = ProductsCategories.objects.filter(categoris_id=category_id).values_list('products_id', flat=True)
        products = Products.objects.filter(id__in=products_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)