from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..serializers.account_Serializer import PasswordResetRequestSerializer, SetNewPasswordSerializer 
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()

class PasswordResetRequestView(APIView):
    @swagger_auto_schema(
        request_body=PasswordResetRequestSerializer,
        responses={200: openapi.Response('Reset link sent if email exists')}
    )
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                return Response({"detail": "Inactive user."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "If the email exists, a reset link was sent."}, status=200)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        frontend_url = settings.FRONTEND_URL.rstrip('/')
        reset_link = f"{frontend_url}/reset-password/?uid={uid}&token={token}"

        send_mail(
            subject="Reset Your Password",
            message=f"Click the link to reset your password:\n{reset_link}",
            from_email="no-reply@example.com",
            recipient_list=[email],
            fail_silently=False,
        )


        return Response({"detail": "If the email exists, a reset link was sent."}, status=200)


class PasswordResetConfirmView(APIView):
    @swagger_auto_schema(
        request_body=SetNewPasswordSerializer,
        responses={200: openapi.Response('Reset link sent if email exists')}
    )
    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = serializer.validated_data['uid']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({'detail': 'Invalid user identifier.'}, status=400)

        if not default_token_generator.check_token(user, token):
            return Response({'detail': 'Invalid or expired token.'}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Password reset successful.'}, status=200)
