from django.db import models
import uuid
class UserPromoCode(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey('Backend.User',on_delete=models.CASCADE)
    promoCode=models.ForeignKey('Backend.PromoCode',on_delete=models.CASCADE)