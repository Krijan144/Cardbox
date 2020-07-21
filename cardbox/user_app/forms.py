from django import forms
from django.contrib.auth.models import User
from .models import SignupModel
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class meta:
        model = SignupModel
        fields = '__all__'
