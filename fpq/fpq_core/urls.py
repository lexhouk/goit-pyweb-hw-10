from django.urls import path

from . import views

app_name = 'fpq_core'

urlpatterns = [
    path('', views.index, name='index'),
]
