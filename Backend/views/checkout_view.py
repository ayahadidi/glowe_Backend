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




class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        promo_code = request.data.get('promo_code')

        try:
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)

            if not cart_items.exists():
                return Response({"error": "Your cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
            
            total_price = 0
            total_items = 0

            with transaction.atomic():
                for item in cart_items:
                    product=item.product
                    quantity=item.cartItemQuantity


                    inventory=Inventory.objects.select_for_update().get(products=product)
                    if inventory.inStock < quantity:
                        return Response({
                            "error": f"Not enough stock for {product.productName}. Only {inventory.inStock} left."
                    
                        }, status=status.HTTP_400_BAD_REQUEST)
                    

                    inventory.inStock -= quantity
                    inventory.save()

                    total_price += item.cartItemPrice
                    total_items += quantity


                    #Create rating placeholders
                    Rating.objects.create(user=user, product=product, rating=None)


                #Apply promoCode
                discount_amount = 0
                if promo_code:
                    try:
                        promo = PromoCode.objects.get(code=promo_code)
                        discount_amount = (promo.discount_value / 100) * total_price
                        total_price -= int(discount_amount)
                    except PromoCode.DoesNotExist:
                        return Response({"error": "Invalid promo code."}, status=status.HTTP_400_BAD_REQUEST)

                #Save transaction (for simplicity, saving 1 product per transaction)
                for item in cart_items:
                    Transactions.objects.create(
                        user=user,
                        products=item.product,
                        total_revenue=item.cartItemPrice,  # Optional: you can divide revenue if needed
                        total_sold_items=item.cartItemQuantity
                    )

                #Clear cart
                cart_items.delete()
                cart.total_items = 0
                cart.total_price = 0
                cart.save()

            return Response({
                "message": "Checkout successful.",
                "total_price_after_discount": total_price,
                "discount_applied": int(discount_amount),
                "items_bought": total_items
            }, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)