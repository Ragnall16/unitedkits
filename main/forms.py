from django.forms import ModelForm
from main.models import ECommerce

class ECommerceForm(ModelForm):
    class Meta:
        model = ECommerce
        fields = ["name", "season", "type", "description", "quantity", "size"]