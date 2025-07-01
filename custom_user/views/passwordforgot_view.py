from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from ..serializers.account_Serializer import PasswordResetRequestSerializer, SetNewPasswordSerializer

# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()


class PasswordResetRequestView(APIView):
    @swagger_auto_schema(
        request_body=PasswordResetRequestSerializer,
        responses={200: openapi.Response('Password reset link sent')}
    )
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        reset_link = f"http://your-frontend-url/reset-password/{uid}/{token}/"

        send_mail(
            subject="Reset your password",
            message=f"Click the link to reset your password: {reset_link}",
            from_email="no-reply@example.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"detail": "Password reset link sent."}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    @swagger_auto_schema(
        request_body=SetNewPasswordSerializer,
        responses={200: openapi.Response('Password has been reset')}
    )
    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        
        return Response({"detail": "Password has been reset."}, status=status.HTTP_200_OK)
