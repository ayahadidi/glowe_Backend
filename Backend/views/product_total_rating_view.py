from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models.product_model import Products
from Backend.models.rating_model import Rating
from django.db.models import Avg

class ProductTotalRating(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        return Response({
            'product': product.id,
            'average_rating': product.TotalRating
        })