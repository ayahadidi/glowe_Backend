from django.db import models
import uuid

class Colors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code=models.CharField(max_length=50)
    