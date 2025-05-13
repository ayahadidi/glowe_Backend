from rest_framework import generics
from ..models.product_model import Products
from ..serializers.ProductSerializer import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset = Products.objects.all()




