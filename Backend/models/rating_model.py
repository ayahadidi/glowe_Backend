from django.db import models
import uuid
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    value=models.IntegerField(validators=[MaxValueValidator(5)])
    comment=models.CharField(max_length=500)
    user=models.ForeignKey('custom_user.User',on_delete=models.CASCADE) 
    product=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'product')  # Each user can rate a product once

    def __str__(self):
        return f"{self.user} rated {self.product} ({self.value})"