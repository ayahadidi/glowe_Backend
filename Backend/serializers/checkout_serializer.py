from rest_framework import serializers
from ..models.transaction_model import Transactions
from ..models.cart_model import Cart
from .cart_serializer import CartSerializer
class CheckoutSerializer(serializers.Serializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    promoCode = serializers.CharField(write_only=True, required=False,allow_blank=True)







class TransactionSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    class Meta:
        model = Transactions
        fields = [
            'id',
            'total_revenue',
            'total_sold_items',
            'checkoutDate',
            'user',
            'products',
            'inventory',
            'cart',
        ]