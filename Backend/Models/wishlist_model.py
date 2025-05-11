from django.db import models
import uuid
from .user_model import User
from .product_model import Products
class Wishlist(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    ProductId=models.ForeignKey(Products,on_delete=models.CASCADE)
