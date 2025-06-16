from ..models import User
from rest_framework import serializers

class UserProfile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'email', 'first_name', 'phone_number','location']