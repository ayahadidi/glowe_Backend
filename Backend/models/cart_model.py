from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class CartStatus(models.IntegerChoices):
    PENDING=1,'pending'
    ACTIVE=2,'active'
    EXPIRED=3,'expired'
    SAVED_FOR_LATER=4,'saved_for_later'



class Cart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    total_price=models.IntegerField(validators=[MaxValueValidator(100000)],default=0)
    total_items=models.IntegerField(validators=[MaxValueValidator(100)],default=0)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE)
    promocode=models.ForeignKey('Backend.PromoCode',on_delete=models.CASCADE)
    type=models.IntegerField(validators=[MaxValueValidator(10)],default=0)
    

    