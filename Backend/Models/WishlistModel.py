from django.db import models
import uuid
from UserModel import User
from Products import Products
class Wishlist(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    UserId=models.ForeignKey(User,on_delete=models.SET_NULL)
    ProductId=models.ForeignKey(Products,on_delete=models.SET_NULL)
