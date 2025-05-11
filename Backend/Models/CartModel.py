from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from UserModel import User
from Products import Products
class Cart(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    TotalPrice=models.IntegerField(validators=[MaxValueValidator(100000)])
    TotalItems=models.IntegerField(validators=[MaxValueValidator(100)])
    UserId=models.ForeignKey(User,on_delete=models.SET_NULL)
    ProductId=models.ForeignKey(Products,on_delete=models.SET_NULL)