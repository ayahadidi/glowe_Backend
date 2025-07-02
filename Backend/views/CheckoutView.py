# views/checkout_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from ..models.cart_model import Cart, CartStatus
from ..models.cart_item_model import CartItem
from ..models.inventory_model import Inventory
from ..models.transaction_model import Transactions
from ..models.promoCode_model import PromoCode
from ..serializers.checkout_serializer import CheckoutSerializer

class checkoutView(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(
        request_body=CheckoutSerializer,
        responses={201:CheckoutSerializer,400:'Bad Request'}
    )
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cart_id=serializer.validated_data.get('cart')
        promo_code_input = serializer.validated_data.get('promo_code')

        try:
            cart = Cart.objects.get(id=cart_id, type=CartStatus.ACTIVE)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found or already expired'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        total_price = cart.total_price

        if promo_code_input:
            try:
                promo = PromoCode.objects.get(code=promo_code_input)
                discount = promo.discount_value
                total_price -= (total_price * discount / 100)
            except PromoCode.DoesNotExist:
                return Response({'error': 'Invalid promo code'}, status=status.HTTP_400_BAD_REQUEST)

        
        for item in cart_items:
            try:
                inventory = Inventory.objects.get(products=item.product)
            except Inventory.DoesNotExist:
                return Response({'error': f'No inventory for product {item.product.id}'}, status=status.HTTP_400_BAD_REQUEST)

            if inventory.inStock < item.cartItemQuantity:
                return Response({'error': f'Not enough stock for product {item.product.name}, there is {inventory.inStock} instock now'}, status=status.HTTP_400_BAD_REQUEST)

            
            inventory.inStock -= item.cartItemQuantity
            inventory.save()

            
            product = item.product
            product.TotalSoldOfProduct += item.cartItemQuantity
            product.save()

            Transactions.objects.create(
                total_revenue=item.cartItemPrice,
                total_sold_items=item.cartItemQuantity,
                user=cart.user,
                products=product,
                inventory=inventory,
                cart=cart
            )

        
        cart.type = CartStatus.CHECKED_OUT
        cart.total_price = total_price
        cart.save()

        return Response({'message': 'Checkout completed', 'final_price': total_price}, status=status.HTTP_200_OK)
