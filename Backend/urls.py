from django.urls import path
from .views.Best_Sellers_View import Best_Sellers_View
from .views.categoryList_view import CategoryListView
from .views.productListByCategory_view import ProductListByCategory
from .views.addToWishlist_view import addTo_WishList
from .views.addToCart_view import AddToCartView
from .views.productInfo_view import productInfo_view
from .views.wishlist_ListView import wishlist_ListView
from .views.cartList_view import cartList_view
from .views.delete_cart_item_view import delete_cart_item
from .views.minus_cartItem_view import minus_cartItem
from .views.checkoutView import checkoutView
from .views.clearItems_view import Clear
from .views.add_rating_view import AddRatingView
from .views.product_total_rating_view import ProductTotalRating
from .views.product_comments_view import AllCommentsView
from .views.product_colors_view import ProductColorsView
from .views.plus_cartItem_view import plus_cartItem


urlpatterns = [
    path('api/bestSellers/', Best_Sellers_View.as_view(), name='product-list'),
    path('api/categories/', CategoryListView.as_view(),name="category-list"),
    path('api/productsByCategory/<int:category_id>/',ProductListByCategory.as_view(),name='product-list-by-category'),
    path('api/addToWishlist/', addTo_WishList.as_view(), name="wishlist"),
    path('api/AddToCartView/', AddToCartView.as_view(), name="cart"),
    path('api/productInfo/<uuid:product_id>/', productInfo_view.as_view(), name="productInfo"),
    path('api/cartList_view/', cartList_view.as_view(), name="cartList"),
    path('api/wishlist_ListView/', wishlist_ListView.as_view(), name="wishlist_List"),
    path('api/delete_item/<int:item_id>', delete_cart_item.as_view(), name="delete_cart_item"),
    path('api/minus_cartItem/<int:cartItem_id>', minus_cartItem.as_view(), name="minus_cartItem"),
    path('api/clear_items/<uuid:cart_or_wishlist_id>/',Clear.as_view(),name='clear_items'),
    path('api/checkout/<uuid:cart_id>/', checkoutView.as_view(), name='checkout'),
    path('api/add_rating/', AddRatingView.as_view(), name='product-ratings'),
    path('api/products/<uuid:product_id>/total_rating/', ProductTotalRating.as_view(), name='average-rating'),
    path('api/products/<uuid:product_id>/comments', AllCommentsView.as_view(), name='all-ratings'),
    path('api/products/<uuid:product_id>/colors/', ProductColorsView.as_view(), name='product-colors'),
    path('api/plus_cartItem/<int:cartItem_id>', plus_cartItem.as_view(), name="plus_cartItem"),

    
]

