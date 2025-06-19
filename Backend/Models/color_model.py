from django.db import models

class Colors(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    product=models.ForeignKey('Backend.Products', on_delete=models.CASCADE)
    code=models.CharField(max_length=50)
    ColorName=models.CharField(max_length=100)
    