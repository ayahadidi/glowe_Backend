from rest_framework import generics
from ..models.product_model import Products
from ..serializers.Product_Serializer import ProductInList_Serializer

class Best_Sellers_View(generics.ListAPIView):
    serializer_class=ProductInList_Serializer
    
    def get_queryset(self):
        return Products.objects.order_by('-TotalSoldOfProduct')[:10]




