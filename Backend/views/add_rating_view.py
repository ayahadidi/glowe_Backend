from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models.product_model import Products
from Backend.models.rating_model import Rating
from Backend.models.transaction_model import Transactions
from Backend.serializers.rating_serializer import RatingSerializer

class AddRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=RatingSerializer,
        responses={201: RatingSerializer, 400: 'Bad Request'}
    )
    
    def post(self, request):
        serializer=RatingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        product=serializer.validated_data.get('product')
        rating_value = serializer.validated_data.get('value')

        if not Transactions.objects.filter(user=request.user,products=product):
            return Response({
                "error": "You can only rate products you have purchased."}, status=status.HTTP_403_FORBIDDEN)
        
        if Rating.objects.filter(product=product, user=request.user).exists():
            return Response(
                {"error": "You have already rated this product."},
                status=status.HTTP_400_BAD_REQUEST
            )
        rating=serializer.save(user=request.user)
        product.sumOfRatings += rating_value
        product.numberOfRatings += 1
        product.TotalRating = product.sumOfRatings / product.numberOfRatings
        product.save()

        return Response(RatingSerializer(rating).data, status=status.HTTP_201_CREATED)
        
        