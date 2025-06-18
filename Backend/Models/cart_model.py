from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Cart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    total_price=models.IntegerField(validators=[MaxValueValidator(100000)],default=0)
    total_items=models.IntegerField(validators=[MaxValueValidator(100)],default=0)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE)
    product_color=models.ForeignKey('Backend.ProductsColors',on_delete=models.CASCADE)
