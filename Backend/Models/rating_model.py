from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    value=models.IntegerField(validators=[MaxValueValidator(5)])
    comment=models.CharField(max_length=500)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE) 