from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.timezone import now

class CustomToken_ObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token=super().get_token(user)

        token['email']=user.email
        token['first_name']=user.first_name
        token['last_name']=user.last_name

        return token
    def validate(self,attrs):
        data=super().validate(attrs)
        self.user.last_login=now()
        self.user.save(update_fields=['last_login'])
        return data
