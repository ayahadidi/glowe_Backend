from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers.Auth_Serializer import AuthenticationSerializer
from Backend.utils.cart import merge_guest_cart_with_user_cart

class RegisterView(generics.CreateAPIView):
    serializer_class=AuthenticationSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args, **kwargs):
        request.session.modified = True  
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.user
                merge_guest_cart_with_user_cart(request, user)

        return response

