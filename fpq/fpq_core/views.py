from abc import ABC, abstractmethod
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, QueryDict
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from fpq_quote.models import Quote
from fpq_tag.models import Tag


Response = HttpResponse | HttpResponsePermanentRedirect


class FormView(ABC, View):
    def _context(self) -> dict:
        return dict()

    @abstractmethod
    def _guest(self) -> bool:
        ...

    def _save(
        self,
        response: QueryDict,
        form: ModelForm,
        commit: bool = True
    ) -> Any:
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
    query = Quote.objects
    context = {}

    if (tag_id := request.GET.get('tag')):
        context['current_tag'] = Tag.objects.filter(pk=tag_id).first()

        if context['current_tag']:
            query = query.filter(tags=tag_id)

    context['quotes'] = query.all()

    return render(request, 'fpq_core/index.html', context)
