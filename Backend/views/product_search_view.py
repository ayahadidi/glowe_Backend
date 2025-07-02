import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.product_model import Products
from ..serializers.Product_Serializer import productInfo_serializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rapidfuzz import fuzz

# Normalize text: lowercase, remove special characters, collapse whitespace
def normalize(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', text.lower())).strip()

class ProductSearchView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'search': openapi.Schema(type=openapi.TYPE_STRING, description='Search term'),
            },
            required=[],
        ),
        responses={200: productInfo_serializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        search_query_raw = request.data.get('search', '')
        search_query = normalize(search_query_raw)

        all_products = Products.objects.all()
        results = []

        if search_query:
            # Set threshold dynamically (more forgiving for shorter queries)
            threshold = 30 if len(search_query) < 3 else 60

            for product in all_products:
                name = normalize(product.name or '')
                description = normalize(product.description or '')

                name_score = fuzz.partial_ratio(search_query, name)
                desc_score = fuzz.partial_ratio(search_query, description)

                # Weighted score (name is more important than description)
                combined_score = 0.7 * name_score + 0.3 * desc_score

                # Uncomment for debug:
                # print(f"[DEBUG] {product.name} → Name: {name_score}, Desc: {desc_score}, Total: {combined_score}")

                if combined_score >= threshold:
                    results.append((product, combined_score))

            # Sort products by highest score
            results.sort(key=lambda x: x[1], reverse=True)
            products = [item[0] for item in results]
        else:
            products = all_products

        if not products:
            return Response({'message': 'No matching products found.'}, status=status.HTTP_200_OK)

        serializer = productInfo_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
