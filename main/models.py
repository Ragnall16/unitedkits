from django.db import models
import uuid

# Create your models here.
class ECommerce(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    quantity = models.IntegerField()
    size = models.CharField(max_length=255)

    @property
    def is_avai(self):
        return self.quantity > self.sold