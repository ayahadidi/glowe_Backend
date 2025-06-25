# serializers/rating_serializer.py

from rest_framework import serializers
from ..models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'review', 'product', 'user']
        read_only_fields = ['product', 'user']
