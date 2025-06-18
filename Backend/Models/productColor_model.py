from django.db import models
import uuid

class ProductsColors(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    products=models.ForeignKey('Backend.Products',on_delete=models.CASCADE)
    colors=models.ForeignKey('Backend.Colors',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.products.name} - {self.colors.code}"