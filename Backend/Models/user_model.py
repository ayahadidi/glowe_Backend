from django.db import models
import uuid
from .promoCode_model import PromoCode
class User(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Password=models.CharField(max_length=30)
    PhoneNumber=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Location=models.CharField(max_length=200)
    PromoCodeId=models.ForeignKey(PromoCode,on_delete=models.CASCADE)