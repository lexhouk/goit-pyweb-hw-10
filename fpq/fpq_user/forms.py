from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput, TextInput


ATTRIBUTES = {'class': 'form-control'}


class FpqUserAuthenticationForm(AuthenticationForm):
    username = CharField(
        min_length=3,
        max_length=16,
        required=True,
        widget=TextInput({'id': 'username', **ATTRIBUTES}),
    )

    password = CharField(
        required=True,
        widget=PasswordInput({'id': 'password', **ATTRIBUTES}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')
