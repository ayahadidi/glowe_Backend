from rest_framework import serializers
from Backend.models.rating_model import Rating
from custom_user.serializers.UserProfile_Serializer import UserProfile_Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['value', 'comment','user','product',]
        read_only_fields= ['product','user']



class ProductCommentsSerializer(serializers.ModelSerializer):
    user=UserProfile_Serializer(read_only=True)
    class Meta:
        model = Rating
        fields = [ 'user', 'value', 'comment']
