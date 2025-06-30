# utils/cart.py
from ..models.cart_model import Cart
from ..models.wishlist_model import Wishlist
from ..models.cart_item_model import CartItem
from ..models.color_model import Colors


def get_or_create_guest_cart(request):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            return Cart.objects.get(id=cart_id, user=None)
        except Cart.DoesNotExist:
            pass  

    
    new_cart = Cart.objects.create(type=1)  
    request.session['cart_id'] = str(new_cart.id)
    return new_cart




def get_or_create_guest_wishlist(request):
    wishlist_id = request.session.get('wishlist_id')

    if wishlist_id:
        try:
            return Wishlist.objects.get(id=wishlist_id, user=None)
        except Wishlist.DoesNotExist:
            pass  

    
    new_wishlist = Wishlist.objects.create()
    request.session['wishlist_id'] = str(new_wishlist.id)
    return new_wishlist










def add_product_to_cart(cart, product, color, quantity):
    from ..models.cart_item_model import CartItem
    from ..models.inventory_model import Inventory

    inventory = Inventory.objects.get(products=product)

    existing_item = CartItem.objects.filter(cart=cart, product=product, productColor=color.code).first()
    existing_quantity = existing_item.cartItemQuantity if existing_item else 0
    total_requested = existing_quantity + quantity

    if total_requested > inventory.inStock:
        raise ValueError(f"Only {inventory.inStock} item(s) available in stock. "
                         f"You already have {existing_quantity} in your cart.")

    unit_price = product.price

    if existing_item:
        existing_item.cartItemQuantity += quantity
        existing_item.cartItemPrice += quantity * unit_price
        existing_item.save()
    else:
        existing_item = CartItem.objects.create(
            cart=cart,
            product=product,
            productColor=color.code,
            color_name=color.ColorName,
            cartItemQuantity=quantity,
            cartItemPrice=quantity * unit_price
        )

    cart.total_items += quantity
    cart.total_price += quantity * unit_price
    cart.save()

    return existing_item










def merge_guest_cart_with_user_cart(request, user):
    guest_cart_id = request.session.get('cart_id')
    if not guest_cart_id:
        return

    try:
        guest_cart = Cart.objects.get(id=guest_cart_id)
    except Cart.DoesNotExist:
        return

    user_cart, _ = Cart.objects.get_or_create(user=user, type=1)

    for item in CartItem.objects.filter(cart=guest_cart):
        try:
            color = Colors.objects.get(code=item.productColor, product=item.product)
            add_product_to_cart(user_cart, item.product, color, item.cartItemQuantity)
        except Exception as e:
            print(f"Failed to merge item: {e}")
            continue

    guest_cart.delete()
    if 'cart_id' in request.session:
        del request.session['cart_id']
        request.session.modified = True
