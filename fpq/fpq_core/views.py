from abc import ABC, abstractmethod
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, QueryDict
from django.shortcuts import redirect, render
from django.views import View

from fpq_quote.models import Quote


Response = HttpResponse | HttpResponsePermanentRedirect


class FormView(ABC, View):
    @staticmethod
    def _context() -> dict:
        return dict()

    @abstractmethod
    def _guest(self) -> bool:
        ...

    def _save(response: QueryDict, form: ModelForm, commit=True) -> Any:
        return form.save(commit)

    def dispatch(self, request: WSGIRequest) -> Response:
        if request.user.is_anonymous == self._guest():
            return redirect('fpq_core:index')

        return super().dispatch(request)

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {'form': self.form_class, **self._context()},
        )

    def post(self, request: WSGIRequest) -> Response:
        form = self.form_class(request.POST)

        if form.is_valid():
            self._save(request.POST, form)

            return redirect('fpq_core:index')

        return render(
            request,
            self.template_name,
            {'form': form, **self._context()},
        )


def index(request: WSGIRequest) -> HttpResponse:
    quotes = Quote.objects.all()
    return render(request, 'fpq_core/index.html', {'quotes': quotes})
