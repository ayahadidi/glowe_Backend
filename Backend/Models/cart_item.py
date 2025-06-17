from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class CartItem(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    cartItemQuantity=models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    cartItemPrice=models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    product_color=models.ForeignKey('Backend.ProductsColors',on_delete=models.CASCADE)

