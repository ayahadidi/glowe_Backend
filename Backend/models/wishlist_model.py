from django.db import models
import uuid

class Wishlist(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE, null=True,blank=True)
