from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, EmailInput, PasswordInput, \
    TextInput


USERNAME = {'min_length': 3, 'max_length': 16, 'required': True}


def attributes(identifier: str) -> dict:
    if not identifier:
        raise ValueError('The tag identifier can not be empty.')

    return {'id': identifier, 'class': 'form-control'}


class LoginForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(attributes('username')),
        **USERNAME,
    )

    password = CharField(
        required=True,
        widget=PasswordInput(attributes('password')),
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    username = CharField(widget=TextInput(attributes('username')), **USERNAME)

    email = EmailField(
        min_length=7,
        max_length=40,
        required=True,
        widget=EmailInput(attributes('email')),
    )

    password1 = CharField(
        required=True,
        widget=PasswordInput(attributes('password')),
    )

    password2 = CharField(
        required=True,
        widget=PasswordInput(attributes('confirm-password')),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
