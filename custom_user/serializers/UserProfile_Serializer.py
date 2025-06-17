from ..models import User
from rest_framework import serializers

class UserProfile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'email', 'phone_number','location']