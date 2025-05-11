from django.db import models
import uuid
from .product_model import Products
from django.core.validators import MaxValueValidator
class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    totalRevenue=models.IntegerField(validators=[MaxValueValidator(100000)])
    totalSoldItems=models.IntegerField(validators=[MaxValueValidator(10000)])
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    