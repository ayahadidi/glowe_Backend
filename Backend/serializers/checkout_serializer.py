from rest_framework import serializers
from ..models.transaction_model import Transactions
from .promoCode_serializer import PromoCodeSerializer
from ..models.cart_model import Cart
class CheckoutSerializer(serializers.Serializer):
    promoCode = serializers.CharField(write_only=True, required=False)
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())

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
            'promoCode',
        ]