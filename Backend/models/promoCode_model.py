from django.db import models
import uuid
from django.core.validators import MaxValueValidator
class PromoCode(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    code=models.CharField(max_length=10)
    discount_value=models.IntegerField(validators=[MaxValueValidator(100)])
    