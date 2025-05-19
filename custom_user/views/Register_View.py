from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers.Auth_Serializer import AuthenticationSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class=AuthenticationSerializer
    permission_classes=[AllowAny]

