from django.forms import ModelForm, Form, ChoiceField
from main.models import ECommerce

class ECommerceForm(ModelForm):
    class Meta:
        model = ECommerce
        fields = ["name", "season", "type", "description", "quantity", "size"]

class JerseyForm(Form):
    season = ChoiceField(choices=ECommerce.SEASON_CHOICES, label='Season')
    type = ChoiceField(choices=ECommerce.TYPE_CHOICES, label='Type')