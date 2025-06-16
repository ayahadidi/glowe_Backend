from django.db import models

class Colors(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    code=models.CharField(max_length=50)
    