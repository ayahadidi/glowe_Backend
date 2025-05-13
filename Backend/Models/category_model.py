from django.db import models
import uuid

class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url=models.CharField(max_length=50)
    category_name=models.CharField(max_length=50)
    