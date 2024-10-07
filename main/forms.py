from django.forms import ModelForm, Form, ChoiceField
from main.models import ECommerce
from django.utils.html import strip_tags

class ECommerceForm(ModelForm):
    class Meta:
        model = ECommerce
        fields = ["name", "season", "type", "description", "quantity", "size"]
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

class JerseyForm(Form):
    season = ChoiceField(choices=ECommerce.SEASON_CHOICES, label='Season')
    type = ChoiceField(choices=ECommerce.TYPE_CHOICES, label='Type')