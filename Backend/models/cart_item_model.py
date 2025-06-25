#CartItem model
from django.db import models
from django.core.validators import MaxValueValidator

class CartItem(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    cartItemQuantity=models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    cartItemPrice=models.FloatField(validators=[MaxValueValidator(10000)], default=0)
    productColor=models.CharField(max_length=50)
    color_name=models.CharField(max_length=100)
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    cart=models.ForeignKey('Backend.Cart',on_delete=models.CASCADE, null=True, blank=True)
