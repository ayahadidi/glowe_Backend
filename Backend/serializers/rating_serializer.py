from rest_framework import serializers
from ..models.rating_model import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['id','value','comment','user']