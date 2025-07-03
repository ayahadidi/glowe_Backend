import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.product_model import Products
from ..serializers.Product_Serializer import productInfo_serializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rapidfuzz import fuzz


def normalize(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', text.lower())).strip()


class ProductSearchView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'search': openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
            },
            required=[],  # 'search' is optional
        ),
        responses={200: productInfo_serializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        search_query_raw = request.data.get('search', '')
        search_query = normalize(search_query_raw)

        products = Products.objects.all()

        if search_query:
            query_length = len(search_query)
            results = []

            # Set threshold and scorer based on query length
            if query_length == 1:
                threshold = 30
                scorer = fuzz.partial_ratio
            elif query_length == 2:
                threshold = 40
                scorer = fuzz.partial_ratio
            elif query_length==3:
                threshold=50
                scorer=fuzz.partial_ratio
            elif query_length==4 :
                threshold=55
                scorer=fuzz.partial_ratio
            else:
                threshold = 60
                scorer = fuzz.token_set_ratio

            for product in products:
                name_score = scorer(search_query, normalize(product.name or ''))
                combined_score = 0.7 * name_score + 0.3 

                if combined_score >= threshold:
                    results.append((product, combined_score))

            results.sort(key=lambda x: x[1], reverse=True)
            products = [item[0] for item in results]

        if not products:
            return Response({'message': 'No matching products found.'}, status=status.HTTP_200_OK)

        serializer = productInfo_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
