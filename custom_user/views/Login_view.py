from custom_user.serializers.Login_Serializer import CustomToken_ObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class=CustomToken_ObtainPairSerializer
    Permission_Class=AllowAny