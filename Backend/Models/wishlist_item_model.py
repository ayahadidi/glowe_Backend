from django.db import models
from django.core.validators import MaxValueValidator

class wishlist_Item(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    wishlist=models.ForeignKey('Backend.Wishlist',on_delete=models.CASCADE)
    product_color=models.ForeignKey('Backend.ProductsColors',on_delete=models.CASCADE)

