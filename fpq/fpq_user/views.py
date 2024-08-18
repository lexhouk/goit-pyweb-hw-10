from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.views import View

from .forms import RegisterForm


Response = HttpResponse | HttpResponsePermanentRedirect


class RegisterView(View):
    template_name = 'fpq_user/register.html'
    form_class = RegisterForm

    def dispatch(self, request: WSGIRequest) -> Response:
        return super().dispatch(request) if request.user.is_anonymous else \
            redirect('fpq_core:index')

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request: WSGIRequest) -> Response:
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect('fpq_core:index')

        return render(request, self.template_name, {'form': form})


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('fpq_core:index')
