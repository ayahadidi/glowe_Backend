from django.db import models
import uuid
from .Products import Products

class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products=models.ForeignKey(Products)
    inStock=models.IntegerField(max_length=100000)
    
    