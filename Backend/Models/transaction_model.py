from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_revenue=models.IntegerField(validators=[MaxValueValidator(100000)])
    total_sold_items=models.IntegerField(validators=[MaxValueValidator(10000)])
    products=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    