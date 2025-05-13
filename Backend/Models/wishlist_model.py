from django.db import models
import uuid

class Wishlist(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    UserId=models.ForeignKey('Backend.User',on_delete=models.CASCADE)
    ProductId=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
