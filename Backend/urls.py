from django.urls import path
from .views.ProductList_View import ProductListView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
]
