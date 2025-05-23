from rest_framework import generics
from ..models.product_model import Products
from ..serializers.ProductSerializer import ProductSerializer

class Best_Sellers_View(generics.ListAPIView):
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        return Products.objects.order_by('-TotalSoldOfProduct')[:10]




