from django.db import models
import uuid

class ProductsCategories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    categoris=models.ForeignKey('Backend.Categories', on_delete=models.CASCADE)