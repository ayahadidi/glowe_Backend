from rest_framework import serializers
from ..models.product_model import Products
from .rating_serializer import RatingSerializer

class ProductInList_Serializer(serializers.ModelSerializer):
    ratings=RatingSerializer(many=True,read_only=True, source='rating_set')
    class Meta:
        model=Products
        fields=['id','name','image','price','ratings']


class productInfo_serializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','description','image','usage','price',
                'ingredients','brandName','TotalSoldOfProduct','ratings']
