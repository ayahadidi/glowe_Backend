from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from .user_model import User
class Rating(models.Model):
    Id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Value=models.IntegerField(validators=[MaxValueValidator(5)])
    Comment=models.CharField(max_length=500)
    UserId=models.ForeignKey(User,on_delete=models.CASCADE) 