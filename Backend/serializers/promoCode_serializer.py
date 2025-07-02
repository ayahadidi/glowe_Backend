from rest_framework import serializers
from ..models.promoCode_model import PromoCode
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PromoCode
        fields=['id','code','discount_value']