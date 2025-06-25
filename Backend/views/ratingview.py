from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from ..models import Rating, Products
from ..serializers.rating_serializer import RatingSerializer

# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AddRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_uuid):
        ratings = Rating.objects.filter(product__id=product_uuid)
        serializer = RatingSerializer(ratings, many=True)

        avg_rating = ratings.aggregate(average=Avg("rating"))["average"]
        avg_rating = round(avg_rating, 2) if avg_rating is not None else 0.0

        return Response({
            "average_rating": avg_rating,
            "ratings": serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=RatingSerializer,
        responses={
            201: RatingSerializer,
            400: "Bad Request",
            404: "Product not found",
        }
    )
    def post(self, request, product_uuid):
        try:
            product = Products.objects.get(id=product_uuid)
        except Products.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                product=product,
                user=request.user if request.user.is_authenticated else None
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
