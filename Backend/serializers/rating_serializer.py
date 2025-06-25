from rest_framework import serializers
from Backend.models.rating_model import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['value', 'comment']  # only fields the user needs to submit
