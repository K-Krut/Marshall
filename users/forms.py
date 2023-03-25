from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User

        fields = ("email", "username", "password1", "password2",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.EmailInput(attrs={"class": "form-control"}),
        }


class LoginUserForm(AuthenticationForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User

        fields = ("email", "password",)
