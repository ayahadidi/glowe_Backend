from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    value=models.FloatField(validators=[MaxValueValidator(5)])
    comment=models.CharField(max_length=500, null=True, blank=True)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE) 
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    