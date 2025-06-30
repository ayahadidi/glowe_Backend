from django.db import models
from django.core.validators import MaxValueValidator

class wishlist_Item(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    wishlist=models.ForeignKey('Backend.Wishlist',on_delete=models.CASCADE,related_name='items',null=True)
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    productColor=models.CharField(max_length=50)
    ColorName=models.CharField(max_length=100)
