#cart model
from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class CartStatus(models.IntegerChoices):
    ACTIVE=1,'active'
    CHECKED_OUT=2,'checked_out'



class Cart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    total_price=models.FloatField(validators=[MaxValueValidator(100000)],default=0)
    total_items=models.IntegerField(validators=[MaxValueValidator(100)],default=0)
    type=models.IntegerField(validators=[MaxValueValidator(10)],default=1)
    promocode=models.ForeignKey('Backend.PromoCode',on_delete=models.CASCADE,default=1)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE)