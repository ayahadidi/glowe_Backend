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














# #cart model
# from django.db import models
# import uuid
# from django.core.validators import MaxValueValidator

# class CartStatus(models.IntegerChoices):
#     PENDING=1,'pending'
#     ACTIVE=2,'active'
#     EXPIRED=3,'expired'
#     SAVED_FOR_LATER=4,'saved_for_later'



# class Cart(models.Model):
#     id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     total_price=models.FloatField(validators=[MaxValueValidator(100000)],default=0)
#     total_items=models.IntegerField(validators=[MaxValueValidator(100)],default=0)
#     type=models.IntegerField(validators=[MaxValueValidator(10)],default=2)
#     promocode=models.ForeignKey('Backend.PromoCode',on_delete=models.CASCADE,default=1)
#     user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE)




# #inventory model
# from django.db import models
# import uuid
# from .product_model import Products
# from django.core.validators import MaxValueValidator
# class Inventory(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     inStock=models.IntegerField(validators=[MaxValueValidator(100000)])
#     products=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)



# #product model
# from django.db import models
# import uuid
# from django.core.validators import MaxValueValidator

# class Products(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name=models.CharField(max_length=50)
#     description=models.CharField(max_length=250)
#     image=models.ImageField()
#     usage=models.CharField(max_length=500)
#     price=models.FloatField(validators=[MaxValueValidator(1000)],default=0)
#     ingredients=models.CharField(max_length=500)
#     brandName=models.CharField(max_length=50)
#     TotalSoldOfProduct=models.IntegerField(default=0)
#     TotalRating=models.FloatField(validators=[MaxValueValidator(5)],default=0)
#     sumOfRatings=models.IntegerField(validators=[MaxValueValidator(1000000)],default=0)
#     numberOfRatings=models.IntegerField(validators=[MaxValueValidator(1000000)],default=0)
#     def __str__(self):
#         return self.name