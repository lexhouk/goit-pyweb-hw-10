from django.forms import CharField, DateField, DateInput, ModelForm, \
    SlugField, Textarea, TextInput

from fpq_core.forms import attributes
from .models import Author


class CreationForm(ModelForm):
    name = CharField(
        min_length=10,
        max_length=50,
        required=True,
        widget=TextInput(attributes('name')),
    )

    born_date = DateField(
        required=True,
        widget=DateInput(attrs=attributes('born-date'), format='%B %d, %Y'),
    )

    born_location = CharField(
        min_length=10,
        max_length=100,
        required=True,
        widget=TextInput(attributes('born-location')),
    )

    bio = SlugField(
        allow_unicode=True,
        required=True,
        widget=Textarea(attributes('bio')),
    )

    class Meta:
        model = Author
        fields = ('name', 'born_date')
