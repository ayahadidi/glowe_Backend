from rest_framework import generics
from rest_framework.permissions import AllowOnly
from ..serializers.AuthenticationSerializer import AuthenticationSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class=AuthenticationSerializer
    permission_classes=[AllowOnly]

    ## C:\Yasmin\Django\glowe_Backend\Backend\views\authentication_view.py