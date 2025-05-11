from django.db import models
import uuid
from .product_model import Products
from .category_model import Categories

class ProductsCategories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    categoris=models.ForeignKey(Categories, on_delete=models.CASCADE)