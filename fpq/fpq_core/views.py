from abc import ABC, abstractmethod

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.views import View


Response = HttpResponse | HttpResponsePermanentRedirect


class FormView(ABC, View):
    @abstractmethod
    def _guest(self) -> bool:
        ...

    def dispatch(self, request: WSGIRequest) -> Response:
        if request.user.is_anonymous == self._guest():
            return redirect('fpq_core:index')

        return super().dispatch(request)

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request: WSGIRequest) -> Response:
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect('fpq_core:index')

        return render(request, self.template_name, {'form': form})


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'fpq_core/index.html')
