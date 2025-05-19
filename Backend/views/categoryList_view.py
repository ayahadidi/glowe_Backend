from rest_framework import generics
from Backend.models import Categories
from ..serializers.category_serializer import CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategorySerializer