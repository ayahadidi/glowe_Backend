#product model
from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField()
    usage=models.CharField(max_length=500)
    price=models.FloatField(validators=[MaxValueValidator(1000)],default=0)
    ingredients=models.CharField(max_length=500)
    brandName=models.CharField(max_length=50)
    TotalSoldOfProduct=models.IntegerField(default=0)
    TotalRating=models.FloatField(validators=[MaxValueValidator(5)],default=0)
    sumOfRatings=models.IntegerField(validators=[MaxValueValidator(1000000)],default=0)
    numberOfRatings=models.IntegerField(validators=[MaxValueValidator(1000000)],default=0)
    def __str__(self):
        return self.name