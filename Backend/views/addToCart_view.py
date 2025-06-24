from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..models.product_model import Products
from ..serializers.cartItem_serializer import CartItem_Serializer
from ..models.color_model import Colors
from ..models.product_model import Products
from ..models.inventory_model import Inventory
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart



class AddToCartView(APIView):
    permission=[IsAuthenticated]

    def post(self,request,product_id, color_id):
        try:
            product=Products.objects.get(id=product_id)
            color = Colors.objects.get(id=color_id, product=product)
        except (Colors.DoesNotExist, Products.DoesNotExist):
            return Response({"error": "This product isn't available in the selected color."}, status=status.HTTP_404_NOT_FOUND)
        
        askednumber=int(request.data.get('cartItemQuantity',1))
        
        try:
            inventory = Inventory.objects.get(products=product)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory data not available for this product."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        try:
            cart = Cart.objects.get(user=request.user, type=2)  
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

       
        existing_item = CartItem.objects.filter(cart=cart, product=product, productColor=color.code).first()
        existing_quantity = existing_item.cartItemQuantity if existing_item else 0

        total_requested = existing_quantity + askednumber

        if total_requested > inventory.inStock:
            return Response(
                {"error": f"Only {inventory.inStock} item(s) available in stock. "
                          f"You already have {existing_quantity} in your cart."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer=CartItem_Serializer(data={
            'product':product_id,
            'cartItemQuantity':askednumber,
            'cartItemPrice':request.data.get('cartItemPrice',product.price),
            'productColor':request.data.get('productColor',color.code),
            'color_name':request.data.get('color_name',color.ColorName),

            },context={'request':request})
        
        if serializer.is_valid():
            cart_item=serializer.save()
            return Response(CartItem_Serializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)
