from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from Backend.models.rating_model import Rating
from Backend.serializers.rating_serializer import ProductCommentsSerializer
from django.db.models import Q

class AllCommentsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, product_id):
        ratings = Rating.objects.filter(product_id=product_id).exclude(
            Q(comment__isnull=True) | Q(comment__regex=r'^\s*$')
        )
        serializer = ProductCommentsSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
