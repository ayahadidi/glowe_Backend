from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg.utils import swagger_auto_schema

from ..models.product_model import Products
from Backend.models.rating_model import Rating
from Backend.models.transaction_model import Transactions
from Backend.serializers.rating_serializer import RatingSerializer


# ✅ Submit a rating for a product
class AddRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=RatingSerializer,
        responses={201: RatingSerializer, 400: 'Bad Request'}
    )
    def post(self, request,product_id):
        rating_value = request.data.get("value")
        comment = request.data.get("comment")
        product =get_object_or_404(Products,id=product_id)
        
        
        if not Transactions.objects.filter(user=request.user,products=product):
            return Response({
                "error": "You can only rate products you have purchased."}, status=status.HTTP_403_FORBIDDEN)
        
        if Rating.objects.filter(product=product, user=request.user).exists():
            return Response(
                {"error": "You have already rated this product."},
                status=status.HTTP_400_BAD_REQUEST
            )

        rating = Rating.objects.create(
            value=rating_value,
            comment=comment,
            user=request.user,
            product=product
        )   
        product.sumOfRatings += rating_value
        product.numberOfRatings += 1
        product.TotalRating = product.sumOfRatings / product.numberOfRatings
        product.save()

        serializer = RatingSerializer(rating)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        