from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..serializers.UserProfile_Serializer import UserProfile_Serializer

class UserProfile_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user=request.user
        serializer=UserProfile_Serializer(user)
        return Response(serializer.data)

class EditUserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    
    @swagger_auto_schema(request_body=UserProfile_Serializer)
    def put(self,request):
        serializer=UserProfile_Serializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)