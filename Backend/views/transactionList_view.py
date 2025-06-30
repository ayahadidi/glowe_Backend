from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Cart
from ..serializers.cart_serializer import CartSerializer

class TransactionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user, type=2)

        if not carts:
            return Response({"detail": "No carts checked out"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CartSerializer(carts,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
