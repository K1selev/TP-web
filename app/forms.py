from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import ModelForm
from django import forms

from app import models
from app.models import Question, Answer, Tag, Profile

class RegisterForm(forms.Form):
    login = forms.CharField(
        max_length=40,
        label='Login',
        widget=forms.TextInput(
            attrs={ 'class': 'form-control' }
        )
    )
    email = forms.EmailField(
        max_length=40,
        label='Email',
        widget=forms.EmailInput(
            attrs={ 'class': 'form-control' }
        )
    )
    password = forms.CharField(
        max_length=40,
        label='Password',
        widget=forms.PasswordInput(
            attrs={ 'class': 'form-control' }
        )
    )
    rep_password = forms.CharField(
        max_length=40,
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={ 'class': 'form-control' }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=20, widget=forms.TextInput(attrs={'placeholder':'Your login', 'class':"form-control log_in ",}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control log_in", 'placeholder':'Your password'}), max_length=20, )

    def clean_password(self):
        data = self.cleaned_data['password']
        if data == "password":
            raise ValidationError("password password can't be used")
        return data

class ProfileForm(forms.Form):
    login = forms.CharField(
        required=False,
        max_length=40,
        label='Login',
        widget=forms.TextInput(
            attrs={ 'class': 'form-control' }
        )
    )
    email = forms.EmailField(
        required=False,
        max_length=40,
        label='Email',
        widget=forms.EmailInput(
            attrs={ 'class': 'form-control' }
        )
    )

class AskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={ 'class': 'form-control' }
        )
    )
    text = forms.CharField(
        max_length=400,
        widget=forms.Textarea(
        attrs={ 'class': 'form-control' }
        )
    )
    tags = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={ 'class': 'form-control' },
        )
    )

class AnswerForm(forms.Form):
    textarea = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={ 'class': 'form-control' }
        )
    )
