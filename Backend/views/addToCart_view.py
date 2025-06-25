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
            return Response({"error": "This product isn't available in the selected color."}, status=201)
        
        askednumber=int(request.data.get('cartItemQuantity',1))
        
        try:
            inventory = Inventory.objects.get(products=product)
        except Inventory.DoesNotExist:
            return Response({"error": "Not enough product quantity in the inventory"})
        
        try:
            cart = Cart.objects.get(user=request.user, type=2)  
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                user=request.user
            )

       
        existing_item = CartItem.objects.filter(cart=cart, product=product, productColor=color.code).first()
        existing_quantity = existing_item.cartItemQuantity if existing_item else 0

        total_requested = existing_quantity + askednumber

        if total_requested > inventory.inStock:
            return Response(
                {"error": f"Only {inventory.inStock} item(s) available in stock. "
                          f"You already have {existing_quantity} in your cart."},
                status==201
            )

        serializer=CartItem_Serializer(data={
            'cartItemQuantity':askednumber,
            'cartItemPrice':request.data.get('cartItemPrice',product.price),
            'productColor':request.data.get('productColor',color.code),
            'color_name':request.data.get('color_name',color.ColorName),

            },context={'request':request,'product':product})
        
        if serializer.is_valid():
            cart_item=serializer.save()
            return Response(CartItem_Serializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)
