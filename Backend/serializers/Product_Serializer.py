from rest_framework import serializers
from ..Models.product_model import Products

class ProductInList_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['image','name','ratings','price']


class productInfo_serializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['image','name','ratings','price','description','usage','ingredients','brandName']
