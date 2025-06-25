from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg.utils import swagger_auto_schema

from ..models.product_model import Products
from Backend.models.rating_model import Rating
from Backend.serializers.rating_serializer import RatingSerializer


# ✅ Submit a rating for a product
class AddRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=RatingSerializer,
        responses={201: RatingSerializer, 400: 'Bad Request'}
    )
    def post(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
