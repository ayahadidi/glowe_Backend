from django.db import models
import uuid
from .product_model import Products
from django.core.validators import MaxValueValidator
class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inStock=models.IntegerField(validators=[MaxValueValidator(100000)])
    products=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)