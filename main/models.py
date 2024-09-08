from django.db import models

# Create your models here.
class ECommerce(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    quantity = models.IntegerField()
    sold = models.IntegerField()

    @property
    def is_avai(self):
        return self.quantity > self.sold