from django.db import models
from django.core.validators import MaxValueValidator

class CartItem(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    cartItemQuantity=models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    cartItemPrice=models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    cart=models.ForeignKey('Backend.Cart',on_delete=models.CASCADE)
    productColor=models.CharField(max_length=50)



## C:\Users\hadid\Desktop\glowe_back\Backend\Models\__pycache__\__init__.cpython-313.pyc
