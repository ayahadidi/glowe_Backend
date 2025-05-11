from django.db import models
import uuid
from .Products import Products

class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products=models.ForeignKey(Products)
    totalRevenue=models.IntegerField(max_length=100000)
    totalSoldItems=models.IntegerField(max_length=10000)
    