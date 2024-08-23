from typing import Any

from django.forms import ModelForm
from django.http import QueryDict

from fpq_author.models import Author
from fpq_core.views import FormView
from .forms import CreationForm


class CreationView(FormView):
    template_name = 'fpq_quote/create.html'
    form_class = CreationForm

    def _context() -> dict:
        return {**super()._context(), 'authors': Author.objects.all()}

    def _guest(self) -> bool:
        return True

    def _save(response: QueryDict, form: ModelForm, commit=True) -> Any:
        quote = super()._save(False)

        quote.author = response['author']

        quote.save()

        return quote
