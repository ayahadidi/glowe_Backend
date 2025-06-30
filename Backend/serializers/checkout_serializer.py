from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    promo_code = serializers.CharField(required=False, allow_blank=True)
