# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

User = get_user_model()

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email.")
        return value


# class SetNewPasswordSerializer(serializers.Serializer):
#     uidb64 = serializers.CharField()
#     token = serializers.CharField()
#     new_password = serializers.CharField(min_length=8)

#     def validate(self, attrs):
#         try:
#             uid = force_str(urlsafe_base64_decode(attrs['uidb64']))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             raise serializers.ValidationError("Invalid UID")

#         if not default_token_generator.check_token(user, attrs['token']):
#             raise serializers.ValidationError("Invalid or expired token")

#         user.set_password(attrs['new_password'])
#         user.save()

#         return attrs



class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SetNewPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)

