from django.db import models
import uuid
import Products, Categories

class ProductsCategories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products=models.ForeignKey(Products)
    categoris=models.ForeignKey(Categories)