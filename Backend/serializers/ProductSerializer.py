from rest_framework import serializers
from ..models.product_model import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['image','name','ratings','price']