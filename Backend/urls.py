from django.urls import path
from .views.ProductList_View import ProductListView
from .views.categoryList_view import CategoryListView
from .views.productListByCategory_view import ProductListByCategory
urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/categories/', CategoryListView.as_view(),name="category-list"),
    path('api/productsByCategory/<int:category_id>/',ProductListByCategory.as_view(),name='product-list-by-category'),
]
