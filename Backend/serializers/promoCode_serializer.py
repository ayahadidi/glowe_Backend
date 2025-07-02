from rest_framework import serializers
from ..models.promoCode_model import PromoCode

class PromoCodeSerializer(serializers.Serializer): 
    class Meta:
        model=PromoCode
        fields=['id','code','discount_value']
        read_only_fields=['id','discount_value']