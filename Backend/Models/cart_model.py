from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Cart(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    TotalPrice=models.IntegerField(validators=[MaxValueValidator(100000)])
    TotalItems=models.IntegerField(validators=[MaxValueValidator(100)])
    UserId=models.ForeignKey('Backend.User',on_delete=models.CASCADE)
    ProductId=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)