from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.UserProfile_Serializer import UserProfile_Serializer

class UserProfile_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user=request.user
        serializer=UserProfile_Serializer(user)
        return Response(serializer.data)

