from django.db import models
import uuid

class Categories(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    url=models.CharField(max_length=50)
    category_name=models.CharField(max_length=50)
    