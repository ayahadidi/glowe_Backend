# utils/cart.py
from ..models.cart_model import Cart
from ..models.wishlist_model import Wishlist
from ..models.cart_item_model import CartItem

def get_or_create_guest_cart(request):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            return Cart.objects.get(id=cart_id, user=None)
        except Cart.DoesNotExist:
            pass  

    
    new_cart = Cart.objects.create(type=2)  # ACTIVE type
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




def merge_guest_cart_with_user_cart(request, user):
    guest_cart_id = request.session.get('cart_id')
    if not guest_cart_id:
        return

    try:
        guest_cart = Cart.objects.get(id=guest_cart_id)
    except Cart.DoesNotExist:
        return

    user_cart, _ = Cart.objects.get_or_create(user=user, defaults={'type': 1})

    
    for item in CartItem.objects.filter(cart=guest_cart):
        existing = CartItem.objects.filter(
            cart=user_cart,
            product=item.product,
            productColor=item.productColor
        ).first()

        if existing:
            unit_price = item.cartItemPrice / item.cartItemQuantity
            existing.cartItemQuantity += item.cartItemQuantity
            existing.cartItemPrice = existing.cartItemQuantity * unit_price
            existing.save()
        else:
            item.cart = user_cart
            item.save()

   
    total_items = 0
    total_price = 0.0
    for item in CartItem.objects.filter(cart=user_cart):
        total_items += item.cartItemQuantity
        total_price += item.cartItemPrice

    user_cart.total_items = total_items
    user_cart.total_price = total_price
    user_cart.save()

    guest_cart.delete()
    if 'cart_id' in request.session:
        del request.session['cart_id']
        request.session.modified = True
