from django.urls import path
from .views.Best_Sellers_View import Best_Sellers_View
from .views.categoryList_view import CategoryListView
from .views.productListByCategory_view import ProductListByCategory
from .views.wishlist_view import addTo_WishList
from .views.cart_view import AddToCartView

urlpatterns = [
    path('api/bestSellers/', Best_Sellers_View.as_view(), name='product-list'),
    path('api/categories/', CategoryListView.as_view(),name="category-list"),
    path('api/productsByCategory/<int:category_id>/',ProductListByCategory.as_view(),name='product-list-by-category'),
    path('api/wishlist/<uuid:product_color_id>/', addTo_WishList.as_view(), name="wishlist"),
    path('api/cart/<uuid:product_color_id>/', AddToCartView.as_view(), name="cart"),
]
