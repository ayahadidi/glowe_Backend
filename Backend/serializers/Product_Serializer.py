from rest_framework import serializers
from ..models.product_model import Products
from .rating_serializer import RatingSerializer
from .color_serializer import ColorSerializer

class ProductInList_Serializer(serializers.ModelSerializer):
    ratings=RatingSerializer(many=True,read_only=True, source='rating_set')
    colors=ColorSerializer(many=True,read_only=True,source='colors_set')
    class Meta:
        model=Products
        fields=['id','name','image','price','TotalRating','ratings','colors']


class productInfo_serializer(serializers.ModelSerializer):
    ratings=RatingSerializer(many=True,read_only=True, source='rating_set')
    colors=ColorSerializer(many=True,read_only=True,source='colors_set')
    class Meta:
        model=Products
        fields=['id','name','description','image','usage','price',
                'ingredients','brandName','TotalSoldOfProduct','ratings','colors']
