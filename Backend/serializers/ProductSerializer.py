from rest_framework import serializers
from ..Models.product_model import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['image','name','ratings','price']
