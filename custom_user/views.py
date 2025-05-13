from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializer import AuthenticationSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class=AuthenticationSerializer
    permission_classes=[AllowAny]