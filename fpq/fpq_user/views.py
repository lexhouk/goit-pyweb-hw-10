from django.contrib.auth import logout
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect


def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('fpq_core:index')
