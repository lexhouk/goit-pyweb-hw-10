from django.forms import CharField, ModelForm, Textarea

from fpq_core.forms import FormHelper
from .models import Quote


class CreationForm(FormHelper, ModelForm):
    phrase = CharField(
        required=True,
        widget=Textarea(FormHelper.attributes('phrase')),
    )

    class Meta:
        model = Quote
        fields = ('phrase',)
        exclude = ('author',)
