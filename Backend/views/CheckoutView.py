from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from ..models.inventory_model import Inventory
from ..models.promoCode_model import PromoCode
from ..models import Transactions, Rating
from django.db import transaction

from decimal import Decimal

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request ):
        user = request.user
        promo_code = request.data.get('promo_code')

        try:
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)

            if not cart_items.exists():
                return Response({"error": "Your cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

            total_price = Decimal('0.00')
            total_items = 0
            discount_amount = Decimal('0.00')

            # Validate promo code early
            promo = None
            if promo_code:
                try:
                    promo = PromoCode.objects.get(code=promo_code)
                except PromoCode.DoesNotExist:
                    return Response({"error": "Invalid promo code."}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                for item in cart_items:
                    product = item.product
                    quantity = item.cartItemQuantity

                    inventory = Inventory.objects.select_for_update().get(products=product)
                    if inventory.inStock < quantity:
                        return Response({
                            "error": f"Not enough stock for {product.productName}. Only {inventory.inStock} left."
                        }, status=status.HTTP_400_BAD_REQUEST)

                    inventory.inStock -= quantity
                    inventory.save()

                    total_price += item.cartItemPrice
                    total_items += quantity

                    # Create rating placeholder
                    Rating.objects.create(user=user, product=product, rating=None)

                # Apply promo code
                if promo:
                    discount_amount = (promo.discount_value / 100) * total_price
                    total_price -= discount_amount

                # Save transactions
                for item in cart_items:
                    Transactions.objects.create(
                        user=user,
                        products=item.product,
                        total_revenue=item.cartItemPrice,
                        total_sold_items=item.cartItemQuantity
                    )

                # Delete the current cart
                cart_items.delete()
                cart.delete()

                # Create a new empty cart for the user
                Cart.objects.create(user=user, total_items=0, total_price=Decimal('0.00'))

            return Response({
                "message": "Checkout successful.",
                "total_price_after_discount": str(total_price),
                "discount_applied": str(discount_amount),
                "items_bought": total_items
            }, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
