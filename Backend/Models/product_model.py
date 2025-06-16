from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    image=models.ImageField()
    email=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    usage=models.CharField(max_length=500)
    price=models.IntegerField(validators=[MaxValueValidator(1000)])
    ingredients=models.CharField(max_length=500)
    brandName=models.CharField(max_length=50)
    quantity=models.IntegerField(validators=[MaxValueValidator(100)])
    TotalSoldOfProduct=models.IntegerField(default=0)
    ratings=models.ForeignKey('Backend.Rating',on_delete=models.CASCADE)

    def __str__(self):
        return self.name