from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.product_model import Products
from ..serializers.cartItem_serializer import CartItem_Serializer
from ..models.color_model import Colors
from ..models.product_model import Products
from ..models.inventory_model import Inventory
from ..models.cart_item_model import CartItem
from ..models.cart_model import Cart
from ..utils.cart import get_or_create_guest_cart


request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['product_id', 'color_id'],
    properties={
        'product_id': openapi.Schema(type=openapi.TYPE_STRING,
                                    format='uuid',
                                    description='Product Id (UUID)'),
        'color_id': openapi.Schema(type=openapi.TYPE_INTEGER,
                                    description='Color Id (INT)'),
    }
)
class AddToCartView(APIView):

    @swagger_auto_schema(
            request_body=request_body,
            operation_description="Add product to cart",
            responses={200: 'Success'}
        )
    
    def post(self,request):
        product_id=request.data.get('product_id')
        color_id = request.data.get('color_id')
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
        

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user, type=1)
        else:
            cart = get_or_create_guest_cart(request)

        

       
        existing_item = CartItem.objects.filter(cart=cart, product=product, productColor=color.code).first()
        existing_quantity = existing_item.cartItemQuantity if existing_item else 0

        total_requested = existing_quantity + askednumber

        if total_requested > inventory.inStock:
            return Response(
                {"error": f"Only {inventory.inStock} item(s) available in stock. "
                          f"You already have {existing_quantity} in your cart."},
                status==201
            )
        
        if existing_item:
            existing_item.cartItemQuantity += askednumber
            existing_item.save()
            return Response(CartItem_Serializer(existing_item).data, status=200)


        serializer=CartItem_Serializer(data={
            'product': str(product.id),
            'cart': str(cart.id),
            'cartItemQuantity':askednumber,
            'cartItemPrice':product.price,
            'productColor':color.code,
            'color_name':color.ColorName,
            },context={'request':request,'product':product})
        
        if serializer.is_valid():
            cart_item=serializer.save()
            return Response(CartItem_Serializer(cart_item).data, status=201)
        return Response(serializer.errors, status=400)