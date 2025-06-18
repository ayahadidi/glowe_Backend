from rest_framework import serializers
from ..Models.category_model import Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=['id','url','category_name']