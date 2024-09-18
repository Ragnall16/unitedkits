from django.db import models
import uuid

# Create your models here.
def season_choices(start_year=1992, end_year=2025):
    choices = []
    for year in range(start_year, end_year):
        next_year = year + 1
        season = f"{str(year)[2:]}/{str(next_year)[2:]}"
        choices.append((season, season))
    return choices

class ECommerce(models.Model):
    # List of Tuples for Dropbox choices
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    SEASON_CHOICES = season_choices()
    TYPE_CHOICES = [
        ('home', 'Home'),
        ('away', 'Away'),
        ('third', 'Third'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default = 1500000)
    description = models.TextField()
    quantity = models.IntegerField()
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default= "M")
    season = models.CharField(max_length=5, choices=SEASON_CHOICES, default='24/25')
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='home')

    @property
    def is_customer_rich(self):
        return self.quantity > 10