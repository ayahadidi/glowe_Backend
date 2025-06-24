from rest_framework import serializers
from ..models.color_model import Colors

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Colors
        fields=['id','code','ColorName']