from django.db import models
from django.core.validators import MaxValueValidator

class wishlist_Item(models.Model):
<<<<<<< HEAD:Backend/models/wishlist_item_model.py
    id = models.AutoField(primary_key=True, editable=False)
    wishlist=models.ForeignKey('Backend.Wishlist',on_delete=models.CASCADE,related_name='items')
=======
    id = models.IntegerField(primary_key=True, editable=False)
    wishlist=models.ForeignKey('Backend.Wishlist',on_delete=models.CASCADE)
>>>>>>> d4f251cf3fcb50c5b0311dee30a6706da098aef5:Backend/Models/wishlist_item_model.py
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    productColor=models.CharField(max_length=50)
    ColorName=models.CharField(max_length=100)
