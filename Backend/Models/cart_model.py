from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Cart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    total_price=models.IntegerField(validators=[MaxValueValidator(100000)])
    total_items=models.IntegerField(validators=[MaxValueValidator(100)])
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE)
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)