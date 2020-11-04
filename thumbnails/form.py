from django import forms
from .models import rating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

MAX_RATE = 10

class input_form(forms.ModelForm):
    class Meta:
        model = rating
        fields = ["rate"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']