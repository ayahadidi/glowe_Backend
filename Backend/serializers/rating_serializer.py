from rest_framework import serializers
from Backend.models.rating_model import Rating
from custom_user.serializers.UserProfile_Serializer import UserProfile_Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['product','value', 'comment','user']
        read_only_fields= ['user']

from rest_framework import serializers
from Backend.models.rating_model import Rating

class ProductCommentsSerializer(serializers.ModelSerializer):
    user=UserProfile_Serializer(read_only=True)
    class Meta:
        model = Rating
        fields = [ 'user', 'value', 'comment']
