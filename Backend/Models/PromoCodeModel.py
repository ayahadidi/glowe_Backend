from django.db import models
import uuid
from django.core.validators import MaxValueValidator
class PromoCode(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Code=models.CharField(max_length=10)
    DiscountValue=models.IntegerField(validators=[MaxValueValidator(100)])
    