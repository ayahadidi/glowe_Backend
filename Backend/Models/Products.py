from django.db import models
import Colors 
import uuid

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    colors=models.ForeignKey(Colors)
    ratings=models.ForeignKey()
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    image=models.CharField(max_length=250)
    email=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    usage=models.CharField(max_length=500)
    price=models.DecimalField(max_digits=1000)
    ingredients=models.CharField(max_length=500)
    brandName=models.CharField(max_length=50)
    quantity=models.IntegerField(max_digits=100)

